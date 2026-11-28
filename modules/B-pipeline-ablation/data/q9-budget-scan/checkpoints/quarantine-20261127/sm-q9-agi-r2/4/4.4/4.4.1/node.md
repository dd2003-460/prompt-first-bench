# N72: Llama-3-8B (FP16) 在单张 V100 (16GB) 上的显存占用约为 16GB (权重 16GB + KV Cache 溢出)，无法独立运行；若

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Llama-3-8B (FP16) 在单张 V100 (16GB) 上的显存占用约为 16GB (权重 16GB + KV Cache 溢出)，无法独立运行；若采用 INT8 量化，权重约 8GB，剩余 8GB 可用于 KV Cache，支持 max_seq_len=8192 时的单并发推理。

## Corrected Claim

Llama-3-8B (FP16) 在单张 V100 (16GB) 上的显存占用约为 16GB (权重 16GB + KV Cache 溢出)，无法独立运行；若采用 INT8 量化，权重约 8GB，剩余 8GB 可用于 KV Cache，支持 max_seq_len=8192 时的单并发推理。

## Evidence

先验知识/题面给定，逻辑校验通过：Llama-3-8B参数量约8.03B，FP16权重约16.06GB，超过V100 16GB显存，无法运行；INT8量化后权重约8.03GB，剩余约8GB显存用于KV Cache及激活值，在max_seq_len=8192单并发场景下显存占用合理，符合工程常识。
