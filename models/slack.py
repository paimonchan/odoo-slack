import requests
from odoo import models
from werkzeug import urls
from ..helpers import const

class Slack(models.AbstractModel):
    _name = 'paimon.slack'

    def _construct_url(self, endpoint):
        base_url = const.API_SLACK
        return urls.url_join(base_url, endpoint)

    def post_message(self, channel, message):
        """
        REF: https://api.slack.com/methods/chat.postMessage
        """
        method = 'chat.postMessage'
