#!/usr/bin/env python
import rospy 
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s", data.data)

def subscribe():
    rospy.init_node('subscriber', anonymous=True)
    # define the subscriber with TOPIC, MESSAGE TYPE, ACTION
    rospy.Subscriber("chatter", String, callback)

    # keeps this script running
    rospy.spin()

if __name__ == '__main__':
    subscribe()