# N47: 讨价还价弹性 ε = b * C_search / W，其中 b 为价格敏感度系数，C_search 为买家搜索成本，ε 直接决定最终成交价 P_final =

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

讨价还价弹性 ε = b * C_search / W，其中 b 为价格敏感度系数，C_search 为买家搜索成本，ε 直接决定最终成交价 P_final = P_ask * (1 - ε) 的分布

## Corrected Claim

讨价还价弹性 ε = b * C_search / W，其中 b 为价格敏感度系数，C_search 为买家搜索成本，ε 直接决定最终成交价 P_final = P_ask * (1 - ε) 的分布

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上分别对应公式中的参数 b、C_search 以及最终结果分布，彼此正交且无冗余。但完备性不足：父节点公式中明确包含分母 W（通常指代卖家保留价格或基准工资/价值），但子节点仅解释了 b 和 C_search，未对 W 的定义、估计方法或其在分布中的作用进行分解说明，导致公式变量覆盖不全。）
