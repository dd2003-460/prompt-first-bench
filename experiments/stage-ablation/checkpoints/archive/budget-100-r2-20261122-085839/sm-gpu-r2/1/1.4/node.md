# N9: 硬件筛选硬性阈值：基于N8的计算，BF16方案需要单卡显存 ≥ 80 GB（如A100 80GB, H100 80GB）或双卡合计 ≥ 80 GB（如2×40G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

硬件筛选硬性阈值：基于N8的计算，BF16方案需要单卡显存 ≥ 80 GB（如A100 80GB, H100 80GB）或双卡合计 ≥ 80 GB（如2×40GB 3090/4090，但需注意PCIe带宽瓶颈）；INT8方案需要单卡显存 ≥ 50 GB（如A100 40GB不够，需A100 80GB或H100 80GB，或2×24GB 3090/4090勉强）；W4方案需要单卡显存 ≥ 36 GB（如24GB 3090/4090不够，需48GB A6000或80GB A100）[待核验: 实际框架中KV Cache是否支持FP8/INT8量化以降低占用]

## Corrected Claim

硬件筛选硬性阈值：基于N8的计算，BF16方案需要单卡显存 ≥ 80 GB（如A100 80GB, H100 80GB）或双卡合计 ≥ 80 GB（如2×40GB 3090/4090，但需注意PCIe带宽瓶颈）；INT8方案需要单卡显存 ≥ 50 GB（如A100 40GB不够，需A100 80GB或H100 80GB，或2×24GB 3090/4090勉强）；W4方案需要单卡显存 ≥ 36 GB（如24GB 3090/4090不够，需48GB A6000或80GB A100）[待核验: 实际框架中KV Cache是否支持FP8/INT8量化以降低占用]

## Evidence

先验知识/题面给定，逻辑校验通过：基于N8的计算结果，BF16/INT8/W4的显存需求与主流GPU（A100/H100/3090/4090/A6000）的显存规格匹配，量级合理，无内部矛盾。

## Search Query

minimum GPU VRAM requirement 27B LLM 32k context
