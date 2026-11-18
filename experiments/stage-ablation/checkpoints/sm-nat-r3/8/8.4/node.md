# N75: 可缓存对象数量 K 的精确值：K 不是 C/E[S]，而是满足 Σ_{i=1}^K s_i ≤ C 的最大整数 K。由于 s_i 随 i 递减（热门小），K 显

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

可缓存对象数量 K 的精确值：K 不是 C/E[S]，而是满足 Σ_{i=1}^K s_i ≤ C 的最大整数 K。由于 s_i 随 i 递减（热门小），K 显著大于 C/E[S]。需数值积分计算 K 使得累积大小 Σ_{i=1}^K E[s_i|rank_i] = 1.374e11 bytes。

## Corrected Claim

可缓存对象数量 K 的精确值：K 不是 C/E[S]，而是满足 Σ_{i=1}^K s_i ≤ C 的最大整数 K。由于 s_i 随 i 递减（热门小），K 显著大于 C/E[S]。需数值积分计算 K 使得累积大小 Σ_{i=1}^K E[s_i|rank_i] = 1.374e11 bytes。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点定义中的三个核心逻辑环节：1. 单点分布近似（微观基础），2. 累积分布/数值求解方法（宏观计算），3. 与独立假设的理论对比（效应量化）。三者逻辑递进，无重复且无矛盾，共同构成了确定K值的完整方法论。）

## Search Query

calculate number of objects in cache with Pareto size and popularity distribution

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Probability_distribution', 'type': None, 'title': 'wiki-full: Probability distribution'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://blog.csdn.net/weixin_45792450/article/details/144888860&rut=c7d185f285fa57500e8960315dd7ff6d48fb75762a40ac6e532c4ee18a5b5ace', 'type': 'ddg', 'title': '大型模型K V Cache机制详解 - CSDN博客'}
