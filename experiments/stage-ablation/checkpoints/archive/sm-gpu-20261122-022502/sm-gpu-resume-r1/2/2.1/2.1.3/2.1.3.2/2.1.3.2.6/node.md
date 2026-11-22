# N561: RX 9070 GRE 显存容量 12GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：显存不足，无法加载模型，故 RX 9070 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

RX 9070 GRE 显存容量 12GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：显存不足，无法加载模型，故 RX 9070 GRE 不可行

## Corrected Claim

RX 9070 GRE 显存容量 12GB 对 Qwen3-27B INT4 量化 (13.5GB) 的可行性分析：显存不足，无法加载模型，故 RX 9070 GRE 不可行

## Evidence

先验知识/题面给定，逻辑校验通过：12GB < 13.5GB，显存容量小于模型量化后大小，物理上无法加载，结论成立。

## Search Query

Qwen3-27B INT4 memory requirement 12GB insufficient
