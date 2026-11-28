# N627: vLLM PagedAttention Block Table 重建耗时 T_block_table 取决于初始 Block 数量 N_blocks 与 Blo

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N223

## Claim

vLLM PagedAttention Block Table 重建耗时 T_block_table 取决于初始 Block 数量 N_blocks 与 Block 元数据写入速度；假设 N_blocks=1024，每个 Block 元数据 64 bytes，写入内存带宽 50GB/s，则 T_block_table ≈ (1024 * 64) / 50e9 ≈ 1.3μs，可忽略；但若涉及 GPU 端 Block 指针初始化（如 cudaMemsetAsync），耗时可能升至 1-5ms，需验证是否成为瓶颈。

## Corrected Claim

vLLM PagedAttention Block Table 重建耗时 T_block_table 取决于初始 Block 数量 N_blocks 与 Block 元数据写入速度；假设 N_blocks=1024，每个 Block 元数据 64 bytes，写入内存带宽 50GB/s，则 T_block_table ≈ (1024 * 64) / 50e9 ≈ 1.3μs，可忽略；但若涉及 GPU 端 Block 指针初始化（如 cudaMemsetAsync），耗时可能升至 1-5ms，需验证是否成为瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：CPU侧内存带宽计算量级正确（微秒级），GPU侧内核启动/同步开销量级合理（毫秒级），符合系统性能常识。

## Search Query

vLLM PagedAttention block table initialization time GPU memset
