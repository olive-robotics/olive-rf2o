# olive-rf2o

Source mirror of the RF2O laser odometry package used by Olive Robotics ANT1.
It includes the recovered robot source, the deployed launch configuration,
original author notices, and the complete GNU GPL version 3 license.

The ROS package remains `rf2o_laser_odometry`; its executable remains
`rf2o_laser_odometry_node`.

## Source and license

The recovered implementation is based on
[MAPIRlab/rf2o_laser_odometry](https://github.com/MAPIRlab/rf2o_laser_odometry),
`ros2` commit `b38c68e46387b98845ecbfeb6660292f967a00d3`.
The original MAPIR and Adlink Git histories are preserved.

Compared with MAPIR, the recovered C++ changes disable routine execution-time,
pose, and publication logging. The recovered headers are unchanged from MAPIR.
The robot launch configuration adds namespaced topics and frames and optional
global TF topics.

- [LICENSE](LICENSE): complete GNU GPL version 3 text.
- [NOTICE](NOTICE): author credits and dated publication changes.
- [UPSTREAM_README.md](UPSTREAM_README.md): original MAPIR documentation.
- [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md): recovery evidence, release
  fingerprints, and validation limits.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json): SHA-256 hashes of the recovered
  package and the deployed launch configuration.

The tag `ant1-recovered-2026-11-24` preserves the recovered package files
byte-for-byte. The `main` branch adds publication documentation, dependency
metadata, license installation, and the launch configuration recovered from
both installed Humble and Jazzy packages.

## Build

Use a ROS 2 Humble development environment with `colcon`, `rosdep`, a C++
compiler, CMake, Boost, and Eigen 3. The commands below use the standard ROS
installation location; adjust the setup path for a custom installation.

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

```bash
ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py \
  namespace:=olive/olixG1/id001
```

The launch configuration uses relative `scan` and `odom` topics, 10 Hz
processing, and namespace-prefixed `base_link` and `odom` frame IDs. TF
publication defaults to namespaced `tf` and `tf_static` topics. To use global
TF topics, add `global_tfs:=true`.

Provide a laser scan stream and a transform between the laser frame and the
configured base frame. Avoid conflicting odometry/TF publishers for the same
frames. `olive_rf2o.launch.py` is an equivalent launch entry point.

## Original work

**Planar Odometry from a Radial Laser Scanner. A Range Flow-based Approach**,
ICRA 2016. See the original README and source headers for the paper and credits.
