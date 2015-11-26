from .overview import Overview

OVERVIEW_URL = '/overview/heatpump'

class Heatpump(object):

    def __init__(self, session):
        self._session = session

    def get(self):
        status = self._session.get(OVERVIEW_URL)
        return [Overview('heatpump', val) for val in status]
