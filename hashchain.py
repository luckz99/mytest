#!/usr/bin/env python2.7
import md5;
import sys;
import socket;

HOST = 'shell2017.picoctf.com';
PORT = 7691;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((HOST, PORT)); #Connect to server

s.recv(4096);
s.send('f\n'); #We would like to get flag
data = s.recv(4096);
user = data.split('\n')[0].split(' ')[5]; #get user id
data = s.recv(4096);
tkn = data.split('\n')[0]; #Get token

print("User: "+user+"\nToken: "+tkn);
seed = md5.new(user).hexdigest();
result = tkn;
print("Seed: "+seed);
found = False;
hashc = seed;

while(found == False):
	if (md5.new(hashc).hexdigest() == result):
		print("Hash found: "+hashc);
		found = True;
	else:
		hashc = md5.new(hashc).hexdigest();
#s.recv(4096)
print("Sending hash...");
s.send(hashc+'\n');
print(s.recv(4096));
