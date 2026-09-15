from launch import LaunchDescription
from launch.substitutions import Command

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    pkg_path = get_package_share_directory(
        'diff_drive_robot'
    )

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'robot.urdf.xacro'
    )


    robot_description = Command(
        [
            'xacro ',
            xacro_file
        ]
    )


    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',

        parameters=[
            {
                'robot_description': robot_description
            }
        ],

        output='screen'
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )
    robot_node = Node(
        package='diff_drive_robot',
        executable='robot_node',
        output='screen'
    )


    cmd_publisher = Node(
        package='diff_drive_robot',
        executable='cmd_publisher',
        output='screen'
    )


    rviz_config = os.path.join(
        pkg_path,
        'config',
        'robot_view.rviz'
    )


    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        output='screen',
        arguments=[
            '-d',
            rviz_config
        ]
    )


    return LaunchDescription(
        [
            robot_state_publisher,
            joint_state_publisher,
            robot_node,
            cmd_publisher,
            rviz_node
        ]
    )
