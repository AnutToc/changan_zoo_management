from odoo import models, fields

class ZooAnimalGroup(models.Model):
    _name = 'zoo.animal.group'
    _description = 'Animal Group / Classification'

    name = fields.Char(string='Group Name', required=True, translate=True)
    description = fields.Text(string='Description')
    animal_ids = fields.One2many('zoo.animal', 'group_id', string='Animals in this Group')
