/** @jsx React.DOM */
var TodoListItem = React.createClass({
    render: function () {
        return <li>{this.props.todo.text}</li>;
    }
});

var TodoList = React.createClass({
    getInitialState: function () {
        return { todos: [{ text: 'Dishes!', dueDate: new Date() }] };
    },

    render: function () {
        var todos = this.state.todos.map(function (todo) {
            return <TodoListItem todo={todo} />;
        });

        return <ul>{todos}</ul>;
    }
});

React.renderComponent(<TodoList />, document.body);
