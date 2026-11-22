# N17: 理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i)；在r_i ∝ i^{-0.9}和s_i ∝ i^{-1.1}且负相关的情况下，分子由头部对象主导，H_opt通常接近1.0（>95%），因为β+α=2.0>1导致字节流量高度集中在头部少数对象上。

## Corrected Claim

理想缓存策略（Optimal/Mark）的字节命中率基准值 H_opt = (Σ_{i=1}^k r_i s_i) / (Σ_{i=1}^{N} r_i s_i)；在r_i ∝ i^{-0.9}和s_i ∝ i^{-1.1}且负相关的情况下，分子由头部对象主导，H_opt通常接近1.0，因为β+α=2.0>1导致字节流量高度集中在头部少数对象上。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式的分子和分母，结构上正且互补。虽然数值推导中隐含了k与N的具体量级假设（如N=100000），但作为对父节点中“接近1.0”结论的量化验证，逻辑自洽且无实质性重复。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/661746274&rut=680c3fcb1ceca3cf51b00c88449cd16e88623a39f6fb52ea7a36654011074be1', 'type': 'ddg', 'title': 'P-OPT（Practical Optimal Cache Replacement）针对于图形处理的Cache替换策略阅读笔记'}
- {'url': 'https://zhuanlan.zhihu.com/p/2045143515269706934&rut=a7b063e824fe6538e31fae3785d9cf453eb8cee8372ad2aa43a51f4a1b4204e5', 'type': 'ddg', 'title': '一文说清大模型缓存命中机制，同样的token，命中和未命中价格相差120倍!不懂KV Cache的人，每个月都在白烧钱'}
