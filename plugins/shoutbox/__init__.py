#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from bottle import Bottle, post, get, response, HTTPError # route, get, run, template, static_file, request
from datetime import datetime

import hashlib


class ShoutBox(Bottle):
    def __init__(self, application):
        Bottle.__init__(self)
        self._application = application
        self._path = '/shoutbox'
        self._chat = [(datetime.now(), "PirateBox", "Chat and share files anonymously!", "def")]
        self._etag = hashlib.sha1(str(self._chat)).hexdigest()

        self.get('/content')(self._getContent)
        self.post('/line')(self._addLine)

    def getTopNav(self):
        return None

    def getLocales(self):
        return None

    def getHTML(self):
        return """
                <h2>Chat</h2>
				<div id="shoutbox" class="shoutbox_content"></div>
                <script language="javascript">

function displayShoutbox() {
    $.get('/shoutbox/content', function(data) {
   	    $('div#shoutbox').html(data);
        mytime=setTimeout('displayShoutbox()', 10000);
   	});
}

function sendChat() {
	$.post("/shoutbox/line" , $("#sb_form").serialize())
	.success(function() {
		displayShoutbox();
	});
	$('#shoutbox-input .message').val('');
}

$('div#shoutbox').ready(function() {
    displayShoutbox();
});

                </script>
				<form method="POST" name="psowrte" id="sb_form" action="javascript:sendChat();">
					<div id="shoutbox-input" data-l10n-id="shoutbox_input_block">                                     
						<input class="nickname" type="text" 	name="name" 	placeholder="Nickname" value="Anonymous"/>
						<input class="message" 	type="text" 	name="data" 	placeholder="Message..." />
						<input class="button" 	type="submit" 	name="submit" 	value="Send" />
					</div>
					<div id="shoutbox-options">
						<h3 data-l10n-id="shoutbox_color_title">Text Color:</h3>
						<label for="def" 	class="bg-black"  data-l10n-id="shoutbox_default"> <input name="color" type="radio" value="def" 	id="def" checked />Default</label>
						<label for="blue" 	class="bg-blue"   data-l10n-id="shoutbox_blue">	   <input name="color" type="radio" value="blue" 	id="blue"		 />Blue</label>
						<label for="green" 	class="bg-green"  data-l10n-id="shoutbox_green">   <input name="color" type="radio" value="green" 	id="green"		 />Green</label>
						<label for="orange" class="bg-orange" data-l10n-id="shoutbox_orange">  <input name="color" type="radio" value="orange"  id="orange"		 />Orange</label>
						<label for="red" 	class="bg-red"    data-l10n-id="shoutbox_red">	   <input name="color" type="radio" value="red" 	id="red"		 />Red</label>
					</div>
				</form>
"""        

    def _addLine(self):
        now = datetime.now()
        name = request.forms.get('name')
        data = request.forms.get('data')
        color = request.forms.get('color')
        self._chat.append((now, name, data, color))
        self._etag = hashlib.sha1(str(self._chat)).hexdigest()
        raise HTTPError(204)

    def _getContent(self):
        if request.get_header('If-None-Match') == self._etag:
            raise HTTPError(304)
        response.set_header('ETag', self._etag)
        return template('plugins/shoutbox/chat_content', chat=self._chat)   
        
        
def factory(application, options):
    sb = ShoutBox(application)
    return sb