#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Script para recuperar senha das configurações do Remmina 

import glob
import base64
import ConfigParser
from Crypto.Cipher import DES3
from os.path import expanduser

config = ConfigParser.RawConfigParser()
config.read(expanduser('~')+'/.remmina/remmina.pref')
secretEncoded = config.get('remmina_pref', 'secret')

files = glob.glob(expanduser('~')+'/.remmina/*.remmina')

for configFile in files:
	config = ConfigParser.RawConfigParser()
	config.read(configFile)

	passwordEncoded = config.get('remmina','password')
	name = config.get('remmina','name')
	server = config.get('remmina','server')

	secret = base64.decodestring(secretEncoded)
	password = base64.decodestring(passwordEncoded)
	print 'Remmina config'
	print '--------------'
	print 'file:     ' + configFile
	print 'name:     ' + name
	print 'server:   ' + server
	print 'password: ' + DES3.new(secret[:24], DES3.MODE_CBC, secret[24:]).decrypt(password)
	print ''

