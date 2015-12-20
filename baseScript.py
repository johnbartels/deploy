import os
import sys
import subprocess
import argparse
import json

'''
This script will house various common methods
'''


#- General Purpose print command:
def println(s):
    print (str(s))
    #- Call .flush(); to see output in jenkins job's console output while script is executing as opposed to on completion:
    sys.stdout.flush()


#- General purpose run command:
def runcommand(command, show_command=True, throwOnFailure=True):
    if show_command is True:
        println('command: %s' % (str(command)))
    output = None
    returncode = None
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output = p.communicate()[0]
        returncode = p.returncode
    except Exception, exc:
        println('***Command Error: %s' % (str(command)))
        println(exc.message)
    if returncode != 0 and throwOnFailure is True:
        println('***Error in command, exiting. Command: %s\n' % (command))
        println('Output: %s\n' % (str(output)))
        raise Exception("Command_Error")
    return output, returncode

def parse_args():
    #- Parse command line args:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--num_items', help='Number of Items.', default=5, type=int)
    parser.add_argument('--job_dir', help='Directory to get size of.', default='/var/build/jenkins/jobs/myjobname')
    args = parser.parse_args()
    return args

args = parse_args()