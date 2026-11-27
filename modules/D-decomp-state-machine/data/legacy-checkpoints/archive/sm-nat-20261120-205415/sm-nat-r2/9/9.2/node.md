# N82: LFU理论增益上限ΔH = H_LFU - H_LRU 的解析表达式为 ΔH = [∑_{i∈F} (h_i * s_i) - ∑_{i∈L} (h_i * s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LFU理论增益上限ΔH = H_LFU - H_LRU 的解析表达式为 ΔH = [∑_{i∈F} (h_i * s_i) - ∑_{i∈L} (h_i * s_i)] / ∑_{i=1}^{N} (h_i * s_i)，其中F和L均为大小K的对象集合，但排序准则不同；在Pareto分布下，ΔH的最大值出现在F完全由高频小对象组成而L包含低频大对象的极端情况。

## Corrected Claim

LFU理论增益上限ΔH = H_LFU - H_LRU 的解析表达式为 ΔH = [∑_{i∈F} (h_i * s_i) - ∑_{i∈L} (h_i * s_i)] / ∑_{i=1}^{N} (h_i * s_i)，其中F和L均为大小K的对象集合，但排序准则不同；在Pareto分布下，ΔH的最大值出现在F完全由高频小对象组成而L包含低频大对象的极端情况。

## Evidence

先验知识/题面给定，逻辑校验通过
