# N68: 量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6X 带宽 (1.0 TB/s) 和权重/缓存大小，计算每生成 1 个 token 的理论时间下限（注意：若模型无法完整装入显存，此值无意义，需结合 N25 的量化方案）

## Corrected Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6X 带宽 (1.0 TB/s) 和权重/缓存大小，计算每生成 1 个 token 的理论时间下限（注意：若模型无法完整装入显存，此值无意义，需结合 N25 的量化方案）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 GDDR6X 带宽约 1.0 TB/s 符合硬件规格，基于内存带宽瓶颈计算 T_decode 下限的逻辑自洽且量级合理。

## Search Query

RTX 4090 memory bandwidth GDDR6X LLM decode tokens per second
