# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Smile. All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields
from matrix_field import matrix



class smile_activity_workload(osv.osv):
    _name = 'smile.activity.workload'

    _columns = {
        'name': fields.char('Name', size=32),
        'period_id': fields.many2one('smile.activity.period', "Period", required=True),
        'start_date': fields.related('period_id', 'start_date', type='date', string="Start date", readonly=True),
        'end_date': fields.related('period_id', 'end_date', type='date', string="End date", readonly=True),
        'line_ids': fields.one2many('smile.activity.workload.line', 'workload_id', "Workload lines"),
        #'matrix_line_ids': matrix('line_ids', 'cell_ids', string="Workload lines", readonly=False),
        }

smile_activity_workload()



class smile_activity_workload_line(osv.osv):
    _name = 'smile.activity.workload.line'

    _columns = {
        'name': fields.char('Name', size=32),
        'workload_id': fields.many2one('smile.activity.workload', "Workload", required=True, ondelete='cascade'),
        }

smile_activity_workload_line()