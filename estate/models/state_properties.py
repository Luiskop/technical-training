from odoo import models, fields

class TestModel(models.Model):
    _name = "state.properties"
    _description = "Test Model"
  
    name = fields.Char(default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availbility = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')])
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(default=False)


















