import os
from ament_index_python.package import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('signal_decomposition')
            'config',
            'params.yaml'
    )
    
    signal_generator_node = Node(
        package='courseworks',
        executable='signal_generator',
        output='screen',
        parameters= [config]
    )

    reconstruction_node = Node(
        package='courseworks',
        executable='reconstruction',
        output='screen',
    )

    rqt_graph_node = Node(
        package='rqt_graph',
        executable='rqt_graph',
        output='screen',
    )

    rqt_plot_node = Node(
        package='rqt_plot',
        executable='rqt_plot',
        parameters=[{'args':'/signal/wave/data /signal_reconstructed/wave'}]
    )

    l_d = LaunchDescription([signal_generator_node, reconstruction_node, 
                            rqt_plot_node])
    return l_d

