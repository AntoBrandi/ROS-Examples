#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    # libreria tf fornisce una implementazione di TransformListener 
    # che aiuta a ricevere matrici di trasformazione piu facilmente
    # creo quindi una instanza della classe tf.TransformListeneru
    listener = tf.TransformListener()

    # mostro a schermo una nuova tartaruga turtle2
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')
    # imposto la velocita di movimento della nuova tartaruga
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    # inizio a ricevere tf matrici di trasformazione e le bufferizzo per 10 secondi
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # interrogo il listener per una specifica matrice di trasformazione 
            # in questo caso voglio la trasformazione di turtle1 
            # rispetto al sistema di riferimento di turtle2
            # infine indico il tempo al quale voglio questa trasformazione e con Time(0)
            # indico di volere l'ultima trasformazione disponibile
            (trans,rot) = listener.lookupTransform('/turtle2', '/carrot1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        # calcolo di quanto deve spostarsi la tartaruga 2 per compensare la trasformazione
        # della tartaruga 1 e pubblico questo spostamento
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()