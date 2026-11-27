# N266: GPTQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的具体耗时：基于校准集大小 128 样本、Batch Size 16、序列长度 204

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

GPTQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的具体耗时：基于校准集大小 128 样本、Batch Size 16、序列长度 2048，实测耗时约 2.5-3.5 小时（需引用 HuggingFace AutoGPTQ 或 GPTQModel 库的官方 benchmark 或社区 Issue 报告）

## Corrected Claim

GPTQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的耗时受校准集大小、Batch Size 及序列长度影响，具体数值需参考 GPTQModel 或 AutoGPTQ 社区实测报告，通常耗时在数小时量级。

## Evidence

[质询]该陈述包含具体的经验性耗时数据（2.5-3.5小时），属于硬件性能与软件库效率的经验事实，无法从第一性原理推导。且缺乏官方或社区权威来源直接支持该特定配置下的精确耗时区间，不同校准集、硬件驱动版本及库版本可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

GPTQ quantization time RTX 4090 Qwen3-27B 128 samples calibration
