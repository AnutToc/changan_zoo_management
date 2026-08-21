from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ZooZookeeper(models.Model):
    _name = 'zoo.zookeeper'
    _description = 'Zookeeper Profile'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        string='Gender',
        required=True
    )
    position = fields.Char(string='Position', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    picture = fields.Image(string='Picture')
    monthly_salary = fields.Monetary(string='Monthly Salary', currency_field='currency_id', tracking=True, groups="changan_zoo.group_zoo_manager")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    zone_ids = fields.One2many('zoo.living.zone', 'zookeeper_id', string='Managed Zones')
    
    zone_count = fields.Integer(string='Zone Count', compute='_compute_zone_count')

    @api.depends('zone_ids')
    def _compute_zone_count(self):
        for record in self:
            record.zone_count = len(record.zone_ids)

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age and record.age <= 0:
                raise ValidationError(_("Zookeeper age must be greater than 0."))

    def action_view_zones(self):
        return {
            'name': _('Managed Zones'),
            'res_model': 'zoo.living.zone',
            'view_mode': 'tree,form',
            'domain': [('zookeeper_id', '=', self.id)],
            'context': {'default_zookeeper_id': self.id},
            'type': 'ir.actions.act_window',
        }
