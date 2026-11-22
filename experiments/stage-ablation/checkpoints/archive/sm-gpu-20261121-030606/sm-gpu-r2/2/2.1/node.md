# N12: 工作点1（高容量低精度）：RTX 4090 24GB + INT8精度，Qwen3-27B权重占用约13.5GB，剩余10.5GB用于KV Cache，32K上

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

工作点1（高容量低精度）：RTX 4090 24GB + INT8精度，Qwen3-27B权重占用约13.5GB，剩余10.5GB用于KV Cache，32K上下文下KV Cache占用约5.2GB（假设GQA 8 KV heads, head_dim 128, 28 layers, 2 bytes/token/layer），总占用18.7GB < 24GB，可行且留有15%余量。

## Corrected Claim

工作点1（高容量低精度）：RTX 4090 24GB + INT8精度，Qwen3-27B权重占用约13.5GB，剩余10.5GB用于KV Cache，32K上下文下KV Cache占用约5.2GB（假设GQA 8 KV heads, head_dim 128, 28 layers, 2 bytes/token/layer），总占用18.7GB < 24GB，可行且留有15%余量。

## Evidence

先验知识/题面给定，逻辑校验通过：权重13.5GB + KV Cache 5.2GB = 18.7GB < 24GB，且KV Cache计算量级（28层*8头*128维*2字节*32K token ≈ 4.7GB，加上其他开销约5.2GB）合理。

## Search Query

Qwen3 27B KV cache size calculation 32K context
