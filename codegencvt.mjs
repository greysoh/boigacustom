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

function camelToUnderscore(key) {
  var result = key.replace( /([A-Z])/g, " $1" );
  return result.split(' ').join('_').toLowerCase();
}

const input = {};

let template = `import boigacustom

__structure__ = ${JSON.stringify(input, null, 2).replaceAll("true", "True").replaceAll("false", "False")}
__structure__ = boigacustom.ExtensionBlockStructure(__structure__, True)

# This code was generated by BoigaCustom.
`;

for (const block of input.blocks) {
  if (typeof block != "object") throw new Error("Invalid input detected");
  template += `"""
${block.text}
"""
def ${camelToUnderscore(block.opcode)}(${Object.keys(block.arguments).join(", ")}):
  return __structure__.expression("${block.opcode}", ${Object.keys(block.arguments).join(", ")})\n\n`
}

if (typeof Deno != "undefined") {
  await Deno.writeTextFile("modulegen.py", template);
} else {
  console.log(template);
}