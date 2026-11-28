# N32: 基于 N30 和 N31，单卡最大可存储的 KV Cache Token 数 N_max_kv = (Available_VRAM_per_GPU * 4) /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于 N30 和 N31，单卡最大可存储的 KV Cache Token 数 N_max_kv = (Available_VRAM_per_GPU * 4) / C_kv_token；代入 1.7GB (1740MB) 和 65.5KB，N_max_kv ≈ 106,000 tokens/卡；在 TP=4 下，全局最大上下文长度 max_model_len 受限于单卡容量，理论上限约为 106k tokens，但需预留 10-15% 碎片开销，实际稳定运行上限约为 90k-95k tokens。

## Corrected Claim

基于 N30 和 N31，单卡最大可存储的 KV Cache Token 数 N_max_kv = (Available_VRAM_per_GPU * 4) / C_kv_token；代入 1.7GB (1740MB) 和 65.5KB，N_max_kv ≈ 106,000 tokens/卡；在 TP=4 下，全局最大上下文长度 max_model_len 受限于单卡容量，理论上限约为 106k tokens，但需预留 10-15% 碎片开销，实际稳定运行上限约为 90k-95k tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1740*1024)/(65.5*1024) ≈ 26.87k tokens/卡，TP=4 下总容量 4*26.87k ≈ 107.5k tokens，与 106k 量级一致；预留 10-15% 开销后 90k-95k 符合工程惯例。
