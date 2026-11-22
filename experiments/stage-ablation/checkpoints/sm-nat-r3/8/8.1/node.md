# N95: LFU 相对 LRU 的理论最大提升 ΔH_max 的解析上界公式：ΔH_max ≈ (H_byte_LFU - H_byte_LRU) = (Σ_{i∈S_L

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

LFU 相对 LRU 的理论最大提升 ΔH_max 的解析上界公式：ΔH_max ≈ (H_byte_LFU - H_byte_LRU) = (Σ_{i∈S_LFU∖S_LRU} p_i s_i - Σ_{i∈S_LRU∖S_LFU} p_i s_i) / (Σ_all p_i s_i)，其中 S_LFU 和 S_LRU 分别为在 128GB 容量下 LFU 和 LRU 保留的对象集合，需分别计算两个集合的字节加权访问概率差。

## Corrected Claim

LFU 相对 LRU 的理论最大提升 ΔH_max 的解析上界公式：ΔH_max ≈ (H_byte_LFU - H_byte_LRU) = (Σ_{i∈S_LFU∖S_LRU} p_i s_i - Σ_{i∈S_LRU∖S_LFU} p_i s_i) / (Σ_all p_i s_i)，其中 S_LFU 和 S_LRU 分别为在 128GB 容量下 LFU 和 LRU 保留的对象集合，需分别计算两个集合的字节加权访问概率差。

## Evidence

父节点级核验未通过：非正交（子节点之间存在逻辑矛盾与参数冲突。子节点1引用了 'ρ=-0.3' 场景，而子节点2引用了 'Pareto(β=0.9)' 场景，这两个是不同的工作负载假设，无法在同一个 ΔH_max 计算中同时作为单一确定性的输入值进行相减。此外，子节点3直接基于这两个不同场景下的数值进行了算术运算，导致结论在逻辑上是不成立的（即不能将不同模型假设下的局部指标直接线性组合得出全局理论界）。）
