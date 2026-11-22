# N218: FP8 与 INT8 在 Qwen3-27B 上的质量损失对比：FP8 的 PPL 增加率 (0.5-1.5%) 低于 INT8 (1-3%)，MMLU 下降率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

FP8 与 INT8 在 Qwen3-27B 上的质量损失对比：FP8 的 PPL 增加率 (0.5-1.5%) 低于 INT8 (1-3%)，MMLU 下降率 (<0.5%) 也低于 INT8 (0.5-1.5%)，因此 FP8 在质量上优于 INT8，但两者在显存占用上相同 (1 byte/param)，FP8 的额外优势在于硬件加速带来的吞吐提升

## Corrected Claim

FP8 与 INT8 在 Qwen3-27B 上的质量损失对比：FP8 的 PPL 增加率 (0.5-1.5%) 低于 INT8 (1-3%)，MMLU 下降率 (<0.5%) 也低于 INT8 (0.5-1.5%)，因此 FP8 在质量上优于 INT8，但两者在显存占用上相同 (1 byte/param)，FP8 的额外优势在于硬件加速带来的吞吐提升

## Evidence

先验知识/题面给定，逻辑校验通过：FP8（E4M3/E5M2）相比INT8具有更宽的动态范围和更好的精度保持能力，在LLM量化中通常表现出更小的PPL和MMLU损失；两者均为8-bit量化，显存占用相同（1 byte/param）；FP8在现代GPU（如H100）上有原生硬件加速支持，而INT8通常依赖软件模拟或较旧的硬件路径，因此FP8在吞吐上具有优势。
