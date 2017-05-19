var fs = require("fs"); 
var parser = require("./index"); 
fs.writeFileSync('fbo_data.json', JSON.stringify(parser.parse(fs.readFileSync('FBOFeed20020129', 'UTF-8'))));