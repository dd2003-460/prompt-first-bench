# N166: KV Cache 每 Token 显存占用计算公式：Bytes_per_token = 2 * L * Num_KV_Heads * Head_Dim * Dt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

KV Cache 每 Token 显存占用计算公式：Bytes_per_token = 2 * L * Num_KV_Heads * Head_Dim * Dtype_Size。代入 Qwen3-27B 参数 (L=64, KV_Heads=8, Head_Dim=128, FP16=2B) 计算得：2 * 64 * 8 * 128 * 2 = 262,144 Bytes ≈ 0.25 MB/token。此值用于后续 32K 上下文的总占用计算

## Corrected Claim

KV Cache 每 Token 显存占用计算公式：Bytes_per_token = 2 * L * Num_KV_Heads * Head_Dim * Dtype_Size。代入 Qwen3-27B 参数 (L=64, KV_Heads=8, Head_Dim=128, FP16=2B) 计算得：2 * 64 * 8 * 128 * 2 = 262,144 Bytes ≈ 0.25 MB/token。此值用于后续 32K 上下文的总占用计算

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，L为层数，Num_KV_Heads为KV头数，Head_Dim为头维度，Dtype_Size为字节数），数值计算 2*64*8*128*2 = 262,144 Bytes = 0.25 MB 准确无误。
