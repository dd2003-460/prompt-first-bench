# N23: 对于Pareto(β=0.9)热度分布，前k%对象占据的请求比例 P_req(k) = 1 - k^{β-1} = 1 - k^{-0.1}。例如，前1%对象占

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于Pareto(β=0.9)热度分布，前k%对象占据的请求比例 P_req(k) = 1 - k^{β-1} = 1 - k^{-0.1}。例如，前1%对象占据 1 - 0.01^{-0.1} ≈ 1 - 0.794 = 20.6% 的请求；前10%对象占据 1 - 0.1^{-0.1} ≈ 1 - 0.794 = 20.6% (注：Pareto尾部极长，需精确计算：0.1^-0.1 ≈ 0.7943, 0.01^-0.1 ≈ 0.6309, 故前10%占 1-0.6309=36.9%, 前1%占 1-0.7943=20.6% 是错误的，应为 1 - (0.01)^-0.1? 不，CDF F(h)=1-(h_min/h)^(β-1). 若h_min=1, F(100)=1-(1/100)^-0.1=1-100^0.1≈1-1.58<0 错误。正确公式：若β=0.9<1，分布无均值，CDF形式为 1-(x/x_min)^(1-β) 当 x>=x_min. 即 F(x) = 1 - (x/x_min)^(-0.1). 前1%对象 (rank 1 to 1000) 的热度阈值 h_1000 满足 F(h)=0.99 => 0.01 = (h/h_min)^-0.1 => h/h_min = 0.01^-10 = 10^8. 这意味着热度分布极度长尾，前1%对象的热度极高，但请求量占比计算需用积分。更简单的经验法则：在Zipf-like分布中，前1%通常占约20-30%流量。此处需引用具体数值模拟结果或近似公式。

## Corrected Claim

对于 Pareto(β=0.9) 分布，若指代 Zipf 定律下的请求分布，前 k% 对象占据的请求比例通常通过累积分布函数或积分计算。简单的幂律公式 P(k) = 1 - k^{1-β} 仅在特定归一化条件下近似成立，且需确保 k 在 (0,1] 区间内指数为正。例如，若使用 Zipf 近似，前 1% 对象占据的请求比例约为 1 - (0.01)^{1-0.9} = 1 - 0.01^{0.1} ≈ 1 - 0.794 = 20.6%（注意此处指数应为 1-β=0.1 而非 β-1=-0.1，且底数为 k 而非 1/k 的倒数关系需明确）。原陈述公式符号错误导致计算失效。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=d1f36e1dcdd328dca36f26158320367e6d6eac92aaea3431d05154d1bb1df302', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
- {'url': 'https://zhuanlan.zhihu.com/p/27173875583&rut=813a7dd5764aafafe6763a06f3f8a3572d479be046e39d53beeec4e456801689', 'type': 'ddg', 'title': '帕累托分布 - 知乎 - 知乎专栏'}
