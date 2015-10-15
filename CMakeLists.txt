cmake_minimum_required(VERSION 2.8.3)
project(hw2)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  visualization_msgs
  message_generation
  tf
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)


