#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Welcome():

    def getMenu(self, language):
        return {
            'address': '/', 
            'class': 'current',
            'text': 'Home'
        }
        
    def getDiv(self, language):
        return Null
        
    def getAdmin(self, language):
        return Null
        
def run():
    return Welcome()