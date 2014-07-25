#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, get, run, template, static_file, request
import os

class PirateBox10():
    def __init__(self, application):
        self._application = application

    def staticfiles(self, file):
        return static_file(file, root='./plugins/piratebox10/www/')

    def page(self):
        return template(os.path.join(os.path.dirname(__file__), 'index'),  
            homeMenu = ('Home'), 
            topNav =  [{
                'address': '/board', 
                'text': ('Forum')
            },{
                'address': '/Shared', 
                'text': ('Files')
            }],
            contents = [{
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
                'block': 'main',
                'id': 'chat',
                'title': 'Chat',
                'div':
                """<div id="shoutbox" class="shoutbox_content"></div>
				<form method="POST" name="psowrte" id="sb_form" >
					<div id="shoutbox-input">
						<input class="nickname" type="text" 	name="name" 	value="Anonymous" placeholder="Nickname">
						<input class="message" 	type="text" 	name="data" 	placeholder="Message...">
						<input class="button" 	type="submit" 	name="submit" 	value="Send">
					</div>
					<div id="shoutbox-options">
						<h3>Text Color:</h3>
						<label for="def" 	class="bg-black">	<input name="color" type="radio" value="def" 	id="def" checked>Default</label>
						<label for="blue" 	class="bg-blue">	<input name="color" type="radio" value="blue" 	id="blue"		>Blue</label>
						<label for="green" 	class="bg-green">	<input name="color" type="radio" value="green" 	id="green"		>Green</label>
						<label for="orange" class="bg-orange">	<input name="color" type="radio" value="orange" id="orange"		>Orange</label>
						<label for="red" 	class="bg-red">		<input name="color" type="radio" value="red" 	id="red"		>Red</label>
					</div>
				</form>"""
            }]
		)
        
def run(application, path):
    pb = PirateBox10(application)
    get(path)(pb.page)
    get(path + 'index.htm')(pb.page)
    get(path + 'index.html')(pb.page)     
    get(path + 'piratebox10/<file:path>')(pb.staticfiles)   

    
    return pb  