# N323: TensorRT-LLM 已知 Bug 列表中影响 Qwen3-27B 推理稳定性的关键问题：检索 GitHub Issues 或 NVIDIA 开发者论坛中关

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114, N115, N117

## Claim

TensorRT-LLM 已知 Bug 列表中影响 Qwen3-27B 推理稳定性的关键问题：检索 GitHub Issues 或 NVIDIA 开发者论坛中关于 Qwen3 模型在 TensorRT-LLM 中出现的 NaN 输出、内存泄漏或特定序列长度（如 32K）下崩溃的报告，并评估这些 Bug 的修复状态及 Workaround 成本。

## Corrected Claim

TensorRT-LLM 在运行 Qwen3-27B 时可能存在推理稳定性问题（如 NaN 输出、内存泄漏或长序列崩溃），需查阅 GitHub Issues 或 NVIDIA 开发者论坛以确认具体 Bug 详情、修复状态及 Workaround 成本。

## Evidence

[质询]该陈述预设了特定Bug（NaN、内存泄漏、32K崩溃）的存在及其对Qwen3-27B的影响，属于具体的经验性工程事实。由于缺乏检索来源，无法验证这些特定Bug是否真实存在、是否已修复或具体的Workaround成本，存在将推测当事实的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体Bug列表及修复状态）

## Search Query

TensorRT-LLM Qwen3 bug NaN crash 32K context github issues
