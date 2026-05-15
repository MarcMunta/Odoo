from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_linkedin_url = fields.Char(
        string="LinkedIn",
        help="URL del perfil de LinkedIn del cliente.",
    )
    x_instagram_url = fields.Char(
        string="Instagram",
        help="URL del perfil de Instagram del cliente.",
    )
