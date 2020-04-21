#include <ros/ros.h>
#include <ros/package.h>
// PCL specific includes
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

bool saved = false;
void  cloudCallback (const sensor_msgs::PointCloud2ConstPtr& msg)
{
  std::string path = ros::package::getPath("save_image_n_pcd");
  pcl::PointCloud<pcl::PointXYZRGB> cloud;
  pcl::fromROSMsg(*msg, cloud);
  std::string file_name = path + "/file/image_pcd.pcd";
  pcl::io::savePCDFileASCII (file_name, cloud);
  ROS_INFO("PCD SAVED");
  saved = true;

}

int main (int argc, char** argv)
{
  ros::init (argc, argv, "save_pcd");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe ("/camera/depth/points", 100, cloudCallback);
  //Spin
  while (ros::ok && !saved)
  {
      ros::spinOnce();
  }
  
  
}