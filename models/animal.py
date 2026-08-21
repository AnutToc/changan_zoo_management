from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ZooAnimal(models.Model):
    _name = 'zoo.animal'
    _description = 'Zoo Animal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    species = fields.Char(string='Species', required=True, tracking=True)
    group_id = fields.Many2one('zoo.animal.group', string='Animal Group', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown')
    ], string='Gender', default='unknown', tracking=True)
    birth_date = fields.Date(string='Birth Date', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    picture = fields.Image(string='Picture')
    zone_id = fields.Many2one('zoo.living.zone', string='Living Zone', tracking=True)
    
    state = fields.Selection([
        ('alive', 'Alive & Healthy'),
        ('sick', 'Under Treatment'),
        ('transferred', 'Transferred'),
        ('deceased', 'Deceased')
    ], string='Status', default='alive', tracking=True)
    death_date = fields.Date(string='Date of Death', tracking=True)
    death_reason = fields.Text(string='Cause of Death', tracking=True)

    next_health_check = fields.Date(string='Next Health Check', tracking=True)
    health_check_status = fields.Selection([
        ('overdue', 'Overdue'),
        ('upcoming', 'Upcoming (7 Days)'),
        ('ok', 'Normal')
    ], string='Check Status', compute='_compute_health_status')

    @api.depends('next_health_check', 'state')
    def _compute_health_status(self):
        today = date.today()
        for record in self:
            if record.state in ['deceased', 'transferred'] or not record.next_health_check:
                record.health_check_status = False
            else:
                delta = (record.next_health_check - today).days
                if delta < 0:
                    record.health_check_status = 'overdue'
                elif delta <= 7:
                    record.health_check_status = 'upcoming'
                else:
                    record.health_check_status = 'ok'

    @api.depends('birth_date', 'death_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birth_date:
                end_date = record.death_date if record.death_date else today
                age = end_date.year - record.birth_date.year - ((end_date.month, end_date.day) < (record.birth_date.month, record.birth_date.day))
                record.age = age
            else:
                record.age = 0

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date and record.birth_date > date.today():
                raise ValidationError(_("Birth date cannot be in the future."))
