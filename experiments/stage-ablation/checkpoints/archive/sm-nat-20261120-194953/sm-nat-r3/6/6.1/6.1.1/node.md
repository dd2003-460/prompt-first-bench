# N147: 突发窗口内驱逐的对象数 $K_{evict}$ 由突发请求量 $R_{burst}$ 与冷对象平均大小 $E[S_{cold}]$ 决定：$K_{evict} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

突发窗口内驱逐的对象数 $K_{evict}$ 由突发请求量 $R_{burst}$ 与冷对象平均大小 $E[S_{cold}]$ 决定：$K_{evict} = \min(K_{cap}, \lceil R_{burst} \cdot E[S_{cold}] / E[S_{hot}] \rceil)$。假设突发请求集中在后 90% 对象，$E[S_{cold}] \approx 5$ KB（Pareto 尾部），$E[S_{hot}] \approx 10$ KB（头部略大但受负相关限制），若突发请求量为总日请求的 1% ($5 \times 10^5$ 次)，则 $K_{evict} \approx 5 \times 10^5 \times 5 / 10 = 2.5 \times 10^5$，但受 $K_{cap}$ 限制，实际驱逐数取决于缓存剩余空间，在全量驻留下需驱逐等量热点以容纳冷对象。

## Corrected Claim

突发窗口内驱逐的对象数 $K_{evict}$ 由突发请求量 $R_{burst}$ 与冷对象平均大小 $E[S_{cold}]$ 决定：$K_{evict} = \min(K_{cap}, \lceil R_{burst} \cdot E[S_{cold}] / E[S_{hot}] \rceil)$。假设突发请求集中在后 90% 对象，$E[S_{cold}] \approx 5$ KB（Pareto 尾部），$E[S_{hot}] \approx 10$ KB（头部略大但受负相关限制），若突发请求量为总日请求的 1% ($5 \times 10^5$ 次)，则 $K_{evict} \approx 5 \times 10^5 \times 5 / 10 = 2.5 \times 10^5$，但受 $K_{cap}$ 限制，实际驱逐数取决于缓存剩余空间，在全量驻留下需驱逐等量热点以容纳冷对象。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合缓存替换的基本容量约束逻辑，数值量级（5e5 * 0.5 = 2.5e5）计算正确，且明确指出了受 K_cap 限制的实际物理意义。
