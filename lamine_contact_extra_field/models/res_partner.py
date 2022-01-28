from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    workplace_id = fields.Many2one("work.place", string="Work Place")
    medical_id = fields.Many2one("medical.speciality", string="Medical Speciality")
    region_id = fields.Many2one("geographical.region", string="Geographical Region")
    last_name = fields.Char("Last Name")
    department_id = fields.Many2one("department", string="Department")
    brick_id = fields.Many2one("brick.ims", string="Brick IMS")
    is_health = fields.Boolean("is_health", copy=False)

    @api.onchange("state_id")
    def _onchange_region(self):
        if self.state_id:
            self.region_id = self.state_id.region_id.id
        else:
            self.region_id = False

    @api.onchange("industry_id")
    def _onchange_industry(self):
        if self.industry_id:
            if self.industry_id.name == "Health/Social":
                self.is_health = True
            else:
                self.is_health = False


class CountryState(models.Model):
    _inherit = "res.country.state"

    region_id = fields.Many2one("geographical.region", string="Region")
