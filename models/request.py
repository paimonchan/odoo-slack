# -*- coding: utf-8 -*-

import json
import logging
import requests

from odoo import models
from werkzeug import urls
from odoo.tools import config

logger = logging.getLogger(__name__)

class Request(models.AbstractModel):
    _name = 'paimon.request'
    _base_url_config_key = ''