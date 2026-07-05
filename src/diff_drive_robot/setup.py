from setuptools import setup

package_name = 'diff_drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='ROS2 differential drive robot',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'robot_node = diff_drive_robot.robot_node:main',
            'cmd_publisher = diff_drive_robot.cmd_publisher:main',
        ],
    },
)
