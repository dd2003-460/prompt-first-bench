# N30: 请求热度分布上界 h_max 的量化约束：h_max 必须满足 h_max ≥ P_99(H)（第99百分位热度），在 Pareto(β=0.9) 下 P_99

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

请求热度分布上界 h_max 的量化约束：h_max 必须满足 h_max ≥ P_99(H)（第99百分位热度），在 Pareto(β=0.9) 下 P_99(H) = h_min * (0.99)^(-1/(β-1)) ≈ h_min * 1.01，因此 h_max 的选取对热度分布的截断影响较小，通常取总请求数 50M 除以对象总数 100k 得到的平均热度 500 次/对象/天 作为基准。

## Corrected Claim

在假设请求热度服从Pareto(β=0.9)分布且总请求数为50M、对象总数为100k的特定场景下，h_max通常取平均热度500次/对象/天作为基准，此时P_99(H)≈h_min*1.01，截断影响较小。

## Evidence

[质询]参考来源与事实主题完全无关（来源讨论大模型参数，事实讨论缓存/请求热度分布），且该陈述包含具体的经验性假设（如Pareto参数β=0.9、总请求数50M、对象数100k），这些并非第一性原理可推导的数学恒等式，而是特定场景下的工程设定或经验数据，缺乏来源支持。 | 逻辑上Pareto分布计算自洽，但参考来源[1]与大模型参数相关，与请求热度分布无关，无法提供外部支持；该事实属于特定场景下的经验性量化约束，非通用数学真理。

## Search Query

CDN request frequency distribution maximum frequency Zipf law

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/24484122371&rut=2a1be4f8d890da8da08666cc02022ec82caccfba443bbee57a18a759bc465649', 'type': 'ddg', 'title': '大模型参数如何设置（温度、Top-p、Top-k）+使用场景 - 知乎'}
