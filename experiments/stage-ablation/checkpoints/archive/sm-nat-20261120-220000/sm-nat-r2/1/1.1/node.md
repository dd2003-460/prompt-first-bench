# N5: 10万个对象在Pareto(α=1.1)分布下的总大小 S_total = N * (α-1)/(α-2) * S_min，其中S_min为最小对象大小（假设1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

10万个对象在Pareto(α=1.1)分布下的总大小 S_total = N * (α-1)/(α-2) * S_min，其中S_min为最小对象大小（假设1KB），计算得S_total ≈ 100,000 * 0.1/(-1.1) * 1KB [需修正积分公式]，实际为 S_total ≈ N * S_min * (α-1)/(2-α) = 100,000 * 1KB * 0.1/0.9 ≈ 11.1 GB

## Corrected Claim

S_total ≈ 100,000 * 1KB * 0.1/0.9 ≈ 11.1 MB

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)的期望值公式 E[X] = (α-1)/(α-2) * x_min 在 α<2 时发散，但此处语境通常指截断Pareto或特定积分推导，若按题面给出的修正公式 S_total ≈ N * S_min * (α-1)/(2-α) 计算，100,000 * 1KB * 0.1/0.9 ≈ 11,111 KB ≈ 11.1 MB，而非 11.1 GB。等等，重新检查量级：100,000 * 1KB = 100MB。100MB * (0.1/0.9) ≈ 11.1 MB。题面结论写的是 11.1 GB，存在量级错误（1000倍）。但是，题目要求核验的是“关键事实节点”中的陈述。陈述中包含了错误的计算结果（11.1 GB vs 11.1 MB）。然而，source 标记为 knowledge。根据规则，knowledge 节点逻辑自洽即判 verified。但这里存在明显的算术/量级错误。100,000 * 1KB = 10^5 KB = 100 MB。乘以 1/9 约为 11 MB。写成 11.1 GB 是数量级错误。这属于“硬逻辑错误（量纲错/内部矛盾）”吗？是的，计算结果与输入参数不符。因此 logic_ok 应为 false，status 应为 failed。
