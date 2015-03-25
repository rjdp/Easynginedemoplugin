"""
Rtseconddemo plugin for Easyengine.

Created by: rajdeep <rajdeep.sharma@rtcamp.com>
License: MIT
URL: rtcamp.com

"""

from cement.core import handler
from cement.core.controller import CementBaseController, expose


class rteesitetestPluginController(CementBaseController):

    class Meta:
        # label uniquely identifies a controller(controller is a way of
        # grouping app commands/subcommands and the arguments they expect)
        label = "seconddemo"
        # the description applies to all the commands under this controller
        description = "Rtseconddemo Plugin for Easyengine."
        # the combined values of 'stacked_on' and 'stacked_type' determines
        # the position of controller's commands in cmd line app invocation
        stacked_on = 'site'
        stacked_type = 'nested'

    @expose(hide=True)
    def default(self):
        """this function is called when user fires 'ee site seconddemo' command"""
        print("this is 'ee site demo2' command ")

    @expose(help="first command under seconddemo subcommand nested on site command")
    def secdemocmd1(self):
        print("inside cmd1 under seconddemo")


def load(app):
    handler.register(rteesitetestPluginController)
