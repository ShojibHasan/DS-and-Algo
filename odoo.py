import xlwt
import base64
import io
from datetime import datetime, timedelta,date
from odoo.addons.helper import utility
from dateutil.relativedelta import relativedelta
from odoo import api, exceptions, fields, models,_
from dateutil import rrule

class ProjectMemberAssignedDateExtend(models.TransientModel):
    _name = "project.member.assigned.date.extend"
    _description ="Project Member Assigned Date Extand Wizard"

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    def project_member_assigned_date_extand(self):
        previous = date.today().replace(day=1) - timedelta(days=1)

        records = self.env['project.project'].browse(self._context['active_id'])
        members = records.project_members
        startDate = self.start_date
        endDate = self.end_date
      

        exist_member = members.filtered(lambda i: get_only_month_year(i.last_assigned_date) >= str(previous.strftime('%Y-%m')))

        for i in exist_member:
            start = datetime.strptime(startDate, '%Y-%m-%d').date()
            end = datetime.strptime(endDate, '%Y-%m-%d').date()
            if end <= start:
                raise exceptions.ValidationError("Start date can not be getter then End Date")
            else:
                for j in i.member_invoice_ids:
                    while start < end:
                        start += relativedelta(months=1)
                        if str(start.strftime('%Y-%m')) > get_only_month_year(i.last_assigned_date):
                            monthly_invoice = {
                                'month_year': start,
                                'is_buffer': j.is_buffer,
                                'is_ojt': j.is_ojt,
                                'invoiced_percent': j.invoiced_percent,
                                'engaged_percent': j.engaged_percent,
                                'po_price': j.po_price,
                                'notes': j.notes,
                                'member_id': i.id,
                            }
                            member_invoice = self.env['monthly.member.invoice.line'].search([('member_id', '=', i.id)])
                            member_invoice.create(monthly_invoice)


def get_only_month_year(dep_date):
    get_dep_date = datetime.strptime(str(dep_date), '%Y-%m-%d')
    get_date = str(get_dep_date.year) + '-' + str(get_dep_date.month)
    if get_dep_date.month<10:
        get_date = str(get_dep_date.year) + '-0' + str(get_dep_date.month)
    return get_date




