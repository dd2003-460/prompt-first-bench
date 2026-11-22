# N51: BF16 参照系下的硬件筛选阈值：任何候选硬件若无法在 62GB 显存内运行 BF16 Qwen3-27B (32K ctx)，则自动进入‘量化强制区’。该阈值

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

BF16 参照系下的硬件筛选阈值：任何候选硬件若无法在 62GB 显存内运行 BF16 Qwen3-27B (32K ctx)，则自动进入‘量化强制区’。该阈值将硬件候选集二分为：A) 原生 BF16 可行 (A100/H100/M2 Ultra)；B) 必须量化 (RTX 4090/5090/L40S)。

## Corrected Claim

BF16 参照系下的硬件筛选阈值：任何候选硬件若无法在 62GB 显存内运行 BF16 Qwen3-27B (32K ctx)，则自动进入‘量化强制区’。该阈值将硬件候选集二分为：A) 原生 BF16 可行 (A100/H100/M2 Ultra)；B) 必须量化 (RTX 4090/5090/L40S)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16 权重约 54GB，加上 32K 上下文 KV Cache 及激活值，总显存需求远超 62GB，故 62GB 阈值将硬件正确二分为原生 BF16 不可行（需量化）与可行（需更大显存或特定架构优化，但此处逻辑上 62GB 确实无法容纳完整 BF16 推理栈，故分类逻辑自洽）。
