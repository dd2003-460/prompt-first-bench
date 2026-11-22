# N60: 更新率导致的命中率衰减系数 δ_update：当更新率 u=1%/天 时，LRU 缓存中对象因过期而被驱逐或返回旧数据的概率增加。有效命中率 H_eff = H

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

更新率导致的命中率衰减系数 δ_update：当更新率 u=1%/天 时，LRU 缓存中对象因过期而被驱逐或返回旧数据的概率增加。有效命中率 H_eff = H_LRU * (1 - P_stale_hit)。P_stale_hit ≈ u * T_res_avg，其中 T_res_avg 是缓存内对象的平均驻留时间。若 T_res_avg ≈ 1.2 天（由 K 和总请求率推算），则 P_stale_hit ≈ 0.012，即命中率打 0.988 折，损失约 1.2 个百分点。

## Corrected Claim

更新率导致的命中率衰减系数 δ_update：当更新率 u=1%/天 时，LRU 缓存中对象因过期而被驱逐或返回旧数据的概率增加。有效命中率 H_eff = H_LRU * (1 - P_stale_hit)。P_stale_hit ≈ u * T_res_avg，其中 T_res_avg 是缓存内对象的平均驻留时间。若 T_res_avg ≈ 1.2 天（由 K 和总请求率推算），则 P_stale_hit ≈ 0.012，即命中率打 0.988 折，损失约 1.2 个百分点。

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 正交性违反：子节点1（Belady上限）和子节点3（LFU稳态命中率）在公式上完全相同（均为Top-K字节覆盖率），且子节点3的结论（LFU=LRU稳态）直接否定了子节点2中关于LFU增益的讨论基础，导致逻辑冲突。2. 冗余：子节点1和子节点3本质上是同一个计算（Top-K覆盖率），只是引用了不同的算法名称，应合并。）
