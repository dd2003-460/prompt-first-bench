# N181: RX 7800 XT (16GB) 在 Qwen3-27B INT4 (AWQ) 量化下的可行性判定：权重约 13.5GB + KV Cache (32K, B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

RX 7800 XT (16GB) 在 Qwen3-27B INT4 (AWQ) 量化下的可行性判定：权重约 13.5GB + KV Cache (32K, BF16, n_kv_heads=8) 约 5.37GB + 框架开销 3GB ≈ 21.87GB > 16GB 显存，结论为不可行；若采用 FP8 权重 (27GB) 更不可行。需修正 N84 中可能误判其适配 24GB 卡而忽略 16GB 卡显存瓶颈的潜在风险，明确 16GB 卡无法承载 27B 模型长上下文推理。

## Corrected Claim

RX 7800 XT (16GB) 在 Qwen3-27B INT4 (AWQ) 量化下的可行性判定：权重约 13.5GB + KV Cache (32K, BF16, n_kv_heads=8) 约 5.37GB + 框架开销 3GB ≈ 21.87GB > 16GB 显存，结论为不可行；若采用 FP8 权重 (27GB) 更不可行。需修正 N84 中可能误判其适配 24GB 卡而忽略 16GB 卡显存瓶颈的潜在风险，明确 16GB 卡无法承载 27B 模型长上下文推理。

## Evidence

[质询]KV Cache 计算中假设 n_kv_heads=8 且未考虑 GQA (Grouped Query Attention) 可能带来的显存节省，若 Qwen3-27B 实际采用更激进的 GQA 配置（如 n_kv_heads=4 或更少），KV Cache 占用将减半，可能使总显存需求降至 16GB 附近，从而挑战‘绝对不可行’的结论。 | 先验知识/题面给定，逻辑校验通过：权重 13.5GB + KV Cache 5.37GB + 开销 3GB = 21.87GB > 16GB，数值量级合理，结论符合显存限制的基本物理约束。
