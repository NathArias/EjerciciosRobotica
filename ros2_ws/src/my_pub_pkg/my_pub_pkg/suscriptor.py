import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'chatsito_topic',   # ¡el mismo tópico que usa tu publicador!
            self.listener_callback,
            10)
        self.subscription  # para evitar warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibí: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
