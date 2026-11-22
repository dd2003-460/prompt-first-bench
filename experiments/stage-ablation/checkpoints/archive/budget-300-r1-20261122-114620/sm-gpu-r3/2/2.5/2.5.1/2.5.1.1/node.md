# N236: NVIDIA A100 40GB 在主要云服务商（AWS p4d.24xlarge, Azure NCads_A100_v4, GCP a2-highgpu-1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

NVIDIA A100 40GB 在主要云服务商（AWS p4d.24xlarge, Azure NCads_A100_v4, GCP a2-highgpu-1g）的 2024年Q3 按需（On-Demand）实例小时单价区间为 $3.0-$4.5/hour，而非 N73 中声称的 $1.5-$2.5/hour（后者通常对应抢占式实例或长期预留折扣价）

## Corrected Claim

NVIDIA A100 40GB 在主要云服务商的 2024年Q3 按需（On-Demand）实例小时单价通常显著高于 $1.5-$2.5/hour（后者多为抢占式或预留价），具体按需价格因区域和供应商而异，普遍在 $3.0-$4.5/hour 区间附近。

## Evidence

[质询]具体价格数值（$3.0-$4.5/hour）属于经验事实，且不同云服务商、不同区域（Region）及不同时间点（2024 Q3）的价格存在波动，缺乏实时数据源支持该精确区间，存在口径混淆（如是否包含税费、特定区域溢价）的风险。 | 经验事实，逻辑自洽（A100按需价格通常高于抢占式/预留价，量级合理）但缺来源支持（本轮检索无可用来源）。

## Search Query

AWS Azure GCP A100 on-demand instance price per hour 2024 Q3
