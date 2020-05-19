#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf
import math

# Pubblico un sistema di riferimento che cambia nel tempo. 
# il valore dell'offset che il sistema di riferimento child ha rispetto al parent
# e parametrico ed e fuznione del tempo

if __name__ == '__main__':
    rospy.init_node('dynamic_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec() * math.pi
        # invece che definire un offset fisso tra il sistema di riferimento child ed 
        # il suo parent, ho definito un offset parametrico in funzione del tempo
        br.sendTransform((2.0 * math.sin(t), 2.0 * math.cos(t), 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "carrot1",
                         "turtle1")
        rate.sleep()