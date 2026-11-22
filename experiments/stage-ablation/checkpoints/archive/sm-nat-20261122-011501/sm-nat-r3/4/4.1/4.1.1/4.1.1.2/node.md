# N120: T_res 与对象大小 s_i 的耦合效应：由于 ρ=-0.3，小对象（s_i < s_median）的 P_access 比独立假设高约 10-20%（N32

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

T_res 与对象大小 s_i 的耦合效应：由于 ρ=-0.3，小对象（s_i < s_median）的 P_access 比独立假设高约 10-20%（N32），因此其 T_res 比独立假设短 10-20%；大对象（s_i > s_median）的 T_res 比独立假设长 10-20%。这导致 LRU 驱逐边界在大小维度上非对称，小对象驱逐更快，大对象驻留更久。

## Corrected Claim

T_res 与对象大小 s_i 的耦合效应：由于 ρ=-0.3，小对象（s_i < s_median）的 P_access 比独立假设高约 10-20%（N32），因此其 T_res 比独立假设短 10-20%；大对象（s_i > s_median）的 T_res 比独立假设长 10-20%。这导致 LRU 驱逐边界在大小维度上非对称，小对象驱逐更快，大对象驻留更久。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关系数意味着小对象访问概率高于独立假设，进而导致其平均响应时间（T_res）缩短，符合排队论与缓存机制的基本逻辑。
