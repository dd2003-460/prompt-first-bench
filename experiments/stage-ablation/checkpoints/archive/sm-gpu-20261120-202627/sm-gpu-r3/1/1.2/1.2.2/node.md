# N39: 32K 上下文下 KV Cache 显存占用的数值计算（BF16 精度）：代入 N36 参数 (64 layers, 4096 hidden, 8 KV hea

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

32K 上下文下 KV Cache 显存占用的数值计算（BF16 精度）：代入 N36 参数 (64 layers, 4096 hidden, 8 KV heads, 32768 seq_len, 2 bytes)，计算得 KV_Cache = 2 * 64 * 4096 * 8 * 32768 * 2 / 1e9 ≈ 2.8 GB。

## Corrected Claim

32K 上下文下 KV Cache 显存占用的数值计算（BF16 精度）：代入 N36 参数 (64 layers, 4096 hidden, 8 KV heads, 32768 seq_len, 2 bytes)，计算得 KV_Cache = 2 * 64 * 4096 * 8 * 32768 * 2 / 1e9 ≈ 27.5 GB。

## Evidence

父节点级核验未通过：不完备（父节点明确限定为“KV Cache 显存占用的数值计算”，但子节点不仅重复了KV Cache的结果，还引入了“权重显存”、“总显存”以及“硬件可行性分析”。这导致子节点内容远超父节点范围（Scope Mismatch），且父节点的核心内容（KV Cache计算过程/结果）并未被独立、完整地拆解为子节点，而是被混合在子节点中作为前提条件出现。）
