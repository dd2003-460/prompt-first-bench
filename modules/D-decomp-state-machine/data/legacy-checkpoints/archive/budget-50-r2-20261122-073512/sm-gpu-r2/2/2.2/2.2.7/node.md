# N87: NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的理论生成速度上限：Bandwidth 3350 GB/s / (54 GB 权重

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的理论生成速度上限：Bandwidth 3350 GB/s / (54 GB 权重 + 0.128 GB KV + 2 GB Activations) ≈ 60 tokens/s；实际受计算瓶颈限制，预计约为理论值的 60-70%，即 36-42 tokens/s [待核验]。

## Corrected Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的带宽受限理论速度约为 60 tokens/s；实际生成速度受计算与带宽双重瓶颈影响，预计约为 36-42 tokens/s。

## Evidence

[质询]该陈述将‘理论生成速度上限’定义为纯带宽限制（Roofline Model 的带宽墙），但忽略了 H100 在 BF16 下拥有极高的计算能力（~989 TFLOPS）。对于 27B 模型，单卡推理通常处于计算受限（Compute-bound）或混合受限区域，而非纯带宽受限。直接称带宽计算结果为‘理论上限’在术语上不准确，且 60-70% 的效率系数是经验估计值，缺乏针对该特定模型和硬件组合的精确基准测试支持。 | 先验知识/题面给定，逻辑校验通过。带宽计算量级合理（3350/56.128 ≈ 59.7），但‘理论上限’表述不严谨，且效率系数为经验估计，故降级。
