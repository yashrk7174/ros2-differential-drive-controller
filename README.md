# ROS2 Differential Drive Robot Controller

A ROS2 Humble-based differential drive robot controller developed in Python, demonstrating ROS2 communication, differential-drive kinematics, odometry, TF2, URDF/Xacro robot description, joint-state publishing, and RViz2 visualization.

This project is developed as a robotics engineering portfolio project to demonstrate practical mobile robot software development concepts relevant to industrial robotics, autonomous mobile robots (AMRs), and robotic control systems.

---

## Project Overview

The project implements a complete differential-drive robot software pipeline:

```text
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
      +----------------------+
      |                      |
      v                      v
 Odometry (/odom)          TF2
                             |
                             v
                       odom -> base_link
```

The robot receives velocity commands through `/cmd_vel`, applies differential-drive kinematics, updates its simulated pose, publishes odometry, broadcasts TF2 transformations, and visualizes the robot model in RViz2.

---

# Features

## ROS2 Publisher and Subscriber Architecture

The system contains two main ROS2 Python nodes.

### `cmd_publisher`

Publishes velocity commands to:

```text
/cmd_vel
```

Message type:

```text
geometry_msgs/msg/Twist
```

The node provides the velocity command input for the differential-drive controller.

### `robot_node`

Main differential-drive controller node.

Responsibilities:

* Subscribe to `/cmd_vel`
* Apply differential-drive kinematics
* Update robot position and orientation
* Calculate odometry
* Publish `/odom`
* Broadcast TF2 transformation
* Maintain the simulated robot pose

---

# Differential Drive Kinematics

The controller models a differential-drive mobile robot using:

* Linear velocity `v`
* Angular velocity `ω`
* Robot position `x`
* Robot position `y`
* Robot orientation `θ`

The planar robot motion is calculated using:

```text
x_dot = v cos(θ)

y_dot = v sin(θ)

θ_dot = ω
```

The resulting pose is integrated over time to generate simulated robot motion.

This provides the mathematical foundation for later integration with wheel-level control, `ros2_control`, simulation, and autonomous navigation.

---

# Odometry

The controller publishes:

```text
/odom
```

Message type:

```text
nav_msgs/msg/Odometry
```

The odometry message contains:

* Robot position
* Robot orientation
* Linear velocity
* Angular velocity
* Pose information
* Twist information

The odometry update is used as the dynamic source for the robot's motion estimate.

---

# TF2 Coordinate Transformations

The current TF structure is:

```text
odom
  |
  v
base_link
  |
  +-- left_wheel
  |
  +-- right_wheel
  |
  +-- caster_wheel
```

TF2 is broadcast at approximately 10 Hz.

TF can be inspected using:

```bash
ros2 run tf2_tools view_frames
```

The TF tree will be expanded in a later development phase to introduce a dedicated `base_footprint` frame for mobile-robot navigation.

---

# Robot Description — URDF and Xacro

The robot description has been migrated from a monolithic URDF to a modular Xacro-based architecture.

Current robot description:

```text
urdf/
├── robot.urdf.xacro
├── base.xacro
├── wheels.xacro
└── materials.xacro
```

### `robot.urdf.xacro`

Main robot description and Xacro entry point.

### `base.xacro`

Defines the robot chassis, including:

* Visual geometry
* Collision geometry
* Inertial properties
* Mass properties

### `wheels.xacro`

Defines:

* Left wheel
* Right wheel
* Caster wheel
* Wheel links
* Wheel joints

### `materials.xacro`

Contains reusable visual material definitions.

This modular structure makes the robot description easier to maintain, parameterize, and extend for simulation.

---

# Robot Model

The current robot consists of:

```text
                  Base Chassis
              +----------------+
              |                |
      Wheel   |                |   Wheel
       O      |                |      O
              |                |
              +----------------+
                    |
                 Caster
```

The model includes:

* Base chassis
* Left drive wheel
* Right drive wheel
* Caster wheel
* Visual geometry
* Collision geometry
* Inertial properties
* Wheel joints
* TF-compatible link structure

The URDF/Xacro description has been validated using `check_urdf`.

---

# Joint State Publishing

`joint_state_publisher` is included in the robot visualization workflow to provide joint-state information for the robot model.

This allows the wheel joints to participate correctly in the robot's TF tree through `robot_state_publisher`.

---

# RViz2 Visualization

The complete visualization system can be launched using:

```bash
ros2 launch diff_drive_robot robot_view.launch.py
```

The launch system starts the required components for the robot visualization and control workflow, including:

* `robot_node`
* `cmd_publisher`
* `robot_state_publisher`
* `joint_state_publisher`
* RViz2

The robot description is generated dynamically from the Xacro files.

---

# ROS2 Package Structure

The current ROS2 workspace follows a standard workspace/package structure:

