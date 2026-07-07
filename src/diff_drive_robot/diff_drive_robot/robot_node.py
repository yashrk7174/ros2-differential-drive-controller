import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DifferentialDriveRobot(Node):

    def __init__(self):
        super().__init__('diff_drive_robot')

        self.x = 0.0
        self.linear_velocity = 0.0

        self.subscription = self.create_subscription(
            Float32,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.publisher = self.create_publisher(
            Float32,
            '/robot_position',
            10
        )

        self.timer = self.create_timer(0.1, self.update_robot)

        self.get_logger().info("Robot Node Started")

    def cmd_callback(self, msg):
        self.linear_velocity = msg.data

    def update_robot(self):
        dt = 0.1
        self.x += self.linear_velocity * dt

        msg = Float32()
        msg.data = self.x

        self.publisher.publish(msg)

        self.get_logger().info(f"X position: {self.x:.2f}")


def main():
    rclpy.init()
    node = DifferentialDriveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
