# N35: 垂直风切变经验系数 k_shear 的量级估算方法（基于能量守恒或数值模拟拟合），用于将 ΔV_vertical 转换为 dE/dt

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

垂直风切变经验系数 k_shear 的量级估算方法（基于能量守恒或数值模拟拟合），用于将 ΔV_vertical 转换为 dE/dt

## Corrected Claim

垂直风切变对风能的影响通常通过风切变指数（如幂律指数）描述风速随高度的变化，进而影响风机扫掠面积内的平均风速和功率输出，而非直接通过一个名为 k_shear 的系数将 ΔV_vertical 线性转换为 dE/dt。

## Evidence

[质询]来源[1]讨论的是用于风速垂直分布外推的“风切变指数”（如幂律指数α），而非用于能量转换效率计算的“经验系数 k_shear”。两者物理意义和用途完全不同，存在概念混淆风险。 | 来源[1]主题相关（风切变）但内容不匹配（讨论风速剖面指数而非能量转换系数），无法提供直接支持；该系数属于特定工程经验参数，缺乏多源一致证据，故降级。

## Search Query

vertical wind shear empirical coefficient energy loss rate tropical cyclone decay model fitting

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/678297120&rut=a019b64c4707104f07d92fe7a5fc14968e22d63dc3e0416fe2b0cf073e672ada', 'type': 'ddg', 'title': 'Python计算风切变指数 - 知乎'}
