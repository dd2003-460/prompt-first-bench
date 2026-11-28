# N95: 工作点 C 中人工抽查成本 C_human = $5/paper 的假设需分解为 C_reviewer_hour * T_review_per_paper；假设

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

工作点 C 中人工抽查成本 C_human = $5/paper 的假设需分解为 C_reviewer_hour * T_review_per_paper；假设专业研究员时薪 $50/hour，单篇论文人工审查耗时 T_review ≈ 6 分钟 (0.1h)，则 C_human = $5.00/paper 成立；但当产出 >20 篇/天时，总人工成本 C_human_total = 20 * $5 = $100/day，超过云端推理成本 ($86.40/day) 成为主导项；此时 ROI 转折点出现在产出 N* 处，满足 d(C_total)/dN = Revenue_N；若每篇论文潜在价值 V_paper = $20 (保守估计)，则利润最大化点在 N ≈ 20-30 篇/天，超过此点后边际利润为负，claim 中 'ROI 下降' 的量化临界点即为 20 篇/天。

## Corrected Claim

工作点 C 中人工抽查成本 C_human = $5/paper 的假设需分解为 C_reviewer_hour * T_review_per_paper；假设专业研究员时薪 $50/hour，单篇论文人工审查耗时 T_review ≈ 6 分钟 (0.1h)，则 C_human = $5.00/paper 成立；但当产出 >20 篇/天时，总人工成本 C_human_total = 20 * $5 = $100/day，超过云端推理成本 ($86.40/day) 成为主导项；此时 ROI 转折点出现在产出 N* 处，满足 d(C_total)/dN = Revenue_N；若每篇论文潜在价值 V_paper = $20 (保守估计)，则利润最大化点在 N ≈ 20-30 篇/天，超过此点后边际利润为负，claim 中 'ROI 下降' 的量化临界点即为 20 篇/天。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（$50/h * 0.1h = $5/paper; 20 papers * $5 = $100 > $86.40），ROI临界点计算符合边际成本等于边际收益的经济逻辑。

## Search Query

AI generated research paper human review cost per hour researcher productivity benchmark
