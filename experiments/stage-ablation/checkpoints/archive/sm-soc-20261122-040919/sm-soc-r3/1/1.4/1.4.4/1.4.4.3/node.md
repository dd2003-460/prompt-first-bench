# N174: 均衡失效的噪声阈值：当 σ²_noise 增大至使 E[U_buyer]/√Var[U_buyer] < 0 时，均衡失效；具体阈值需通过模拟 σ²_noise

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

均衡失效的噪声阈值：当 σ²_noise 增大至使 E[U_buyer]/√Var[U_buyer] < 0 时，均衡失效；具体阈值需通过模拟 σ²_noise 从 0.0025 逐步增加，找到 P(U_buyer > 0) = 0.5 的临界点（[待核验]）

## Corrected Claim

均衡失效的噪声阈值取决于具体模型参数；通常需通过模拟确定当噪声方差增大至使买方效用期望值低于其标准差（或概率分布中位数低于0）时的临界点，具体数值（如0.0025）需依据特定模型设定验证。

## Evidence

[质询]该陈述包含具体的数值阈值（σ²_noise 从 0.0025 开始）和特定的均衡失效判据（E[U]/√Var < 0 对应 P(U>0)=0.5），这属于特定模型下的经验事实或模拟结果，无法从第一性原理直接推出，且参考来源完全无关，缺乏外部证据支持其具体数值和逻辑等价性。 | 参考来源[1][2]讨论的是电路噪声和带宽，与博弈论/经济学中的均衡失效及买方效用噪声阈值无关，属于无关来源；该事实为特定模型下的经验/模拟结论，逻辑上自洽（若U近似正态，均值/标准差<0确实意味着均值<0，即P(U>0)<0.5，但具体阈值0.0025及模拟过程无法验证），故降级。

## Search Query

equilibrium stability noise threshold Monte Carlo simulation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/711471381&rut=8fcd5e57d1bfe3738c0572c34eb8ebd665003c6196f700fc3d3b0d4f89becbb7', 'type': 'ddg', 'title': '高等模拟设计——噪声 Noise - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/30138186618&rut=21de377f509d037f8ec06f0f35ec5ab797661bf6e5a9a6484cdddd7a4d30079e', 'type': 'ddg', 'title': '等效噪声带宽（Equivalent Noise Bandwidth，ENBW） - 知乎'}
