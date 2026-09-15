# ROS2 Differential Drive Robot Controller

A ROS2 Humble based differential drive robot controller developed in Python using ROS2 communication, differential drive kinematics, URDF, TF2, odometry, and RViz visualization.

This project is developed as a robotics engineering portfolio project to demonstrate fundamental mobile robot software development concepts used in industrial robotics applications.


## Project Overview

The system implements a complete differential drive robot pipeline:

Velocity Command
|
v
cmd_publisher
|
v
/cmd_vel
|
v
robot_node
|
+----------------+
| |
v v
Odometry (/odom) TF2
|
v
odom -> base_link


The robot receives velocity commands, calculates motion using differential drive kinematics, publishes odometry information, and visualizes the robot model in RViz.


# Features

## ROS2 Publisher and Subscriber Architecture

Implemented ROS2 nodes:

### cmd_publisher

Publishes robot velocity commands:
/cmd_vel


Message type:
geometry_msgs/msg/Twist




### robot_node

Main robot controller node.

Responsibilities:

- Subscribe to velocity commands
- Apply differential drive kinematics
- Calculate robot pose
- Publish odometry
- Broadcast TF transformation


# Differential Drive Kinematics

The controller calculates robot motion using:

- Linear velocity (v)
- Angular velocity (ω)

The robot state is updated using:

- Position x
- Position y
- Orientation θ


# Odometry

The robot publishes:
/odom 

Message type:
nav_msgs/msg/Odometry


Odometry provides:

- Robot position
- Robot orientation
- Robot movement information


# TF2 Coordinate Transformation

The project publishes the robot coordinate relationship:

odom
|
|
base_link


TF2 is generated at approximately 10 Hz.

Verification:

```bash
ros2 run tf2_tools view_frames

URDF Robot Description

The robot model is created using URDF.

Location:
urdf/
 └── robot.urdf

Current robot model includes:

Base chassis link
Visual geometry
Robot state publisher integration

RViz Visualization

RViz is launched automatically using:

ros2 launch diff_drive_robot robot_view.launch.py


The launch file starts:

robot_state_publisher
robot controller node
command publisher node
RViz2


diff_drive_robot

├── diff_drive_robot
│   ├── cmd_publisher.py
│   └── robot_node.py
│
├── launch
│   └── robot_view.launch.py
│
├── urdf
│   └── robot.urdf
│
├── config
│   └── robot_view.rviz
│
├── package.xml
├── setup.py
└── setup.cfg

ROS2 Topics
Topic	Message Type	Purpose
/cmd_vel	geometry_msgs/msg/Twist	Velocity commands
/odom	nav_msgs/msg/Odometry	Robot odometry
/tf	tf2_msgs/msg/TFMessage	Coordinate transformation
/robot_description	std_msgs/msg/String	URDF robot model
Installation and Build

Create workspace:

mkdir -p ~/ros2_ws/src

Clone repository:

cd ~/ros2_ws/src
git clone https://github.com/yashrk7174/ros2-differential-drive-controller.git

Build:

cd ~/ros2_ws

colcon build --symlink-install

source install/setup.bash
Running the Project

Launch complete system:

ros2 launch diff_drive_robot robot_view.launch.py
Verification Commands

Check nodes:

ros2 node list

Check topics:

ros2 topic list

Check odometry:

ros2 topic echo /odom

Check TF:

ros2 run tf2_tools view_frames
Screenshots

RViz visualization and ROS2 verification screenshots are available in:

screenshots/
Technologies Used
ROS2 Humble
Python
URDF
TF2
RViz2
Linux Ubuntu 22.04
WSL2
Future Development Roadmap

Planned improvements:

Add wheel links and joints
Add joint_state_publisher
Improve URDF robot model
Add realistic differential drive simulation
Implement PID controller
Add Gazebo simulation
Integrate Nav2 autonomous navigation
Add automated testing




Author

Yash Khiste

M.Sc. Electrical Engineering and Information Technology

Focus Areas:

Robotics
Control Systems
Industrial Automation
ROS2 Development
