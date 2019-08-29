#!/usr/bin/env python3
import sys

#def really_parse(strg, char):
#    index = strg.find(char)
#    print(strg, char, index)
#    print(strg[:index+1])

#def get_ip(line):
    #this will take in a line
#    line = line.strip().split(' ')
#    ip_list = line[0]
#    character = line[1]
#    print(line, string, character)

def src_ip():
    

def main():
    filename = sys.argv[1]
    #read first file in command line
    f = open(filename, 'r')
    #open and read file given in command line
    lines = f.readlines()
    print()

if __name__ = '__main__':
    main()

#Get a log file, read the log file from command line
#First we will collect IP sources
#Look at each line in the iptablesyslog
#If the characters SRC= appears, then split the line and collect the characters that follow the '=' until you reach the first space
#If the IP is unique, add the ip to a list of source ips with the count 1
#IF the IP is not unique, increase the count on the existing IP by 1
#continue looking at each line until there are no more lines to look at
#return the list of source ip addresses

#next we will collect IP destinations
#Look at each line in the iptablesyslog
#If the characters DST= appears, then split the line and collect the characters that follow the '=' until you reach the first space
#If the IP is unique, add the ip to a list of source ips with the count 1
#If the IP is not unique, increase the count on the existing IP by 1
#continue looking at each line until there are no more lines to look at
#return the list of destination ip addresses

