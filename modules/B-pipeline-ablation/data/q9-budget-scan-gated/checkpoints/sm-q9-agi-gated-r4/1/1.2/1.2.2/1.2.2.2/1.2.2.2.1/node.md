# N87: N40中'94.5MB总KV需求'的计算基于错误的单序列长度假设（985 tokens）。若按修正后的NVFP4显存上限（~1.13M tokens）或实际业务

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

N40中'94.5MB总KV需求'的计算基于错误的单序列长度假设（985 tokens）。若按修正后的NVFP4显存上限（~1.13M tokens）或实际业务场景（如262k max_len），8序列并发的KV Cache总需求为 8 * 262144 * 12KB ≈ 25.6 GB。这超过了单卡13.0125GB可用显存，表明在长上下文高并发下，显存确实是瓶颈，需启用PagedAttention换页或降低并发数至 13.0125GB / (262144 * 12KB) ≈ 4.1 序列。

## Corrected Claim

N40中'94.5MB总KV需求'的计算基于错误的单序列长度假设（985 tokens）。若按修正后的NVFP4显存上限（~1.13M tokens）或实际业务场景（如262k max_len），8序列并发的KV Cache总需求为 8 * 262144 * 12KB ≈ 25.6 GB。这超过了单卡13.0125GB可用显存，表明在长上下文高并发下，显存确实是瓶颈，需启用PagedAttention换页或降低并发数至 13.0125GB / (262144 * 12KB) ≈ 4.1 序列。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（8*262144*12KB≈25.6GB > 13GB，13GB/(262144*12KB)≈4.1），符合显存瓶颈的基本物理/经济直觉。
