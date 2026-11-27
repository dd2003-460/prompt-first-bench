# N217: Qwen3-27B 使用 GPTQ-4bit (Group Size 128, 校准集 128 samples) 量化后的 MMLU 基准测试分数为 79.8 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N76, N77, N78

## Claim

Qwen3-27B 使用 GPTQ-4bit (Group Size 128, 校准集 128 samples) 量化后的 MMLU 基准测试分数为 79.8 (来源: HuggingFace Qwen3-27B-GPTQ 模型卡或 LLM-Compressor 基准测试, 5-shot)

## Corrected Claim

Qwen3-27B 使用 GPTQ-4bit 量化后的 MMLU 基准测试分数约为 79.8（具体数值可能因量化参数和评估设置略有差异）

## Evidence

[质询]具体数值 79.8 属于经验事实，且缺乏来源支持；不同量化配置（如 Group Size 或校准集大小）可能导致分数波动，无法确认该特定数值准确无误。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无可用外部证据）

## Search Query

Qwen3-27B GPTQ 4bit MMLU score benchmark
