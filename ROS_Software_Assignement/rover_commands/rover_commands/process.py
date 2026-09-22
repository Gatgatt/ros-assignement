import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ProcessNode(Node):

    def __init__(self):
        super().__init__('process_node')

        # TODO: Create a subscriber on the 'input_cmd' topic
        self.gamepad_subscriber = self.create_subscription(Twist, "input_cmd", self.gamepad_callback, 10)

        # TODO: Create a subscriber on the 'correction_cmd' topic
        self.sensor_subscriber = self.create_subscription(Twist, "correction_cmd", self.sensor_callback, 10)

        # TODO: Create a publisher of type Twist on the 'gps_pos' topic
        self.publisher = self.create_publisher(Twist, "gps_pos", 10)

        # Local Twist instance
        self.current_pos = Twist()

        # Create a timer for the node so that it triggers a function call (publish_real_pos here) every second
        self.create_timer(1.0, self.publish_real_pos)
        self.get_logger().info('Process node has been started.')

    # TODO: Add the necessary functions, make sure to read the note on the process node
    # You can (and should !) refactor both functions into one, here I decided that each command received
    # has its own callback for more clarity during your learning phase of ROS

    # Add the received command to the local twist instance
    def gamepad_callback(self, msg):
        self.current_pos.linear.x += msg.linear.x
        self.current_pos.linear.y += msg.linear.y
        self.current_pos.linear.z += msg.linear.z

        self.current_pos.angular.x += msg.angular.x
        self.current_pos.angular.x += msg.angular.y
        self.current_pos.angular.x += msg.angular.z

    def sensor_callback(self, msg):
        self.current_pos.linear.x += msg.linear.x
        self.current_pos.linear.y += msg.linear.y
        self.current_pos.linear.z += msg.linear.z

        self.current_pos.angular.x += msg.angular.x
        self.current_pos.angular.y += msg.angular.y
        self.current_pos.angular.z += msg.angular.z

    # Publish the local twist instance to the gps_pos topic
    def publish_real_pos(self):
        self.publisher.publish(self.current_pos)

def main(args=None):
    rclpy.init(args=args)
    node = ProcessNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
