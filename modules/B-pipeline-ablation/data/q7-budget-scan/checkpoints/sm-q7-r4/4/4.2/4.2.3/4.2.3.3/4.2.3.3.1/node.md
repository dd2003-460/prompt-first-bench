# N461: 修正悲观工作点的重建时间：采用 N69 修正后的 16TB CMR 盘单盘持续写带宽 180MB/s（取 150-200MB/s 中值），而非 N204 原用的

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N204

## Claim

修正悲观工作点的重建时间：采用 N69 修正后的 16TB CMR 盘单盘持续写带宽 180MB/s（取 150-200MB/s 中值），而非 N204 原用的 150MB/s；考虑 50% I/O 抑制后有效带宽为 90MB/s。

## Corrected Claim

修正悲观工作点的重建时间：采用 N69 修正后的 16TB CMR 盘单盘持续写带宽 180MB/s（取 150-200MB/s 中值），而非 N204 原用的 150MB/s；考虑 50% I/O 抑制后有效带宽为 90MB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：180MB/s为150-200MB/s的中值，50%抑制后90MB/s计算正确，符合CMR硬盘性能常识
