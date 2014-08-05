import types
import textwrap
from docopt import docopt
import inspect
import sys
import importlib
from cmd3.shell import command
from pprint import pprint

from cloudmesh.config.cm_projects import cm_projects

from cloudmesh_common.logger import LOGGER

log = LOGGER(__file__)


class cm_shell_project:

    """opt_example class"""

    def _load_projects(self):
        if not self.cm_shell_project_loaded :
            filename = "$HOME/.futuregrid/cloudmesh.yaml"
            self.projects = cm_projects(filename)
            if self.echo:
                log.info(
                    "Reading project information from -> {0}".format(filename))
            self.cm_shell_project_loaded = True
        
    def activate_shell_project(self):
        self.register_command_topic('cloud','project')
        #
        # BUG this should be done outside of the activate
        #
        self.cm_shell_project_loaded = False
        pass

    @command
    def do_project(self, args, arguments):
        """
        Usage:
               project info [--json]
               project default NAME
               project NOTIMPLEMENTED members
               
        Manages the project

        Arguments:

          NAME           The name of the project


        Options:

           -v       verbose mode

        """
        # log.info(70 * "-")
        # log.info(arguments)
        # log.info(70 * "-")

        if arguments["default"] and arguments["NAME"]:
            log.info("sets the default project")

            self._load_projects()
            project = arguments["NAME"]
            #if project in self.projects.names("active"):
            #    self.projects.default(project)

            print project
            return
        
        elif arguments["info"]:

            self._load_projects()
            
            # log.info ("project info for all")
            if arguments["--json"]:
                print self.projects.dump()
                return
            else:
                print
                print "Project Information"
                print "-------------------"
                print
                if self.projects.names("default") is not "" and not []:
                    print "%10s:" % "default", self.projects.names("default")
                else:
                    print "%10s:" % "default ", \
                          "default is not set, please set it"
                if len(self.projects.names("active")) > 0:
                    print "%10s:" % "projects", \
                        ', '.join(self.projects.names("active"))


                if len(self.projects.names("completed")) > 0:
                    print "%10s:" % "completed", \
                        ', '.join(self.projects.names("completed"))
                print

            return

        elif arguments["members"]:
            log.info("list the project members")
            return

        else:
            log.info("NOT IMPLEMENTED")
            return
            
