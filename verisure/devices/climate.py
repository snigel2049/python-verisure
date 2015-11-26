from .overview import Overview

OVERVIEW_URL = '/overview/climatedevice'

class Climate(object):

    def __init__(self, session):
        self._session = session

    def get(self):
        status = self._session.get(OVERVIEW_URL)
        return [Overview('climate', val) for val in status]
