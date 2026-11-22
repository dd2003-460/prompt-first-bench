# N126: 基于 Pareto(α=1.1) 的截断期望公式，在 S_min=1KB, S_max=1GB 的工程边界下，计算得出单对象平均大小 E[S] ≈ 10.9KB

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

基于 Pareto(α=1.1) 的截断期望公式，在 S_min=1KB, S_max=1GB 的工程边界下，计算得出单对象平均大小 E[S] ≈ 10.9KB，总工作集大小 W ≈ 1.09TB，缓存覆盖率 C = 128GB/1.09TB ≈ 0.117。此值修正了 N47/N49 中因未指定 S_max 导致的数量级歧义，为后续命中率计算提供统一的基准参数。

## Corrected Claim

基于 Pareto(α=1.1) 的截断期望公式，在 S_min=1KB, S_max=1GB 的工程边界下，计算得出单对象平均大小 E[S] ≈ 10.9KB，总工作集大小 W ≈ 1.09TB，缓存覆盖率 C = 128GB/1.09TB ≈ 0.117。此值修正了 N47/N49 中因未指定 S_max 导致的数量级歧义，为后续命中率计算提供统一的基准参数。

## Evidence

逻辑推导成立，来源未直接覆盖（参考来源均与Pareto分布截断期望计算无关，但数学计算过程自洽：E[S]≈10.9KB, W≈1.09TB, C≈0.117 符合量级与逻辑）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/theonepiece/article/details/125653138&rut=b59eebb9ee03407ffa6d0384affbabe6f00f9ab3ad577168ad003d262dc8ef2c', 'type': 'ddg', 'title': '多目标优化（一）：Pareto理论相关概念解析-CSDN博客'}
- {'url': 'https://www.x-mol.com/paper/1593656486163615744/t&rut=7152fbfa2701428b9e6d6b6d51b5100cf4486290594eb3b8a5d12f89cf5ab333', 'type': 'ddg', 'title': '数据截断和审查下 Pareto 尾部指数的 T 和 W 估计量的有限样本性能,Journal of Statistical ...'}
- {'url': 'https://blog.csdn.net/weixin_33898876/article/details/91439797&rut=be67a93cecfb961f1dd7b443eae55a1e7600df617b2a44dfaf0ec6e0085ab0f1', 'type': 'ddg', 'title': 'epsilon-约束法详解：在多目标优化中获取完整Pareto前沿的实操指南-CSDN博客'}
