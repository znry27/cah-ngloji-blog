# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _
import datetime

class MyService(models.Model):    
    _name = 'my.service'
    _description = 'Service'

    customer = fields.Char(string="Nama Pelanggan")
    device = fields.Char(string="Nama Mesin")
    device_sn = fields.Char(string="Serial Number Mesin")
    is_guarantee = fields.Boolean(string="Garansi",default=False)
    description = fields.Text(string="Keluhan Pelanggan")
    service_date = fields.Datetime(string="Tanggal Service",default=fields.Datetime.now)
    scheduled_date = fields.Datetime(string="Perkiraan Selesai",default=fields.Datetime.now)
    finish_date = fields.Datetime(string="Tanggal Selesai")
    take_by_customer_date = fields.Datetime(string="Tanggal Ambil")
    type_of_service = fields.Selection([
            ('normal','Normal'),
            ('quick','Kilat'),
            ('extra','Super Kilat')
        ],default='normal',string="Tipe Service")
    state = fields.Selection([
            ('draft','Draft'),
            ('in_progress','In Progress'),
            ('stuck','Stuck'),
            ('cancel','Cancelled'),
            ('finish','Finish'),
            ('take','Take by User')
        ],default='draft')


    @api.multi
    def update_form_to_in_progress(self):
        for record in self:
            record.write({'state':'in_progress'})


    @api.multi
    def update_form_to_cancel(self):
        for record in self:
            record.write({'state':'cancel'})


    @api.multi
    def update_form_to_finish(self):
        for record in self:
            record.write({'state':'finish','finish_date':datetime.datetime.now()})

