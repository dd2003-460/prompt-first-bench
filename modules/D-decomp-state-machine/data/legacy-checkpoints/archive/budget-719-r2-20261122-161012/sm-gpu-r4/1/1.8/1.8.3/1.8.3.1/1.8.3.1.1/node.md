# N464: Qwen3-27B 在 BF16 精度下 MMLU 总得分为 82.5%（基于 Qwen3 技术报告 Table 1 中 27B 模型的 MMLU 成绩，若官方

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N192

## Claim

Qwen3-27B 在 BF16 精度下 MMLU 总得分为 82.5%（基于 Qwen3 技术报告 Table 1 中 27B 模型的 MMLU 成绩，若官方未单独列出 27B，则引用 Qwen2.5-32B 的 84.1% 或 Llama-3-70B 的 86.0% 进行保守插值 [待核验]）。

## Corrected Claim

Qwen3 系列中不存在 27B 参数规模的官方模型；若指代相近规模，Qwen3-32B 在 BF16 精度下的 MMLU 得分需参考官方技术报告具体数值（通常高于 82.5%），原陈述中的 82.5% 及 27B 规格均缺乏可靠来源支持。

## Evidence

[质询]Qwen3 系列目前官方并未发布 27B 参数规模的模型（常见规格为 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B 等），且 MMLU 82.5% 这一具体数值缺乏官方技术报告直接支持，属于经验事实且存在模型规格混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 Qwen3 无 27B 官方规格，数值无法从第一性原理推出）

## Search Query

Qwen3-27B MMLU score BF16 official report
