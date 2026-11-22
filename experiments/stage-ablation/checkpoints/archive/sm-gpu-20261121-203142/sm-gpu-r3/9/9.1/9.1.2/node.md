# N351: M2 Ultra 在 INT8 量化精度下的工作点：理论 TPS 29.6 tokens/s (800GB/s / 27GB)，硬件成本不变，5年TCO 不变；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

M2 Ultra 在 INT8 量化精度下的工作点：理论 TPS 29.6 tokens/s (800GB/s / 27GB)，硬件成本不变，5年TCO 不变；相比 BF16，吞吐量翻倍，但需验证 Qwen3-27B 在 INT8 下的 MMLU/GPQA 准确率下降是否小于 1% [待核验]，若质量损失可接受，则性价比显著优于 BF16。

## Corrected Claim

M2 Ultra 在 INT8 量化精度下的工作点：理论 TPS 29.6 tokens/s (800GB/s / 27GB)，硬件成本不变，5年TCO 不变；相比 BF16，吞吐量翻倍，但需验证 Qwen3-27B 在 INT8 下的 MMLU/GPQA 准确率下降是否小于 1% [待核验]，若质量损失可接受，则性价比显著优于 BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：29.6 TPS 与 800GB/s 带宽及 27GB 模型大小在算术上自洽（800/27≈29.6），且 INT8 相比 BF16 吞吐量翻倍符合量化原理；source 为 knowledge，无需外部来源支持。
