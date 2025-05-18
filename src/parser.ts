import * as ts from "typescript";
import * as fs from "fs";

export interface ParseResult {
    interfaces: {[key: string]: any}
    types: {[key: string]: any}
    enums: {[key: string]: any}
    variables: {[key: string]: any}
}
const result: any = {
  interfaces: {},
  types: {},
  enums: {},
  variables: {}
};

function evalLiteral(expr: ts.Expression): any {
  if (ts.isStringLiteral(expr)) return expr.text;
  if (ts.isNumericLiteral(expr)) return Number(expr.text);
  if (expr.kind === ts.SyntaxKind.TrueKeyword) return true;
  if (expr.kind === ts.SyntaxKind.FalseKeyword) return false;
  if (ts.isObjectLiteralExpression(expr)) {
    const obj: any = {};
    expr.properties.forEach(prop => {
      if (ts.isPropertyAssignment(prop)) {
        const key = prop.name.getText();
        obj[key] = evalLiteral(prop.initializer);
      }
    });
    return obj;
  }
  if (ts.isArrayLiteralExpression(expr)) {
    return expr.elements.map(evalLiteral);
  }
  return undefined;
}

export function Parse(fileName): ParseResult {
    const sourceCode = fs.readFileSync(fileName, "utf-8");
    const sourceFile = ts.createSourceFile(fileName, sourceCode, ts.ScriptTarget.Latest, true);

    sourceFile.forEachChild(node => {
        /* interface */
        if (ts.isInterfaceDeclaration(node)) {
            const name = node.name.text;
            const members: any = {};
            node.members.forEach(member => {
            if (ts.isPropertySignature(member) && member.name && member.type) {
                const key = (member.name as ts.Identifier).text;
                const type = member.type.getText(sourceFile);
                members[key] = type;
            }
            });
            result.interfaces[name] = members;
        }

        /* type */
        else if (ts.isTypeAliasDeclaration(node)) {
            const name = node.name.text;
            result.types[name] = node.type.getText(sourceFile);
        }

        /* enum */
        else if (ts.isEnumDeclaration(node)) {
            const name = node.name.text;
            const members: any = {};
            node.members.forEach(member => {
            const key = member.name.getText(sourceFile);
            const value = member.initializer ? eval(member.initializer.getText(sourceFile)) : key;
            members[key] = value;
            });
            result.enums[name] = members;
        }

        /* variable decl */
        else if (ts.isVariableStatement(node)) {
            node.declarationList.declarations.forEach(decl => {
            if (ts.isIdentifier(decl.name)) {
                const name = decl.name.text;
                const type = decl.type ? decl.type.getText(sourceFile) : "any";
                const initializer = decl.initializer ? evalLiteral(decl.initializer) : undefined;
                result.variables[name] = { type, value: initializer };
            }
            });
        }
    });

    console.log("Parsing complete")

    return result as ParseResult
}