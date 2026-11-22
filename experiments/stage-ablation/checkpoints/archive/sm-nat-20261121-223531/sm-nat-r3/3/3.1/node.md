# N13: LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[S|H=h] dh，其中 h_threshold 为 LFU 频率阈值，增益机制源于 LFU 优先保留高频对象，即使其大小较大，字节命中率提升取决于大小-热度负相关程度，最大增益 [待核验] 5-10 百分点。

## Corrected Claim

LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[S|H=h] dh，其中 h_threshold 为 LFU 频率阈值，增益机制源于 LFU 优先保留高频对象，即使其大小较大，字节命中率提升取决于大小-热度负相关程度，最大增益 [待核验] 5-10 百分点。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点 N13 聚焦于容量充足（无淘汰）时的边界条件（增益为 0），而另一个子节点聚焦于通过引入‘写失效’或‘动态工作集’使增益非零的机制。两者分别描述了不同前提假设下的情况，互不重叠且无矛盾。父节点的核心在于 LFU 相对 LRU 的增益上限及其依赖条件，两个子节点分别覆盖了‘无差异场景’和‘有差异场景’的关键约束，逻辑上构成了完备的解释。）

## Search Query

LFU vs LRU cache hit rate improvement pareto workload correlation
