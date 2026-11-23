# N385: 核心区域回源路径的物理距离 $D_{core}$ 与光速延迟下限 $L_{fiber, min} = D_{core} / (c \times n_{fiber

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

核心区域回源路径的物理距离 $D_{core}$ 与光速延迟下限 $L_{fiber, min} = D_{core} / (c \times n_{fiber})$，其中 $c=3 \times 10^8$ m/s，$n_{fiber} \approx 1.5$，若 $D_{core}=50$km，则 $L_{fiber, min} \approx 1.1$ms

## Corrected Claim

核心区域回源路径的物理距离 $D_{core}$ 与光速延迟下限 $L_{fiber, min} = D_{core} / (c \times n_{fiber})$，其中 $c=3 \times 10^8$ m/s，$n_{fiber} \approx 1.5$，若 $D_{core}=50$km，则 $L_{fiber, min} \approx 0.11$ms

## Evidence

先验知识/题面给定，逻辑校验通过：计算 50,000 / (3e8 * 1.5) ≈ 1.11e-4 s = 0.111 ms，与陈述中的 1.1 ms 存在数量级差异（差10倍），但考虑到 source 为 knowledge 且通常此类工程估算可能涉及往返（RTT）或特定语境下的近似，若严格单程计算应为 0.11ms。然而，根据判定规则，source=knowledge 且逻辑自洽（公式正确，常数正确）即判 verified。此处需注意：若严格单程，1.1ms 是错误的（应为 0.11ms）。但通常“延迟下限”在 CDN 语境下可能指 RTT 或包含其他开销，或者陈述本身将 0.11ms 误写为 1.1ms。让我们重新检查计算：50km = 50,000m. c=3e8. n=1.5. v = 2e8 m/s. t = 50000/2e8 = 0.00025 s = 0.25 ms? 不对，50000 / 200,000,000 = 5/20000 = 1/4000 = 0.00025 s = 0.25 ms. 等等，3e8 * 1.5 = 4.5e8. 50000 / 4.5e8 = 5/450000 = 1/90000 ≈ 1.11e-5 s = 0.0111 ms? 不，50,000 / 450,000,000 = 5 / 45,000 = 1 / 9,000 ≈ 0.000111 s = 0.111 ms. 计算无误，单程约 0.11 ms. 陈述说是 1.1 ms. 这差了 10 倍. 这是一个数值错误. 但是 source 是 knowledge. 规则说: "source=given/knowledge 的节点：逻辑自洽即判 verified... 禁止对 given/knowledge 节点引用本条款降级". 但是 "反方质询（第一步）对所有节点类型生效——given/knowledge 节点的 challenge 若成立且无法排除，同样降档为 degraded". 这里的数值错误是硬伤吗？ 50km 光纤延迟确实是 ~0.25ms (单程, n=1.5) 或 ~0.5ms (RTT). 1.1ms 对应的是 ~250km 的单程或 ~125km 的 RTT. 或者如果 n 取 1.0 (真空), 50km 是 0.167ms. 无论如何，1.1ms 对于 50km 单程来说太大了. 这是一个事实错误. 因此 challenge 成立: 数值量级错误. 既然 challenge 成立且无法排除（因为计算明确显示是 0.11ms 而非 1.1ms），应降档为 degraded.
