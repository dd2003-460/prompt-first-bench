# N180: vLLM 的 PagedAttention Block Table 显存开销：Block Table 本身占用显存 = max_num_seqs * num_b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

vLLM 的 PagedAttention Block Table 显存开销：Block Table 本身占用显存 = max_num_seqs * num_blocks_per_seq * sizeof(int32)，对于 32K 上下文和 16 Block/Seq 的配置，该开销通常小于 0.1GB，可忽略不计；但 vLLM 还会预分配一块用于 KV Cache 的连续显存池，其大小由 --gpu-memory-utilization 参数决定（默认 0.9），即总显存 * 0.9 - (Model + CUDA + PyTorch)

## Corrected Claim

vLLM 的 PagedAttention Block Table 显存开销：Block Table 本身占用显存 = max_num_seqs * num_blocks_per_seq * sizeof(int32)，对于 32K 上下文和 16 Block/Seq 的配置，该开销通常小于 0.1GB，可忽略不计；但 vLLM 还会预分配一块用于 KV Cache 的连续显存池，其大小由 --gpu-memory-utilization 参数决定（默认 0.9），即总显存 * 0.9 - (Model + CUDA + PyTorch)

## Evidence

先验知识/题面给定，逻辑校验通过：Block Table 显存计算量级合理（32K上下文下通常仅需少量块，int32数组开销极小），vLLM 显存分配机制（gpu-memory-utilization 默认 0.9 及预留逻辑）符合其设计原理。

## Search Query

vLLM gpu-memory-utilization parameter default value KV cache pool allocation
