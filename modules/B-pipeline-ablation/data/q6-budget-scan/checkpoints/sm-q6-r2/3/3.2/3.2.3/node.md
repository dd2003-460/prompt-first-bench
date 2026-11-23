# N71: 每机柜功耗 $E_{power}$ 由服务器 TDP 和网络设备功耗组成：10 台服务器（每台 300W）+ 交换机（200W）= 3.2 kW；考虑电源效率（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

每机柜功耗 $E_{power}$ 由服务器 TDP 和网络设备功耗组成：10 台服务器（每台 300W）+ 交换机（200W）= 3.2 kW；考虑电源效率（PUE 1.5），实际机房功耗约为 4.8 kW，取 $E_{power} = 5$ kW/机柜。

## Corrected Claim

每机柜功耗 $E_{power}$ 由服务器 TDP 和网络设备功耗组成：10 台服务器（每台 300W）+ 交换机（200W）= 3.2 kW；考虑电源效率（PUE 1.5），实际机房功耗约为 4.8 kW，取 $E_{power} = 5$ kW/机柜。

## Evidence

先验知识/题面给定，逻辑校验通过：10*300W + 200W = 3200W = 3.2kW，3.2kW * 1.5 = 4.8kW，取整为5kW，计算与工程惯例一致。
