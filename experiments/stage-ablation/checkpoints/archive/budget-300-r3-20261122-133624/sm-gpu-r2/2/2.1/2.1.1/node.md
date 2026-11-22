# N67: 单卡 BF16 方案的硬件成本 C_hw 需细分：RTX 6000 Ada (48GB) 全新价格约为 $6800，H100 PCIe (80GB) 全新价格约

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

单卡 BF16 方案的硬件成本 C_hw 需细分：RTX 6000 Ada (48GB) 全新价格约为 $6800，H100 PCIe (80GB) 全新价格约为 $25000，A100 80GB 二手价格约为 $8000-$12000；不同硬件的折旧率（3 年直线折旧）影响 TCO 中的残值计算，通常取 20-30% 残值率。

## Corrected Claim

单卡 BF16 方案的硬件成本 C_hw 需细分：RTX 6000 Ada (48GB)、H100 PCIe (80GB) 及 A100 80GB 二手卡的市场价格存在显著差异，通常 H100 价格远高于 RTX 6000 Ada，A100 二手价格介于两者之间或更低；不同硬件的折旧率（3 年直线折旧）影响 TCO 中的残值计算，通常取 20-30% 残值率。

## Evidence

[质询]具体硬件价格（如RTX 6000 Ada $6800, H100 $25000, A100二手 $8000-$12000）属于高度波动的市场经验数据，且不同渠道、时间、地区价格差异巨大，缺乏实时市场数据支持，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），具体价格数值无法通过第一性原理推导，需降级为定性表述。

## Search Query

RTX 6000 Ada price 2024 H100 PCIe price A100 80GB used price 2024
