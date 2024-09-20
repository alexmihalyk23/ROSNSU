
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

cmds = ['turn_right', 'turn_left', 'move_forward', 'move_backward']

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
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
