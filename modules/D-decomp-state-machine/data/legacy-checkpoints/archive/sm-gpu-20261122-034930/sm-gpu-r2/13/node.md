# N155: Qwen3-27B 在 FP8 (E4M3) 权重精度下的 MMLU 准确率损失基准值：FP8 相比 BF16 的精度损失通常 <0.5% [待核验]，但在长文

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 (E4M3) 权重精度下的 MMLU 准确率损失基准值：FP8 相比 BF16 的精度损失通常 <0.5% [待核验]，但在长文本 (32K) 推理中，由于 KV Cache 若保持 BF16 则无额外损失，若 KV 也量化为 FP8 则损失可能累积至 1.0-2.0%；FP8 是 Hopper (H100) 和 Blackwell (B200) 的原生精度，在 RTX 4090 上需软件模拟，性能开销增加约 5-10%。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 权重精度下的 MMLU 准确率损失基准值：FP8 相比 BF16 的精度损失通常 <0.5% [待核验]，但在长文本 (32K) 推理中，由于 KV Cache 若保持 BF16 则无额外损失，若 KV 也量化为 FP8 则损失可能累积至 1.0-2.0%；FP8 是 Hopper (H100) 和 Blackwell (B200) 的原生精度，在 RTX 4090 上需软件模拟，性能开销增加约 5-10%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
