# N105: 自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 为 10 个 POP 的总缓存容量（GB），W_active 为热点内容工作集大小（GB），H_pop 直接决定跳数为 1 的请求比例。

## Corrected Claim

自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 为 10 个 POP 的总缓存容量（GB），W_active 为热点内容工作集大小（GB），H_pop 直接决定跳数为 1 的请求比例。

## Evidence

父节点级核验未通过：非正交（子节点4（缓存一致性/有效命中率）与子节点1（总容量）及子节点3（命中率对延迟的影响）存在概念重叠和逻辑耦合。子节点3讨论的是理论命中率 H_pop 对延迟的影响，而子节点4引入了有效命中率 H_pop_eff，这实际上是对 H_pop 的修正或细化，两者在“命中率如何影响系统表现”这一维度上不正交。此外，子节点4中的 E_rate 计算依赖于 C_pop_total（子节点1）和 Q_write（未定义的输入），导致子节点间存在参数依赖和逻辑纠缠，而非完全独立的分解维度。）
