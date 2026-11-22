# N692: RTX 5090 单卡满载功耗为 575W，在双卡配置下总 GPU 功耗为 1150W；结合 CPU (约 150W) 及平台其他组件 (约 100W)，系统总

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N286

## Claim

RTX 5090 单卡满载功耗为 575W，在双卡配置下总 GPU 功耗为 1150W；结合 CPU (约 150W) 及平台其他组件 (约 100W)，系统总功耗约为 1400W，因此必须配置 1600W 或更高功率的 80+ 白金/钛金电源。

## Corrected Claim

RTX 5090 单卡满载功耗为 575W，在双卡配置下总 GPU 功耗为 1150W；结合 CPU (约 150W) 及平台其他组件 (约 100W)，系统总功耗约为 1400W，因此必须配置 1600W 或更高功率的 80+ 白金/钛金电源。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 TDP 575W 符合 NVIDIA 官方规格，双卡 1150W + CPU/平台 250W = 1400W 总功耗计算正确，1600W 电源满足 80% 负载效率区间及峰值余量要求，逻辑自洽且数值量级合理。

## Search Query

RTX 5090 TDP 575W dual card power supply recommendation 1600W
