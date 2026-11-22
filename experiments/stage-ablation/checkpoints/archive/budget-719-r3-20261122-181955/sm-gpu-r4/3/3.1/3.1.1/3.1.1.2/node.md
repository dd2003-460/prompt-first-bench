# N266: 基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 2 bytes = 4.295 GB，修正 N89 原估算 32.77 GB 的错误。

## Corrected Claim

基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 2 bytes = 4.295 GB，修正 N89 原估算 32.77 GB 的错误。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了单token的基础单位（128 KB），子节点2基于该单位推导32K上下文的总容量（4.0 GB）。两者在逻辑上是“单位定义”与“总量计算”的正交关系，无重复。父节点的核心内容（参数修正、单token值、总容量值、对N89/N266错误的修正）均被两个子节点完整覆盖。虽然总容量存在GiB与GB的细微差别（4.0 GiB vs 4.295 GB），但子节点2已明确解释了这一差异来源，因此不构成矛盾或冗余。）
