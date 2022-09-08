import shlex, subprocess, os, time


#command_line = 'sudo apt-get install python3 -y'

command_line = 'df -h'
args = shlex.split(command_line)
print (args)
subprocess.call(args)

a=subprocess.getoutput('ls /bin/ls')
print (a)

print (os.uname())

#print(os.O_RDONLY)


def printlog(prompt):
    year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
    print("%04d-%02d-%02d %02d:%02d:%02d %s" % (year, mon , mday, hour, min, 
sec, prompt))


printlog("Esto es un error")
