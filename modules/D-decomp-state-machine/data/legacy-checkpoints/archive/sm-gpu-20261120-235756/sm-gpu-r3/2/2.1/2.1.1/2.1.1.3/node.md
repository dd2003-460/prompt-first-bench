# N185: 长上下文场景下KV Cache瓶颈的量化阈值：在RTX 5090 (32GB)上，若权重占用13.5GB (FP8)，KV Cache (BF16) 占用8GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

长上下文场景下KV Cache瓶颈的量化阈值：在RTX 5090 (32GB)上，若权重占用13.5GB (FP8)，KV Cache (BF16) 占用8GB (32K)，剩余10.5GB用于激活和框架。若上下文扩展至64K，KV Cache增至16GB，总占用29.5GB，接近显存上限，此时必须启用FP8 KV Cache (降至8GB) 或限制Batch Size=1。

## Corrected Claim

长上下文场景下KV Cache瓶颈的量化阈值：在RTX 5090 (32GB)上，若权重占用13.5GB (FP8)，KV Cache (BF16) 占用8GB (32K)，剩余10.5GB用于激活和框架。若上下文扩展至64K，KV Cache增至16GB，总占用29.5GB，接近显存上限，此时必须启用FP8 KV Cache (降至8GB) 或限制Batch Size=1。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（13.5+8+10.5=32, 13.5+16=29.5），KV Cache随上下文线性增长符合原理，显存瓶颈判断合理。

## Search Query

RTX 5090 32GB KV cache limit 64k context
