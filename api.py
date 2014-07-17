#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import imp
from bottle import route, get, run, template, static_file
import configparser

class Application:
    """
    Application Class for the main plugin.
    """
    
    def __init__(self, path, host, port, debug=False, reloader=False):
        """
        Init method.
        Looks for plugins' and run WebServer.
        """
        PLUGINS_FOLDER = './plugins'
        MAIN_MODULE = '__init__'
        
        self._plugins = {}
        self._path = path
        get(path)(self.portal)
        get(path + 'index.htm')(self.portal)
        get(path + 'index.html')(self.portal)
        
# load plugins
        for plugin in os.listdir(PLUGINS_FOLDER):
            location = os.path.join(PLUGINS_FOLDER, plugin)
            if not os.path.isdir(location) or \
               not MAIN_MODULE + '.py' in os.listdir(location):
                continue
            info = imp.find_module(MAIN_MODULE, [location]) 
            try:
                self._plugins[plugin] = imp.load_module(MAIN_MODULE, *info).run()
            except AttributeError as e:
                print("Plugin '{}' MUST have a run() method. Plugin ignored.".format(plugin))

    def run(self):
# run the web server
        run(host=host, port=port, debug=debug, reloader=reloader)

    def portal(self):
        
        menuWelcome = self._plugins['welcome'].getMenu(language='')
    
        return template('index', 
            webTitle='PirateBox - Share Freely',
            iconTitle='PirateBox - Share Freely',
            topNav =  [menuWelcome, {
                'address': '/board', 
                'text': 'Forum'
            },{
                'address': '/Shared', 
                'text': 'Files'
            },{
                'address': '#about', 
                'text': 'About'
            }],
            contents = [{
                'block': 'top',
                'id': 'welcome',
                'title': 'Welcome',
                'div': 
                """<p>Now, first of all, there is nothing illegal or scary going on 
                here. This is a social place where you can chat and share files 
                with people around you, <strong>anonymously</strong>! This is an 
                off-line network, specially designed and developed for 
                file-sharing and chat services. Staying off the grid is a 
                precaution to maintain your full anonymity. Please have fun, 
                chat with people, and feel free to share any files you may like.</p>
                <input id="thanks" class="button" type="submit" value="Thanks">"""
            },{
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
            }],
            footer = 
            """<p class="to-top"><a href="#header">Back to top</a></p>
		<h2>About PirateBox</h2>
		<p>Inspired by pirate radio and the free culture movment, PirateBox is a self-contained mobile collaboration and file sharing device. PirateBox utilizes Free, Libre and Open Source software (FLOSS) to create mobile wireless file sharing networks where users can anonymously share images, video, audio, documents, and other digital content.</p>
		<p>PirateBox is designed to be safe and secure. No logins are required and no user data is logged. The system is purposely not connected to the Internet in order to prevent tracking and preserve user privacy.</p>
		<small>PirateBox is licensed under GPLv3.</small>"""

        )
    


@route('/<filepath:path>')
def staticFiles(filepath):
    return static_file(filepath, root='./www/')

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('application.cfg')
    
    port = int(os.environ.get('PORT', config.getint('server','port', 8080)))
    app = Application('/', host='0.0.0.0', port=port, debug=True, reloader=True)
    app.run()

    
    
    