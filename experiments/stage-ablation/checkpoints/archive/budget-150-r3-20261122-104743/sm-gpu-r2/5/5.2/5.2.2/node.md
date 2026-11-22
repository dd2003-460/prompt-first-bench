# N152: NVIDIA A100 SXM4 显存带宽为 2039 GB/s，显存容量 80GB，不支持 FP8 计算单元（Ampere 架构），仅支持 BF16/INT8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

NVIDIA A100 SXM4 显存带宽为 2039 GB/s，显存容量 80GB，不支持 FP8 计算单元（Ampere 架构），仅支持 BF16/INT8 量化，单卡 BF16 27B 模型推理可行，剩余显存 26GB 可用于 KV Cache

## Corrected Claim

NVIDIA A100 SXM4 显存带宽为 2039 GB/s，显存容量 80GB，不支持 FP8 计算单元（Ampere 架构），仅支持 BF16/INT8 量化，单卡 BF16 27B 模型推理可行，剩余显存 26GB 可用于 KV Cache

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 带宽 2039 GB/s 与 80GB 容量符合官方规格；Ampere 架构确实不支持原生 FP8（Hopper 引入）；27B 模型 BF16 权重约 54GB，剩余 26GB 显存用于 KV Cache 计算合理。
