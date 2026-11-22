# N17: LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L_i) / R_total，其提升幅度 Δ_max = H_lfu - H_lru 取决于LRU未能缓存的尾部大对象的总字节流量占比。

## Corrected Claim

LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L_i) / R_total，其提升幅度 Δ_max = H_lfu - H_lru 取决于LRU未能缓存的尾部大对象的总字节流量占比。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性失败：子节点4中H_lfu的分子定义（S_i > C/k_eff）与子节点2中k_eff的定义（基于LRU容量限制）存在概念混淆，且子节点4的截断条件与父节点给出的标准LFU公式（通常基于频率或特定阈值，而非简单的平均驻留大小）不完全一致，导致逻辑链条断裂。2. 完备性失败：父节点核心是计算Δ_max = H_lfu - H_lru。子节点提供了H_lfu的近似/特定计算（子节点4）和中间变量T_LRU/k_eff（子节点1,2），但**完全缺失了H_lru的计算公式**。没有H_lru，无法得出最终的提升幅度Δ_max。此外，子节点3讨论的'D'（疑似衰减或概率参数）在父节点中未定义，属于引入未声明变量，破坏了解释的自包含性。）

## Search Query

LFU vs LRU cache hit rate theoretical bound static workload
