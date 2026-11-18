# N74: 考虑大小-热度负相关 (ρ=-0.3) 后，对象 i 的大小 s_i 的条件期望 E[s_i | rank_i] 的解析近似：使用高斯 Copula 或 Cla

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

考虑大小-热度负相关 (ρ=-0.3) 后，对象 i 的大小 s_i 的条件期望 E[s_i | rank_i] 的解析近似：使用高斯 Copula 或 Clayton Copula 将排名 i 映射到标准化正态变量 u_i，再映射到 Pareto 大小分布。具体地，s_i ≈ x_min * (1 - F_S^{-1}(Φ(ρ * Φ^{-1}(F_H(i)))) )，其中 F_H 为热度 CDF，F_S 为大小 CDF。

## Corrected Claim

考虑大小-热度负相关 (ρ=-0.3) 后，对象 i 的大小 s_i 的条件期望 E[s_i | rank_i] 的解析近似：使用高斯 Copula 或 Clayton Copula 将排名 i 映射到标准化正态变量 u_i，再映射到 Pareto 大小分布。具体地，s_i ≈ x_min * (1 - F_S^{-1}(Φ(ρ * Φ^{-1}(F_H(i)))) )，其中 F_H 为热度 CDF，F_S 为大小 CDF。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 768)

## Search Query

conditional expectation size rank Gaussian Copula Pareto distribution

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Outline_of_finance', 'type': None, 'title': 'wiki-full: Outline of finance'}
- {'url': 'https://arxiv.org/list/stat.ME/recent', 'type': None, 'title': 'direct-browser: https://arxiv.org/list/stat.ME/recent'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/17207153253&rut=659f8ec587d3714335c0cd638963560e52696e189dc7900e4867c67412cf7fce', 'type': 'ddg', 'title': '条件期望（Conditional Expectation） - 知乎'}
