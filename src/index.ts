import * as https from "https";
import * as fs from "fs";
import { Parse } from "./parser";
import { Compile } from "./compile";

const robloxTS_files: {[key: string]: string} = {
    'None.d.ts': "https://raw.githubusercontent.com/roblox-ts/types/refs/heads/master/include/generated/None.d.ts",
    'PluginSecurity.d.ts': "https://raw.githubusercontent.com/roblox-ts/types/refs/heads/master/include/generated/PluginSecurity.d.ts",
    'enums.d.ts': "https://raw.githubusercontent.com/roblox-ts/types/refs/heads/master/include/generated/enums.d.ts"
}

function downloadFile(url: string, outputPath: string) {
  const file = fs.createWriteStream(outputPath);
  https.get(url, response => {
    response.pipe(file);
    file.on("finish", () => {
      file.close();
      console.log("Download complete");
    });
  });
}

for (const file in robloxTS_files){
    const path = 'include/'+file
    downloadFile(robloxTS_files[file], path)
    
    const parsed = Parse(path)
    const compiled = Compile(parsed)

    fs.writeFileSync(path.replace('.ts', '.py'), compiled, "utf8");
}