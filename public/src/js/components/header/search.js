module.exports = React.createClass({
    render: function () {
        // Create menu items.
        var menuItems = [];
        this.props.menuItems.forEach(function (item){
            menuItems.push(<li><a href="item.link">item.text</a></li>);
        });

        return <div class="search">
            <input type="submit" placeholder="What do you want to learn today?" />
        </div>;
    }
});
