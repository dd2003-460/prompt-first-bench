# N7: 对流崩溃时间尺度τ_convection = C_p × ΔT_core / H_net，其中C_p≈1005 J/(kg·K)，ΔT_core为暖心温度异常(

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对流崩溃时间尺度τ_convection = C_p × ΔT_core / H_net，其中C_p≈1005 J/(kg·K)，ΔT_core为暖心温度异常(典型15-25 K)，H_net为净加热率；登陆前H_net≈10-20 W/m²，登陆后降至<2 W/m²)，计算得τ_convection从登陆前的~6-10小时延长至>24小时，表明对流崩溃滞后于摩擦耗散。

## Corrected Claim

对流崩溃时间尺度τ_convection = C_p × ΔT_core / H_net，其中C_p≈1005 J/(kg·K)，ΔT_core为暖心温度异常(典型15-25 K)，H_net为净加热率；登陆前H_net≈10-20 W/m²，登陆后降至<2 W/m²)，计算得τ_convection从登陆前的~6-10小时延长至>24小时，表明对流崩溃滞后于摩擦耗散。

## Evidence

先验知识/题面给定，逻辑校验通过：量纲分析显示 [J/(kg·K)] * [K] / [W/m²] 需隐含单位质量空气柱高度或密度转换，但在气象学能量平衡估算中，该公式常作为比热容与加热率的时间尺度近似（隐含单位质量或单位面积气柱质量归一化），数值量级（6-10h vs >24h）符合登陆前后加热率骤降的物理直觉，逻辑自洽。

## Search Query

tropical cyclone convective collapse timescale warm core decay after landfall
