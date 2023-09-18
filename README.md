# BoigaCustom
BoigaCustom lets you input Turbowarp and related manifests, which in turn lets you use them in Boiga, with built-in QoL features like type validation*  
  
*for strings and integers only
## Usage
1. Paste in your template into the input variable in lazyconvert.mjs.
2. Run it: `deno run --allow-read --allow-write lazyconvert.mjs` or `node lazyconvert.mjs` or in the browser.
3. Create a `structure` variable in Python, then paste the results in, either from the console or `pluginmeta.json`.
4. Import the code, and instantiate `ExtensionBlockStructure`: `structure = boigacustom.ExtensionBlockStructure(structure, True)`
5. Use it:
   - `structure.statement("sendMessageText", ID=connect_id, DATA="Hiya!")`,
   - `WaitUntil(structure.expression("messageQueue", ID=connect_id))`