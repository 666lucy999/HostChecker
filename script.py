#
# Project: WORKING WITH MULTIPLE LINKS FROM A TEXT FILE
# Author: Lukhanyo Vakele
# Date: 20/06/2020
#

#modules we are going to need
from urllib import request as req
from datetime import datetime

#Get an array of host from our file
file = open('hosts.txt', 'r+')
raw_array = file.readlines()

# Let's loop through our raw array and remove all unwanted things
arr_links = [] # Init our filtered array

for item in raw_array:
    item = item.strip()
    if item != '':    
        arr_links.append(item)
    
#Choose a protocol for your test cases
protocol = 'https://'

# Lets loop through the array and open each link and print out the status code
# Before we do that let's check if we do have links in our array
if len(arr_links) != 0:
    print('[#] Now then let the magic start')
    working_hosts = [] # Init array of working hosts
    dummy_hosts = [] # Init array of dummy hosts
    weird_hosts = [] # Init array of weird hosts
    for link in arr_links:
        print()
        print('Now checking:',link)
        try:
            link = (link if('http' in link) else protocol+link)
            res = req.urlopen(link)
            cod = res.code
            print('Status Code:', cod)
            if cod == 200:
                working_hosts.append(link)
            else:
                weird_hosts.append(link)
        except:
            dummy_hosts.append(link)
            print('Host not working / Something is wrong with your internet connection')
            pass
else:
    print('Please make sure their are hosts in hosts.txt')


# Now then let's check if we found zero rated hosts
if len(working_hosts) != 0:
    wHost = open('Zero Rated Hosts.txt', 'a+')
    #write the zero rated host on each line
    wHost.write('######## Zero Rated Sites ########')
    wHost.write('\n')
    for host in working_hosts:
        wHost.write(host+'\n')
    #time stamp of last record
    wHost.write('######### '+datetime.now().strftime('%H:%M %d-%m-%Y')+' #########')
    wHost.write('\n'*2)
    #now then let's close the file
    wHost.close()    

# Now then let's check if we found dummy rated hosts
if len(dummy_hosts) != 0:
    dHost = open('Dummy Rated Hosts.txt', 'a+')
    #write the dummy rated host on each line
    dHost.write('######## Dummy Rated Sites ########')
    dHost.write('\n')
    for host in dummy_hosts:
        dHost.write(host+'\n')
    #time stamp of last record
    dHost.write('######### '+datetime.now().strftime('%H:%M %d-%m-%Y')+' #########')
    dHost.write('\n'*2)
    #now then let's close the file
    dHost.close()

# Now then let's check if we found weird rated hosts
if len(weird_hosts) != 0:
    wHost = open('Weird Rated Hosts.txt', 'a+')
    #write the dummy rated host on each line
    wHost.write('######## Weird Rated Sites ########')
    wHost.write('\n')
    for host in weird_hosts:
        wHost.write(host+'\n')
    #time stamp of last record
    wHost.write('######### '+datetime.now().strftime('%H:%M %d-%m-%Y')+' #########')
    wHost.write('\n'*2)
    #now then let's close the file
    wHost.close()

print("Created with pain and suffering by: Lukhanyo Vakele")
