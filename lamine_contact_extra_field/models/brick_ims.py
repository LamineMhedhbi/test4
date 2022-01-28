from odoo import models, fields


class Brick(models.Model):
    _name = "brick.ims"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Brick IMS Name should be unique!")]

    name = fields.Char(string="Brick IMS")
