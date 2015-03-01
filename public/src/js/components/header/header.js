var Menu = require('./menu');
var Search = require('./search');
// var User = require('./user');

module.exports = React.createClass({
    // getInitialState: function () {
    //     return { todos: [{ text: 'Dishes!', dueDate: new Date() }] };
    // },

    render: function () {
        return <div class="header">
            <Menu />
            <Search />
        </div>;
    }
});

