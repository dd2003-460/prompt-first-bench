# N116: 自建 POP 两级缓存命中率 H_self_two_level = H_L1_self + (1 - H_L1_self) * H_L2_self，其中 H_L

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

自建 POP 两级缓存命中率 H_self_two_level = H_L1_self + (1 - H_L1_self) * H_L2_self，其中 H_L1_self 为 POP-L1 命中率，H_L2_self 为 POP-L2 命中率；POP-L1 容量 C_pop_L1 通常为 100GB-500GB，POP-L2 容量 C_pop_L2 通常为 1TB-10TB，具体配置取决于硬件成本预算。

## Corrected Claim

自建 POP 两级缓存命中率 H_self_two_level = H_L1_self + (1 - H_L1_self) * H_L2_self，其中 H_L1_self 为 POP-L1 命中率，H_L2_self 为 POP-L2 命中率；POP-L1 容量 C_pop_L1 通常为 100GB-500GB，POP-L2 容量 C_pop_L2 通常为 1TB-10TB，具体配置取决于硬件成本预算。

## Evidence

先验知识/题面给定，逻辑校验通过：两级缓存命中率公式符合概率论全概率公式（第一性原理）；容量范围（L1 100GB-500GB, L2 1TB-10TB）符合边缘节点硬件成本与存储介质（SSD/HDD）的工程常识，量级合理。
