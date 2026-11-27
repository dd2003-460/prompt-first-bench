# N143: Apple M3 Ultra 使用 MLX 框架运行 Qwen3-27B (BF16) 时，由于缺乏 Tensor Core 等效硬件加速，纯 CPU/GPU 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Apple M3 Ultra 使用 MLX 框架运行 Qwen3-27B (BF16) 时，由于缺乏 Tensor Core 等效硬件加速，纯 CPU/GPU 混合推理的吞吐量约为 5-8 tokens/s，且 512GB 统一内存带宽 (819 GB/s) 成为主要瓶颈，无法达到 NVIDIA 消费级显卡的 15+ tokens/s 水平。

## Corrected Claim

Apple M3 Ultra 使用 MLX 框架运行 Qwen3-27B (BF16) 时，受限于统一内存带宽（819 GB/s）及计算架构特性，其吞吐量通常低于 NVIDIA 消费级显卡，具体数值需依据实际基准测试确定，但理论上受带宽限制约为 15 tokens/s 左右。

## Evidence

[质询]数值量级与硬件规格存在潜在矛盾：M3 Ultra 的内存带宽通常标称为 819 GB/s，但 Qwen3-27B (BF16) 模型大小约为 54GB，理论最大吞吐量约为 819/54 ≈ 15 tokens/s。陈述中给出的 5-8 tokens/s 远低于理论上限，暗示存在巨大的非带宽瓶颈（如计算延迟或内存访问效率极低），这与 Apple Silicon 在 LLM 推理中通常接近带宽瓶颈特性的经验直觉不符，且缺乏具体基准测试数据支持该特定低值。 | 先验知识/题面给定，逻辑校验通过但数值缺乏直接来源支持且与理论带宽上限存在偏差，降级为定性表述。
