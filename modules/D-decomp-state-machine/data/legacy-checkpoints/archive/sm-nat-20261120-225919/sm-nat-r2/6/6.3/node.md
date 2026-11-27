# N86: k_max 的正确定义并非简单的 C/C_avg，而是满足 Σ_{i=1}^{k} S_i ≤ C 的最大 k。由于大小与热度负相关（ρ=-0.3），最热的 k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

k_max 的正确定义并非简单的 C/C_avg，而是满足 Σ_{i=1}^{k} S_i ≤ C 的最大 k。由于大小与热度负相关（ρ=-0.3），最热的 k 个对象倾向于较小，因此 k_max 应基于“热度排序后的大小累积和”而非“随机样本的平均大小”。

## Corrected Claim

k_max 的正确定义并非简单的 C/C_avg，而是满足 Σ_{i=1}^{k} S_i ≤ C 的最大 k。由于大小与热度负相关（ρ=-0.3），最热的 k 个对象倾向于较小，因此 k_max 应基于“热度排序后的大小累积和”而非“随机样本的平均大小”。

## Evidence

先验知识/题面给定，逻辑校验通过：k_max 定义为满足累积大小约束的最大对象数，且基于热度排序而非随机平均，符合缓存替换策略（如 LFU/LRU 变体）的基本逻辑与物理直觉。
