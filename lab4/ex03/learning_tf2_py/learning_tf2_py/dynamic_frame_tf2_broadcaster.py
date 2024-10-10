# Copyright 2021 Open Source Robotics Foundation, Inc.
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

import math

from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster


class DynamicFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('dynamic_frame_tf2_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.declare_parameter('radius', 1)
        self.declare_parameter('direction_of_rotation', 1)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
        #param_descriptor = ParameterDescriptor(
         #   description='Sets the velocity (in m/s) of the robot.')
        #self.declare_parameter('radius', 0.0, param_descriptor)

    def broadcast_timer_callback(self):
        seconds, n = self.get_clock().now().seconds_nanoseconds()
        r = self.get_parameter('radius').get_parameter_value().integer_value
        d_of_r = self.get_parameter('direction_of_rotation').get_parameter_value().integer_value
        #self.get_logger().info('Hello %f!' % r)
        self.get_logger().info('Hello1 %f!' % d_of_r)
        x = seconds*d_of_r
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot1'
        t.transform.translation.x = r*math.sin(x)
        t.transform.translation.y = r*math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = DynamicFrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
