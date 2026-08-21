from odoo import models, fields, api, _

class ZooLivingZone(models.Model):
    _name = 'zoo.living.zone'
    _description = 'Living Zone'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    zookeeper_id = fields.Many2one('zoo.zookeeper', string='Zookeeper', tracking=True)
    animal_ids = fields.One2many('zoo.animal', 'zone_id', string='Animals')
    
    animal_count = fields.Integer(string='Animal Count', compute='_compute_animal_count')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Living Zone name must be unique!')
    ]

    @api.depends('animal_ids')
    def _compute_animal_count(self):
        for record in self:
            record.animal_count = len(record.animal_ids)

    def action_view_animals(self):
        return {
            'name': _('Animals in Zone'),
            'res_model': 'zoo.animal',
            'view_mode': 'tree,form',
            'domain': [('zone_id', '=', self.id)],
            'context': {'default_zone_id': self.id},
            'type': 'ir.actions.act_window',
        }
