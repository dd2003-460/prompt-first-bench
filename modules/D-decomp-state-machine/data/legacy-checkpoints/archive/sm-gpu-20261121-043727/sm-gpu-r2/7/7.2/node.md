# N90: NVIDIA H100 SXM 年电力成本计算：TDP 700W = 0.7 kW，24/7 满载年耗电量 = 0.7 kW * 8760 h = 6132 k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

NVIDIA H100 SXM 年电力成本计算：TDP 700W = 0.7 kW，24/7 满载年耗电量 = 0.7 kW * 8760 h = 6132 kWh，电价 $0.1/kWh，年电费 = $613.2。修正负载因子 (80%) 后，年电费约为 $490.56。H100 的每 token 电力成本显著高于 RTX 4090，但需结合吞吐率计算每 token 成本。

## Corrected Claim

NVIDIA H100 SXM 年电力成本计算：TDP 700W = 0.7 kW，24/7 满载年耗电量 = 0.7 kW * 8760 h = 6132 kWh，电价 $0.1/kWh，年电费 = $613.2。修正负载因子 (80%) 后，年电费约为 $490.56。H100 的每 token 电力成本显著高于 RTX 4090，但需结合吞吐率计算每 token 成本。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W 为公开规格，数学计算 0.7*8760*0.1=613.2 及 613.2*0.8=490.56 准确无误，量纲与逻辑自洽。
