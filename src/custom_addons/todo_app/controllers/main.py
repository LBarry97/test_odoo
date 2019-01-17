from odoo import http


class Todo(http.Controller):

    @http.route('/todo')
    def main(self, **kwargs):
        todo_task = http.request.env['todo.task']
        domain_todo = [('is_done', '=', False)]
        tasks = todo_task.search(domain_todo)
        return http.request.render('todo_app.index_template', {'tasks': tasks})
