# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    active = fields.Boolean(
        string='Active',
        default=True,
        copy=False)
