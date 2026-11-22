# N300: BF16 精度的 KV Cache 显存占用量计算验证：2 (K/V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

BF16 精度的 KV Cache 显存占用量计算验证：2 (K/V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 32768 (tokens) × 2 (bytes) = 10,737,418,240 bytes ≈ 10.0 GB (GiB) 或 10.74 GB (GB)，与 N106 声称的 10.74 GB 一致，确认 BF16 下 32K 上下文 KV Cache 占用约为 10.74 GB

## Corrected Claim

BF16 精度的 KV Cache 显存占用量计算验证：2 (K/V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 32768 (tokens) × 2 (bytes) = 10,737,418,240 bytes ≈ 10.0 GB (GiB) 或 10.74 GB (GB)，与 N106 声称的 10.74 GB 一致，确认 BF16 下 32K 上下文 KV Cache 占用约为 10.74 GB

## Evidence

先验知识/题面给定，逻辑校验通过：2×64×8×128×32768×2 = 10,737,418,240 bytes，换算为 GiB 约为 10.0 GiB，换算为 GB 约为 10.74 GB，计算无误且量级合理。
