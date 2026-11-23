# N224: 合规阈值 T 的设定公式：T = T_base + k * sigma，其中 T_base 为 P50 延迟，k 为安全系数（通常 3-5），sigma 为延迟

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

合规阈值 T 的设定公式：T = T_base + k * sigma，其中 T_base 为 P50 延迟，k 为安全系数（通常 3-5），sigma 为延迟标准差；对于 C 端视频平台，行业基准 T_base ≈ 100ms，sigma ≈ 50ms，故 T ≈ 250-350ms。

## Corrected Claim

合规阈值 T 的设定公式：T = T_base + k * sigma，其中 T_base 为 P50 延迟，k 为安全系数（通常 3-5），sigma 为延迟标准差；对于 C 端视频平台，行业基准 T_base ≈ 100ms，sigma ≈ 50ms，故 T ≈ 250-350ms。

## Evidence

检索失败: no sources from any channel (all 5 failed)
