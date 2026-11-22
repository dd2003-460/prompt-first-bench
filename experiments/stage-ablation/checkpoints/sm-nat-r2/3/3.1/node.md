# N15: LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 Cache_LFU 为 LFU 保留的对象集合，需确定 LFU 在长尾负载下的保留策略。

## Corrected Claim

LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 Cache_LFU 为 LFU 保留的对象集合，需确定 LFU 在长尾负载下的保留策略。

## Evidence

父节点级核验未通过：不完备（子节点1关注集合确定准则（定义Cache_LFU），子节点2关注基于该集合的性能指标计算（计算Hit Probability），两者逻辑上正交且互补。然而，父节点核心在于'上限公式'及'长尾负载下的保留策略'，子节点2引入了具体的Pareto分布参数（β=0.9）和与LRU的对比，这超出了父节点'确定保留策略'的通用理论范畴，且未明确说明该具体分布是否代表父节点所指代的'长尾负载'的一般情况，导致完备性存疑（缺少对一般长尾分布下策略的通用性讨论或明确界定）。）
