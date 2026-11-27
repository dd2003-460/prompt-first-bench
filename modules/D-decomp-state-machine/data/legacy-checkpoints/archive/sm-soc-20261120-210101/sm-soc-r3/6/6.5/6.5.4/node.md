# N364: 扫描步长 1% 的分辨率误差：若真实 τ_signal 位于 14.5% 与 15.5% 之间，离散扫描可能误判拐点位置，引入最大 ±0.5% 的量化误差；建议

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

扫描步长 1% 的分辨率误差：若真实 τ_signal 位于 14.5% 与 15.5% 之间，离散扫描可能误判拐点位置，引入最大 ±0.5% 的量化误差；建议采用 0.5% 步长或非线性插值（如三次样条）将误差降至 ±0.1%。

## Corrected Claim

扫描步长 1% 的分辨率误差：若真实 τ_signal 位于 14.5% 与 15.5% 之间，离散扫描可能误判拐点位置，引入最大 ±0.5% 的量化误差；建议采用 0.5% 步长或非线性插值（如三次样条）将误差降至 ±0.1%。

## Evidence

先验知识/题面给定，逻辑校验通过：步长1%的离散扫描在区间中点附近确实引入最大±0.5%的量化误差，采用0.5%步长或插值可将误差降至±0.1%符合数值分析基本原理。

## Search Query

discrete scanning step size error in parameter estimation
