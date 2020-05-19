#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publish():
    # cerate a publisher instance with TOPIC, MESSAGE TYPE, QUEUE SIZE
    pub = rospy.Publisher('chatter',String, queue_size=10)
    rospy.init_node('publisher', anonymous =True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # message String that will be published
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass