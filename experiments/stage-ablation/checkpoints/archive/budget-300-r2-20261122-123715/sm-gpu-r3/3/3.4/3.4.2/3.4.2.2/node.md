# N265: NVIDIA H100 SXM5 的 3 年故障概率 P_fail_3y 略高于 A100，估计为 3-6% (MTBF ≈ 50-100 年)，主要源于 HB

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

NVIDIA H100 SXM5 的 3 年故障概率 P_fail_3y 略高于 A100，估计为 3-6% (MTBF ≈ 50-100 年)，主要源于 HBM3 显存的高功耗密度 (TDP 700W) 导致的局部热点效应；在 TCO 模型中，C_failure 项需基于此 P_fail 与 H100 高昂的更换成本 ($25k+) 计算，通常高于 A100 的故障成本。

## Corrected Claim

NVIDIA H100 SXM5 的 3 年故障概率 P_fail_3y 估计为 3-6%（对应 MTBF 约 50-100 年，但实际数据中心 GPU MTBF 通常更低），主要源于 HBM3 显存的高功耗密度 (TDP 700W) 导致的局部热点效应；在 TCO 模型中，C_failure 项需基于此 P_fail 与 H100 高昂的更换成本 ($25k+) 计算，通常高于 A100 的故障成本。

## Evidence

[质询]MTBF 50-100年与3年故障率3-6%存在数量级矛盾（3年3-6%对应MTBF约50-100年，但通常数据中心GPU MTBF在数千小时级别，即数年，而非数十年；且H100 TDP 700W是SXM5规格，但局部热点导致故障率显著高于A100缺乏直接数据支持，属于经验推测） | 无可用外部证据；逻辑校验发现MTBF与故障率换算存在量级疑问（3年3-6%故障率对应MTBF约50-100年，但实际数据中心GPU MTBF通常远低于此，且H100故障率高于A100缺乏直接数据支持，属于经验事实且缺来源支持）

## Search Query

NVIDIA H100 SXM5 MTBF failure rate 3 year prediction HBM3 thermal stress
