#!/usr/bin/env python3
import sys

#def really_parse(strg, char):
#    index = strg.find(char)
#    print(strg, char, index)
#    print(strg[:index+1])

def get_ip(line):
    #this will take in a line
    line = line.strip().split(' ')
    ip_list = line[0]
    character = line[1]
#    print(line, string, character)
    #print the result to the screen

def main():
    filename = sys.argv[1]
    #read first file in command line
    f = open(filename, 'r')
    #open and read file given in command line
    lines = f.readlines()
    for line in lines:
        get_ip(line)
        #loop through each line in file

if __name__ = '__main__':
    main()

#Get a log file, read the log file from command line
#grab all IP addresses (all numbers with 4 octets)
#verify if each of the 4 octet numbers is a valid IP address by labeling as True or False
#count how many times each IP address shows up
#print IP addresses, along with # and True/False

