import stomp
import sys
import getopt
import time
import logging

class SimpleListener(object):
    def on_error(self, headers, message):
        print('received an error %s'%message)
    def on_message(self, headers, message):
        print('received a message %s (%s)'%(message, headers))

def listen():
    con = stomp.Connection(host_and_ports=[('localhost', 61613)])
    con.set_listener('', SimpleListener())
    con.start()
    con.connect()
    
    con.subscribe(destination='/queue/test', id=1, ack='auto', headers={'transformation' : 'jms-map-json'})
    
    time.sleep(60)
    con.disconnect()
