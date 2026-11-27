# N380: Intel Gaudi 2 的电力成本动态修正：Decode 阶段功耗约为 TDP (500W) 的 60-70%（约 300-350W），Prefill 阶段

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N149

## Claim

Intel Gaudi 2 的电力成本动态修正：Decode 阶段功耗约为 TDP (500W) 的 60-70%（约 300-350W），Prefill 阶段接近 TDP。若工作负载为 50% Decode / 50% Prefill，加权平均功耗 P_avg ≈ 425W。3 年电费成本修正为 425W × 8760h × 3y × $0.12/kWh ≈ $1,498.44，相比恒定 TDP 假设 ($1,587.84) 节省约 $89.40。

## Corrected Claim

Intel Gaudi 2 的电力成本动态修正：Decode 阶段功耗约为 TDP (500W) 的 60-70%（约 300-350W），Prefill 阶段接近 TDP。若工作负载为 50% Decode / 50% Prefill，加权平均功耗 P_avg ≈ 425W。3 年电费成本修正为 425W × 8760h × 3y × $0.12/kWh ≈ $1,498.44，相比恒定 TDP 假设 ($1,587.84) 节省约 $89.40。

## Search Query

Intel Gaudi 2 power consumption decode vs prefill
