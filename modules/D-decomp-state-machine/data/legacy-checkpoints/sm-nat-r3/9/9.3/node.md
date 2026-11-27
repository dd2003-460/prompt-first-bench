# N103: 有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，其中分子为因更新失效而丢失的字节加权访问概率，分母为缓存内总字节加权访问概率。

## Corrected Claim

有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，其中分子为因更新失效而丢失的字节加权访问概率，分母为缓存内总字节加权访问概率。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点将父节点的通用精确公式拆解为三个特定工作点（均匀、集中、混合）的近似或数值解，存在明显的参数取值冗余。此外，父节点强调的是“精确表达式”的结构定义，而子节点主要关注“数值估算”，缺失了对公式中核心变量（如失效概率 P_invalid(i) 与更新率/驻留时间关系）的通用推导或定义，导致对“精确表达式”本身的解析不完备。）
