About this package
=================

This repository contains code to command a two-link planar robot and publish markers to rviz showing the recent positions of the end effector.

## Package contents ##
This package contains two nodes:
- `draw_circle_ik` uses inverse kinematics to calculate the joint angles for a 2 DOF planar robot. The x and y coordinates of the end effector are specified to go in a circle, and this node publishes the necessary joint angles to accomplish this. The path of the robot can easily be changed by setting a different for x(t) and y(t) on lines 29 and 30.
- `animate` looks up the tf transform from the base link to the end effector and publishes this as markers in a markerarray to show the recent positions of the end effector. The length of the marker array can be changed with the `MARKERS_MAX` variable on line 34.
- This package uses the robot_state_publisher to publish joint angles from the ik controller and the joint_state_publisher to publish joint angles from the GUI.

This package contains three configuration files:
- `my_robot.urdf` establishes the robot model.
- `testbot_rviz.launch` launches the simulation.
- `two-link.rviz` specifies the rviz configuration.

## Running this package ##
- The default run of the simulation can be the launched with the command: `roslaunch hw2 testbot_rviz.launch use_ik:=true`. 
- To launch the robot and use a gui to set the joint angles, the argument `use_gui` should be set instead of `use_ik`.
- Rviz can be turned off with the argument `rviz:=false`.
- The time period of the circle drawing can be set with argument `period`.

## Topics ##
- The `draw_circle_ik` node and the `joint_state_publisher` publish JointState messages on the `joint_states` topic.
- The `animate` node publishes MarkerArray messages on the `visualization_marker_array` topic.
- The `animate` node listens to tf messages using a `TransformListener` to get information about robot link transforms.



