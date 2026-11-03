# ROS2 & micro-ROS coursework (TE3002B)

Exercises from TE3002B (Intelligent Robotics Implementation) at Tecnológico de Monterrey, 2024: ROS2 basics and talking to a microcontroller with micro-ROS.

## Contents

### `minireto3.ino`: micro-ROS on an ESP32
An Arduino sketch that makes an ESP32 a micro-ROS node:
- reads a potentiometer on the ADC and publishes the raw value (`Int32`) and the voltage (`Float32`) on two timers
- subscribes to a PWM duty cycle (0–100%, `Float32`) and drives an output pin with it
- blinks the onboard LED if micro-ROS setup fails

### `ros2_ws/`: ROS2 workspace
| Package | What it covers |
|---|---|
| `basic_comms` | Talker/listener nodes and launch files, including grouped launches |
| `courseworks_params` | ROS2 parameters |
| `msgs_clase` | A custom message type (`Sphere.msg`) |
| `sphere_msgs` | A node that uses the custom message |
| `signal_decomposition` | A signal generator node and a node that reconstructs the signal |
| `courseworks` | An earlier version of the signal generator and reconstruction nodes |
| `signal_msg` | Custom message (`SignalDecomposed.msg`) carrying the signal type, amplitude, frequency, offset, phase and time |
| `final_challenge` | Setpoint node that generates sine, square or sawtooth reference signals, configured through a YAML parameter file, and publishes it to the ESP32 on `micro_ros_esp32/setpoint` |

## Running

Build the workspace:
```bash
cd ros2_ws
colcon build
source install/setup.bash
ros2 launch basic_comms chit_chat_launch.py
ros2 launch final_challenge setpoint_launch.py
```

For the ESP32 sketch, install the `micro_ros_arduino` library, flash `minireto3.ino`, and start a micro-ROS agent on the host.
