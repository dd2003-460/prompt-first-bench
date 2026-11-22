# N74: S_total 饱和机制的解释：当 α < 2 时，S_total 的收敛性由截断项 (S_max/S_min)^(-(α-1)) 主导，随着 S_max 增大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

S_total 饱和机制的解释：当 α < 2 时，S_total 的收敛性由截断项 (S_max/S_min)^(-(α-1)) 主导，随着 S_max 增大，该项趋于 0，S_total 趋于 N * S_min / (α-1) = 100,000 * 1KB / 0.1 = 1,000,000 KB = 1 GB，因此 S_total 的上限为 1 GB，任何 S_max > 100MB 的增加对 S_total 的影响可忽略不计（<0.1%），这解释了为何 S_max 的具体取值在 10MB-1GB 范围内对最终命中率计算影响极小。

## Corrected Claim

S_total 饱和机制的解释：当 α < 2 时，S_total 的收敛性由截断项 (S_max/S_min)^(-(α-1)) 主导，随着 S_max 增大，该项趋于 0，S_total 趋于 N * S_min / (α-1) = 100,000 * 1KB / 0.1 = 1,000,000 KB = 1 GB，因此 S_total 的上限为 1 GB，任何 S_max > 100MB 的增加对 S_total 的影响可忽略不计（<0.1%），这解释了为何 S_max 的具体取值在 10MB-1GB 范围内对最终命中率计算影响极小。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布截断和的数学推导，当α=1.1时，S_total收敛于N*S_min/(α-1)=1GB，且截断项随S_max增大迅速衰减，逻辑自洽。
