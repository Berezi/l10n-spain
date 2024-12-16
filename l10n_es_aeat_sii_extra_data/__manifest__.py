# Copyright 2024 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Suministro Inmediato de Información en el IVA Datos Extra",
    "version": "14.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/OCA/l10n-spain",
    "author": "AvanzOSC, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "development_status": "Production/Stable",
    "maintainers": ["avanzosc"],
    "depends": [
        "l10n_es_aeat_sii_oca",
        "l10n_es_extra_data",
    ],
    "data": [
        "data/aeat_sii_map_data.xml",
    ],
}
