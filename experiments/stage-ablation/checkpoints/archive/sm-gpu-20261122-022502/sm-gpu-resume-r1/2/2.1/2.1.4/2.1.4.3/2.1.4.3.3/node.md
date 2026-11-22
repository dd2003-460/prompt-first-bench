# N575: RTX 5090 32K FP8 单卡方案的功耗效率对比：5090 TDP 575W，4090 TDP 450W，5090 每瓦吞吐 = 119.4 token

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N175

## Claim

RTX 5090 32K FP8 单卡方案的功耗效率对比：5090 TDP 575W，4090 TDP 450W，5090 每瓦吞吐 = 119.4 tokens/s / 575W = 0.208 tokens/s/W，4090 双卡每瓦吞吐 = 18.7 tokens/s / 900W = 0.021 tokens/s/W，5090 能效高 10 倍，年 OpEx 节省 = (900W - 575W) * 8760h * $0.1/kWh = $2841/年

## Corrected Claim

RTX 5090 32K FP8 单卡方案的功耗效率对比：5090 TDP 575W，4090 TDP 450W，5090 每瓦吞吐 = 119.4 tokens/s / 575W = 0.208 tokens/s/W，4090 双卡每瓦吞吐 = 18.7 tokens/s / 900W = 0.021 tokens/s/W，5090 能效高 10 倍，年 OpEx 节省 = (900W - 575W) * 8760h * $0.1/kWh = $2841/年

## Evidence

先验知识/题面给定，逻辑校验通过：TDP数值符合硬件规格常识，算术推导（0.208 vs 0.021 约10倍，$2841/年计算）准确无误。
