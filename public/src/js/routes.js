var Backbone = require('backbone');

var router = Backbone.Router.extend({
    routes: {
        '': 'index',
        'feed': 'feed'
    }
});

Backbone.history.start({pushState: true});
