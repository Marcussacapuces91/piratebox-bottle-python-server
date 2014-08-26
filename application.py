#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import os, sys
from imp import find_module, load_module
from bottle import Bottle, mount, route, get, run, template, static_file, view
import ConfigParser

class PirateBox(Bottle):
    """
    Main class application.
    Use factory function to instanciate the class.
    """
    
    def __init__(self):
        """Constructor. Call inherited class Bottle."""
        Bottle.__init__(self)
        self._plugins = self._loadAllPlugins()
        self._subapp = {}
        self._style = None

    def run(self, plugins, style, **kwargs):
        self._style = style
        self.get('/<filepath:path>')(self._staticFiles)
        self._subapp = {}
        for p in plugins:
            self._subapp[p[0]] = (self._plugins[p[0]])(self, p[1])
            self.mount('/' + p[0], self._subapp[p[0]])
            
        self.get('/')(self._index)
        self.get('/manifest.json')(self._manifest)
        Bottle.run(self, **kwargs)

    def _index(self):
        return template(
            'styles/' + self._style + '/index',
            topNav = [self._subapp[a].getTopNav() for a in self._subapp if self._subapp[a].getTopNav()],
            mainContent = [self._subapp[a].getHTML() for a in self._subapp if self._subapp[a].getHTML()],
            plugins = self._subapp
        )

    def pageTemplate(self, **kwargs):
        return template(
            'styles/' + self._style + '/others',
            topNav = [self._subapp[a].getTopNav() for a in self._subapp if self._subapp[a].getTopNav()],
            **kwargs
        )
        
    def _manifest(self):
        return {
            "locales": ["en", "fr"],
            "default_locale": "en",
            "resources": [
                "/{{locale}}/strings.l20n"
            ] + [self._subapp[a].getLocales() for a in self._subapp if self._subapp[a].getLocales()]
        }        
    
    def _staticFiles(self, filepath):
        return static_file(filepath, root='styles/' + self._style + '/www/')

    def _loadAllPlugins(folder='plugins', main_module='__init__'):
        """Class method returning all plugins"""
        PLUGINS_FOLDER = 'plugins'
        MAIN_MODULE = '__init__'
        
        plugins = {}
        for plugin in os.listdir(PLUGINS_FOLDER):
            # Fast path: see if the module has already been imported.
            try:
                plugins[plugin] = sys.modules[plugin]
                # silently pass
                continue
            except KeyError:
                pass
        
            # Search for module's path        
            location = os.path.join(PLUGINS_FOLDER, plugin)
            if not os.path.isdir(location) or \
               not main_module + '.py' in os.listdir(location):
                continue
            try:
                path = [os.path.abspath(location)] 
                print("Loading plugin {}... ".format(plugin), end='')
                f, filename, description = find_module(main_module, path)
                try:
                    plugins[plugin] = (load_module(main_module, f, filename, description)).factory
                    print("Ok.")
                finally:
                    if f: f.close()
            except Exception as e:
                print("KO with exception {}.".format(e))
        return plugins


if __name__ == '__main__':
#    config = configparser.ConfigParser(allow_no_value=True)  # for plugins' name
    config = ConfigParser.RawConfigParser(
#        {
#            'host': '0.0.0.0',
#            'port': 80,
#            'debug': 'false',
#            'reloader': 0 
#        }, 
        allow_no_value=True)
    config.read('application.cfg')
    
    app = PirateBox()
    app.run(
        plugins = config.items('plugins'), 
        style = 'piratebox10',
        host = config.get('server', 'host'), 
        port = config.getint('server', 'port'), 
        debug = config.getboolean('server', 'debug'), 
        reloader = (config.getint('server', 'reloader') > 0),
        interval = config.getint('server', 'reloader')
    )    
    
    