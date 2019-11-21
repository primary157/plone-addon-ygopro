# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from rapido.core import app
import requests


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.ygopro:uninstall',
        ]


def post_install(context):
    """Post install script"""
    app.safe_modules.requests = requests


def uninstall(context):
    """Uninstall script"""
    app.safe_modules.requests = requests
    del app.safe_modules.requests
