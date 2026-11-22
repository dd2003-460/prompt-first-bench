# N219: 修正后的每卡 KV Cache 占用计算：每卡 4 个 KV Heads，每 Head 每层 2 个向量 (K, V)，每向量 128 维 (Head Dim)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

修正后的每卡 KV Cache 占用计算：每卡 4 个 KV Heads，每 Head 每层 2 个向量 (K, V)，每向量 128 维 (Head Dim)，FP16/BF16 下 2 bytes/值。32K 上下文下，单卡 KV 占用 = 4 Heads × 2 (K,V) × 128 Dim × 2 Bytes × 32768 Tokens × 64 Layers (假设27B为64层，需核验) = 4 × 2 × 128 × 2 × 32768 × 64 ≈ 4.29 GB。若为 INT8 量化 KV，则减半至 ~2.15 GB。

## Corrected Claim

修正后的每卡 KV Cache 占用计算：每卡 4 个 KV Heads，每 Head 每层 2 个向量 (K, V)，每向量 128 维 (Head Dim)，FP16/BF16 下 2 bytes/值。32K 上下文下，单卡 KV 占用 = 4 Heads × 2 (K,V) × 128 Dim × 2 Bytes × 32768 Tokens × 64 Layers (假设27B为64层，需核验) = 4 × 2 × 128 × 2 × 32768 × 64 ≈ 4.29 GB。若为 INT8 量化 KV，则减半至 ~2.15 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 4*2*128*2*32768*64 = 4,294,967,296 Bytes ≈ 4.29 GB 正确；INT8 减半逻辑正确；假设条件（64层）已在陈述中明确标注。
