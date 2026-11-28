# N18: 摩擦耗散项（Mechanism 1）的量化参数不确定性：边界层高度 $h$ 的典型范围（500-1000m）及其随下垫面粗糙度 $z_0$ 变化的函数关系 $h

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

摩擦耗散项（Mechanism 1）的量化参数不确定性：边界层高度 $h$ 的典型范围（500-1000m）及其随下垫面粗糙度 $z_0$ 变化的函数关系 $h \propto z_0^{1/3}$ 缺乏统一的解析解，需引用特定观测数据集（如 ASAS）进行校准。

## Corrected Claim

摩擦耗散项（Mechanism 1）的量化参数存在不确定性：边界层高度 h 的典型范围（约500-1000m）及其随下垫面粗糙度 z0 的变化关系（通常表现为正相关，如 h ∝ z0^α）缺乏普适的统一解析解，需结合特定观测数据集（如 ASAS）进行校准。

## Evidence

[质询]参考来源均为通用流体力学/应用数学中的边界层理论（涉及y+、匹配渐近法等），与大气边界层（Atmospheric Boundary Layer, ABL）中摩擦耗散、粗糙度z0及具体观测数据集（ASAS）的校准完全无关，属于领域错配；且具体数值范围（500-1000m）和幂律指数（1/3）属于经验事实，无法从第一性原理严格推导。 | 逻辑自洽（大气边界层高度通常在数百米至千米量级，且随粗糙度增加而增厚符合物理直觉），但参考来源[1][2]讨论的是流体动力学中的微观/工程边界层，与大气科学中的宏观边界层无关，无法提供外部支持；作为经验事实，缺乏直接来源支持故降级。

## Search Query

boundary layer height dependency on surface roughness tropical cyclone landfall

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/657541084&rut=6c2b14ee9a9b48e02c958dd1874fd7bd58b66e0c654da0d3ef8bfe199e50089b', 'type': 'ddg', 'title': '1. 边界层理论及y+的确定 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1936594788146221699&rut=367c477a5f02d4b9a9eabc0ec824b603002be9ce79098becf31f7d3ddd732976', 'type': 'ddg', 'title': '应用数学笔记04：边界层分析（2） - 知乎'}
