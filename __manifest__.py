{
    'name' : 'Recruitment - Survey',
    'version' : '1.0',
    'summary': 'Recruitment & Survey',
    'sequence': 10,
    'description': "",
    'category': 'Recruitment/Survey',
    'depends': ['hr_recruitment', 'survey'],
    'data': [
        'views/hr_applicant_views.xml',
        'views/hr_job_views.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
