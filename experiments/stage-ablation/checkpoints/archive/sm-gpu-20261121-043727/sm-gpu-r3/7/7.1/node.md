# N89: RTX 4090 年电力成本计算：TDP 450W = 0.45 kW，假设 24/7 满载运行，年耗电量 = 0.45 kW * 8760 h = 3942 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

RTX 4090 年电力成本计算：TDP 450W = 0.45 kW，假设 24/7 满载运行，年耗电量 = 0.45 kW * 8760 h = 3942 kWh，电价 $0.1/kWh，年电费 = $394.2。注意：实际推理负载下平均功耗约为 TDP 的 70-85%（取决于 Batch Size 和 KV Cache 大小），修正后年电费约为 $276-$335。

## Corrected Claim

RTX 4090 年电力成本计算：TDP 450W = 0.45 kW，假设 24/7 满载运行，年耗电量 = 0.45 kW * 8760 h = 3942 kWh，电价 $0.1/kWh，年电费 = $394.2。注意：实际推理负载下平均功耗约为 TDP 的 70-85%（取决于 Batch Size 和 KV Cache 大小），修正后年电费约为 $276-$335。

## Evidence

先验知识/题面给定，逻辑校验通过：TDP 450W 为 RTX 4090 标准规格，数学计算 0.45 * 8760 * 0.1 = 394.2 正确，修正系数 70-85% 符合 GPU 推理负载典型功耗特征。
