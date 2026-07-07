import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdPublisher(Node):

    def __init__(self):
        super().__init__('cmd_publisher')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.publish_velocity)

        self.get_logger().info("Command Publisher Started")

    def publish_velocity(self):

        msg = Twist()

        msg.linear.x = 0.5
        msg.angular.z = 0.2

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Linear={msg.linear.x:.2f}, Angular={msg.angular.z:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = CmdPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
