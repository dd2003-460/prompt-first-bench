# N227: Jarque-Bera 检验统计量 JB 在拉普拉斯分布下的理论期望值推导：对于服从拉普拉斯分布的数据，其偏度 S=0，峰度 K=6。代入公式 JB = n *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Jarque-Bera 检验统计量 JB 在拉普拉斯分布下的理论期望值推导：对于服从拉普拉斯分布的数据，其偏度 S=0，峰度 K=6。代入公式 JB = n * [S²/6 + (K-3)²/24]，得 JB = n * [0 + (6-3)²/24] = n * 9/24 = 0.375n。

## Corrected Claim

Jarque-Bera 检验统计量 JB 在拉普拉斯分布下的理论期望值推导：对于服从拉普拉斯分布的数据，其偏度 S=0，峰度 K=6。代入公式 JB = n * [S²/6 + (K-3)²/24]，得 JB = n * [0 + (6-3)²/24] = n * 9/24 = 0.375n。

## Evidence

先验知识/题面给定，逻辑校验通过：拉普拉斯分布对称故偏度S=0，超额峰度为3（总峰度K=6），代入Jarque-Bera公式 JB = n(S²/6 + (K-3)²/24) 计算得 0.375n，推导无误。
