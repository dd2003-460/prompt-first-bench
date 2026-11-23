# N76: TTL 设置对存储成本的影响：C_storage(TTL) = C_base * (1 + (TTL/T_base)^γ)，其中 C_base 为基准存储成本，

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

TTL 设置对存储成本的影响：C_storage(TTL) = C_base * (1 + (TTL/T_base)^γ)，其中 C_base 为基准存储成本，T_base 为基准 TTL，γ 为成本增长指数（通常 0.3-0.7）

## Corrected Claim

TTL 设置对存储成本的影响：C_storage(TTL) = C_base * (1 + (TTL/T_base)^γ)，其中 C_base 为基准存储成本，T_base 为基准 TTL，γ 为成本增长指数（通常 0.3-0.7）

## Evidence

父节点级核验未通过：不完备（子节点之间在定义上保持了较好的正交性，分别涵盖了输入参数（T_update, C_base, T_base）、中间变量（β, δ, γ, H）以及最终优化目标（TTL_opt）。但是，父节点明确给出的公式是 C_storage(TTL) = C_base * (1 + (TTL/T_base)^γ)，而子节点8引入的优化目标 C_total(TTL) 包含了 C_bw 和 C_penalty，这超出了父节点“存储成本”的范畴。此外，子节点3的混合命中率公式和子节点2的β指数虽然相关，但β通常用于描述命中率对TTL的敏感度，而子节点3直接给出了加权命中率公式，两者存在概念上的重叠或依赖关系未完全厘清（β应作为计算H_i(TTL)的参数，而非独立并列的概念）。最关键的是，父节点仅关注“存储成本”，但子节点8引入了带宽成本和惩罚成本，导致子节点集合扩展到了父节点未涵盖的领域，破坏了针对“存储成本”这一特定主题的完备性和聚焦性。）
