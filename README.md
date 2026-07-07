# ROS2 Differential Drive Robot Controller

A ROS2 Humble based differential drive mobile robot controller developed in Python using ROS2 communication, differential drive kinematics, URDF, TF2, odometry, and RViz2 visualization.

This project demonstrates the fundamental software architecture used in mobile robotics applications, including robot control, coordinate transformations, robot description, and visualization.

---

# Project Overview

The project implements a complete differential drive robot pipeline:
Velocity Command
|
v
cmd_publisher Node
|
v
/cmd_vel
|
v
robot_node Controller
|
+----------------+
| |
v v
Odometry (/odom) TF2
|
v
odom → base_link


The robot receives velocity commands, calculates motion using differential drive kinematics, updates its position, publishes odometry information, and broadcasts TF transformations for visualization.

---

# Features

## ROS2 Publisher and Subscriber Architecture

The project contains two main ROS2 nodes.

### cmd_publisher

Responsible for publishing velocity commands.

Publishes:
/cmd_vel

Message type:
geometry_msgs/msg/Twist


---

### robot_node

Main differential drive controller node.

Responsibilities:

- Subscribe to velocity commands
- Calculate robot motion
- Apply differential drive kinematics
- Update robot pose
- Publish odometry
- Broadcast TF transformation

---

# Differential Drive Kinematics

The controller calculates robot movement using:

- Linear velocity (v)
- Angular velocity (ω)

The robot state is updated using:

- X position
- Y position
- Heading angle (θ)

The motion model represents a standard differential drive mobile robot.

---

# Odometry

The robot publishes:
/odom

Message type:
nav_msgs/msg/Odometry

Odometry provides:

- Robot position
- Robot orientation
- Robot movement information

The odometry publisher runs at approximately 10 Hz.

---

# TF2 Coordinate Transformation

The project uses ROS2 TF2 for coordinate management.

Current TF tree:

odom
|
|
base_link

The transformation is broadcast between:
odom → base_link


TF verification is performed using ROS2 TF tools.

---

# URDF Robot Description

The robot model is created using URDF (Unified Robot Description Format).

Current model contains:

- Base chassis link
- Visual geometry
- Robot state publisher integration

Robot description file:

urdf/
└── robot.urdf


---

# RViz2 Visualization

The project includes RViz2 visualization support.

RViz displays:

- Robot model
- TF frames
- Odometry information
- Robot movement

The launch system starts all required components:

- robot_state_publisher
- differential drive controller
- command publisher
- RViz2

---

# Package Structure
ros2-differential-drive-controller/

├── config/
│ └── robot_view.rviz
│
├── diff_drive_robot/
│ ├── init.py
│ ├── cmd_publisher.py
│ └── robot_node.py
│
├── launch/
│ └── robot_view.launch.py
│
├── urdf/
│ └── robot.urdf
│
├── resource/
│ └── diff_drive_robot
│
├── package.xml
├── setup.py
├── setup.cfg
├── README.md
└── .gitignore


---

# ROS2 Topics

| Topic | Message Type | Purpose |
|------|--------------|---------|
| `/cmd_vel` | geometry_msgs/msg/Twist | Robot velocity commands |
| `/odom` | nav_msgs/msg/Odometry | Robot odometry |
| `/tf` | tf2_msgs/msg/TFMessage | Coordinate transformations |
| `/robot_description` | std_msgs/msg/String | URDF robot model |

---

# How To Run

## Build Workspace

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

Launch Robot System:
ros2 launch diff_drive_robot robot_view.launch.py
Verification Commands:
ros2 node list
Expected:

/cmd_publisher
/robot_node
/robot_state_publisher
/rviz

Check ROS2 Topics
ros2 topic list
Check Odometry
ros2 topic echo /odom
Check TF Tree
ros2 run tf2_tools view_frames
Screenshots

Project screenshots are available in:

screenshots/

Included demonstrations:

ROS2 nodes and topics: 
TF tree visualization
Odometry output
RViz visualization


Technologies Used
ROS2 Humble
Python
URDF
TF2
RViz2
Linux Ubuntu 22.04
WSL2
Future Development Roadmap

##Planned improvements:

Add wheel links and joints
Add joint_state_publisher
Improve robot URDF model
Add realistic wheel rotation
Implement PID controller
Add Gazebo simulation
Integrate Nav2 autonomous navigation
Add automated testing
Improve controller architecture



Author
Yash Khiste
M.Sc. Electrical Engineering and Information Technology
Focus Areas:
Robotics
Control Systems
Industrial Automation
ROS2 Development

