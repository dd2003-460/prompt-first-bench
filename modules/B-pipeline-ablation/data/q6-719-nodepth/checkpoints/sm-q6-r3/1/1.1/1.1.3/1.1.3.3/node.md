# N152: 在西部/东北长尾区域用户低密度场景下，约 10% 用户位于该区域，最近 POP 平均距离 d_avg ≈ 500-1000km，代表低用户密度/高平均延迟工作点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

在西部/东北长尾区域用户低密度场景下，约 10% 用户位于该区域，最近 POP 平均距离 d_avg ≈ 500-1000km，代表低用户密度/高平均延迟工作点，通常由公有云 CDN 覆盖，自建 POP 成本效益低。

## Corrected Claim

在西部/东北长尾区域用户低密度场景下，约 10% 用户位于该区域，最近 POP 平均距离 d_avg ≈ 500-1000km，代表低用户密度/高平均延迟工作点，通常由公有云 CDN 覆盖，自建 POP 成本效益低。

## Evidence

先验知识/题面给定，逻辑校验通过：西部/东北长尾区域用户密度低，500-1000km 的平均距离符合地理分布直觉，且该距离下自建 POP 的边际成本高于收益，符合 CDN 经济学原理。

## Search Query

China user distribution West Northeast long tail CDN coverage distance
