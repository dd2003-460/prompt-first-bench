# N93: Qwen3-27B 在 INT4 (AWQ) 量化下，MMLU 基准测试的准确率下降幅度：相比 BF16 基线 (约 85-88%)，INT4 版本准确率通常下

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N28

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，MMLU 基准测试的准确率下降幅度：相比 BF16 基线 (约 85-88%)，INT4 版本准确率通常下降 2-4 个百分点 (即降至 81-86%)，对应 Q_score 约为 0.92-0.95。此数据基于 LLM.int8() 及 AWQ 官方在 7B-30B 规模模型上的平均退化统计 [待核验]。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，MMLU 基准测试的准确率通常会有所下降，具体下降幅度取决于量化实现和模型版本，一般预期在几个百分点以内，Q_score 通常保持在较高水平（如 0.9 以上）。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU准确率基线85-88%、下降幅度2-4%、Q_score 0.92-0.95），且明确标注为[待核验]。这些具体数值属于经验事实，无法从第一性原理推导，且缺乏来源支持。此外，Qwen3-27B的具体量化退化数据可能因模型版本、量化实现细节（如AWQ的具体配置）而异，直接断言固定区间存在风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3 27B AWQ INT4 MMLU accuracy drop vs BF16
