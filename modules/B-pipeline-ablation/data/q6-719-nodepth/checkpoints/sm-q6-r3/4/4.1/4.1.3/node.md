# N79: C_max_pop 取 min(带宽瓶颈, 计算瓶颈)：带宽允许6.93Gbps但计算仅允许5Gbps，故 C_max_pop = 5Gbps；需满足 2TB/

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

C_max_pop 取 min(带宽瓶颈, 计算瓶颈)：带宽允许6.93Gbps但计算仅允许5Gbps，故 C_max_pop = 5Gbps；需满足 2TB/10 = 0.2TB/POP = 200GB/POP 日均流量 ≤ 5Gbps * 0.8 * 86400s = 345GB，条件满足

## Corrected Claim

C_max_pop 取 min(带宽瓶颈, 计算瓶颈)：带宽允许6.93Gbps但计算仅允许5Gbps，故 C_max_pop = 5Gbps；需满足 2TB/10 = 0.2TB/POP = 200GB/POP 日均流量 ≤ 5Gbps * 0.8 * 86400s = 345GB，条件满足

## Evidence

父节点级核验未通过：不完备（子节点分别定义了计算瓶颈和带宽瓶颈，逻辑正交且无冗余。但父节点结论中 C_max_pop = 5Gbps，而子节点计算出的带宽瓶颈 C_bw_pop = 7.5Gbps，计算瓶颈 C_comp_pop = 6.72Gbps，两者取 min 应为 6.72Gbps，而非 5Gbps。子节点未解释 5Gbps 的来源（如是否包含其他未提及的限制因素），导致子节点推导结果与父节点结论不一致，存在逻辑断裂。）
