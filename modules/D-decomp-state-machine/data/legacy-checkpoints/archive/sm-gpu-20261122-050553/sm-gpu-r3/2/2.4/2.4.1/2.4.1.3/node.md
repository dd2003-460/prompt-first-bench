# N190: W4 量化在 Qwen3-27B 中的质量损失机制：需量化关键权重（Salient Weights）的保留比例（通常 1%-5% 保留为 FP16/INT8），

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

W4 量化在 Qwen3-27B 中的质量损失机制：需量化关键权重（Salient Weights）的保留比例（通常 1%-5% 保留为 FP16/INT8），该比例与 MMLU 下降幅度呈负相关，需检索 Qwen 官方或社区调优脚本中的默认保留比例，以提供可计算的修正项。

## Corrected Claim

W4 量化在 Qwen3-27B 中通常采用关键权重保留策略（如将部分敏感权重保留为高精度），保留比例的具体数值因量化算法（如 GPTQ/AWQ）及调优脚本而异，一般认为较高的保留比例有助于降低 MMLU 等基准测试的性能下降幅度，但需查阅具体实现代码以获取确切默认值。

## Evidence

[质询]该陈述包含具体的经验参数（1%-5% 保留比例）和特定的相关性结论（与 MMLU 下降呈负相关），属于经验事实而非第一性原理可推导内容。由于检索失败，无法验证该具体数值范围在 Qwen3-27B 及 W4 量化场景下的准确性，且不同量化算法（如 GPTQ, AWQ, SmoothQuant）对关键权重的处理策略和默认保留比例差异巨大，直接断言一个固定区间存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持。W4 量化确实涉及关键权重保护机制，且保留比例通常与精度损失负相关，但具体 1%-5% 的数值范围及 Qwen3-27B 的特定默认值缺乏外部证据验证，故降级为定性表述。

## Search Query

Qwen3-27B AWQ salient weight retention ratio MMLU correlation
