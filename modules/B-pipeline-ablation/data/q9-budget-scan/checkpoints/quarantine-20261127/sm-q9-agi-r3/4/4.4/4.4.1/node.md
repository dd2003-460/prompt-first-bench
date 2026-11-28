# N72: Llama-3-8B (FP16) 在单张 V100 (16GB) 上的显存占用约为 16GB (权重 16GB + KV Cache 溢出)，无法独立运行；若

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 641)
