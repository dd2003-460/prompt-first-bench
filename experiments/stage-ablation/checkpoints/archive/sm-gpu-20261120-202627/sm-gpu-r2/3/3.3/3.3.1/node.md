# N74: AMD MI300X (192GB) 在 Qwen3-27B 上的显存带宽为 5300 GB/s，当前单卡采购均价约为 $15000-$20000 [待核验：实

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

AMD MI300X (192GB) 在 Qwen3-27B 上的显存带宽为 5300 GB/s，当前单卡采购均价约为 $15000-$20000 [待核验：实时价格]，其 TDP 为 750W，ROCm 软件栈对 Qwen 系列模型的支持成熟度需验证 [待核验：vLLM/ROCm 兼容性]。

## Corrected Claim

AMD MI300X (192GB) 在 Qwen3-27B 上的显存带宽为 5300 GB/s，其 TDP 为 750W。单卡采购均价需根据实时市场数据核实（通常高于 $15000-$20000 区间），ROCm 软件栈对 Qwen 系列模型的支持成熟度需验证。

## Evidence

[质询]单卡采购均价 $15000-$20000 严重偏离市场常识（MI300X 单卡市场价通常在 $30,000-$40,000 以上），且 ROCm 对 Qwen 的支持成熟度属于动态变化的经验事实，缺乏实时数据支撑。 | 先验知识/题面给定，逻辑校验通过：MI300X 的 192GB 显存、5.3TB/s 带宽及 750W TDP 符合 AMD 官方规格；但价格区间明显偏低（疑似混淆了二手价或特定渠道价，或量级错误），且软件栈兼容性为经验事实，无来源支持，故降级。

## Search Query

AMD MI300X memory bandwidth TDP price ROCm Qwen support
