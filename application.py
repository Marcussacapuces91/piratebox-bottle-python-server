#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os, sys
from importlib import import_module
from bottle import route, get, run, template, static_file
import ConfigParser
from gettext import gettext as _

class Application:
    """
    Application Class calling the first plugins.
    """
    
    def __init__(self):
        """
        Init method.
        Looks for plugins' and run WebServer.
        """
        PLUGINS_FOLDER = 'plugins'
        MAIN_MODULE = '__init__'
        
        self._plugins = {};
        self._path = '/'
        
# load all (!) plugins
        for plugin in os.listdir(PLUGINS_FOLDER):
            location = os.path.join(PLUGINS_FOLDER, plugin)
            if not os.path.isdir(location) or \
               not MAIN_MODULE + '.py' in os.listdir(location):
                continue
            cmd_folder = os.path.abspath(location)
            if cmd_folder not in sys.path:
                sys.path.insert(0, cmd_folder)
            
            print(_("Loading plugin %s... " % (str(plugin))), end='')
            self._plugins[plugin] = import_module(MAIN_MODULE)
            print(_("Ok."))
            
    def run(self, plugins, host, port, debug=False, reloader=False, interval=1):
#        for plugin in plugins:
#            print(_("Running plugin %s... " % (str(plugin))), end='')
#            self._plugins[plugin].run(self, self._path)
#            print(_("Ok."))

# run the web server
        run(host=host, port=port, debug=debug, reloader=reloader, interval=interval)

@route('/<filepath:path>')
def staticFiles(filepath):
    return static_file(filepath, root='./www/')

if __name__ == '__main__':
#    config = configparser.ConfigParser(allow_no_value=True)  # for plugins' name
    config = ConfigParser.RawConfigParser({
            'host': '0.0.0.0',
            'port': 80,
            'debug': 'false',
            'reloader': 0 
        }, 
        allow_no_value=True)
    config.read('application.cfg')
    
    app = Application()
        
    port = int(os.environ.get('PORT', config.getint('server', 'port')))
    app.run(
        plugins=config.items('plugins'), 
        host=config.get('server', 'host'), 
        port=port, 
        debug=config.getboolean('server', 'debug'), 
        reloader=(config.getint('server', 'reloader') > 0),
        interval=config.getint('server', 'reloader')
    )

    
    
    