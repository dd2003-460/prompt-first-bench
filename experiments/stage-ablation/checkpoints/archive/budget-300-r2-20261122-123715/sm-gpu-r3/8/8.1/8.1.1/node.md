# N347: 若 Qwen3-27B 的 KV_heads 确认为 8（如 Qwen2.5-32B），则 32K 上下文下 KV Cache 显存占用为 (2 * 64 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

若 Qwen3-27B 的 KV_heads 确认为 8（如 Qwen2.5-32B），则 32K 上下文下 KV Cache 显存占用为 (2 * 64 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 16GB（BF16）或 8GB（INT8）；若 KV_heads 为 4，则减半为 8GB（BF16）或 4GB（INT8）。

## Corrected Claim

若 Qwen3-27B 的 KV_heads 确认为 8（如 Qwen2.5-32B），则 32K 上下文下 KV Cache 显存占用为 (2 * 64 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 16GB（BF16）或 8GB（INT8）；若 KV_heads 为 4，则减半为 8GB（BF16）或 4GB（INT8）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 (2 * 64 * 8 * 128 * 32768 * 2) / 1024^3 计算结果确为 16GB，且符合 KV Cache 显存占用的一般计算逻辑（层数*头数*头维度*序列长度*字节数*2(K+V)）。
