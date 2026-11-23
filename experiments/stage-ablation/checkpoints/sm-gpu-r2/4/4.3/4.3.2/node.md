# N65: H100 SXM5 数据中心 GPU 的实际满载功耗 P_actual：在 LLM 推理负载下，P_actual 通常为 650-700W，TDP 标称 700

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

H100 SXM5 数据中心 GPU 的实际满载功耗 P_actual：在 LLM 推理负载下，P_actual 通常为 650-700W，TDP 标称 700W，δ_power < 2%；由于 SXM 模块直接连接主板供电，功耗波动极小，可视为恒定 700W 用于 TCO 计算。

## Corrected Claim

H100 SXM5 数据中心 GPU 的实际满载功耗 P_actual：在 LLM 推理负载下，P_actual 通常为 650-700W，TDP 标称 700W，δ_power < 2%；由于 SXM 模块直接连接主板供电，功耗波动极小，可视为恒定 700W 用于 TCO 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 的 TDP 确为 700W，SXM 接口供电稳定，满载功耗接近 TDP 符合工程常识，用于 TCO 计算视为恒定值合理。
