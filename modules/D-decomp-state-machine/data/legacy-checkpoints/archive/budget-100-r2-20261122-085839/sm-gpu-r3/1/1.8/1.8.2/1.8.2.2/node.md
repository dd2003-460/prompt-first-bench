# N183: GPTQ (W4A16) 在 Qwen3-27B 上的 GSM8K 分数实测值为 83.5%（基线 90.0%，损失 6.5%），该数值需验证是否包含 CoT（

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53, N54, N55

## Claim

GPTQ (W4A16) 在 Qwen3-27B 上的 GSM8K 分数实测值为 83.5%（基线 90.0%，损失 6.5%），该数值需验证是否包含 CoT（Chain-of-Thought）提示词，因为 GSM8K 在 CoT 下的量化敏感性显著高于 Zero-shot，通常 CoT 下损失较小（约 3-5%）。

## Corrected Claim

GPTQ (W4A16) 在 Qwen3-27B 上的 GSM8K 分数实测值约为 83.5%（基线 90.0%，损失 6.5%），该数值需验证是否包含 CoT 提示词；通常 CoT 下的量化敏感性低于 Zero-shot，损失较小（约 3-5%），具体数值需以官方基准测试为准。

## Evidence

[质询]该陈述包含具体的经验性数值（GPTQ W4A16在Qwen3-27B上的GSM8K分数83.5%及基线90.0%），属于特定模型、特定量化配置下的实测结果，无法从第一性原理或数学公理推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及CoT敏感性结论）

## Search Query

Qwen3-27B GPTQ W4A16 GSM8K chain-of-thought benchmark
