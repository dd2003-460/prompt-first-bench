# N262: Qwen3-27B 在 FP8 (E4M3) 权重与 KV Cache 下，MMLU 基准测试准确率相比 BF16 基线下降具体数值（预期 <0.5%，需引用 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

Qwen3-27B 在 FP8 (E4M3) 权重与 KV Cache 下，MMLU 基准测试准确率相比 BF16 基线下降具体数值（预期 <0.5%，需引用 Qwen3 官方技术报告或社区复现数据如 HuggingFace OpenLLM 评测）

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 权重与 KV Cache 下，MMLU 基准测试准确率相比 BF16 基线下降幅度极小（通常 <0.5%），具体数值需参考官方技术报告或社区复现数据。

## Evidence

[质询]具体数值（如0.3%或0.4%）属于经验事实，且不同评测集（MMLU 5-shot vs 0-shot）及实现细节可能导致结果波动，缺乏具体来源支持无法确定精确数值。 | 经验事实，逻辑自洽（FP8量化对大模型精度影响通常极小，<0.5%符合业界共识）但缺来源支持

## Search Query

Qwen3-27B FP8 MMLU accuracy drop vs BF16 benchmark
