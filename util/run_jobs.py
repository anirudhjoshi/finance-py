from numpy import *
from scipy import *

import sys
import subprocess



# arguments
#    'command file'- file containing list of jobs to run, created by prep_run
#    'num Cpus' - number of cpus to use, at any givent time



numCpus = 3;
if (sys.argv.__len__() == 2):
	cmdFile = sys.argv[1];	
elif (sys.argv.__len__() == 3):
	cmdFile = sys.argv[1];
	#workPath= sys.argv[2];
	numCpus = sys.argv[2];	
else:
	print("incorrect parameters provided");
	exit()
	
	


# determine number of process that currently exist
x = subprocess.Popen("c:\\cygwin\\bin\\ps.exe", stdout=subprocess.PIPE).communicate()





fCmd = open(cmdFile,'r')
commands = fCmd.readlines()
fCmd.close()


for command in commands:
	command = command.strip('\n')
	print command
	subprocess.Popen(command)
	# what the command should look like
	#subprocess.Popen("python c:\\owc\\dvg_study\\src\\backtest\\tester.py c:\\owc\dvg_study\\src\\backtest\\test1 parameters.xml")
