#!/usr/bin/python

import commands

#Format => var = commands.getoutput("cmd")

#Variables
#host - hostname
#load - Load Averages
#cpu - CPU Usage
#cores - No of cores
#uptime - System Uptime
#memreal - Free Memory
#memcache - Cached Memory
#swap - Swap in use
#disk - Disk usage
#usernames - Logged in users
#usersrc - Sources of logged in users
#ospretty - Os name from /etc/os-release
#whether - Whether from wttr.in


global ospretty
host = commands.getoutput("hostname")
load = commands.getoutput("cat /proc/loadavg")
cpu = commands.getoutput("ps -eo pcpu | awk 'NR>1' | awk '{tot=tot+$1} END {print tot}'")
cores = commands.getoutput("cat /proc/cpuinfo | grep -c processor")
uptime = commands.getoutput("uptime | awk '{ print $3,$4 }' | cut -f1")
memreal = commands.getoutput("free -h | head -n 2 | tail -n 1 | awk {'print $4'}")
memcache = commands.getoutput("free -h | head -n 3 | tail -n 1 | awk {'print $3'}")
swap = commands.getoutput("free -h | tail -n 1 | awk {'print $3'}")
disk = commands.getoutput("df / | awk '{ a = $5 } END { print a }'")
usernames = commands.getoutput("w -sh | awk '{print $1 }'")
usersrc = commands.getoutput("w -sh | awk '{print $3 }'")
ospretty = commands.getoutput("cat /etc/os-release | grep PRETTY_NAME| awk -F '=' '{print $2}'")
whether = commands.getoutput("curl --silent wttr.in | head -n 7")
ipsint = commands.getoutput("hostname -I")
ipinternal = ipsint.split(" ")
ipexternal = commands.getoutput("dig +short myip.opendns.com @resolver1.opendns.com")
	

def printfull():


	print "Operating System          = "+ospretty	
	print "Server Name               = "+host
	print "Internal IPs              = " +ipinternal[0]
	print "External IP               = "+ipexternal
	print "Load Averages             = "+load
	print "CPU Usage	 	  = "+cpu
	print "No of Cores		  = "+cores
	print "System Uptime             = "+uptime
	print "Memory free (real)        = "+memreal
	print "Memory free (cache)       = "+memcache
	print "Swap in use               = "+swap
	print "Disk Space Used           = "+disk
	print "Logged in Users		  = "+usernames,usersrc
	print whether
	
printfull()

