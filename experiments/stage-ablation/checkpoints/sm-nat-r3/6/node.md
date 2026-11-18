# N21: 在 Zipf-Pareto 混合模型下，缓存前 k 个最热门对象（按请求频率排序）的字节命中率下界 H_byte_lower 可通过累积分布函数计算：H_byt

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 Zipf-Pareto 混合模型下，缓存前 k 个最热门对象（按请求频率排序）的字节命中率下界 H_byte_lower 可通过累积分布函数计算：H_byte_lower = (Σ_{i=1}^{k} f_i * s_i) / (Σ_{i=1}^{N} f_i * s_i)，其中 f_i 服从 Pareto(β)，s_i 服从 Pareto(α)，且 k 由总容量 C 和加权平均大小决定。对于 β=0.9, α=1.1, N=100,000, C=128GB，前 1% 对象（k=1000）通常覆盖约 50-60% 的字节流量。

## Corrected Claim

在 Zipf-Pareto 混合模型下，缓存前 k 个最热门对象的字节命中率下界 H_byte_lower 可通过累积分布函数计算：H_byte_lower = (Σ_{i=1}^{k} f_i * s_i) / (Σ_{i=1}^{N} f_i * s_i)。对于 β=0.9, α=1.1, N=100,000, C=128GB 的参数设置，前 1% 对象（k=1000）通常覆盖较高比例的字节流量（具体数值需通过数值积分或模拟确定，典型值可能在 50-70% 区间，但缺乏特定来源支持确切范围）。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点公式中分子（Numerator）的近似计算，完全缺失了分母（Denominator）的计算、k值的确定逻辑以及最终数值结果（50-60%）的推导验证，导致内容严重不完备。）

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://baike.baidu.com/item/%E5%9C%A8/4625648', 'type': 'bing', 'title': '在（汉语汉字）_百度百科'}
