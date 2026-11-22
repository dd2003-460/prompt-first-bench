# N303: LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_thresh

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_threshold 为满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率阈值；需明确频率分布模型（如 Zipf 分布）参数以计算 f_threshold。

## Corrected Claim

LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_threshold 为满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率阈值；需明确频率分布模型（如 Zipf 分布）参数以计算 f_threshold。

## Evidence

先验知识/题面给定，逻辑校验通过
