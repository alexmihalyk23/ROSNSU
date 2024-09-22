import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MoveToGoal(Node):
    def __init__(self):
        super().__init__('move_to_goal')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pose = None
        self.goal_x = float(self.declare_parameter('x', 5.0).value)
        self.goal_y = float(self.declare_parameter('y', 5.0).value)
        self.goal_theta = float(self.declare_parameter('theta', 0.0).value)
        self.tolerance = 0.1
        self.goal_reached = False
        self.control_loop_timer = self.create_timer(0.1, self.control_loop)

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):
        if self.pose is None:
            return

        # Calculate the error in position and orientation
        dx = self.goal_x - self.pose.x
        dy = self.goal_y - self.pose.y
        distance = math.sqrt(dx * dx + dy * dy)
        angle_to_goal = math.atan2(dy, dx)
        angle_error = angle_to_goal - self.pose.theta

        # Normalize angle error to [-pi, pi]
        if angle_error > math.pi:
            angle_error -= 2 * math.pi
        elif angle_error < -math.pi:
            angle_error += 2 * math.pi

        # Create a Twist message to send to the turtle
        twist = Twist()

        if distance > self.tolerance:
            # Rotate to face the goal
            twist.angular.z = 1.5 * angle_error
            # Move towards the goal
            twist.linear.x = 0.5 * distance
        else:
            # Rotate to the final orientation
            final_angle_error = self.goal_theta - self.pose.theta
            if final_angle_error > math.pi:
                final_angle_error -= 2 * math.pi
            elif final_angle_error < -math.pi:
                final_angle_error += 2 * math.pi

            if abs(final_angle_error) > 0.01:
                twist.angular.z = 1.5 * final_angle_error
            else:
                self.goal_reached = True
                self.get_logger().info('Goal reached!')
                self.control_loop_timer.cancel()
                self.destroy_node()
                rclpy.shutdown()

        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    move_to_goal = MoveToGoal()
    rclpy.spin_until_future_complete(move_to_goal, move_to_goal.goal_reached)
    move_to_goal.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()