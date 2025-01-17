# Copyright 2017-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017-2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2017-2018 Dinar Gabbasov <https://it-projects.info/team/GabbasovDinar>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Sync POS orders across multiple sessions""",
    "summary": """Use multiple POS for handling orders""",
    "category": "Point Of Sale",
    # "live_test_url": 'http://apps.it-projects.info/shop/product/pos-multi-session?version=12.0',
    "images": ["images/pos-multi-session.png"],
    "version": "12.0.4.2.10",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "pos@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/12.0/pos_multi_session/",
    "license": "LGPL-3",
    "price": 360.00,
    "currency": "EUR",

    "depends": [
        "pos_multi_session_sync"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/pos_multi_session_data.xml",
        "security/ir.model.access.csv",
        "views/pos_multi_session_views.xml",
        "multi_session_view.xml"
    ],
    "qweb": [
        "static/src/xml/pos_multi_session.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": False,

    "demo_title": "Sync POS orders across multiple sessions",
    "demo_addons": [
        "pos_disable_payment",
        "pos_multi_session_sync",
        "pos_multi_session_restaurant",
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-multi-session",
    "demo_summary": "Use multiple POSes for handling orders",
    "demo_images": [
        "images/pos-multi-session.png",
    ]
}
