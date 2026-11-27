# N66: 算法惩罚机制的量化阈值：定义‘频繁变价’为 7 天内价格变动次数 N_change > 3 或累计降幅 ΔP_cum > 15%，触发后搜索权重 W 的衰减系数

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

算法惩罚机制的量化阈值：定义‘频繁变价’为 7 天内价格变动次数 N_change > 3 或累计降幅 ΔP_cum > 15%，触发后搜索权重 W 的衰减系数 λ_decay 通常为 0.8 (即 W' = 0.8 * W)，具体阈值需通过 A/B 测试数据或平台公开规则核实。

## Corrected Claim

算法惩罚机制通常会对频繁变价行为进行权重衰减，但具体的量化阈值（如时间窗口、变动次数、降幅比例及衰减系数）因平台而异且多为非公开黑盒参数，需通过特定平台的A/B测试数据或逆向工程核实，不存在通用的固定标准值。

## Evidence

[质询]该陈述包含具体的经验性参数（如7天、N>3、15%、λ=0.8），这些并非第一性原理可推导的数学或物理常数，而是特定平台（如亚马逊、淘宝等）的运营策略或黑盒算法参数，不同平台甚至同一平台不同时期均可能不同，且通常不公开具体数值，属于典型的经验事实。 | 参考来源[1]讨论的是量化交易中的Alpha指标，与电商搜索算法惩罚机制完全无关，无可用外部证据支持；该事实为经验事实，逻辑自洽但缺乏来源直接支持，故降级。

## Search Query

e-commerce platform algorithm penalty frequent price change weight decay

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2022270090142336222&rut=c15475ea2d121af29e3da36d3b3d29492e4eaae17ad12f75927a35291dd16a08', 'type': 'ddg', 'title': '量化交易7大核心概念深度解析：指标、阈值与实战案例 - 知乎'}
