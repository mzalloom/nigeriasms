#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import rapidsms
import datetime

class App(rapidsms.app.App):

    def configure (self, title="Message Tester", tab_link="/http", host="http://192.168.10.20", port=8000):
        # overridden by App and Backend subclasses
        self._port = int(port) 
        self._host = host
        # aw poop.  where can i stick these?  how about some ugly
        # global variables for now
    
    def handle(self, message):
    
        self.debug("got message %s", message.text)
        response = "You said: %s" % message.text
        self.debug("responding with %s", response)
        message.respond(response)
        return True
        
    def outgoing(self, message):
        pass

    @property
    def port(self):
        return self._port
    
    @property
    def host(self):
        return self._host
