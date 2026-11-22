# N5: LRU稳态字节命中率下界的理论定义采用Belady最优置换（Optimal）算法作为上界参考，而LRU特定下界定义为在已知未来请求序列下，LRU策略因缺乏预知导

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LRU稳态字节命中率下界的理论定义采用Belady最优置换（Optimal）算法作为上界参考，而LRU特定下界定义为在已知未来请求序列下，LRU策略因缺乏预知导致的命中率损失最小化值，其数值可通过模拟或解析近似得到。

## Corrected Claim

LRU稳态字节命中率下界的理论定义采用Belady最优置换（Optimal）算法作为上界参考，而LRU特定下界定义为在已知未来请求序列下，LRU策略因缺乏预知导致的命中率损失最小化值，其数值可通过模拟或解析近似得到。

## Evidence

先验知识/题面给定，逻辑校验通过
