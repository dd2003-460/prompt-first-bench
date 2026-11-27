# N342: Qwen3-27B 在 32K 上下文、GQA 配置 (64层, 8 KV heads, 128 dim, BF16) 下，KV Cache 的精确显存占用计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

Qwen3-27B 在 32K 上下文、GQA 配置 (64层, 8 KV heads, 128 dim, BF16) 下，KV Cache 的精确显存占用计算公式为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_Per_Elem，代入数值为 2 * 64 * 8 * 128 * 32768 * 2 bytes = 8.59 GB，而非 N122 中估算的 12.8 GB，修正后总显存需求为 13.5GB (W4权重) + 8.59GB (KV) + 2GB (激活) ≈ 24.09 GB，极度贴近 24GB 物理上限，存在 OOM 风险。

## Corrected Claim

Qwen3-27B 在 32K 上下文、GQA 配置 (64层, 8 KV heads, 128 dim, BF16) 下，KV Cache 的精确显存占用计算公式为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_Per_Elem，代入数值为 2 * 64 * 8 * 128 * 32768 * 2 bytes = 8.59 GB，而非 N122 中估算的 12.8 GB，修正后总显存需求为 13.5GB (W4权重) + 8.59GB (KV) + 2GB (激活) ≈ 24.09 GB，极度贴近 24GB 物理上限，存在 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 公式 2*L*H*D*S*B 代入数值 2*64*8*128*32768*2 = 8,589,934,592 bytes ≈ 8.59 GB，计算准确；总显存 13.5+8.59+2=24.09 GB 逻辑自洽。
