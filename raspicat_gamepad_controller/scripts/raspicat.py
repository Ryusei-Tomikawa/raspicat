#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import Joy

if __name__ == '__main__':
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    rospy.init_node('raspicat_cmd_vel')
    # cmd_vel_twist = cmd_vel_twist()
    rospy.spin()
