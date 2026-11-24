# N96: 平均单个短视频大小 s_vid，基于典型 C 端短视频参数（H.264/HEVC，分辨率 720p，时长 15s，码率 2-4 Mbps）估算，典型值约为 5-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

平均单个短视频大小 s_vid，基于典型 C 端短视频参数（H.264/HEVC，分辨率 720p，时长 15s，码率 2-4 Mbps）估算，典型值约为 5-10 MB，取中值 7.5 MB = 0.00713 GB，[时效待核]。

## Corrected Claim

平均单个短视频大小 s_vid，基于典型 C 端短视频参数（H.264/HEVC，分辨率 720p，时长 15s，码率 2-4 Mbps）估算，典型值约为 5-10 MB，取中值 7.5 MB = 0.00713 GB，[时效待核]。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应低、标准、高三个不同的工作点（码率/分辨率/时长组合），彼此独立无重叠（正交）；涵盖了父节点定义的典型范围及不同应用场景（完备）；虽然本质上是同一参数公式在不同输入下的计算结果，但作为‘工作点’分解，每个节点提供了独特的场景定义和成本量级，具有独立的业务参考价值，不构成需要压缩的冗余信息。）

## Search Query

average short video file size 720p 15 seconds bitrate
