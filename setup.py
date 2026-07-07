from setuptools import setup
import os
from glob import glob

package_name = 'diff_drive_robot'

setup(
    name=package_name,
    version='0.0.0',

    packages=[package_name],

    data_files=[
        # Register package
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        # Install package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Install launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        # Install URDF files
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf')
        ),

        # Install RViz configuration
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.rviz')
        ),
    ],

    install_requires=[
        'setuptools',
    ],

    zip_safe=True,

    maintainer='khisteyash',
    maintainer_email='khiste.workspace@gmail.com',

    description='ROS2 differential drive robot controller with URDF, TF2, Odometry and RViz',

    license='Apache-2.0',

    tests_require=[
        'pytest',
    ],

    entry_points={
        'console_scripts': [
            'robot_node = diff_drive_robot.robot_node:main',
            'cmd_publisher = diff_drive_robot.cmd_publisher:main',
        ],
    },
)
