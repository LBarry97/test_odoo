from odoo import fields, models


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', translate=True)
    # Tag class relationship to Tasks
    task_ids = fields.Many2many(
        'todo.task',    # related model
        string='Tasks')

