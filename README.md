# olive-rf2o

RF2O estimates planar robot motion from consecutive 2D laser scans. This
repository publishes the upstream ROS 2 implementation and the Olive Robotics
launch configuration under the GNU General Public License, version 3.

The ROS package and executable retain their upstream names:
`rf2o_laser_odometry` and `rf2o_laser_odometry_node`.

## Origin and license

- Upstream: <https://github.com/Adlink-ROS/rf2o_laser_odometry>
- Imported branch: `humble-devel`
- Imported commit: `313bb4c4123bcc0cc2e042f278312b19a3c46f31`
- Original Git history and source notices are preserved.
- The full license is in [LICENSE](LICENSE); attribution is in [NOTICE](NOTICE).
- The original README is preserved in [UPSTREAM_README.md](UPSTREAM_README.md).

The original RF2O work is **Planar Odometry from a Radial Laser Scanner.
A Range Flow-based Approach**, ICRA 2016. See the upstream README for the
project reference.

## Source coverage

This publication contains the upstream C++ implementation, headers, build
definition, and Olive's recovered robot launch configuration.

**It has not yet been verified as the exact source of the existing Olive
Humble or Jazzy binaries.** Their original build source was not present in
the workspace used to prepare this publication. Publishing this repository
does not, by itself, establish that those binary releases have complete
corresponding source available.

See [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md) for the known changes,
binary fingerprints, and remaining verification.

## Build

Use a ROS 2 Humble development environment with `colcon`, `rosdep`, a C++
compiler, CMake, Boost, and Eigen 3. The documented baseline is Humble;
this publication has not been built or tested against Jazzy.

```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/rf2o_ws/src
cd ~/rf2o_ws/src
git clone https://github.com/olive-robotics/olive-rf2o.git
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select rf2o_laser_odometry
source install/setup.bash
```

## Run

To use the original upstream launch configuration:

```bash
ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py
```

To use the Olive Robotics launch configuration:

```bash
ros2 launch rf2o_laser_odometry olive_rf2o.launch.py \
  namespace:=olive/olixG1/id001
```

The Olive launch configuration uses relative `scan` and `odom` topics,
10 Hz processing, and namespace-prefixed `base_link` and `odom` frame IDs.
By default, TF topics are relative to the namespace. Set `global_tfs:=true`
to use global `/tf` and `/tf_static` topics.

Provide a laser scan stream and a transform between the laser frame and
the configured base frame. Do not run this node and another odometry
publisher with conflicting TF authority.
