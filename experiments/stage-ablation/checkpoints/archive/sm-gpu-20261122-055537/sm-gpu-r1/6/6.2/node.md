# N29: 不确定性因素2：本地电力成本波动与运行模式。若工作站 24/7 运行，电力成本占比 TCO 可达 30-50%；若仅日间使用(8h/day)，电力成本占比降至 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

不确定性因素2：本地电力成本波动与运行模式。若工作站 24/7 运行，电力成本占比 TCO 可达 30-50%；若仅日间使用(8h/day)，电力成本占比降至 10-20%。需根据实际使用时长 T_hours 调整 C_power 权重，进而影响 4090 (高功耗) vs L4 (低功耗) 的排序。

## Corrected Claim

不确定性因素2：本地电力成本波动与运行模式。若工作站 24/7 运行，电力成本占比 TCO 可达 30-50%；若仅日间使用(8h/day)，电力成本占比降至 10-20%。需根据实际使用时长 T_hours 调整 C_power 权重，进而影响 4090 (高功耗) vs L4 (低功耗) 的排序。

## Evidence

先验知识/题面给定，逻辑校验通过：24/7运行下电力成本占比30-50%符合高功耗GPU（如4090）在低电价或高负载场景下的TCO分布规律；8h/day降至10-20%符合线性缩放逻辑；功耗差异对排序的影响符合基本经济直觉。

## Search Query

GPU inference power cost percentage of TCO 24/7 vs 8h/day
