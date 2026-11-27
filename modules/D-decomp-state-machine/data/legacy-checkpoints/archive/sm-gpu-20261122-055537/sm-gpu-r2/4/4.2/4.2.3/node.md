# N66: 2x RTX 4090 多卡方案的整机满载功耗 P_draw_2x4090 约为 1100-1200W（含2x GPU TDP 900W + 双卡系统基础负载 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

2x RTX 4090 多卡方案的整机满载功耗 P_draw_2x4090 约为 1100-1200W（含2x GPU TDP 900W + 双卡系统基础负载 ~200-300W），需注意多卡散热风道效率降低导致的额外风扇功耗。

## Corrected Claim

2x RTX 4090 多卡方案的整机满载功耗 P_draw_2x4090 约为 1100-1200W（含2x GPU TDP 900W + 双卡系统基础负载 ~200-300W），需注意多卡散热风道效率降低导致的额外风扇功耗。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 TDP 为 900W，加上系统基础负载 200-300W，总功耗 1100-1200W 符合物理直觉与工程常识。
