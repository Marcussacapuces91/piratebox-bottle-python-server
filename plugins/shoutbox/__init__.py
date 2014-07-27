#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


class ShoutBox():
    def __init__(self, application, path):
        self._application = application
        self._path = path

    def getMenu(self):
        return Null
        
    def getTitle(self):
        return 'Chat'
        
    def getHTML(self):
        return """
                <h2>Chat</h2>
				<div id="shoutbox" class="shoutbox_content"></div>
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
				</form>
"""        
        
def run(application, path):
    sb = ShoutBox(application, path)
    return sb  