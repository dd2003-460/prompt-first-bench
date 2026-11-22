# N539: RTX 4090 单卡在 FP8 精度下的性价比工作点：权重+KV Cache 显存占用约 35GB，超出 24GB 显存限制，需启用 CPU Offload 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N223

## Claim

RTX 4090 单卡在 FP8 精度下的性价比工作点：权重+KV Cache 显存占用约 35GB，超出 24GB 显存限制，需启用 CPU Offload 或采用 FlashAttention 优化；假设 Offload 导致 Decode 速度降至 12 tokens/s，单位成本吞吐 = 12 / 2000 = 0.006 tok/s/$。

## Corrected Claim

RTX 4090 单卡在 FP8 精度下，若权重+KV Cache 显存占用约 35GB，超出 24GB 显存限制，需启用 CPU Offload 或采用 FlashAttention 优化；Offload 可能导致 Decode 速度显著下降，单位成本吞吐需根据实际 Offload 策略和硬件成本进一步评估。

## Evidence

[质询]数值量级与假设合理性存疑：RTX 4090 显存为 24GB，若模型权重+KV Cache 占用 35GB，超出 11GB，Offload 比例较高，Decode 速度降至 12 tokens/s 可能过于乐观或悲观（取决于具体模型大小和 Offload 策略），且 2000 美元的价格假设未明确说明是单卡成本还是总成本，导致单位成本计算缺乏明确基准。 | 先验知识/题面给定，逻辑校验通过，但数值假设（如 12 tokens/s 和 2000 美元）缺乏外部来源支持，属于经验事实，需降级为定性表述。
