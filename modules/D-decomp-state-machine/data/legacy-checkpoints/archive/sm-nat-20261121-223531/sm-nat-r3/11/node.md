# N85: 在缓存容量受限（C < S_total）且热度服从Pareto(β=0.9)分布的假设下，LRU稳态字节命中率下界的通用推导公式为 H_LRU_lb = 1 -

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在缓存容量受限（C < S_total）且热度服从Pareto(β=0.9)分布的假设下，LRU稳态字节命中率下界的通用推导公式为 H_LRU_lb = 1 - (1 - k)^{1-β} * (E[S|Cold] / E[S])，其中k为缓存覆盖率（C/S_total），E[S|Cold]为未缓存对象的平均大小。若β=0.9，前10%对象覆盖约20.6%请求，若大小独立，字节命中率下界约为20.6%。

## Corrected Claim

在缓存容量受限且热度服从Pareto(β=0.9)分布的假设下，若对象大小独立于热度，前10%对象覆盖约20.6%请求，则LRU稳态字节命中率下界约为20.6%（基于请求覆盖率近似）。

## Evidence

[质询]公式推导存在逻辑漏洞：LRU的字节命中率下界通常由缓存覆盖的字节比例决定，而非简单的请求热度分布变换。若大小独立，前10%对象覆盖20.6%请求，其字节命中率应接近20.6%（假设大小分布均匀或独立），但公式中引入 E[S|Cold]/E[S] 项且指数为 1-β 缺乏标准缓存理论支持，且未明确说明该公式在何种特定假设下成立，容易误导为通用推导。 | 参考来源[1]为CSAPP Cachelab实验指南，[2]为KV Cache优化论文，均未提供LRU命中率与Pareto分布的具体数学推导公式，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/456858668&rut=3b866ededf3bbcd84f1ca3ec786d98ad236b3ecafdb81cc2b7092a42429692f4', 'type': 'ddg', 'title': 'CSAPP: Cachelab全注释+思路和建议 - 知乎'}
- {'url': 'https://arxiv.org/abs/2512.01953&rut=683e7ea7a407b2419e423889e15df2993f3c5ff6de833c6e79a008d10fd9f5da', 'type': 'ddg', 'title': '[2512.01953] KV Pareto: Systems-Level Optimization of KV Cache and ...'}