```text
ros2_differential_drive_controller/
│
├── README.md
├── .gitignore
│
└── src/
    └── diff_drive_robot/
        │
        ├── diff_drive_robot/
        │   ├── __init__.py
        │   ├── cmd_publisher.py
        │   └── robot_node.py
        │
        ├── launch/
        │   └── robot_view.launch.py
        │
        ├── urdf/
        │   ├── base.xacro
        │   ├── materials.xacro
        │   ├── robot.urdf.xacro
        │   └── wheels.xacro
        │
        ├── config/
        │   └── robot_view.rviz
        │
        ├── resource/
        │   └── diff_drive_robot
        │
        ├── test/
        │   ├── test_copyright.py
        │   ├── test_flake8.py
        │   └── test_pep257.py
        │
        ├── package.xml
        ├── setup.py
        └── setup.cfg
```

---

# ROS2 Topics

| Topic                | Message Type              | Purpose                    |
| -------------------- | ------------------------- | -------------------------- |
| `/cmd_vel`           | `geometry_msgs/msg/Twist` | Velocity commands          |
| `/odom`              | `nav_msgs/msg/Odometry`   | Robot odometry             |
| `/tf`                | `tf2_msgs/msg/TFMessage`  | Coordinate transformations |
| `/robot_description` | `std_msgs/msg/String`     | Robot description          |

---

# Installation

## Requirements

* Ubuntu 22.04
* ROS2 Humble
* Python 3
* Git
* Colcon
* RViz2
* Xacro
* WSL2 (for Windows development)

---

## Create ROS2 Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

## Clone Repository

```bash
git clone https://github.com/yashrk7174/ros2-differential-drive-controller.git
```

Move into the workspace:

```bash
cd ~/ros2_ws
```

## Build

```bash
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

---

# Running the Project

Launch the complete robot system:

```bash
ros2 launch diff_drive_robot robot_view.launch.py
```

---

# Verification

## Check ROS2 Nodes

```bash
ros2 node list
```

Expected nodes include:

```text
/cmd_publisher
/joint_state_publisher
/robot_node
/robot_state_publisher
/rviz
```

## Check Topics

```bash
ros2 topic list
```

## Monitor Velocity Commands

```bash
ros2 topic echo /cmd_vel
```

## Monitor Odometry

```bash
ros2 topic echo /odom
```

## Check Odometry Frequency

```bash
ros2 topic hz /odom
```

## Check TF

```bash
ros2 run tf2_tools view_frames
```

## Inspect TF Rate

```bash
ros2 topic hz /tf
```

---

# Robot Description Verification

Generate the URDF from Xacro:

```bash
ros2 run xacro xacro src/diff_drive_robot/urdf/robot.urdf.xacro > /tmp/robot_test.urdf
```

Validate the generated URDF:

```bash
check_urdf /tmp/robot_test.urdf
```

Successful validation confirms that the modular Xacro description can be converted into a valid URDF model.

---

# Screenshots

Project screenshots demonstrating ROS2 nodes, topics, odometry, velocity commands, and RViz2 visualization are available in:

```text
screenshots/
```

---

# Technologies Used

* ROS2 Humble
* Python
* ROS2 `rclpy`
* Differential-drive kinematics
* URDF
* Xacro
* TF2
* `robot_state_publisher`
* `joint_state_publisher`
* RViz2
* Linux
* Ubuntu 22.04
* WSL2
* Git / GitHub
* Colcon

---

# Development Roadmap

The project is being developed incrementally toward a more complete mobile robotics software stack.

### Completed

* ROS2 Humble development environment
* ROS2 workspace and package
* Publisher/subscriber communication
* `/cmd_vel` velocity command interface
* Differential-drive kinematic model
* Robot pose integration
* Odometry publisher
* TF2 odometry transformation
* Professional URDF robot model
* Collision geometry
* Inertial properties
* Wheel links and joints
* Caster wheel
* Joint-state publishing
* RViz2 visualization
* Modular Xacro robot description
* Modular base, wheel, and material definitions
* ROS2 launch system
* GitHub project structure

### Planned

* Introduce `base_footprint`
* Improve TF architecture and frame ownership
* Parameterize robot dimensions and controller settings
* Implement wheel-level velocity relationships
* Add realistic wheel odometry
* Add PID-based velocity control
* Integrate `ros2_control`
* Add Gazebo simulation
* Add sensor simulation
* Integrate LiDAR
* Integrate Nav2
* Implement autonomous navigation
* Add SLAM/localization
* Add automated ROS2 testing
* Develop an industrial-style digital-twin workflow

---

# Engineering Objective

The long-term objective is to evolve this project from a basic differential-drive controller into a complete robotics software stack covering:

```text
Robot Modeling
      ↓
ROS2 Communication
      ↓
Kinematics
      ↓
Odometry
      ↓
TF2
      ↓
Robot Description
      ↓
Simulation
      ↓
ros2_control
      ↓
Sensors
      ↓
Localization
      ↓
SLAM
      ↓
Nav2
      ↓
Autonomous Mobile Robot
```

This progression demonstrates practical skills in robot modeling, control, state estimation, ROS2 software architecture, simulation, and autonomous robotics.

---

# Author

**Yash Khiste**

M.Sc. Electrical Engineering and Information Technology
Otto von Guericke University Magdeburg, Germany

### Focus Areas

* Robotics
* Control Systems
* Industrial Automation
* ROS2 Development
* Mobile Robotics
* Robot Control
* Systems and Automation Engineering
