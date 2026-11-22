# N6: LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中 F_req 是热度 Pareto(β=0.9) 的 CDF，N_cap 是缓存对象数

## Corrected Claim

LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中 F_req 是热度 Pareto(β=0.9) 的 CDF，N_cap 是缓存对象数

## Evidence

父节点级核验未通过：不完备（子节点存在严重的逻辑矛盾和事实错误。子节点2声称 N_cap (13,100,000) 远大于总对象数 N (100,000)，这在数学上是成立的，但由此推导出的结论“LRU 实际上可以缓存所有对象”与父节点公式中 N_cap 作为“缓存对象数”的定义在常规语境下可能冲突（通常 N_cap 指缓存容量能容纳的对象数，若容量极大则命中率趋近1）。更关键的是，父节点公式旨在计算一个基于部分缓存（N_cap < N）时的下界，而子节点2直接断言 N_cap > N 导致命中率理论值为 100%，这忽略了父节点公式存在的意义（即处理 N_cap < N 的情况）。此外，子节点1仅定义了 CDF，未解释 S_mean 项，导致对父节点公式的分解不完备。）
