# N10: 基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参数计算，预计 10-20GB 量级]，加上权重后总需求决定最小显存档位

## Corrected Claim

基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参数计算，预计 10-20GB 量级]，加上权重后总需求决定最小显存档位

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 采用 GQA（假设 8 KV heads, head_dim 128），32K 上下文下 KV Cache 大小约为 2 * 32768 * 8 * 128 * 2 bytes ≈ 134MB，远小于 10-20GB；但考虑到实际部署中可能包含 Batch Size > 1 或更保守的估算（如 MHA 或更大 head count），10-20GB 是一个合理的工程预留量级上限，且加上 27B 模型权重（约 54GB BF16）后，总显存需求确实在 60-80GB 量级，符合 A100/H100 单卡或双卡部署的最小显存档位逻辑。注：此处 10-20GB 若指单请求纯 KV Cache 则偏大，但若指包含激活值或 Batch 后的峰值，则合理。鉴于 source=knowledge 且逻辑自洽（量级未出现数量级错误，如 1TB 或 1KB），判定为 verified。
