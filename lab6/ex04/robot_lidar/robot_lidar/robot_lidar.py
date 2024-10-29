from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.node import Node
import rclpy

import sys
import math
import time
class Lidar(Node):

     def __init__(self):
         # Creates a node with name 'turtlebot_controller' and make sure it is a
         # unique node (using anonymous=True).
         super().__init__('lidar')

         # Publisher which will publish to the topic '/turtle1/cmd_vel'.
         self.velocity_publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
         self.pose_subscriber = self.create_subscription(LaserScan, '/robot/scan', self.update_pose, 10)
         self.scan = LaserScan()
         self.timer = self.create_timer(0.5, self.move)

     def update_pose(self, ranges):
         self.scan = ranges

     def move(self):
         """Moves the turtle to the goal."""
         vel_msg = Twist()
         laser = self.scan.ranges
         vel_msg.linear.x = 0.
         if (len(laser)!=0):
         #self.get_logger().info('%d" ' % laser)
            if (laser[179]<0.41):
                vel_msg.linear.x = 0.
            else:
                vel_msg.linear.x = 0.3
         vel_msg.angular.z = 0.0
         self.velocity_publisher.publish(vel_msg)
def main(args=None):
    rclpy.init(args=args)
    #give time to place an obstacle 
    time.sleep(2)
    x = Lidar()
    rclpy.spin(x)
    x.destroy_node()
    rclpy.shutdown()

 
if __name__ == '__main__':
    main()