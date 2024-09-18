# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

cmds = ['turn right', 'turn_left', 'move_forward', 'move_backward']

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        cmd = input()
        if cmd in cmds:
            msg = Twist()
            if cmd == 'move_forward':
                msg.linear.x = 1.5
                self.get_logger().info('Get moved')
            if cmd == 'move_backward':
                msg.linear.x = -1.5
                self.get_logger().info('Get moved')
            if cmd == 'turn_right':
                msg.angular.z = -1.5
                self.get_logger().info('Get rotated')
            if cmd == 'turn_left':
                msg.angular.z = 1.5
                self.get_logger().info('Get rotated')

            self.publisher_.publish(msg)
        else:
            self.get_logger().info('Wrong command!')
            


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()