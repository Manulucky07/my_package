from launch import LaunchDescription
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription([
        Node(
              package='demo_nodes_py',
              executable='listener'
        )
    ])