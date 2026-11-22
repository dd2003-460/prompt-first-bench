# N156: 对象更新率 U=1%/天 对LRU有效命中率的影响系数 D_update ≈ 1 - (U * T_res_avg)，其中 T_res_avg 为缓存内平均对象

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 U=1%/天 对LRU有效命中率的影响系数 D_update ≈ 1 - (U * T_res_avg)，其中 T_res_avg 为缓存内平均对象驻留时间。对于头部对象，T_res_avg << 1/U，故 D_update ≈ 1.0；对于尾部对象，虽然 T_res_avg 可能接近 1/U，但其字节流量权重 < 1%，故整体有效命中率折扣 < 0.1%（即打 0.999 折）。

## Corrected Claim

对象更新率 U=1%/天 对LRU有效命中率的影响系数 D_update ≈ 1 - (U * T_res_avg)，其中 T_res_avg 为缓存内平均对象驻留时间。对于头部对象，T_res_avg << 1/U，故 D_update ≈ 1.0；对于尾部对象，虽然 T_res_avg 可能接近 1/U，但其字节流量权重 < 1%，故整体有效命中率折扣 < 0.1%（即打 0.999 折）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
