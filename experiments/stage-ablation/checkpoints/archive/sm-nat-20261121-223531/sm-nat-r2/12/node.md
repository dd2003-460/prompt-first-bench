# N86: 针对本题具体参数（128GB缓存, 100k对象, Pareto α=1.1, β=0.9），由于总数据量 S_total ≈ 1.15GB < 128GB，缓

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

针对本题具体参数（128GB缓存, 100k对象, Pareto α=1.1, β=0.9），由于总数据量 S_total ≈ 1.15GB < 128GB，缓存覆盖率 k=1.0，因此LRU理论稳态字节命中率下界为 100%。任何声称低于100%的下界计算均隐含了错误的容量约束假设或对象大小分布截断误差。

## Corrected Claim

针对本题具体参数（128GB缓存, 100k对象, Pareto α=1.1, β=0.9），由于总数据量 S_total ≈ 1.15GB < 128GB，缓存覆盖率 k=1.0，因此LRU理论稳态字节命中率下界为 100%。任何声称低于100%的下界计算均隐含了错误的容量约束假设或对象大小分布截断误差。

## Evidence

逻辑推导成立，来源未直接覆盖（来源[1]讨论LLM KV Cache，与本题通用缓存命中率计算无关，但本题为纯数学/逻辑推导：总数据量小于缓存容量时，LRU稳态命中率必为100%）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2016843212178882587&rut=916b50c812ab872982a20f2b29ec3eec836928ce06491ae0bcb651e809817404', 'type': 'ddg', 'title': 'KV Cache 深度解析：从原理到工程优化的完整指南 - 知乎'}
