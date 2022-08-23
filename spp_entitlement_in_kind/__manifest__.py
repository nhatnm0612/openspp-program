# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP Program Entitlement (In-Kind)",
    "category": "OpenSPP",
    "version": "15.0.0.0.1",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp-project/openspp-program",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "stock",
        "g2p_registry_base",
        "g2p_programs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/main_view.xml",
        "views/entitlement_manager_view.xml",
        "views/entitlement_view.xml",
        "wizard/create_program_wizard.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}