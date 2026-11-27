# N144: 共享随机源：噪声抑制系数 β 与噪声方差 σ²_noise 的耦合关系：β = 1 / (1 + σ²_noise / σ²_signal)，其中 σ²_sig

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N36

## Claim

共享随机源：噪声抑制系数 β 与噪声方差 σ²_noise 的耦合关系：β = 1 / (1 + σ²_noise / σ²_signal)，其中 σ²_signal 为信号强度方差。高噪声环境下 β 减小，导致损失厌恶影响衰减。

## Corrected Claim

在特定的共享随机源噪声抑制模型中，噪声抑制系数 β 通常与信噪比负相关（例如 β ∝ 1/(1+SNR) 或类似形式），高噪声环境下 β 减小，导致损失厌恶影响衰减。具体公式形式需依据特定模型定义。

## Evidence

[质询]该公式 β = 1 / (1 + σ²_noise / σ²_signal) 是典型的信噪比（SNR）倒数形式的简化表达，但在行为经济学或特定的“共享随机源”噪声抑制模型中，β 的具体定义和耦合关系高度依赖于特定的理论框架或实验设定。参考来源 [1] 讨论的是扩散模型（Diffusion Model）中的噪声调度（Noise Schedule），属于生成式AI领域，与行为经济学中的“损失厌恶”（Loss Aversion）及“噪声抑制系数”无直接关联。因此，该陈述缺乏针对特定行为经济/决策理论场景的直接来源支持，且公式的具体形式可能因模型假设不同而异。 | 逻辑上，高噪声（σ²_noise 增大）导致分母增大，β 减小，符合“噪声抑制”或“信号衰减”的直觉；但参考来源 [1] 主题为扩散模型噪声控制，与行为经济学中的损失厌恶无关，无法提供直接支持，属于经验/模型特定事实，缺来源支持。

## Search Query

noise suppression coefficient loss aversion pricing model

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2502.04669v1&rut=32aa0af945cf8c6fd8f5747b0bfd2839259e178edb56372848da2c479d1cbdf1', 'type': 'ddg', 'title': 'A Comprehensive Review on Noise Control of Diffusion Model'}
