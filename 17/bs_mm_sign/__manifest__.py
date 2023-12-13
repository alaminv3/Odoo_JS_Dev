# -*- coding: utf-8 -*-
{
    'name': "Bista Sign Customisation",

    'summary': "Bista Sign Customisation",

    'description': """
    Modification in Sign module
    """,
    "license": "OPL-1",
    'author': "Bista Solutions",
    'website': "https://www.yourcompany.com",

    'category': 'Sign',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sign'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_medical_history_tag.xml',
        'data/family_medical_history_tag.xml',
        'views/sign_item_views.xml',
        'views/medical_history_views.xml',
        'views/inherite_res_partner_views.xml',
        'views/inherite_crm_lead_views.xml',
        'views/sign_item_option_views.xml',
        'views/patient_medical_tag_views.xml',
        'views/family_medical_tag_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bs_mm_sign/static/src/js/sign_template/sign_item_custom_popover.js',
            'bs_mm_sign/static/src/js/sign_template/sign_template_body.js',
            'bs_mm_sign/static/src/js/sign_template/sign_template_iframe.js',
            'bs_mm_sign/static/src/js/sign_template/sign_template_action.js',
            'bs_mm_sign/static/src/js/sign_template/sign_item_custom_popover.xml',
        ],
    }
}
