cmake_minimum_required(VERSION 2.8.3)
project(save_image_n_pcd)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  pcl_ros
)


find_package(PCL 1.7 REQUIRED)
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES save_image_n_pcd
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
)

add_executable (save_pcd src/save_pcd.cpp)
target_link_libraries (save_pcd ${catkin_LIBRARIES} ${PCL_LIBRARIES})