# N578: 基于峰值功耗 1800W 和 80 Plus Titanium 认证在 20% 负载下的效率约 85-90%，计算所需电源额定功率：P_rated = P_pe

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N241

## Claim

基于峰值功耗 1800W 和 80 Plus Titanium 认证在 20% 负载下的效率约 85-90%，计算所需电源额定功率：P_rated = P_peak / Efficiency_20% ≈ 1800W / 0.85 ≈ 2118W，因此 1600W 电源在极端峰值下可能触发电源过载保护（OCP），需验证 Corsair AX1600i 的 OCP 阈值是否 >2000W。

## Corrected Claim

基于峰值功耗 1800W 和 80 Plus Titanium 认证在 20% 负载下的效率约 85-90%，计算所需电源额定功率：P_rated = P_peak / Efficiency_20% ≈ 1800W / 0.85 ≈ 2118W，因此 1600W 电源在极端峰值下可能触发电源过载保护（OCP），需验证 Corsair AX1600i 的 OCP 阈值是否 >2000W。

## Evidence

先验知识/题面给定，逻辑校验通过：80 Plus Titanium 20%负载效率确为85-90%，1800W/0.85≈2118W计算正确，且1600W电源在2118W需求下确实会触发OCP，逻辑自洽。
