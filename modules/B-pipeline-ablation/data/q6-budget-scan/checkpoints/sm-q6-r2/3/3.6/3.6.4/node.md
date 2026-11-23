# N116: C_bandwidth_download 的计算公式：若采用按峰值计费，C_bandwidth_download = B_peak * p_peak；若采用按带

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

C_bandwidth_download 的计算公式：若采用按峰值计费，C_bandwidth_download = B_peak * p_peak；若采用按带宽包计费，C_bandwidth_download = N_package * p_package；其中 B_peak 需基于流量分布模型计算，通常 B_peak ≈ 2-3 * V_daily / 86400 * 86400 / 3600 (Mbps) [待核验]

## Corrected Claim

C_bandwidth_download 的计算公式：若采用按峰值计费，C_bandwidth_download = B_peak * p_peak；若采用按带宽包计费，C_bandwidth_download = N_package * p_package；其中 B_peak 需基于具体流量分布模型（如 Poisson 或 Pareto 分布）估算，通常 B_peak 与日均流量 V_daily 的关系取决于业务特征，不能简单用固定系数 2-3 乘以单位换算得出。

## Evidence

[质询]公式中 B_peak ≈ 2-3 * V_daily / 86400 * 86400 / 3600 存在严重的量纲错误和逻辑冗余。V_daily 若为总流量（如 GB），除以 86400 得到平均速率，再乘以 86400 又变回总流量，最后除以 3600 得到的是每小时平均流量，而非峰值带宽（Mbps）。此外，峰值带宽与日均流量的比例系数（2-3）高度依赖于业务类型（如视频流媒体 vs 文件下载），将其作为通用常数缺乏严谨性。 | 先验知识/题面给定，但逻辑校验发现公式量纲混乱且系数缺乏普适性，无法直接判定为 verified。
