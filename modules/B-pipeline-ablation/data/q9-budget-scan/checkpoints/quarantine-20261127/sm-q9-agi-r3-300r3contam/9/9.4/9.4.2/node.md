# N248: 多序列并发下的显存压力临界点：总显存需求 = M_weights_per_gpu + (max_num_seqs * KV_per_seq_per_gpu) +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

多序列并发下的显存压力临界点：总显存需求 = M_weights_per_gpu + (max_num_seqs * KV_per_seq_per_gpu) + M_activations。M_weights_per_gpu ≈ 14GB/4 ≈ 3.5GB (NVFP4 权重分片)。若 max_num_seqs=8，KV 总占用 = 8 * 4.3GB ≈ 34.4GB，远超 16GB 物理限制。因此，在 262k 长度下，实际可行的 max_num_seqs 仅为 1-2，否则必然 OOM。

## Corrected Claim

多序列并发下的显存压力临界点：总显存需求 = M_weights_per_gpu + (max_num_seqs * KV_per_seq_per_gpu) + M_activations。M_weights_per_gpu ≈ 14GB/4 ≈ 3.5GB (NVFP4 权重分片)。若 max_num_seqs=8，KV 总占用 = 8 * 4.3GB ≈ 34.4GB，远超 16GB 物理限制。因此，在 262k 长度下，实际可行的 max_num_seqs 仅为 1-2，否则必然 OOM。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（8*4.3=34.4 > 16），符合显存管理的基本物理约束和推理引擎资源分配逻辑。
