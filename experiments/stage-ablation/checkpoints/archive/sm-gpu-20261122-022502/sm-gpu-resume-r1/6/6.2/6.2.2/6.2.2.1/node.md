# N291: INT8 vs FP8 在代码生成/通用对话场景下的性价比对比：INT8 显存 27GB，FP8 显存 27GB。INT8 质量损失 <1%，FP8 质量损失 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

INT8 vs FP8 在代码生成/通用对话场景下的性价比对比：INT8 显存 27GB，FP8 显存 27GB。INT8 质量损失 <1%，FP8 质量损失 <0.5%。在 RTX 4090 双卡方案中，两者均不可行 (27GB > 24GB/卡)，需 2x 4090 跨卡分片或 1x H100。若使用 Mac Studio (192GB)，两者均可行，但 FP8 在 vLLM 中支持更好 (PagedAttention 优化)，故 FP8 为优选。

## Corrected Claim

INT8 和 FP8 的显存占用取决于模型参数量，27GB 可能对应特定中等规模模型（如 13B-14B）。在 RTX 4090 双卡方案中，若单卡显存不足 27GB，则需跨卡分片或使用更大显存显卡。FP8 在 vLLM 中的支持取决于硬件架构（如 H100 优于 4090）和软件版本，不能简单断言在 4090 上支持更好。

## Evidence

[质询]数值量级与硬件规格存在明显矛盾：27GB 显存占用通常对应约 13B-14B 参数量的模型（如 Llama-3-8B 的 INT8 约为 9-10GB，Llama-3-70B 的 INT8 约为 70GB+）。若模型为 70B 级别，27GB 数值错误；若模型为 8B 级别，27GB 数值过大且无需双卡。此外，'FP8 在 vLLM 中支持更好'这一断言缺乏具体版本和上下文支持，vLLM 对 FP8 的支持依赖于特定硬件（如 Hopper 架构）和软件版本，在 RTX 4090 (Ada Lovelace) 上 FP8 支持情况复杂，不能一概而论为'支持更好'。 | 先验知识/题面给定，逻辑校验未通过：27GB 显存与常见模型规模（8B/70B）不匹配，且 FP8 在消费级显卡（RTX 4090）上的支持情况描述过于绝对，存在逻辑与事实疑点。
