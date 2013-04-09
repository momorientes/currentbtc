# -*- coding: utf-8 -*-
#!/usr/bin/python2
"""
A phenny module to get MtGox BTC value 
momo@shackspace.de
Please donate to 1Np6AdhkRQS7CRAmFXcCNaadehA3nTsvKQ if you like it.
"""
import urllib, urllib2
import simplejson


def getMtGox(phenny, input):
    apiURL = "http://data.mtgox.com/api/1/BTCUSD/ticker"
    s = urllib2.urlopen(apiURL)#, eparams)
    r = s.read()
    r = r.strip()
    jsondata = r
    data = simplejson.loads(jsondata)
    if data['result'] == 'success':
        query = input.group(2)
        if query == "high":
            phenny.say(data['return']['high']['display'])
        elif query == "low":
            phenny.say(data['return']['low']['display'])
        elif query == "buy":
            phenny.say(data['return']['buy']['display'])
        elif query == "sell":
            phenny.say(data['return']['sell']['display'])
        elif not query:
            phenny.say(data['return']['last_all']['display_short'])
        else:
            phenny.say(input.nick + ": I don't know that command, but here's the current BTC price: " + data['return']['last_all']['display_short'])
    else:
        phenny.say("The Mt. Gox API is down or has changed.")

getMtGox.commands = ['btc','bitcoin']
getMtGox.priority = 'high'
