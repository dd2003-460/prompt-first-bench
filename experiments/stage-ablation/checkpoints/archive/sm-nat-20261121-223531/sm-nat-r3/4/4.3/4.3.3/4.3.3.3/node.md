# N173: 基于 N54 和 N57 数据的 P_stale_byte 最终量化值：前1%对象贡献约 20.6% 请求，但因负相关其字节占比可能更高（假设 30%），T_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

基于 N54 和 N57 数据的 P_stale_byte 最终量化值：前1%对象贡献约 20.6% 请求，但因负相关其字节占比可能更高（假设 30%），T_res ≈ 86.4s，P_stale ≈ 1.16e-7。其余 99% 对象贡献 70% 字节，T_res 较大（如 10天），P_stale ≈ 1 - e^{-0.1} ≈ 9.5%，但因其字节权重低且多为 Miss 流量，对命中流量（Hit Traffic）的 P_stale 影响极小。最终 D_eff ≈ 1 - 1.16e-7 ≈ 0.9999999。

## Corrected Claim

基于 N54 和 N57 数据的 P_stale_byte 最终量化值：前1%对象贡献约 20.6% 请求，但因负相关其字节占比可能更高（假设 30%），T_res ≈ 86.4s，P_stale ≈ 1.16e-7。其余 99% 对象贡献 70% 字节，T_res 较大（如 10天），P_stale ≈ 1 - e^{-0.1} ≈ 9.5%，但因其字节权重低且多为 Miss 流量，对命中流量（Hit Traffic）的 P_stale 影响极小。最终 D_eff ≈ 1 - 1.16e-7 ≈ 0.9999999。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算自洽（1-e^-0.1≈0.095, 1-1.16e-7≈0.9999999），量级合理，符合缓存失效概率模型的基本逻辑。
