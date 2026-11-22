# N39: 投影1（高曝光池进入概率）：商品进入高曝光池的概率 P_high_pool = 1 / (1 + exp(-γ * (P_ask/P_market - 1.2)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9

## Claim

投影1（高曝光池进入概率）：商品进入高曝光池的概率 P_high_pool = 1 / (1 + exp(-γ * (P_ask/P_market - 1.2)))，其中 γ 为平台算法的敏感度参数，需估计 γ 使得 P_high_pool 在 δ=15% 时约为 0.6，以匹配观察到的短周期现象。

## Corrected Claim

投影1（高曝光池进入概率）：商品进入高曝光池的概率 P_high_pool 可通过逻辑斯蒂函数建模，形式为 1 / (1 + exp(-γ * (P_ask/P_market - threshold)))，其中 γ 和 threshold 为需根据平台数据估计的参数。

## Evidence

[质询]该陈述包含具体的经验参数设定（如阈值1.2、目标概率0.6、敏感度γ的校准逻辑），属于平台算法内部机制的经验事实，无法从第一性原理推导，且参考来源完全无关，缺乏外部证据支持其具体数值和逻辑的准确性。 | 参考来源[1]讨论的是计算机视觉中的池化操作，与电商曝光概率模型完全无关，属于无关来源；该事实为经验性模型假设，逻辑自洽但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

marketplace ranking algorithm sigmoid sensitivity price premium exposure pool

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/14649563019&rut=5a662eec609ddd9a13baeb6d33b8217911c87fa74c8646d46ad8073013fbed19', 'type': 'ddg', 'title': '最大池化Maxpooling和平均池化Avgpooling - 知乎 - 知乎专栏'}
