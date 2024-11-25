
from odoo import fields, models, _


class Job(models.Model):
    _inherit = "hr.job"

    recruitment_survey_id = fields.Many2one('survey.survey', "Recruitment Survey", help="Choose an survey form for this job position")
