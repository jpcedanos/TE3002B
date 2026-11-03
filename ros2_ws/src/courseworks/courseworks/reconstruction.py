import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import Float32

class Reconstruction(Node):
    def __init__(self):
        super().__init__('reconstruction')
        self.subscription_signal = self.create_subscription(Float32, '/signal', self.signal_callback, 10)
        self.publisher_proc_signal = self.create_publisher(Float32, '/proc_signal', 10)
        self.t = 0.0
        self.timer_period = 0.1
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.get_logger().info('Listener node initialized!!!')

    def signal_callback(self, msg):
        self.msg_proc_signal = msg

    def timer_callback(self):
 
        # Procesar el valor de la señal senoidal recibida
        shift_value = ((math.sin(self.t)*math.cos(math.pi * 2)+math.sin(math.pi * 2)*math.cos(self.t)))
        processed_value = (shift_value * 0.5 ) + 0.5
        # Crear un nuevo mensaje Float32 y asignarle el valor procesado
        msg = Float32()
        msg.data = processed_value
        # Publicar el mensaje procesado en el tópico '/proc_signal'
        self.publisher_proc_signal.publish(msg)
        self.get_logger().info("Time: %f" % self.t)
        # Incrementar el tiempo para el próximo ciclo
        self.t += self.timer_period

def main(args=None):
    rclpy.init(args=args)
    reconstruction = Reconstruction()
    rclpy.spin(reconstruction)
    reconstruction.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()