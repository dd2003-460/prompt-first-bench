# N373: 信号质量溢价估值 V_signal 的量化计算：V_signal = k * ΔQuality_perception * P_ref。代入 k=0.6 和估计的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

信号质量溢价估值 V_signal 的量化计算：V_signal = k * ΔQuality_perception * P_ref。代入 k=0.6 和估计的 ΔQuality_perception=10-15%（取中值12.5%），若 P_ref=100元，则 V_signal = 0.6 * 0.125 * 100 = 7.5元。

## Corrected Claim

信号质量溢价估值 V_signal 的量化计算：V_signal = k * ΔQuality_perception * P_ref。代入 k=0.6 和估计的 ΔQuality_perception=10-15%（取中值12.5%），若 P_ref=100元，则 V_signal = 0.6 * 0.125 * 100 = 7.5元。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 V_signal = k * ΔQuality_perception * P_ref 代入 k=0.6, Δ=0.125, P_ref=100 计算得 7.5，数值量级与算术逻辑自洽。
