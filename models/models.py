# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Books(models.Model):
	_name = 'book'


	name = fields.Char(string='Book Name')
	author = fields.Many2one('author', string='Author')
	year = fields.Char(string='Year')


class Author(models.Model):
	_name = 'author'

	name = fields.Char(string="First Name")
	surname = fields.Char(string="Last Name")