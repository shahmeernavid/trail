var fs = require('fs');
var path = require('path');
var fsutils = require('./fs_utils');

fsutils.mkdir('css');

var buildCss = function (done){
    var output = fsutils.concat([
    ]);

    fsutils.write('css/style.css', output);

    done();
};

task('Compiling CSS Code.', buildCss);

