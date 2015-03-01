/**
 * Collection of useful file system utilities.
 *
 */

var browserify = require('browserify');
var fs = require('fs');
var path = require('path');

var BUNDLE_DIR_ = './public/bundle/';
var SRC_DIR_ = './public/src/';
var TEMP_ = 'js/trail.temp.js';

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
        fs.writeFileSync(SRC_DIR_ + TEMP_, contents);

        var browserified = browserify(SRC_DIR_ + TEMP_);
        // Apply transforms.
        transforms.forEach(function (transform){
            browserified.transform(transform);
        });
        browserified.bundle(function (err, browserifiedCode){
            if (err) {
                throw err;
            }
            // Delete temp file.
            fs.unlinkSync(SRC_DIR_ + TEMP_);
            // Write built file.
            done(browserifiedCode);
        });
    };

    /**
     * Takes an absolute directory path and returns the content of the directory.
     *
     * @param {String} dir: Absolute path to directory.
     *
     * Returns Array of directory contents (absolute paths).
     */
    this.readdir = function (dir){
        var contents = fs.readdirSync(dir);
        return contents.map(function (elem){
            return dir + '/' + elem;
        });
    };

    /**
     * Creates a directory. If a directory exists, will do nothing.
     *
     * @param {String} dir: Path to directory.
     */
    this.mkBundleDir = function (dir){
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
    this.writeToBundle = function (file, content){
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
        dirsOrFiles.forEach(function (elem){
            elem = path.resolve(elem);
            if(fs.statSync(elem).isFile()){
                output += fs.readFileSync(elem) + '\n';
            }
            else if(fs.statSync(elem).isDirectory()){
                if (recursive) {
                    var dirContents = self.readdir(elem);
                    output += self.concat(dirContents);
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