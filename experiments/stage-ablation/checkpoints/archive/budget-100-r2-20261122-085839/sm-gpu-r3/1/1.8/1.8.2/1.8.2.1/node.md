# N182: GPTQ (W4A16) 在 Qwen3-27B 上的 MMLU 分数实测值为 80.8%（基线 85.0%，损失 4.2%），该数值来源于 Qwen 官方技术

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53, N54, N55

## Claim

GPTQ (W4A16) 在 Qwen3-27B 上的 MMLU 分数实测值为 80.8%（基线 85.0%，损失 4.2%），该数值来源于 Qwen 官方技术报告或主流量化库（如 AutoGPTQ/llama.cpp）的公开基准测试，需确认是否为同数据集版本（MMLU 5-shot 或 10-shot）。

## Corrected Claim

GPTQ (W4A16) 在 Qwen3-27B 上的 MMLU 分数通常会有所下降，具体数值（如80.8%）需依据特定量化库和评测协议（如MMLU 5-shot/10-shot）的公开基准测试确认，基线分数约为85.0%。

## Evidence

[质询]具体数值（80.8%）及基线（85.0%）属于经验事实，且未明确MMLU评测的具体设置（如5-shot/10-shot、数据集版本），不同量化库（AutoGPTQ vs llama.cpp）和评测协议下结果可能存在差异，缺乏来源支持无法确认该特定数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GPTQ W4A16 MMLU benchmark score
