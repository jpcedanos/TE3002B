import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import Float32
from scipy import signal

class SignalGenerator(Node):
    
    def __init__(self):
        super().__init__('signal_generator_node')
        
        self.time = 0
        self.signal_timer_period = 1e-3
        self.decomposed_timer_period = 1e-2
        self.current_signal = 0

        self.declare_parameters(
            namespace='',
            parameters=[
                ('signal_type', rclpy.Parameter.Type.INTEGER),
                ('default.amplitude', rclpy.Parameter.Type.DOUBLE),
                ('default.frequency', rclpy.Parameter.Type.DOUBLE),
                ('default.offset', rclpy.Parameter.Type.DOUBLE),
                ('defaul.phase', rclpy.Parameter.Type.DOUBLE),
                ('default.time', rclpy.Parameter.Type.DOUBLE),
                ('square.amplitude', rclpy.Parameter.Type.DOUBLE),
                ('square.frequency', rclpy.Parameter.Type.DOUBLE),
                ('square.offset', rclpy.Parameter.Type.DOUBLE),
                ('square.phase', rclpy.Parameter.Type.DOUBLE),
                ('square.time', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.amplitude', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.frequency', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.offset', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.phase', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.time', rclpy.Parameter.Type.DOUBLE),
                
            ]
        )

        self.signal = 0
        self.t = 0

    
def main(args=None):
    rclpy.init(args=args)
    signal_generator = SignalGenerator()
    rclpy.spin(signal_generator)
    signal_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()