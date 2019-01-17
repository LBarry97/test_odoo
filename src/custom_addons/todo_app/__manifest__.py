{
    'name': 'To-Do Application',
    'description': 'Manage personal to-do tasks.',
    'author': 'Lansana Barry Sow',
    'depends': ['base'],
    'application': True,

    'data': [
        'security/todo_access_rules.xml',
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
}
