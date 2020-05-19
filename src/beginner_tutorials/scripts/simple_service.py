#!/usr/bin/env python

# creation of a simple service in ROS that returns the sum of
# two given numbers
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print "Returning [%s+%s=%s]"%(req.a, req.b, (req.a+req.b))
    return AddTwoIntsResponse(req.a+req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    # create an instance of a new ROS Service
    # with SERVICE NAME, SERVICE TYPE, CALLBACK FUNCTION
    # all the requests are passed to the function handle_add_two_ints
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "ready to add two ints"

    # keep the script running
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server()