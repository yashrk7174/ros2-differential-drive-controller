import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32





class VelocityPublisher(Node):



    def __init__(self):

        super().__init__('velocity_publisher')



        self.publisher = self.create_publisher(

            Float32,

            '/cmd_vel',

            10

        )



        self.timer = self.create_timer(1.0, self.publish_velocity)



    def publish_velocity(self):



        msg = Float32()

        msg.data = 1.0  # constant velocity



        self.publisher.publish(msg)



        self.get_logger().info("Publishing velocity = 1.0")





def main():

    rclpy.init()

    node = VelocityPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()





if __name__ == '__main__':

    main()
