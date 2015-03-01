var fs = require('fs');
var reactify = require('reactify');
var fsutils = require('./fs_utils');

var TEMP = 'main.temp.js';

fsutils.mkdir('js');

// Frontend libraries.
var components = fsutils.concat([
    'public/packages/js/jsxtransformer.js'
]);
// JS code.
var js_list = fsutils.concat([
    'public/src/js/views/todo.js'
]);

// TODO(shahmeer): Minification.
// TODO(shahmeer): Watch.
var buildJs = function (done){
    fsutils.browserify(js_list, [reactify], function (code){
        fsutils.write('js/trail.js', components + code);
        done();
    });
};

task('Compiling JS Code.', buildJs);