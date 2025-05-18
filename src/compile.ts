import { ParseResult } from "./parser"; // assumes your parser is in parser.ts
import * as fs from "fs";

function tsTypeToPython(tsType: string): string {
    return tsType
        .replace(/\bstring\b/g, "str")
        .replace(/\bnumber\b/g, "float")
        .replace(/\bboolean\b/g, "bool")
        .replace(/\bany\b/g, "Any")
        .replace(/\bArray<([^>]+)>/g, "List[$1]")
        .replace(/\bRecord<([^,]+),\s*([^>]+)>/g, "Dict[$1, $2]")
        .replace(/\[/g, "(")
        .replace(/\]/g, ")");
}

export function Compile(parsed: ParseResult): string {
    const lines: string[] = [];

    for (const [name, members] of Object.entries(parsed.interfaces)) {
        lines.push(`class ${name}:`);
        if (Object.keys(members).length === 0) {
            lines.push("    pass\n");
            continue;
        }
        lines.push("    def __init__(self):");
        for (const [key, type] of Object.entries(members)) {
            lines.push(`        self.${key} = None  # type: ${tsTypeToPython(type as string)}`);
        }
        lines.push("");
    }

    for (const [name, type] of Object.entries(parsed.types)) {
        lines.push(`# ${name} = ${tsTypeToPython(type)}`);
    }

    for (const [name, members] of Object.entries(parsed.enums)) {
        lines.push(`class ${name}:`);
        for (const [key, value] of Object.entries(members)) {
            if (typeof value === "string") {
                lines.push(`    ${key} = "${value}"`);
            } else {
                lines.push(`    ${key} = ${value}`);
            }
        }
        lines.push("");
    }

    for (const [name, { type, value }] of Object.entries(parsed.variables)) {
        const pyValue = JSON.stringify(value, null, 4);
        lines.push(`${name} = ${pyValue}  # type: ${tsTypeToPython(type)}`);
    }

    console.log("Compiled!")
    
    return lines.join("\n");
}