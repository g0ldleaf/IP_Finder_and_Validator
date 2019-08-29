#!/usr/bin/env python3
import sys

def really_parse(strg, char):
    index = strg.find(char)
#    print(strg, char, index)
    print(strg[:index+1])

def process(line):
    #this will take in a line
    line = line.strip().split(' ')
    string = line[0]
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
        process(line)
        #loop through each line in file

if __name__ = '__main__':
    main()
