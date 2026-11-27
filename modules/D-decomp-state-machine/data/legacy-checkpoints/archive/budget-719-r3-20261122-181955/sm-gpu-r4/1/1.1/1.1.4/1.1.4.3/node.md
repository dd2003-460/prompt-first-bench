# N143: RTX 4070 Ti Super 的 16GB 显存无法容纳 Qwen3-27B 的 INT4 权重 (13.5GB) + 32K KV Cache (8.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

RTX 4070 Ti Super 的 16GB 显存无法容纳 Qwen3-27B 的 INT4 权重 (13.5GB) + 32K KV Cache (8.59GB) = 22.09GB，即使使用 INT8 KV Cache (4.3GB) 总需求 17.8GB 仍超过 16GB 上限，因此该卡在不使用 CPU Offload 或极端量化 (W3) 的情况下不可行。

## Corrected Claim

RTX 4070 Ti Super 的 16GB 显存无法容纳 Qwen3-27B 的 INT4 权重 (13.5GB) + 32K KV Cache (8.59GB) = 22.09GB，即使使用 INT8 KV Cache (4.3GB) 总需求 17.8GB 仍超过 16GB 上限，因此该卡在不使用 CPU Offload 或极端量化 (W3) 的情况下不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：22.09GB > 16GB 且 17.8GB > 16GB，算术与显存容量限制逻辑自洽。

## Search Query

RTX 4070 Ti Super 16GB insufficient for 27B LLM inference memory requirements
