# N109: A100 80GB/H100 80GB/MI300X 192GB 单卡显存容量与 Qwen3-27B BF16 需求 (55GB) 的匹配度：A100/H100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

A100 80GB/H100 80GB/MI300X 192GB 单卡显存容量与 Qwen3-27B BF16 需求 (55GB) 的匹配度：A100/H100 剩余 25GB 可用于 Batch Size 扩展，MI300X 剩余 137GB 支持更大并发

## Corrected Claim

A100 80GB/H100 80GB/MI300X 192GB 单卡显存容量与 Qwen3-27B BF16 需求 (55GB) 的匹配度：A100/H100 剩余 25GB 可用于 Batch Size 扩展，MI300X 剩余 137GB 支持更大并发

## Evidence

先验知识/题面给定，逻辑校验通过：A100/H100 80GB - 55GB = 25GB，MI300X 192GB - 55GB = 137GB，数值计算准确且符合硬件规格常识。

## Search Query

A100 H100 MI300X VRAM capacity Qwen3-27B inference
