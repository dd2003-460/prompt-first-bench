# N347: MMLU-Pro 的大类定义（n_subjects）实际为 14 个主要学科类别（而非假设的 16 个），因此标准误公式应修正为 SE = σ_subject 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

MMLU-Pro 的大类定义（n_subjects）实际为 14 个主要学科类别（而非假设的 16 个），因此标准误公式应修正为 SE = σ_subject / √14，若 σ_subject=5.0%，则 SE ≈ 1.34%，需确认 MMLU-Pro 官方定义的学科分类数量以修正统计推断精度。

## Corrected Claim

MMLU-Pro 沿用了 MMLU 的 57 个学科类别结构。若需计算整体准确率的标准误，应使用总样本量 N（约 12,000+），公式为 SE = σ / √N，而非基于类别数的公式。

## Evidence

[质询]MMLU-Pro 官方论文中定义的学科类别数量并非 14 个，而是 14 个主要领域（domains）下的 14 个子集（subsets）或者通常引用的 14 个类别（如 STEM, Social Sciences, Humanities, Other 等大类下的细分），但更关键的错误在于：MMLU-Pro 实际上沿用了 MMLU 的 57 个学科类别（subjects），只是将每个学科的问题数量增加并提高了难度。即使假设其按 14 个大类聚合，标准误的计算也依赖于样本量 n 而非仅仅类别数 k，除非题目隐含了“每类取均值”的特定统计模型，否则 SE = σ/√k 的公式本身在统计学上对于整体准确率估计是不成立的（应为 σ/√n）。此外，来源中未提及 14 这个数字，MMLU 原版是 57 个学科，MMLU-Pro 也是基于这 57 个学科构建的。 | 来源 [2] 指出 MMLU-Pro 扩展了选项并增加了推理题，但未改变基础学科结构；MMLU 系列通常包含 57 个学科类别，而非 14 个。且标准误公式 SE=σ/√k 仅在计算“类别均值的方差”时适用，而非整体准确率的标准误（后者应为 σ/√n）。

## Search Query

MMLU-Pro number of subjects categories 14 or 16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/702019999&rut=68fd6a511623f6e35c90dcf829b4a015b6cad3ff88813d5d0f2121c1fb98d6e4', 'type': 'ddg', 'title': 'Aigc每周精选--大模型评测之mmlu-pro与mmlu - 知乎'}
- {'url': 'https://arxiv.org/abs/2406.01574&rut=f435db36adece2baea5278dcfabe577493ca33358f4f7c52b486b0f4e6e5f946', 'type': 'ddg', 'title': 'MMLU-Pro: A More Robust and Challenging Multi-Task Language ...'}
