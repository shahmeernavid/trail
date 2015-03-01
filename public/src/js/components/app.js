var React = require('react');
var Header = require('./header/header');

module.exports = React.createClass({
    render: function (){
        return <div class="main">
            <Header />
        </div>;
    }
});
