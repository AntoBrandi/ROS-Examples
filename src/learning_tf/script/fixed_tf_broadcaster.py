#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf

# Pubblico un sistema di riferimento che non cambia nel tempo. E sempre
# fisso rispetto al sistema di riferimento parent al quale e collegato

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        #  creo un nuovo sistema di riferimento che ha come parent turtle1
        # di cui ne e un child e si chiama carrot1. Tale sistema di riferimento child
        # e posto a 2m di offset rispetto all'ultima posizione del sistema di riferimento parent
        br.sendTransform((0.0, 2.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "carrot1",
                         "turtle1")
        rate.sleep()