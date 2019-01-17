from odoo import api, fields, models


class TodoTask(models.Model):
        _inherit = 'todo.task'

        name = fields.Char(help="What needs to be done?")
        effort_estimate = fields.Integer()
        stage_id = fields.Many2one('todo.task.stage', 'Stage')
        tag_ids = fields.Many2many('todo.task.tag', string='Tags')
