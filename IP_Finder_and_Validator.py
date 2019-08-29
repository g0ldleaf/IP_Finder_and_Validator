#!/usr/bin/env python3
import sys
import re   #regex

def get_ips(logstring):
    #what is the ip_addr?
#    ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', logstring)
#    ips = re.findall('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', logstring)
    #make an empty string
    #make pattern with regex code to find IPs
    return ips

def count_ip(ips):
    #what is count?
    #make dictionary of ip count
    count = {}
    for ip in ips:
        if count.get(ip):
            count[ip] += 1
            #if you can get an ip, add one to the value of the key in the dictionary
        else:
            count[ip] = 1
            #set value to 1
    return count

#def is_valid():
    #True/False?


def format_ip_validator(max_ip_len, ip_addr, count, is_valid):
    pad_length = max_ip_len - len(ip_addr)      #max ip length minus # of charactrs in ip address
    padding = ' ' * pad_length
    output = []     #output is an empty list
    output.append('(%03d)' % count)
    output.append(' ' * (2 if is_valid else 1) + str(is_valid) + ':')
    output.append(padding)
    output.append(ip_addr)
    output.append(' *')
    return ''.join(output)

def main():
    filename = sys.argv[1]
    #read first file in command line
    f = open(filename, 'r')
    #open and read file given in command line
    logstring = f.read()
    ips = get_ips(logstring)
    print(count_ip(ips))

if __name__ == '__main__':
    main()

#Get a log file, read the log file from command line
# get_ips takes in lines and gives back a list of IP addresses
# 
