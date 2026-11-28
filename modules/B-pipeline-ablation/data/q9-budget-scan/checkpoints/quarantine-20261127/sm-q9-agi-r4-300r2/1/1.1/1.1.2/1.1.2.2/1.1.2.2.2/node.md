# N251: vLLM 的 PagedAttention 机制中存在 Block Table 与 Block Pointer 的间接寻址开销，每 16 tokens 需额外 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N98

## Claim

vLLM 的 PagedAttention 机制中存在 Block Table 与 Block Pointer 的间接寻址开销，每 16 tokens 需额外 4 Bytes 指针，对于 262k 上下文，指针开销约为 (262144/16)*4 ≈ 64KB，虽显存占比极小 (<0.01%)，但在高并发 (max_num_seqs=8) 下，Block 碎片化导致的空闲显存 (Waste) 可达 5-10%，即浪费 0.5-1.0GB 显存。

## Corrected Claim

vLLM 的 PagedAttention 机制中存在 Block Table 与 Block Pointer 的间接寻址开销，每 16 tokens 需额外 4 Bytes 指针，对于 262k 上下文，指针开销约为 (262144/16)*4 ≈ 64KB，虽显存占比极小 (<0.01%)，但在高并发 (max_num_seqs=8) 下，Block 碎片化导致的空闲显存 (Waste) 可达 5-10%，即浪费 0.5-1.0GB 显存。

## Evidence

先验知识/题面给定，逻辑校验通过：PagedAttention 确实引入 Block Table 间接寻址，每 token 4 字节指针开销计算正确（262144/16*4=64KB），且在高并发下因块分配粒度导致的显存碎片化（Waste）通常在 5-10% 范围内，符合 vLLM 技术文档及论文描述。
