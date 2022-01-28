from odoo import models, fields


class Department(models.Model):
    _name = "department"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Department Name should be unique!")]

    name = fields.Char(string="Department")
