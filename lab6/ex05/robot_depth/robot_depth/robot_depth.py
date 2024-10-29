from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from rclpy.node import Node
import rclpy

import sys
import math
import time
class Happy(Node):

     def __init__(self):
         # Creates a node with name 'turtlebot_controller' and make sure it is a
         # unique node (using anonymous=True).
         super().__init__('happy')

         # Publisher which will publish to the topic '/turtle1/cmd_vel'.
         self.velocity_publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
         self.pose_subscriber = self.create_subscription(Image, '/depth/image', self.update_pose, 10)
         self.scan = Image()
         self.timer = self.create_timer(0.5, self.move)

     def update_pose(self, data):
         self.scan = data

     def move(self):
         """Moves the turtle to the goal."""
         
         vel_msg = Twist()
         d = self.scan.data
         vel_msg.linear.x = 0.
         if (len(d)!=0):
            tmp = int(d[int(self.scan.width*self.scan.height/2 + self.scan.width/2)])
         #self.get_logger().info('%d" ' % laser)
            if (tmp==0.0 or tmp == 127 or tmp == 128):
                vel_msg.linear.x = 0.3
            else:
                vel_msg.linear.x = 0.0
         vel_msg.angular.z = 0.0
         self.velocity_publisher.publish(vel_msg)

         
 
         
def main(args=None):
    rclpy.init(args=args)
    #give time to place an obstacle 
    time.sleep(2)
    x = Happy()
    rclpy.spin(x)
    x.destroy_node()
    rclpy.shutdown()

 
if __name__ == '__main__':
    main()