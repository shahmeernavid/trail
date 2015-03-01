var async = require('async');
var fs = require('fs');
var fsutils = require('./fs_utils');

var tasks = [];

GLOBAL.task = function (desc, func){
    tasks.push({
        func: func,
        desc: desc
    });
};

fsutils.mkdir();

// Add tasks here.
require('./buildjs');
require('./buildcss');

async.eachSeries(tasks, function (task, done){
    console.log(task.desc);
    task.func(done);
});
