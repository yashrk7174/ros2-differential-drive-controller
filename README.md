# ROS2 Differential Drive Robot Controller

A ROS2 Humble mobile-robot control project implementing differential-drive kinematics, odometry, TF2, modular URDF/Xacro modeling, joint-state publishing, and RViz2 visualization in Python.

The project demonstrates the development of a mobile-robot software stack from low-level velocity commands and kinematic modeling to robot state estimation, coordinate-frame management, and visualization.

![Differential Drive Robot](screenshots/wheel_car.png)

---

## Engineering Highlights

* **Built a differential-drive motion controller** using ROS2 `rclpy` and planar robot kinematics, converting velocity commands into simulated robot motion.

* **Implemented a ROS2 velocity-command interface** using `geometry_msgs/msg/Twist` on `/cmd_vel`, providing a standard mobile-robot motion input.

* **Implemented robot odometry estimation** by integrating linear and angular velocity over time, publishing robot state through `nav_msgs/msg/Odometry`.

* **Implemented dynamic TF2 broadcasting** from `odom` to `base_link`, providing the robot's runtime coordinate transformation.

* **Developed a modular robot description** using URDF/Xacro, separating the robot chassis, wheels, and materials into reusable components.

* **Added wheel and caster links and joints** to the robot model, creating a complete differential-drive mobile robot structure.

* **Added collision and inertial properties** to the robot description, establishing a simulation-ready physical model for future development.

* **Integrated `joint_state_publisher` and `robot_state_publisher`** to propagate joint and link transformations through the robot's TF hierarchy.

* **Built a ROS2 launch workflow** that processes the Xacro robot description and starts the required controller, state publishers, command publisher, and RViz2 components.

* **Validated the robot model** using Xacro generation and `check_urdf`, confirming successful parsing and a valid link/joint structure.

* **Validated ROS2 runtime behavior** using node, topic, odometry, robot-pose, and TF inspection tools.

---

# System Architecture

```text
                         /cmd_vel
                            │
                            ▼
                   ┌─────────────────┐
                   │  cmd_publisher  │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │   robot_node    │
                   │                 │
                   │ Differential    │
                   │ Drive Kinematics│
                   └────────┬────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
              /odom                   TF2
                 │                     │
                 │                     ▼
                 │              odom → base_link
                 │                     │
                 │                     ▼
                 │             robot_state_publisher
                 │                     │
                 │          ┌──────────┼──────────┐
                 │          ▼          ▼          ▼
                 │      left_wheel right_wheel caster_wheel
                 │
                 ▼
             Robot Pose
```

---

# Technical Implementation

## 1. Differential-Drive Motion Control

**Implemented:** Differential-drive robot motion control.

**How:** `robot_node` receives velocity information through ROS2 and applies planar differential-drive kinematics to update the robot state.

The robot pose is represented by:

```text
x
y
θ
```

with the planar motion model:

```text
ẋ = v cos(θ)

ẏ = v sin(θ)

θ̇ = ω
```

**Result:** Linear and angular velocity commands generate continuously updated robot position and orientation.

---

## 2. ROS2 Velocity Interface

**Implemented:** A dedicated velocity-command publisher.

**How:** `cmd_publisher` publishes:

```text
geometry_msgs/msg/Twist
```

to:

```text
/cmd_vel
```

**Result:** The robot controller receives velocity commands through a standard ROS2 mobile-robot interface.

![CMD Publisher](screenshots/cmd_publisher_terminal.jpg)

---

## 3. Robot Controller Node

**Implemented:** A dedicated ROS2 robot-control node.

**How:** `robot_node` subscribes to the robot's velocity command interface, performs motion calculations, updates the robot state, and publishes odometry and TF information.

**Result:** Robot motion, pose integration, odometry, and TF broadcasting are handled within the controller node.

![Robot Node Terminal](screenshots/robot_node_terminal.png)

---

## 4. Odometry Estimation

**Implemented:** Runtime robot odometry.

**How:** Linear and angular velocities are integrated over time to estimate the robot's position and orientation.

The resulting state is published through:

```text
/odom
```

using:

```text
nav_msgs/msg/Odometry
```

**Result:** The ROS2 system continuously exposes the estimated robot pose and velocity.

![Odometry Topic](screenshots/odometry_topic.png)

---

## 5. Robot Pose Integration

**Implemented:** Continuous robot pose calculation.

**How:** The controller integrates the robot's linear and angular motion over the control loop.

**Result:** The estimated position and orientation change according to the commanded robot motion.

![Robot Pose Output](screenshots/robot_pose_output.png)

---

## 6. TF2 Coordinate Frames

**Implemented:** Dynamic robot coordinate transformation.

**How:** The controller broadcasts:

```text
odom → base_link
```

through TF2.

