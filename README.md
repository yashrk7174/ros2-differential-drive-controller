# ROS2 Differential Drive Robot

## Overview
This project implements a ROS2-based differential drive robot simulation using Python, demonstrating publisher-subscriber communication and basic robot motion control.

## Features
- ROS2 Publisher/Subscriber architecture
- Robot motion simulation
- Velocity-based control system
- Linux (WSL2) development environment

## System Flow
cmd_publisher → robot_node → position update

## How to Run

```bash
colcon build
source install/setup.bash

ros2 run diff_drive_robot cmd_publisher
ros2 run diff_drive_robot robot_node
