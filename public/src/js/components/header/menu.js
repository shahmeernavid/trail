module.exports = React.createClass({
    render: function () {
        // Create menu items.
        var menuItems = [];
        this.props.menuItems.forEach(function (item){
            menuItems.push(<li><a href="item.link">item.text</a></li>);
        });

        return <div class="menu">
            <ul>
                {menuItems}
            </ul>
        </div>;
    }
});
