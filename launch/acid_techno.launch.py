from launch import LaunchDescription
from launch_ros.actions import Node
 
 
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='acid_techno',
            executable='path_find_node',
            name='path_find_node',
            output='screen',
            parameters=[
                {'scan_topic': '/scan'},
                {'input_cmd_topic': '/cmd_vel_raw'},
                {'output_cmd_topic': '/cmd_vel'},
                {'stop_distance': 0.25},
                {'front_angle_deg': 30.0},
            ]
        )
    ])
