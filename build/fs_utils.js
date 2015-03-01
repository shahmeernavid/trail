/**
 * Collection of useful file system utilities.
 *
 */

var browserify = require('browserify');
var fs = require('fs');
var path = require('path');
var _ = require('underscore');

var BUNDLE_DIR_ = './public/bundle/';
var TEMP_ = 'trail.temp.js';

module.exports = new (function (){
    var self = this;

    /**
     * Helper to browserify files.
     *
     * @param {String} contents: File contents.
     * @param {Array} transforms: Browserify
     * @param {Function} done: Callback. Passed browserified code.
     */
    this.browserify = function (contents, transforms, done){
        // Defaults.
        transforms = transforms || [];
        done = done || function (){};
        contents = contents || '';

        // Create temp file.
        // TODO(shahmeer): find a way to do this without temps.
        self.write(TEMP_, contents);

        var browserified = browserify(BUNDLE_DIR_ + TEMP_);
        // Apply transforms.
        transforms.forEach(function (transform){
            browserified.transform(transform);
        });
        browserified.bundle(function (err, browserifiedCode){
            if (err) {
                throw err;
            }
            // Delete temp file.
            fs.unlinkSync(BUNDLE_DIR_ + TEMP_);
            // Write built file.
            done(browserifiedCode);
        });
    };

    /**
     * Creates a directory. If a directory exists, will do nothing.
     *
     * @param {String} dir: Path to directory.
     */
    this.mkdir = function (dir){
        dir = path.resolve(BUNDLE_DIR_ + (dir || ''));

        try {
            fs.mkdirSync(dir);
        }
        catch (e){}
    };

    /**
     * Helper to write files. Normalizes paths before writing.
     *
     * @param {String} file: Output directory.
     * @param {String} content: File contents.
     */
    this.write = function (file, content){
        file = path.resolve(BUNDLE_DIR_ + (file || ''));
        fs.writeFileSync(file, content);
    };

    /**
     * Takes either a directory or a list of paths and returns a concatenation of all these paths.
     * Paths must be absolute.
     *
     * @param {String or Array} dirsOrFiles: An absolute path to a directory or an array of absolute
     *         file paths.
     * @param {Boolean} recursive: True if recursive concat is desired. If false, will ignore
     *         directories. True by default.
     *
     * Returns String of the concatenation of all file contents.
     *
     * Raises Error if one of the list item is neither a file nor a directory.
     */
    this.concat = function (dirsOrFiles, recursive){
        // Give default value to recursive.
        if (arguments.length < 2) {
            recursive = true;
        }

        if (!Array.isArray(dirsOrFiles)){
            dirsOrFiles = [dirsOrFiles];
        }

        var output = '';
        _.each(dirsOrFiles, function (elem){
            elem = path.resolve(elem);
            if(fs.statSync(elem).isFile()){
                output += fs.readFileSync(elem) + '\n';
            }
            else if(fs.statSync(elem).isDirectory()){
                if (recursive) {
                    output += self.concat(elem);
                }
            }
            else {
                throw new Error(
                    'Incorrect input into concat: one of the list items was neither a dir or file');
            }
        });

       return output;
    };
})();