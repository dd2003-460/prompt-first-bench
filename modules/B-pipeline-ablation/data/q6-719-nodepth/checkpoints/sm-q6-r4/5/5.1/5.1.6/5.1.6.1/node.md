# N313: Preprovisioned_Capacity 的基准值计算：基于日均下载 2TB，假设峰值系数为 3（即峰值流量为 6TB/天），且峰值集中在 4 小时内，则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

Preprovisioned_Capacity 的基准值计算：基于日均下载 2TB，假设峰值系数为 3（即峰值流量为 6TB/天），且峰值集中在 4 小时内，则单 POP 预置带宽容量为 (6TB / 10 POP) / 4h ≈ 37.5 Gbps/POP，总预置容量为 375 Gbps。

## Corrected Claim

单 POP 预置带宽容量为 (6TB / 10 POP) / 4h ≈ 0.33 Gbps/POP，总预置容量为 3.3 Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过：6TB/10POP=0.6TB/POP，0.6TB/4h=0.15TB/h，0.15*8000Gbps/3600s≈333Gbps? 等等，重新计算：1TB=8000Gbits。0.6TB = 4800Gbits。4800Gbits / 4h = 1200Gbits/h = 1200/3600 Gbps ≈ 0.333 Gbps? 不对。单位换算：1 TB = 8000 Gb (Gigabits)。0.6 TB = 4800 Gb。时间 4 小时 = 14400 秒。带宽 = 4800 Gb / 14400 s = 1/3 Gbps ≈ 0.33 Gbps。这与陈述中的 37.5 Gbps 相差巨大。让我们再检查一遍陈述的计算逻辑。陈述说：(6TB / 10 POP) / 4h ≈ 37.5 Gbps/POP。6/10 = 0.6 TB。0.6 TB / 4 h = 0.15 TB/h。0.15 TB/h * 8000 Gb/TB = 1200 Gb/h。1200 Gb/h / 3600 s/h = 0.333 Gbps。陈述中的 37.5 Gbps 是如何得出的？如果 1 TB = 8000 Gb，那么 1 Gbps 在 1 小时内传输 1/3600 TB ≈ 0.000277 TB。37.5 Gbps * 4h * 3600s = 540,000 Gb = 67.5 TB。这远大于 0.6 TB。或者，陈述可能混淆了单位，比如把 TB 当作 Tbps？不，TB 是容量。如果峰值流量是 6TB/天，集中在 4 小时，平均速率是 1.5 TB/h。单 POP 是 0.15 TB/h。0.15 TB/h = 150 GB/h。150 GB/h = 150 * 8 Gb / 3600 s = 1200 Gb / 3600 s = 0.333 Gbps。陈述中的 37.5 Gbps 是错误的。37.5 Gbps 对应的是 37.5 * 4 * 3600 / 8000 = 67.5 TB/POP/4h，总共 675 TB/4h，这与 6TB/天 不符。或者，陈述中的 37.5 是怎么算出来的？6TB / 10 = 0.6TB。0.6TB / 4h = 0.15TB/h。如果错误地认为 1TB/h = 250 Gbps (1TB=8000Gb, 1h=3600s, 8000/3600≈2.22 Gbps? 不对。1Gbps=1Gb/s. 1TB=8000Gb. 1TB/s=8000Gbps. 1TB/h = 8000/3600 Gbps ≈ 2.22 Gbps. 0.15 * 2.22 ≈ 0.33 Gbps. 37.5 这个数字看起来像是 150/4? 或者 6/10 * 62.5? 62.5 Gbps 是 1TB/4h 的带宽吗？1TB/4h = 0.25TB/h = 0.25*8000/3600 Gbps ≈ 0.55 Gbps. 也不对。37.5 Gbps 通常对应 150 GB/s? 不。37.5 Gbps = 4.6875 GB/s. 4.6875 GB/s * 4h * 3600s = 67500 GB = 67.5 TB. 所以 37.5 Gbps 对应 67.5 TB/4h/POP. 10 POP 就是 675 TB/4h. 而题目说是 6TB/天. 6TB/天 远小于 675TB/4h. 因此，陈述中的数值计算存在严重错误。逻辑不自洽（数值量级错误）。
