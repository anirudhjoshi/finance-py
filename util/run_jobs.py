from numpy import *
from scipy import *

import sys
import subprocess
import re
import time

# arguments
#    'command file'- file containing list of jobs to run, created by prep_run
#    'num Cpus' - number of cpus to use, at any givent time

sleepTime = 0.1 # 100ms

numCpus = 3;
if (sys.argv.__len__() == 2):
	cmdFile = sys.argv[1];	
elif (sys.argv.__len__() == 3):
	cmdFile = sys.argv[1];
	#workPath= sys.argv[2];
	numCpus = int(sys.argv[2]);	
else:
	print("incorrect parameters provided");
	exit()
	
	





fCmd = open(cmdFile,'r')
commands = fCmd.readlines()
fCmd.close()


numCommands = size(commands);
# process handler
v_procH =  empty((numCpus), dtype = subprocess.Popen)

M = min(numCommands, numCpus);
jobsSubmitted= 0;
for index in range(0, M):
	command = commands[jobsSubmitted].strip('\n')
	jobsSubmitted  = jobsSubmitted +1;
	print command
	v_procH[index] = subprocess.Popen(command)
	



while(jobsSubmitted< numCommands):
	time.sleep(sleepTime)
	for index in range(0, numCpus):
		# check to ensure equality is still met, since there is a for loop. 
		if( (v_procH[index].poll() == None) == False and jobsSubmitted< numCommands): # poll to determine when then job is done
			command = commands[jobsSubmitted ].strip('\n')
			jobsSubmitted  = jobsSubmitted +1;
			print command
			v_procH[index] = subprocess.Popen(command)
