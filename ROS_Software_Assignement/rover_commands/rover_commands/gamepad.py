import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GamepadNode(Node):
    def __init__(self):
        super().__init__('gamepad_node')
        # TODO: Create a publisher of type Twist
        # Your code here
        self.publisher = self.create_publisher(Twist, "input_cmd", 10)
        self.get_logger().info('Gamepad node has been started.')

        # TODO: Create a loop here to ask users a prompt and send messages accordingly
        while (True):
            self.cmd_acquisition()

    # Function that prompts user for a direction input, and sends the command
    def cmd_acquisition(self):
        command = input("Enter command (w/a/s/d/t/y - max 2 characters): ")
        twist = Twist()
        # TODO: Complete the function to transform the input into the right command.
        # Your code here
        for c in command[:2]:
            if c == 'w':
                twist.linear.x = 1.0
            elif c == 'a':
                twist.linear.z = -1.0
            elif c == 's':
                twist.linear.x = -1.0
            elif c == 'd':
                twist.linear.z = 1.0
            elif c == 't':
                twist.angular.y = 90.0
            elif c == 'y':
                twist.angular.y = -90.0

        # Log the message 
        tx = twist.linear.x
        ty = twist.linear.y
        tz = twist.linear.z

        rx = twist.angular.x
        ry = twist.angular.y
        rz = twist.angular.z

        self.get_logger().info(f'Published: \n Linear: \n x: {tx}\n y: {ty}\n z: {tz} \n Angular: \n x: {rx} \n y: {ry} \n z: {rz}')

        # Publish the message to the /cmd_vel topic
        self.publisher.publish(twist)
        
def main(args=None):
    rclpy.init(args=args)   # Init ROS python
    node = GamepadNode()  # Create a Node instance
    rclpy.spin(node)  # Run the node in a Thread
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
