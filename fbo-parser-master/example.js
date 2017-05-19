var fs = require("fs");
var parser = require("./index");

fs.writeFileSync('example_output.json', JSON.stringify(parser.parse(fs.readFileSync(arguments, 'UTF-8'))));
