import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TrajectorySubscriber(Node):
    # Deprecated for level 3, works for level 2
    def __init__(self):
        super().__init__('trajectory_subscriber')
        # TODO: Create a subscriber of type Twist, that calls listener_callback
        self.subscriber = self.create_subscription(Twist, "trajectory", self.listener_callback, 10)
        self.get_logger().info('Subscriber node has been started.')

        # ry in degrees, x and z in whatever unit of length the grid is
        self.position = {'x': 0.0, 'z': 0.0, 'ry': 0.0}

    def listener_callback(self, msg):
        # TODO: Interpret the received commands and log the result using self.get_logger().info()
        tx = msg.linear.x
        ty = msg.linear.y
        tz = msg.linear.z

        rx = msg.angular.x
        ry = msg.angular.y
        rz = msg.angular.z

        # Ensure the command is valid
        if ((tz != 0.0 and ry != 0.0) or (tx != 0.0 and tz != 0.0)):
            self.get_logger().warn('Forbidden move')
            return

        # Log what the command was interpreted as
        if tx != 0.0 and ry != 0.0:
            self.get_logger().info(f'Go {"Left" if ry > 0 else "Right"}')
        elif tx != 0.0:
            self.get_logger().info(f'Go {"Forward" if tx > 0 else "Backward"}')
        elif tz != 0.0:
            self.get_logger().info(f'Slide {"Right" if tz > 0 else "Left"}')
        elif ry != 0.0:
            self.get_logger().info(f'Rotating on itself to the {"Left" if ry > 0 else "Right"}')

        # Figure out the rotation first, then move in consequence
        self.position['ry'] = (self.position['ry'] + ry * 90.0) % 360.0   # Rotate by 1 unit = 90° when a rotation command is received
        theta = math.radians(self.position['ry'])
        # Update x and z based on the updated rotation of the rover and the linear component of the command
        self.position['x'] += round(tx * math.cos(theta) + tz * math.sin(theta), 6)
        self.position['z'] += round(-tx * math.sin(theta) + tz * math.cos(theta), 6)

        self.get_logger().info(f'New Position: {self.position}')

def main(args=None):
    rclpy.init(args=args)
    node = TrajectorySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()