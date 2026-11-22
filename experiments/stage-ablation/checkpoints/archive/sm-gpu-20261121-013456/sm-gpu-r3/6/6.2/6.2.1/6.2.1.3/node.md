# N248: 2×RTX 4090 与 1×A100 方案在 3 年周期内的精确 TCO 公式：TCO = (Hardware_Cost + Maintenance_Cost

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

2×RTX 4090 与 1×A100 方案在 3 年周期内的精确 TCO 公式：TCO = (Hardware_Cost + Maintenance_Cost) / N + (Power_Draw_kW * 8760h * N * Electricity_Rate_$kWh)，需代入各自实测功耗（4090~450W, A100~400W）及当前市场价。

## Corrected Claim

2×RTX 4090 与 1×A100 方案在 3 年周期内的 TCO 公式应为：TCO = Hardware_Cost + (Maintenance_Cost * N) + (Power_Draw_kW * 8760h * N * Electricity_Rate_$kWh)，需代入各自实测功耗（4090~450W, A100~400W）及当前市场价。

## Evidence

[质询]TCO公式存在严重的逻辑与量纲错误：1. 硬件成本通常是一次性投入，不应除以N（年限）后再与总电力成本相加，这导致硬件成本被错误地缩小了N倍；2. 电力成本项中 `Power_Draw_kW * 8760h * N` 计算的是N年的总电费，而硬件项 `(Hardware_Cost + Maintenance_Cost) / N` 计算的是年均成本，两者量纲/时间基准不一致（年均 vs 总周期），无法直接相加得出'3年周期内的精确TCO'。 | 先验知识/题面给定，逻辑校验失败：公式中硬件成本项（年均）与电力成本项（总周期）时间基准不一致，且硬件成本不应简单除以年限后与总电费相加，存在硬逻辑错误。
