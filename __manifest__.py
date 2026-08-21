{
    'name': 'CHANGAN Zoo Management',
    'version': '17.0.1.0.0',
    'category': 'Operations/Zoo',
    'summary': 'Manage animals, living zones, and zookeepers for CHANGAN Zoo.',
    'description': """
        CHANGAN Zoo Management System
        - Track Animals
        - Manage Living Zones
        - Manage Zookeepers
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/animal_group_views.xml',
        'views/zookeeper_views.xml',
        'views/living_zone_views.xml',
        'views/animal_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
