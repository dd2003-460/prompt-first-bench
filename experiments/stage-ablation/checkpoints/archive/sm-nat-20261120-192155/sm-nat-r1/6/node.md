# N17: 理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i)；在r_i ∝ i^{-0.9}和s_i ∝ i^{-1.1}且负相关的情况下，分子由头部对象主导，H_opt通常接近1.0（>95%），因为β+α=2.0>1导致字节流量高度集中在头部少数对象上。

## Corrected Claim

理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i)；在r_i ∝ i^{-0.9}和s_i ∝ i^{-1.1}且负相关的情况下，分子由头部对象主导，H_opt通常接近1.0，因为β+α=2.0>1导致字节流量高度集中在头部少数对象上。

## Evidence

[质询]该陈述包含具体的经验性数值结论（H_opt > 95%），这属于经验事实而非纯数学推导。虽然逻辑上β+α=2.0确实导致流量高度集中，但具体是否>95%取决于k/N的具体比例及分布截断情况，仅凭指数参数无法严格推出该具体阈值，且参考来源均未提供此具体数值支持。 | 逻辑推导自洽（Zipf分布下高指数导致头部集中），但参考来源[1]讨论P-OPT算法实现，[2]讨论LLM KV Cache，均与该特定缓存策略的字节命中率数值基准无关，无外部证据支持具体数值>95%。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/661746274&rut=680c3fcb1ceca3cf51b00c88449cd16e88623a39f6fb52ea7a36654011074be1', 'type': 'ddg', 'title': 'P-OPT（Practical Optimal Cache Replacement）针对于图形处理的Cache替换策略阅读笔记'}
- {'url': 'https://zhuanlan.zhihu.com/p/2045143515269706934&rut=a7b063e824fe6538e31fae3785d9cf453eb8cee8372ad2aa43a51f4a1b4204e5', 'type': 'ddg', 'title': '一文说清大模型缓存命中机制，同样的token，命中和未命中价格相差120倍!不懂KV Cache的人，每个月都在白烧钱'}
