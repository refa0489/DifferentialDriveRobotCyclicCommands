import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class Publisher_val(Node):

    def __init__(self):
        super().__init__('cmd_val_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_val', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = Twist()
        msg.linear.x-0.1
        msg.angular.z=0.5
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    publisher_obj = Publisher_val()
    rclpy.spin(publisher_obj)
    
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()