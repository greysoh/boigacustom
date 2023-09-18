const Scratch = {
  BlockType: {
    COMMAND: "COMMAND",
    REPORTER: "REPORTER",
    BOOLEAN: "BOOLEAN",
    HAT: "HAT"
  },

  ArgumentType: {
    STRING: "STRING",
    NUMBER: "NUMBER",
    BOOLEAN: "BOOLEAN",
    COLOR: "COLOR",
    ANGLE: "ANGLE",
    MATRIX: "MATRIX",
    NOTE: "NOTE",
    IMAGE: "IMAGE"
  }
}

const input = {}; //dont-remove-this

if (typeof Deno != "undefined") {
  const selfJS = await Deno.readTextFile("./lazyconvert.mjs");

  let selfJSRemovedInputReconstructed = selfJS.replace("const input = {", 0xDEADBEEF).split(0xDEADBEEF)[0];
  selfJSRemovedInputReconstructed += `const input = {}; //dont-remove-this`;
  selfJSRemovedInputReconstructed += selfJS.replace("const input = {", 0xDEADBEEF).split(0xDEADBEEF)[1].replace("//dont-remove-this", 0xDEADBEEF).split(0xDEADBEEF)[1];

  await Deno.writeTextFile("./pluginmeta.json", JSON.stringify(input, null, 2));
  await Deno.writeTextFile("./lazyconvert.mjs", selfJSRemovedInputReconstructed);
} else {
  console.log(JSON.stringify(input, null, 2));
}