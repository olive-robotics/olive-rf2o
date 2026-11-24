# Source provenance

Publication date: 2026-11-24.

## Upstream source

Repository: <https://github.com/Adlink-ROS/rf2o_laser_odometry>

Branch: `humble-devel`

Commit: `313bb4c4123bcc0cc2e042f278312b19a3c46f31`

All upstream commits were retained. The files under `src/` and `include/`
and the original launch file are unchanged from that commit.
`UPSTREAM_README.md` is an unchanged copy of that commit's README.
`LICENSE` is the unchanged upstream GNU GPL version 3 text.

## Olive changes in this publication

- `launch/olive_rf2o.launch.py` was recovered from the installed Olive
  Humble package. The installed Jazzy launch file has identical contents.
  Apart from the publication notice immediately after the shebang, its
  contents are unchanged. It adds namespace-aware topics, frame names,
  and optional global TF topics.
- `package.xml` declares `nav_msgs`, Boost, and the Python launch
  dependencies already used by the existing code and launch files.
- `CMakeLists.txt` installs the license and attribution/provenance files
  alongside the package.
- `README.md`, `NOTICE`, this file, and `.gitignore` were added for this
  source publication.

## Existing binary releases: correspondence not verified

The publication workspace contained installed Humble and Jazzy packages
but did not contain their original C++ build sources. The installed
package version is `0.1.0`.

The executables embed these source paths:

```text
/opt/olive/hl_ws/humble/tmp_ws/src/navigation/real/rf2o_laser_odometry
/opt/olive/hl_ws/jazzy/tmp_ws/src/navigation/real/rf2o_laser_odometry
```

The logging source locations embedded in the installed executables
differ from the imported upstream source. This is evidence that the
build inputs differed; the original source is needed to identify the
actual changes. The matching package version alone is not proof of
source correspondence.

The following SHA-256 fingerprints identify the existing workspace
artifacts. They are not binaries built from this publication.

| Artifact | SHA-256 |
| --- | --- |
| Humble `rf2o_laser_odometry_node` | `0c41b91b4b928d455de9304b001292c06f9c49ba04afcd290d0e3d4f5191699a` |
| Jazzy `rf2o_laser_odometry_node` | `861f21e9784775bd96f06117d69d6db8bcfd1637e4971463dfa56a2c8049d28b` |
| Installed launch file, both distributions | `7535c97a542422f438326c15fadcc4c1172732b042ef6c737f2b19c3a8786f12` |
| Installed `package.xml`, both distributions | `cf1cd38d584d35ea07523fc4f33eee2260df82f9596ba6a2b275f0c459b61f25` |

## Remaining work for those binary releases

Recover the actual source tree and local changes used to build each
distributed version, together with the relevant build and installation
scripts. Compare and publish those inputs, then identify them with
release-specific commits or tags. Preserve any additional third-party
license notices discovered in those sources.

Until that work is complete, this repository is an upstream source
publication with a recovered Olive launch configuration, rather than
a verified corresponding-source release for those existing binaries.
