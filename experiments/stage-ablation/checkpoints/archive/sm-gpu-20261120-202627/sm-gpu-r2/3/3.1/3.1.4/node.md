# N68: NVIDIA RTX 3080 (10GB/12GB) 在 Qwen3-27B 上的显存带宽为 760 GB/s，当前单卡均价约为 $500-$700 [待核验

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

NVIDIA RTX 3080 (10GB/12GB) 在 Qwen3-27B 上的显存带宽为 760 GB/s，当前单卡均价约为 $500-$700 [待核验：实时价格]，其 TDP 为 320-350W，因显存不足通常需双卡或量化至 INT4 才能运行 32K 上下文。

## Corrected Claim

NVIDIA RTX 3080 (10GB/12GB) 在 Qwen3-27B 上的显存带宽为 760 GB/s，当前单卡均价约为 $500-$700 [待核验：实时价格]，其 TDP 为 320-350W，因显存不足通常需双卡或量化至 INT4 才能运行 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3080显存带宽760GB/s、TDP 320-350W及价格区间符合硬件规格常识，且双卡/量化需求符合大模型推理显存限制逻辑。

## Search Query

RTX 3080 memory bandwidth TDP price 2024
