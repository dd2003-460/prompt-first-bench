# N260: INT8量化下Qwen3-27B在A100 40GB上的权重占用为13.5GB，加上32K上下文KV Cache (FP16, ~6.5GB) 及激活值开销，总

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

INT8量化下Qwen3-27B在A100 40GB上的权重占用为13.5GB，加上32K上下文KV Cache (FP16, ~6.5GB) 及激活值开销，总显存占用约22-24GB，剩余显存不足以支持batch_size>2的高并发推理，限制了单位时间Token吞吐量上限。

## Corrected Claim

INT8量化下Qwen3-27B在A100 40GB上的权重占用为13.5GB，加上32K上下文KV Cache (FP16, ~6.5GB) 及激活值开销，总显存占用约22-24GB，剩余显存不足以支持batch_size>2的高并发推理，限制了单位时间Token吞吐量上限。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重约13.5GB，32K上下文KV Cache约6.5GB，加上激活值开销，总显存占用约22-24GB，符合A100 40GB显存限制下的推理资源分配逻辑。
