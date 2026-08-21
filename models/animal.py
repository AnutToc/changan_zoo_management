from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ZooAnimal(models.Model):
    _name = 'zoo.animal'
    _description = 'Zoo Animal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    species = fields.Char(string='Species', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    picture = fields.Image(string='Picture')
    zone_id = fields.Many2one('zoo.living.zone', string='Living Zone', tracking=True)

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age and record.age < 0:
                raise ValidationError(_("Animal age cannot be negative."))
