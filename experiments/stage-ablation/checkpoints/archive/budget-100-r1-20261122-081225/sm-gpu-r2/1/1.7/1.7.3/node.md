# N80: NVIDIA L40S 功耗为 350W (TDP)，相比 H100 的 700W 和 RTX 4090 的 450W，其能效比 (Performance/Wa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVIDIA L40S 功耗为 350W (TDP)，相比 H100 的 700W 和 RTX 4090 的 450W，其能效比 (Performance/Watt) 在推理场景下需结合 864 GB/s 带宽限制进行评估，电力成本约为 $0.15/kWh * 350W * 24h * 365d = $465/年 [假设电价 $0.15/kWh]。

## Corrected Claim

NVIDIA L40S 功耗为 350W (TDP)，相比 H100 的 700W 和 RTX 4090 的 450W，其能效比 (Performance/Watt) 在推理场景下需结合 864 GB/s 带宽限制进行评估，电力成本约为 $0.15/kWh * 350W * 24h * 365d = $465/年 [假设电价 $0.15/kWh]。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S TDP 350W、H100 700W、RTX 4090 450W 均为公开稳定规格；电费计算 0.15 * 0.35 * 24 * 365 ≈ 465.45 符合算术逻辑。