**Result:** The robot's dynamic pose is available through the ROS2 coordinate-frame system and can be visualized using RViz2 and inspected through TF2 tools.

![TF Tree](screenshots/tf_tree.png)

---

## 7. Modular URDF/Xacro Robot Model

**Implemented:** A modular robot-description architecture.

**How:** The robot model is separated into reusable Xacro components:

```text
urdf/
├── robot.urdf.xacro
├── base.xacro
├── wheels.xacro
└── materials.xacro
```

**Result:** Robot geometry, wheel definitions, materials, and physical properties can be modified independently.

![Xacro Robot Description](screenshots/Xro%20file%20robot.png)

---

## 8. Robot Geometry and Physical Properties

**Implemented:** Chassis, drive-wheel, and caster-wheel modeling.

**How:** Xacro definitions provide visual geometry, collision geometry, mass, inertial properties, and joints.

**Result:** The robot description provides a structured model suitable for visualization and future physics-based simulation.

---

## 9. Robot State Publishing

**Implemented:** Joint-state and robot-state publishing.

**How:** `joint_state_publisher` provides joint-state information while `robot_state_publisher` generates link transformations from the robot description.

**Result:** The robot model is represented as a connected link hierarchy:

```text
base_link
├── left_wheel
├── right_wheel
└── caster_wheel
```

---

## 10. ROS2 Launch System

**Implemented:** Automated robot startup and visualization.

**How:** `robot_view.launch.py` dynamically processes the Xacro robot description and starts the required ROS2 nodes.

**Result:** The complete robot visualization stack can be launched using:

```bash
ros2 launch diff_drive_robot robot_view.launch.py
```

---

# Results & Engineering Evidence

## Final Robot Visualization

![Differential Drive Robot](screenshots/wheel_car.png)

**Result:** Verified the complete differential-drive robot model in the ROS2 visualization environment.

---

## RViz2 Odometry

![RViz2 Odometry](screenshots/rviz_odometry.png)

**Result:** Verified the robot model and odometry-related visualization during runtime execution.

---

## ROS2 Topic Architecture

![ROS2 Topic List](screenshots/ros2_topic_list.png)

**Result:** Verified the ROS2 topic interfaces used by the controller and robot-state system.

---

## Velocity Command Publisher

![CMD Publisher Terminal](screenshots/cmd_publisher_terminal.jpg)

**Result:** Verified velocity-command publication through `/cmd_vel`.

---

## Robot Controller Runtime

![Robot Node Terminal](screenshots/robot_node_terminal.png)

**Result:** Verified execution of the main robot-control node responsible for motion and state updates.

---

## Odometry Output

![Odometry Topic](screenshots/odometry_topic.png)

**Result:** Verified the `/odom` topic and published robot odometry data.

---

## Robot Pose

![Robot Pose Output](screenshots/robot_pose_output.png)

**Result:** Verified the calculated robot position and orientation during runtime motion.

---

## TF2 Frame Tree

![TF2 Tree](screenshots/tf_tree.png)

**Result:** Verified the robot coordinate-frame relationship between `odom`, `base_link`, and the robot's child links.

---

## Xacro Robot Description

![Xacro Robot Description](screenshots/Xro%20file%20robot.png)

**Result:** Verified the modular robot-description implementation used to generate the ROS2 robot model.

---

# Validation

## Package Build

```bash
cd ~/ros2_ws

colcon build --symlink-install

source install/setup.bash
```

Successful build:

```text
Starting >>> diff_drive_robot
Finished <<< diff_drive_robot

Summary: 1 package finished
```

---

## Xacro Generation

```bash
ros2 run xacro xacro \
src/diff_drive_robot/urdf/robot.urdf.xacro \
> /tmp/robot_test.urdf
```

---

## URDF Validation

```bash
check_urdf /tmp/robot_test.urdf
```

Validated robot structure:

```text
robot name: diff_drive_robot

root Link: base_link

child links:
- caster_wheel
- left_wheel
- right_wheel
```

---

## ROS2 Package Verification

```bash
ros2 pkg prefix diff_drive_robot
```

The package is successfully discovered from the built ROS2 workspace.

---

# ROS2 Interfaces

| Interface            | Type                      | Function                           |
| -------------------- | ------------------------- | ---------------------------------- |
| `/cmd_vel`           | `geometry_msgs/msg/Twist` | Velocity command input             |
| `/odom`              | `nav_msgs/msg/Odometry`   | Robot pose and velocity estimation |
| `/tf`                | `tf2_msgs/msg/TFMessage`  | Coordinate transformations         |
| `/robot_description` | Robot description         | Robot model information            |

---

# Runtime Verification

### Inspect Nodes

```bash
ros2 node list
```

### Inspect Topics

```bash
ros2 topic list
```

