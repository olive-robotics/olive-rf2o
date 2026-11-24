# ANT1 source provenance

Recovery and publication date: 2026-11-24.

## Recovered source

The RF2O package was recovered from an OlixOS filesystem backup:

```text
olixos_full_20260914_224342/srv/olixos/opt/olive/hl_ws/tmp_ws/src/navigation/real/rf2o_laser_odometry
```

Its original CMakeLists.txt, package.xml, README, LICENSE, launch file, C++
source, and headers are preserved byte-for-byte at the tag
`ant1-recovered-2026-11-24`. That tag also retains the initial publication
files; the hashes in SOURCE_MANIFEST.json identify the recovered files.

The recovered package was clean in its original navigation repository.
The last package change was commit
`e741952b56dca6a32fbd01d5bfe24e6ba4a32cbc`, dated 2026-05-11.
The two C++ files were last changed in
`9e7f63f97aa5a1e9f1682420323248241024e8f2`, dated 2025-11-17.
Only the RF2O package was copied; unrelated navigation source was excluded.

The C++ implementation and headers on `main` remain byte-for-byte identical
to that recovered package. The deployed launch file on `main` was recovered
separately from the installed Humble and Jazzy packages; those copies are
identical and add the `global_tfs` option to the older backup launch file.

## Identified upstream

Primary upstream: <https://github.com/MAPIRlab/rf2o_laser_odometry>

Branch: `ros2`

Commit: `b38c68e46387b98845ecbfeb6660292f967a00d3`

The recovered headers, CMakeLists.txt, package.xml, README, and LICENSE match
this commit exactly. The two recovered C++ files differ only by disabled
routine logging and a final newline. The recovered launch configuration
contains the Olive robot namespace changes.

The original MAPIR history is a parent of the recovery commit. The initial
Adlink ROS 2 baseline is also retained in history, at
`upstream-humble-313bb4c`. It is not the primary upstream of the recovered
ANT1 implementation.

## Evidence connecting the recovery to installed packages

The installed Humble and Jazzy packages both report version `0.1.0`, and
both package.xml files match the recovered manifest byte-for-byte.

The binaries reference these build source directories:

```text
/opt/olive/hl_ws/humble/tmp_ws/src/navigation/real/rf2o_laser_odometry
/opt/olive/hl_ws/jazzy/tmp_ws/src/navigation/real/rf2o_laser_odometry
```

All observed logging source locations embedded in both binaries match the
recovered C++ files:

| Source | Logging lines |
| --- | --- |
| src/CLaserOdometry2DNode.cpp | 24, 125, 179 |
| src/CLaserOdometry2D.cpp | 68, 842 |

The original publisher/timing/pose logs disabled in the recovered source are
also absent from the installed executables. This evidence connects the
recovered source to the installed package; a byte-for-byte reproduction of
the installed executables has not been demonstrated.

| Installed artifact | SHA-256 |
| --- | --- |
| Humble rf2o_laser_odometry_node | `0c41b91b4b928d455de9304b001292c06f9c49ba04afcd290d0e3d4f5191699a` |
| Jazzy rf2o_laser_odometry_node | `861f21e9784775bd96f06117d69d6db8bcfd1637e4971463dfa56a2c8049d28b` |
| Deployed launch, both distributions | `7535c97a542422f438326c15fadcc4c1172732b042ef6c737f2b19c3a8786f12` |
| package.xml, both distributions | `cf1cd38d584d35ea07523fc4f33eee2260df82f9596ba6a2b275f0c459b61f25` |

## Publication changes

`main` supplements the recovery with dependency declarations for nav_msgs,
Boost, and the Python launch modules, installation of license/provenance
files, publication documentation, and the newer deployed launch file.
These changes do not alter the recovered C++ source or headers.

No prebuilt executable is distributed in this repository. The package is
built from the supplied source using CMake/ament and the dependencies
listed in package.xml. See README.md for build and launch instructions.
