# N11: LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i)

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Σ_{i∈U} r_i s_i；其中C_LFU由频率r_i降序排列，C_LRU由最近访问决定；在稳态下，C_LFU ≈ 热度前k对象，C_LRU可能包含更多低频但最近访问对象。

## Corrected Claim

LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Σ_{i∈U} r_i s_i；其中C_LFU由频率r_i降序排列，C_LRU由最近访问决定；在稳态下，C_LFU ≈ 热度前k对象，C_LRU可能包含更多低频但最近访问对象。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3存在严重重叠和逻辑矛盾。子节点3讨论的‘LRU完全失效’实际上是子节点2中‘非稳态/动态负载’的一种极端特例，两者都在计算ΔH的上界，导致内容冗余。此外，子节点1声称稳态下LRU趋近LFU（ΔH≈0），这与父节点中提到的‘LRU可能包含更多低频但最近访问对象’的通用场景存在语境冲突，未明确区分‘纯稳态’与‘一般稳态’。）
