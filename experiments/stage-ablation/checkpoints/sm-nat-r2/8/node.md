# N23: LRU 稳态字节命中率下界的数学推导路径：1) 定义对象 i 的访问间隔分布 D_i ~ Exp(λ_i)，其中 λ_i 由热度决定；2) LRU 命中条件为 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界的数学推导路径：1) 定义对象 i 的访问间隔分布 D_i ~ Exp(λ_i)，其中 λ_i 由热度决定；2) LRU 命中条件为 D_i < W_i，W_i 为工作集时间窗口；3) 对于 Pareto 热度分布，P(hit_i) = 1 - e^{-λ_i * W_i}；4) 字节命中率 H_byte = Σ (P(hit_i) * s_i * λ_i) / (Σ s_i * λ_i)。在 α=1.1, β=0.9 下，由于长尾效应，H_byte 主要由头部 5-10% 对象决定，下界约为 0.65-0.75。

## Corrected Claim

LRU 稳态字节命中率下界的数学推导路径：1) 定义对象 i 的访问间隔分布 D_i ~ Exp(λ_i)；2) LRU 命中条件为 D_i < W_i；3) P(hit_i) = 1 - e^{-λ_i * W_i}；4) H_byte = Σ (P(hit_i) * s_i * λ_i) / (Σ s_i * λ_i)。在典型长尾热度分布（如 α=1.1, β=0.9）下，H_byte 主要由头部对象决定，具体数值需通过模拟或特定数据集验证，通常处于较高区间。

## Evidence

[质询]数值断言缺乏来源支持：虽然数学推导框架（指数分布间隔、LRU命中条件、字节加权公式）在逻辑上是自洽且标准的，但具体参数（α=1.1, β=0.9）下的下界数值（0.65-0.75）属于经验性/模拟性结论，无法仅从第一性原理严格推出，且参考来源中未包含该具体数值。 | 来源[2]提供了LRU命中率建模的理论背景，间接支持了推导框架的合理性，但未提供具体参数下的数值结果；该数值为经验事实，逻辑自洽但缺直接来源支持。

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/98144430&rut=2586e318c0957df08b32186d301198fd019475f4f712d8b46bb64f08fd098436', 'type': 'ddg', 'title': 'Lru缓存命中率建模 - 知乎专栏'}
- {'url': 'https://zhuanlan.zhihu.com/p/161269766&rut=f8b3c2f4662a3b96e82928ec32c760bf519173056b562900244e4318262aa288', 'type': 'ddg', 'title': 'Lru原理与算法实现 - 知乎专栏'}
