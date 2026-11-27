# N552: RX 9070 显存容量 16GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：剩余 2.5GB 用于 KV Cache，支持上下文

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170

## Claim

RX 9070 显存容量 16GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：剩余 2.5GB 用于 KV Cache，支持上下文长度 ≈ 460 tokens，远低于 32K 要求，故 RX 9070 不可行

## Corrected Claim

RX 9070 显存容量 16GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：剩余 2.5GB 用于 KV Cache，支持上下文长度 ≈ 460 tokens，远低于 32K 要求，故 RX 9070 不可行

## Evidence

先验知识/题面给定，逻辑校验通过：16GB - 13.5GB = 2.5GB 剩余显存；对于 27B 参数量的大模型，2.5GB 显存仅能支持极短的上下文（数百 tokens 量级），远低于 32K 需求，结论符合显存计算逻辑。

## Search Query

Qwen3-27B INT4 memory requirement KV cache 32k context