### Monitor Velocity Commands

```bash
ros2 topic echo /cmd_vel
```

### Monitor Odometry

```bash
ros2 topic echo /odom
```

### Measure Odometry Frequency

```bash
ros2 topic hz /odom
```

### Inspect TF Frames

```bash
ros2 run tf2_tools view_frames
```

### Measure TF Frequency

```bash
ros2 topic hz /tf
```

---

# Repository Structure

```text
ros2-differential-drive-controller/
│
├── README.md
├── .gitignore
├── screenshots/
│   ├── cmd_publisher_terminal.png
│   ├── odometry_topic.png
│   ├── robot_node_terminal.png
│   ├── robot_pose_output.png
│   ├── ros2_topic_list.png
│   ├── rviz_odometry.png
│   ├── tf_tree.png
│   ├── wheel car.png
│   └── Xro file robot.png
│
└── src/
    └── diff_drive_robot/
        │
        ├── diff_drive_robot/
        │   ├── __init__.py
        │   ├── cmd_publisher.py
        │   └── robot_node.py
        │
        ├── config/
        │   └── robot_view.rviz
        │
        ├── launch/
        │   └── robot_view.launch.py
        │
        ├── resource/
        │   └── diff_drive_robot
        │
        ├── test/
        │   ├── test_copyright.py
        │   ├── test_flake8.py
        │   └── test_pep257.py
        │
        ├── urdf/
        │   ├── base.xacro
        │   ├── materials.xacro
        │   ├── robot.urdf.xacro
        │   └── wheels.xacro
        │
        ├── package.xml
        ├── setup.cfg
        └── setup.py
```

---

# Build and Run

## Requirements

* Ubuntu 22.04
* ROS2 Humble
* Python 3
* Colcon
* Xacro
* RViz2
* Git

The project has been developed and tested using Ubuntu 22.04 under WSL2 on Windows.

---

## Clone

```bash
mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src

git clone https://github.com/yashrk7174/ros2-differential-drive-controller.git
```

---

## Build

```bash
cd ~/ros2_ws

colcon build --symlink-install

source install/setup.bash
```

---

## Launch

```bash
ros2 launch diff_drive_robot robot_view.launch.py
```

---

# Development Roadmap

## Completed

* [x] ROS2 Humble development environment
* [x] ROS2 workspace and Python package
* [x] Publisher/subscriber communication
* [x] `/cmd_vel` velocity interface
* [x] Differential-drive kinematics
* [x] Robot pose integration
* [x] `/odom` odometry publisher
* [x] Dynamic `odom → base_link` TF2
* [x] Professional URDF robot model
* [x] Chassis collision geometry
* [x] Inertial and mass properties
* [x] Drive-wheel links and joints
* [x] Caster-wheel model
* [x] Joint-state publishing
* [x] `robot_state_publisher`
* [x] RViz2 visualization
* [x] Modular Xacro architecture
* [x] Separate base, wheel, and material Xacro files
* [x] ROS2 launch system
* [x] Xacro and URDF validation
* [x] Standard ROS2 package structure
* [x] Git/GitHub project organization

## Next Development Phase

* [ ] Introduce `base_footprint`
* [ ] Separate dynamic and static TF ownership
* [ ] Improve mobile-robot TF architecture
* [ ] Parameterize robot dimensions and controller settings
* [ ] Improve wheel-level motion modeling
* [ ] Implement realistic wheel odometry
* [ ] Add PID-based velocity control

## Future Robotics Stack

* [ ] `ros2_control`
* [ ] Gazebo simulation
* [ ] Sensor simulation
* [ ] LiDAR integration
* [ ] Robot localization
* [ ] SLAM
* [ ] Nav2 autonomous navigation
* [ ] Autonomous waypoint following
* [ ] Automated ROS2 integration testing

---

# Technologies

```text
ROS2 Humble
Python
rclpy
Differential-Drive Kinematics
URDF
Xacro
TF2
robot_state_publisher
joint_state_publisher
RViz2
Ubuntu 22.04
WSL2
Linux
Git
GitHub
Colcon
```

---

# Engineering Focus

The project is being developed toward an industrial mobile-robot software stack:

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
Robot State Representation
      ↓
Control
      ↓
Simulation
      ↓
Localization
      ↓
Navigation
```

The implementation emphasizes **modular robot modeling, ROS2 communication, coordinate-frame correctness, runtime validation, and incremental integration of robotics control and autonomy components.**

---

# Author

**Yash Khiste**

M.Sc. Electrical Engineering and Information Technology
Otto von Guericke University Magdeburg, Germany

### Focus Areas

* Robotics
* Control Systems
* Industrial Automation
* Mobile Robotics
* ROS2 Development
* Robot Control
* Systems and Automation Engineering
