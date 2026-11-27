# N101: A100/H100 (80GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 65.6 GB < 80 GB，可行，余量 14.4 GB。该余

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

A100/H100 (80GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 65.6 GB < 80 GB，可行，余量 14.4 GB。该余量可支持 Batch Size=2-4 (取决于 KV Cache 大小) 或扩展上下文至 64K (KV Cache 翻倍至 ~17 GB，总计 ~74 GB，仍可行)。

## Corrected Claim

A100/H100 (80GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 65.6 GB < 80 GB，可行，余量 14.4 GB。该余量可支持 Batch Size=2-4 (取决于 KV Cache 大小) 或扩展上下文至 64K (KV Cache 翻倍至 ~17 GB，总计 ~74 GB，仍可行)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，加上KV Cache及激活值，总需求65.6GB在80GB显存范围内，余量14.4GB支持小批量或长上下文，计算量级合理。
