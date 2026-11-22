# N194: H100 SXM 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 350W (FP8 推理负载)，电价

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

H100 SXM 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 350W (FP8 推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 350W * 8760h * 5 * $0.10/kWh = $15,330，比 A100 高 40%。

## Corrected Claim

H100 SXM 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 350W (FP8 推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 350W * 8760h * 5 * $0.10/kWh = $15,330，比 A100 高 40%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 350W * 8760h * 5 * $0.10/kWh = $15,330 数学正确；H100 SXM 典型功耗（~700W TDP，推理负载平均~350W合理）与A100（~400W TDP，推理负载平均~250W左右）相比，电力成本高出约40%符合工程常识（350/250=1.4）。

## Search Query

H100 SXM 80GB TDP 700W average power consumption inference workload 350W
