#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    namespace = LaunchConfiguration('namespace').perform(context).strip('/')
    global_tfs = LaunchConfiguration('global_tfs').perform(context).lower() == 'true'

    # olive/olixG1/id001 -> olive_olixG1_id001
    frame_prefix = namespace.replace('/', '_')

    def frame(name):
        if frame_prefix:
            return f'{frame_prefix}_{name}'
        return name

    rf2o_laser_odometry = Node(
        package='rf2o_laser_odometry',
        executable='rf2o_laser_odometry_node',
        name='rf2o_laser_odometry',
        namespace=namespace,
        output='screen',
        parameters=[{
            'laser_scan_topic': 'scan',
            'odom_topic': 'odom',
            'publish_tf': True,

            'base_frame_id': frame('base_link'),
            'odom_frame_id': frame('odom'),

            'init_pose_from_topic': '',
            'freq': 10.0,
        }],
        remappings=[] if global_tfs else [
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static'),
        ],
    )

    return [rf2o_laser_odometry]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Robot namespace, e.g. olive/olixG1/id001',
        ),

        DeclareLaunchArgument(
            'global_tfs',
            default_value='false',
            description='Use global /tf and /tf_static topics',
        ),

        OpaqueFunction(function=launch_setup),
    ])
