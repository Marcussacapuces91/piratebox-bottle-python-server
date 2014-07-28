#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from bottle import route, get, run, template, static_file, request
import os

class PirateBox10():
    def __init__(self, application, path):
        self._application = application
        print("Instancing plugin shoutbox... ", end='')
        self._shoutbox = application.getPlugin('shoutbox', path)
        if self._shoutbox == None: 
            raise Exception('The shoubox plugin is not running !')

    def staticfiles(self, file):
        return static_file(file, root='./plugins/piratebox10/www/')

    def page(self):
        return template('plugins/piratebox10/index',  
            homeMenu = ('Home'), 
            topNav =  [{
                'address': '/board', 
                'text': ('Forum')
            },{
                'address': '/Shared', 
                'text': ('Files')
            }],
            contents = [{
                'name': 'upload',
                'block': 'sidebar',
                'id': 'upload',
				'title': 'Upload',
				'div': 
                """<iframe width="100%" height="80" src='http://piratebox.lan:8080'>
					Your browser does not support iframes.. If you want to 
                    upload something, follow this
                    <a href='http://piratebox.lan:8080'>Link</a>.
				</iframe>
				<h3><a href="/Shared">Browse Files -></a></h3>"""
            },{
                'name': 'shoutbox',
                'block': 'main',
                'id': 'chat',
                'title': self._shoutbox.getTitle(),
                'div': self._shoutbox.getHTML()
            }]
		)
        
def run(application, path):
    pb = PirateBox10(application, path)
    get(path)(pb.page)
    get(path + 'index.htm')(pb.page)
    get(path + 'index.html')(pb.page)     
    get(path + 'piratebox10/<file:path>')(pb.staticfiles)   

    
    return pb  