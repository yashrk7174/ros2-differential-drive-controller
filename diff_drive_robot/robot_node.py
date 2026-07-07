import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

import math


class RobotNode(Node):

    def __init__(self):
        super().__init__('robot_node')

        # -----------------------
        # Robot state
        # -----------------------
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.v = 0.0
        self.omega = 0.0

        self.dt = 0.1

        # -----------------------
        # Subscriber
        # -----------------------
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        # -----------------------
        # Publisher (Odometry)
        # -----------------------
        self.odom_pub = self.create_publisher(
            Odometry,
            '/odom',
            10
        )

        # -----------------------
        # TF Broadcaster
        # -----------------------
        self.tf_broadcaster = TransformBroadcaster(self)

        # -----------------------
        # Timer loop
        # -----------------------
        self.timer = self.create_timer(self.dt, self.update_robot)

        self.get_logger().info("Robot Node Started with TF + Odometry")

    # -----------------------
    # Receive velocity
    # -----------------------
    def cmd_callback(self, msg):
        self.v = msg.linear.x
        self.omega = msg.angular.z

    # -----------------------
    # Main update loop
    # -----------------------
    def update_robot(self):

        # -----------------------
        # Kinematics (Differential Drive)
        # -----------------------
        self.x += self.v * math.cos(self.theta) * self.dt
        self.y += self.v * math.sin(self.theta) * self.dt
        self.theta += self.omega * self.dt

        self.theta = math.atan2(
            math.sin(self.theta),
            math.cos(self.theta)
        )

        # ======================================================
        # 1. PUBLISH ODOMETRY
        # ======================================================
        odom = Odometry()

        odom.header.stamp = self.get_clock().now().to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"

        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0

        odom.pose.pose.orientation.z = math.sin(self.theta / 2.0)
        odom.pose.pose.orientation.w = math.cos(self.theta / 2.0)

        odom.twist.twist.linear.x = self.v
        odom.twist.twist.angular.z = self.omega

        self.odom_pub.publish(odom)

        # ======================================================
        # 2. PUBLISH TF
        # ======================================================
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "odom"
        t.child_frame_id = "base_link"

        # translation
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0

        # rotation 
        t.transform.rotation.z = math.sin(self.theta / 2.0)
        t.transform.rotation.w = math.cos(self.theta / 2.0)

        self.tf_broadcaster.sendTransform(t)

        # -----------------------
        # Debug
        # -----------------------
        self.get_logger().info(
            f"TF+ODOM → x={self.x:.2f}, y={self.y:.2f}, θ={self.theta:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = RobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
