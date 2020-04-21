#! /usr/bin/python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()

def imageCallback(msg):
    print("Received an color image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # time = msg.header.stamp
        cv2.imwrite('src/image.jpeg', cv2_img)
        # rospy.sleep(1)

def disparityCallback(msg):
    print("Received an disparity image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "32FC1")
    except CvBridgeError, e:
        print(e)
    else: 
        # time = msg.header.stamp
        cv2.imwrite('src/disparity.jpeg', cv2_img)
        # rospy.sleep(1)

if __name__ == '__main__':
    rospy.init_node('image_listener', anonymous=True)
    image_topic = "/camera/color/image_raw"
    disparity_topic = "/camera/depth/image_raw"
    rospy.Subscriber(image_topic, Image, imageCallback)
    rospy.Subscriber(disparity_topic, Image, disparityCallback)
    # rospy.spin()
