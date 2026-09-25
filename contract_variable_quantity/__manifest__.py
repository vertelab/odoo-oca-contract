# Copyright 2016-2019 Tecnativa - Pedro M. Baeza
# Copyright 2018 Tecnativa - Carlos Dauden
# Copyright 2019 ACSONE SA/NV
# Copyright 2024 Tecnativa - Carolina fernandez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Variable quantity in contract recurrent invoicing",
    'summary': "Adds variable quantities to contract lines.",
    'description': '''
Variable quantity in contract recurrent invoicing
=================================================

    Adds variable quantities to contract lines.

    Features:

        - UI Integration: Extends 6 view(s) in the Odoo interface.
        - Extends Odoo: Builds on contract.abstract.contract.line, contract.contract, contract.line, contract.line.qty.formula.
    ''',
    "version": "18.0.1.0.0",
    "category": "Contract Management",
    "license": "AGPL-3",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-contract/contract_variable_quantity",
    "depends": ["contract"],
    "data": [
        "security/ir.model.access.csv",
        "views/abstract_contract_line.xml",
        "views/contract_line_formula.xml",
        "views/contract_line_views.xml",
        "views/contract_template.xml",
        "views/contract.xml",
        "views/contract_portal_templates.xml",
    ],
    "installable": True,
}
