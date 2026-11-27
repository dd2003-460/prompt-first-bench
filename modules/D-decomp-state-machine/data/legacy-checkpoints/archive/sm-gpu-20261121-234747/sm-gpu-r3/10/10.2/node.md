# N155: FP8 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU 需引用 Qwen 官方技术报告或 AWQ/GPTQ 社区评测中针对 27B 规模模型

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

FP8 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU 需引用 Qwen 官方技术报告或 AWQ/GPTQ 社区评测中针对 27B 规模模型的具体数据，若仅有 7B/14B 数据需通过线性插值估算并标注外推风险，预期范围 0.1%-0.5% [待核验]

## Corrected Claim

FP8 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU 需引用 Qwen 官方技术报告或 AWQ/GPTQ 社区评测中针对 27B 规模模型的具体数据；若仅有 7B/14B 数据，线性插值估算存在外推风险，具体下降幅度需以实测为准，不宜直接断定为 0.1%-0.5%。

## Evidence

[质询]该陈述包含具体的经验数值范围（0.1%-0.5%）和特定的模型规模（Qwen3-27B），属于硬件/模型性能相关的经验事实，无法从第一性原理推导。且当前检索无可用来源，无法验证该具体数值范围的准确性，存在将小模型数据线性外推到大模型导致误差被低估的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围及外推方法的合理性）

## Search Query

Qwen3-27B FP8 MMLU accuracy drop AWQ GPTQ evaluation
