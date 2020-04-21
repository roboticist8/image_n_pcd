#! /usr/bin/python

import rospy
import rospkg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()


if __name__ == '__main__':
    rospy.init_node('image_listener', anonymous=True)
    # topic names
    image_topic = "/camera/color/image_raw"
    disparity_topic = "/camera/depth/image_raw"

    rospack = rospkg.RosPack()
    file_path = rospack.get_path('save_image_n_pcd')

    color_image = rospy.wait_for_message(image_topic, Image, timeout=5)
    cv2_img = bridge.imgmsg_to_cv2(color_image, "bgr8")
    color_file_name = file_path+'/file/image.jpeg'
    cv2.imwrite(color_file_name, cv2_img)

    disparity_image = rospy.wait_for_message(disparity_topic, Image, timeout=5)
    cv2_disp = bridge.imgmsg_to_cv2(disparity_image, "32FC1")
    disparity_file_name = file_path+'/file/disparity.jpeg'
    cv2.imwrite(disparity_file_name, cv2_disp)

    rospy.loginfo("Color and Disparity Image saved")
    # rospy.spin()
