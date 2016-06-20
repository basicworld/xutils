# -*- coding: utf-8 -*-
"""
user-agent middleware for scrapy
"""
import random
# from xagent import AGENTS_ALL
from xagent import AGENTS

class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
