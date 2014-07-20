#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from importlib import import_module
from importlib.util import find_spec
from bottle import route, get, run, template, static_file
import configparser
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
            print(_("Loading plugin %s... " % (str(plugin))), end='')
            self._plugins[plugin] = import_module(location.replace('\\', '.') + '.' + MAIN_MODULE)
            print(_("Ok."))
            
    def run(self, plugins, host, port, debug=False, reloader=False, interval=1):
        for plugin in plugins:
            print(_("Running plugin %s... " % (str(plugin))), end='')
            self._plugins[plugin].run(self, self._path)
            print(_("Ok."))

# run the web server
        run(host=host, port=port, debug=debug, reloader=reloader, interval=interval)

@route('/<filepath:path>')
def staticFiles(filepath):
    return static_file(filepath, root='./www/')

if __name__ == '__main__':
#    config = configparser.ConfigParser(allow_no_value=True)  # for plugins' name
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('application.cfg')
    configServer = config['server']
    
    app = Application()
    
    port = int(os.environ.get('PORT', configServer.get('port', 8080)))
    app.run(
        plugins=config['plugins'], 
        host=configServer.get('host', '0.0.0.0'), 
        port=port, 
        debug=configServer.getboolean('debug', False), 
        reloader=(int(configServer.get('reloader', 0)) > 0),
        interval=int(configServer.get('reloader', 0))
    )

    
    
    