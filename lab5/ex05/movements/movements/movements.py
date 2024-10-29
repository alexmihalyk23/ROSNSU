#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MovementsNode(Node):
    def __init__(self):
        super().__init__('movements_node')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer_period = 0.1  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.direction = 1  
        self.turn_direction = 1  
        self.zigzag_duration = 2.0
        self.zigzag_timer = self.create_timer(self.zigzag_duration, self.change_direction)
        self.turn_count = 0  
        self.max_turns = 5  

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.5 * self.direction  
        twist_msg.angular.z = 0.5 * self.turn_direction  
        self.publisher_.publish(twist_msg)

    def change_direction(self):
        self.turn_direction *= -1  
        self.turn_count += 1 
        if self.turn_count >= self.max_turns:
            self.reverse_direction()

    def reverse_direction(self):
        self.direction *= -1 
        self.turn_count = 0  

def main(args=None):
    rclpy.init(args=args)
    node = MovementsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()