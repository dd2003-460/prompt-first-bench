# N292: 对象更新率 1%/天 导致的 LRU 有效命中率折损系数 D_update = 1 - (1 - e^(-λ_update * T_res_avg))，其中 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 导致的 LRU 有效命中率折损系数 D_update = 1 - (1 - e^(-λ_update * T_res_avg))，其中 T_res_avg 为对象平均驻留时间；在全量缓存且热度 Pareto(β=0.9) 下，热门对象 T_res_avg ≈ 0.1天，冷门对象 T_res_avg ≈ 100天，加权平均折损约为 0.5%，即命中率打 99.5 折。

## Corrected Claim

对象更新率会导致LRU缓存命中率下降，具体折损系数取决于对象驻留时间分布及更新频率，需根据实际业务数据建模计算，通用场景下无固定0.5%的折损值。

## Evidence

[质询]该陈述包含具体的经验性数值（如热门对象驻留时间0.1天、冷门100天、加权折损0.5%），这些参数高度依赖于具体的业务场景和数据分布，无法从第一性原理或通用缓存理论中严格推导得出，属于特定场景下的估算值。 | 参考来源[1]和[2]仅讨论了LRU/LFU的基本原理和缓存污染问题，未提供关于对象更新率导致命中率折损的具体公式或数值模型，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=7d58a4a126ac95d842e1a792f5b31de9d44ec9b6d2a091d938002417e9278387', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
- {'url': 'https://zhuanlan.zhihu.com/p/2025677845498708639&rut=e4f96d4a68d4df41c2ceedac544257f46a448779d6814ef1193317d0e1d4f6cd', 'type': 'ddg', 'title': '千万 Qps 架构，第 101 讲：「缓存淘汰策略：从lru到自适应」'}
