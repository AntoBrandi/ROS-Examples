#!/usr/bin/env python

# creation of a simple ROS client that uses a ROS service
import sys
import rospy
from AddTwoInts.srv import *

def add_two_ints_client(x, y):
    # block the code until the add_two_ints service is available
    rospy.wait_for_service('add_two_ints')
    try:
        # as soon as the service is available, create an handler for the service
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoInts)
        # let's use the handler as a normal function
        resp1 = add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" %e

def usage():
    return "%s [x y]"%sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv)==3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x,y)
    print "%s + %s = %s" %(x,y,add_two_ints_client(x,y))