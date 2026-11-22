# N195: PagedAttention 块表 (Block Table) 的精确显存占用公式为 C_block_table = N_max_seqs * (L_ctx /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

PagedAttention 块表 (Block Table) 的精确显存占用公式为 C_block_table = N_max_seqs * (L_ctx / block_size) * 4 bytes (int32 index)，其中 block_size 默认值为 16 tokens。对于 max_num_seqs=256, L_ctx=32768, block_size=16，计算得 256 * 2048 * 4 = 2,097,152 bytes ≈ 2.0 MB，远低于 N50 声称的 0.1GB 下限，表明 N50 的 0.1-0.3GB 估算严重高估了纯块表开销。

## Corrected Claim

PagedAttention 块表 (Block Table) 的精确显存占用公式为 C_block_table = N_max_seqs * (L_ctx / block_size) * 4 bytes (int32 index)，其中 block_size 默认值为 16 tokens。对于 max_num_seqs=256, L_ctx=32768, block_size=16，计算得 256 * 2048 * 4 = 2,097,152 bytes ≈ 2.0 MB，远低于 N50 声称的 0.1GB 下限，表明 N50 的 0.1-0.3GB 估算严重高估了纯块表开销。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（256 * (32768/16) * 4 = 2,097,152 bytes ≈ 2MB），量级合理，且符合 PagedAttention 块表存储 int32 索引的标准实现逻辑。
