//md-to-html.js
const showdown  = require('showdown');
const converter = new showdown.Converter();
const fs = require('fs');
const path = require('path');

if (process.argv.length < 3) {
    console.log('Usage: node ' + process.argv[1] + ' markdownFile');
    process.exit(1);
}

const inputFile = process.argv[2];
const inputBase = path.basename(inputFile, '.md');
const outputFile = `${path.join(path.dirname(inputFile), path.basename(inputFile, '.md'))}.html`
const title = inputBase.replace(/-/g," ");

console.log(`Converting ${inputFile} to ${outputFile} with title: ${title}`);
const  inputText  = fs.readFileSync(inputFile, {encoding: 'utf8'});
const generatedHtml  = converter.makeHtml(inputText);

const html = `
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body { font-family: Helvetica, Arial; }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
</head>
<body>
    ${generatedHtml}
</body>
</html>
`

fs.writeFileSync(outputFile, html, {encoding: 'utf8'});

console.log("Done!")
