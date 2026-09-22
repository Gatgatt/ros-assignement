import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class Sensor(Node):

    def __init__(self):
        super().__init__('sensor')
        # TODO: Create a publisher of type Twist
        self.publisher = self.create_publisher(Twist, "correction_cmd", 10)
        self.start_time = self.get_clock().now()

		# TODO: Make the `publish_correction` be called every second
		# Hint : the ROS documentation may have something for you

        # Create a timer that calls the publish_correction function every second
        self.timer = self.create_timer(1.0, self.publish_correction)

        self.get_logger().info('Sensor node has been started.')

    def publish_correction(self):
        t = (self.get_clock().now() - self.start_time).nanoseconds / 1e9
        msg = Twist()

        msg.linear.x = math.sin(t)
        msg.linear.z = math.cos(t)
        msg.angular.y = t

        # TODO: Publish 'msg' to the 'correction_cmd' topic
        self.publisher.publish(msg)
        self.get_logger().info(f'Published correction: x={msg.linear.x:.3f}, z={msg.linear.z:.3f}, ry={msg.angular.y:.3f}')

def main(args=None):
    rclpy.init(args=args)
    node = Sensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()