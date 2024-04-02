import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32  # Assuming the position is published as a Float32

class JoyToCmdVelAndServo(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel_and_servo')
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.servo_publisher = self.create_publisher(Float32, '/olive/servo/hook/goal/position', 10)
        
        self.max_velocity = 2.0  # Maximum velocity
        self.servo_position = 0.0  # Initial servo position
        self.servo_step = 0.1  # Increment/decrement step for servo position

    def joy_callback(self, msg):
        # Mapping for linear and angular velocity
        x = msg.axes[0] * self.max_velocity
        y = msg.axes[1] * self.max_velocity
        z = msg.axes[3] * self.max_velocity

        twist = Twist()
        twist.linear.x = y
        twist.linear.y = x
        twist.angular.z = -z
        self.cmd_vel_publisher.publish(twist)

        # Mapping for servo position (adjust button indices as necessary)
        if msg.buttons[0] == 1:  # Assuming button 4 is arrow up
            self.servo_position += self.servo_step
            if self.servo_position > 2:
                self.servo_position = 2.0
        elif msg.buttons[3] == 1:  # Assuming button 5 is arrow down
            self.servo_position -= self.servo_step
            if self.servo_position < -2:
                self.servo_position = -2.0  
        
        self.servo_publisher.publish(Float32(data=self.servo_position))

def main(args=None):
    rclpy.init(args=args)
    joy_to_cmd_vel_and_servo = JoyToCmdVelAndServo()
    rclpy.spin(joy_to_cmd_vel_and_servo)
    joy_to_cmd_vel_and_servo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

