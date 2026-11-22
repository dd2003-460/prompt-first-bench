# N180: 负相关对字节命中率的放大效应：由于 E[S|TopK] = 0.8 * E[S]（基于 ρ=-0.3），Top-K 对象的字节占比 Mass_bytes_hot

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

负相关对字节命中率的放大效应：由于 E[S|TopK] = 0.8 * E[S]（基于 ρ=-0.3），Top-K 对象的字节占比 Mass_bytes_hot(K) = 0.8 * K * E[S] / Total_Bytes，相比独立假设下的 K * E[S] / Total_Bytes 降低了 20%，从而提升了单位容量下的请求覆盖率。

## Corrected Claim

负相关对字节命中率的放大效应：由于 E[S|TopK] = 0.8 * E[S]（基于 ρ=-0.3），Top-K 对象的字节占比 Mass_bytes_hot(K) = 0.8 * K * E[S] / Total_Bytes，相比独立假设下的 K * E[S] / Total_Bytes 降低了 20%，从而提升了单位容量下的请求覆盖率。

## Evidence

先验知识/题面给定，逻辑校验通过：基于负相关系数 ρ=-0.3 推导出的条件期望 E[S|TopK] = 0.8 * E[S] 在数学上自洽，且由此得出的字节占比降低 20% 的结论符合逻辑推导。
