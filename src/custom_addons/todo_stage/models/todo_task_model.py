from odoo.addons.base.res.res_request import referenceable_models
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
        _inherit = ['todo.task', 'mail.thread']
        _name = 'todo.task'

        _sql_constraints = [
                ('todo_task_name_uniq',  # Constraint unique identifier
                 'UNIQUE (name, active)',  # Constraint SQL syntax
                 'Task title must be unique!')  # Validation message
        ]

        name = fields.Char(help="What needs to be done?")
        effort_estimate = fields.Integer()
        stage_id = fields.Many2one('todo.task.stage', 'Stage')
        tag_ids = fields.Many2many('todo.task.tag', string='Tags')
        refers_to = fields.Reference(referenceable_models, 'Refers to')
        stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold', search='_search_stage_fold',
                                    inverse='_write_stage_fold')
        state = fields.Selection(related='stage_id.state', string='Stage State')

        @api.constrains('name')
        def _check_name_size(self):
                for todo in self:
                        if len(todo.name) < 5:
                                raise ValidationError('Must have 5 chars!')

        @api.onchange('user_id')
        def onchange_user_id(self):
                if not self.user_id:
                        self.team_ids = None
                return {
                        'warning': {
                                'title': 'No Responsible',
                                'message': 'Team was also reset.'
                        }
                }

        @api.depends('stage_id.fold')
        def _compute_stage_fold(self):
                for todo in self:
                        todo.stage_fold = todo.stage_id.fold

        def _search_stage_fold(self, operator, value):
                return [('stage_id.fold', operator, value)]

        def _write_stage_fold(self):
                for todo in self:
                        todo.stage_id.fold = todo.stage_fold
