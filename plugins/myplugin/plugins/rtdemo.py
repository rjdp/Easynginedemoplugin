"""
Rtdemo plugin for Easyengine.

Created by: rajdeep <rajdeep.sharma@rtcamp.com>
License: MIT
URL: rtcamp.com

"""

from cement.core import handler
from cement.core.controller import CementBaseController, expose


class rteedemoPluginController(CementBaseController):

    class Meta:
        label = "rtdemo"
        description = "Rtdemo Plugin for Easyengine."
        stacked_on = 'base'
        stacked_type = 'embedded'
        arguments = [
            (['--foo'],
             dict(action='store', help='the infamous foo option')),
            ]

    @expose(help="demo plugin")
    def demo(self):
        print("this is result of running 'ee demo' command")
        if self.app.pargs.foo:
            print("Received option: foo => %s" % self.app.pargs.foo)


def load(app):
    handler.register(rteedemoPluginController)
