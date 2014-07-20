#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, get, run, template, static_file, request
from gettext import translation, find
import os

class PirateBox10():
    def __init__(self, application):
        self._application = application

    def getTranslation(self, acceptlanguage):
        r = []
        for langue in acceptlanguage.split(','):
            try:
                l, q = langue.split(';')
            except ValueError:
                l = langue
            r.append(l)
        return translation('piratebox10', os.path.join(os.path.dirname(__file__), 'locale'), languages=r)  


    def page(self):
        t = self.getTranslation(request.headers['Accept-Language'])        
        if t == None:
            _ = lambda text: text
        else:
            _ = t.gettext
    
#        menuWelcome = self._plugins['welcome'].getMenu(language='')
    
        return template(os.path.join(os.path.dirname(__file__), 'index'),  
            webTitle = _('PirateBox - Share Freely'),
            iconTitle = _('PirateBox - Share Freely'),
            homeMenu = _('Home'), 
            topNav =  [{
                'address': '/board', 
                'text': _('Forum')
            },{
                'address': '/Shared', 
                'text': _('Files')
            }],
            aboutMenu = _('About'),
            contents = [{
                'block': 'top',
                'id': 'welcome',
                'title': _('Welcome'),
                'div': 
                _("""<p>Now, first of all, there is nothing illegal or scary going on 
                here. This is a social place where you can chat and share files 
                with people around you, <strong>anonymously</strong>! This is an 
                off-line network, specially designed and developed for 
                file-sharing and chat services. Staying off the grid is a 
                precaution to maintain your full anonymity. Please have fun, 
                chat with people, and feel free to share any files you may like.</p>
                <input id="thanks" class="button" type="submit" value="Thanks">""")
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
            footerTitle = _("About PirateBox"),
            footerContent = _(
		"""<p>Inspired by pirate radio and the free culture movment, PirateBox is a self-contained mobile collaboration and file sharing device. PirateBox utilizes Free, Libre and Open Source software (FLOSS) to create mobile wireless file sharing networks where users can anonymously share images, video, audio, documents, and other digital content.</p>
		<p>PirateBox is designed to be safe and secure. No logins are required and no user data is logged. The system is purposely not connected to the Internet in order to prevent tracking and preserve user privacy.</p>
		<small>PirateBox is licensed under GPLv3.</small>""")
		)
        
def run(application, path):
    pb = PirateBox10(application)
    get(path)(pb.page)
    get(path + 'index.htm')(pb.page)
    get(path + 'index.html')(pb.page)        
    
    return pb  