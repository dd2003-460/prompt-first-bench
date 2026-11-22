# N62: LFU 与 LRU 命中率差异的理论上限推导：在稳态 Zipf 负载下，LFU 的命中率提升 ΔH 主要来源于消除 LRU 的‘时间局部性失效’。ΔH ≈ P[

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LFU 与 LRU 命中率差异的理论上限推导：在稳态 Zipf 负载下，LFU 的命中率提升 ΔH 主要来源于消除 LRU 的‘时间局部性失效’。ΔH ≈ P[object is hot but recently cold] * (H_LFU - H_LRU_miss)。根据 N23 的 RSE=4.8% 和 N24 的 LRU 污染率 5-10%，LFU 相比 LRU 的最大提升幅度上限约为 3-5 个百分点，前提是 LFU 的频率计数器能够准确区分 Top-10% 与 Top-20%（RSE < 差异幅度）。

## Corrected Claim

LFU 与 LRU 命中率差异的理论上限推导：在稳态 Zipf 负载下，LFU 的命中率提升 ΔH 主要来源于消除 LRU 的‘时间局部性失效’。ΔH ≈ P[object is hot but recently cold] * (H_LFU - H_LRU_miss)。根据 N23 的 RSE=4.8% 和 N24 的 LRU 污染率 5-10%，LFU 相比 LRU 的最大提升幅度上限约为 3-5 个百分点，前提是 LFU 的频率计数器能够准确区分 Top-10% 与 Top-20%（RSE < 差异幅度）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点结构清晰，分别对应概率量化（LRU失效）、误差量化（LFU噪声）、净增益合成（公式分解）以及边界条件验证（不等式约束）。四个节点在逻辑上是递进且互补的，没有内容重复或矛盾，且完整覆盖了父节点中提到的所有关键变量（P[hot but cold], P[LFU_error], ΔH_net, 边界条件）及前提假设。）
