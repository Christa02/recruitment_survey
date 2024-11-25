from datetime import timedelta

from odoo import fields, models, _
from odoo.exceptions import UserError


class Applicant(models.Model):
    _inherit = "hr.applicant"

    recruitment_survey_id = fields.Many2one('survey.survey', related='job_id.recruitment_survey_id', string="Recruitment Survey", readonly=True)

    def action_send_survey(self):
        self.ensure_one()

        # if an applicant does not already has associated partner_id create it
        if not self.partner_id:
            if not self.partner_name:
                raise UserError(_('Please provide an applicant name.'))
            self.partner_id = self.env['res.partner'].sudo().create({
                'is_company': False,
                'name': self.partner_name,
                'email': self.email_from,
                'phone': self.partner_phone,
                'mobile': self.partner_mobile
            })

        self.recruitment_survey_id.check_validity()
        template = self.env.ref('recruitment_survey.mail_template_applicant_survey_invite', raise_if_not_found=False)
        local_context = dict(
            default_applicant_id=self.id,
            default_partner_ids=self.partner_id.ids,
            default_survey_id=self.recruitment_survey_id.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_email_layout_xmlid='mail.mail_notification_light',
            default_deadline=fields.Datetime.now() + timedelta(days=5)
        )

        return {
            'type': 'ir.actions.act_window',
            'name': _("Send an interview"),
            'view_mode': 'form',
            'res_model': 'survey.invite',
            'target': 'new',
            'context': local_context,
        }

