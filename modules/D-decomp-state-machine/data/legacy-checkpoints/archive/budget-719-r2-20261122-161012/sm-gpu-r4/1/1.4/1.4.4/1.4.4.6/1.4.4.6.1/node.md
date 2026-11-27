# N414: H100 SXM 四卡服务器（如 Dell PowerEdge XE9680 配置 4x H100 SXM 或 NVIDIA DGX H100）的整机典型峰值功

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N171

## Claim

H100 SXM 四卡服务器（如 Dell PowerEdge XE9680 配置 4x H100 SXM 或 NVIDIA DGX H100）的整机典型峰值功耗约为 3200W-3600W（4x GPU 2800W + CPU 400-500W + 其他 200-300W），基于 1.5 倍冗余系数，推荐电源系统总容量为 4800W-5400W，标准配置为 4 个 2600W 或 2 个 5000W 钛金级 PSU（N+1 冗余），单模块价格约为 $500-$800，总电源模块硬件成本约为 $2,000-$3,200。

## Corrected Claim

H100 SXM 四卡服务器整机典型峰值功耗约为 3200W-3600W，基于冗余系数推荐电源系统总容量为 4800W-5400W，通常采用 N+1 冗余配置的高功率钛金级 PSU，具体模块规格与成本需依据特定厂商配置确定。

## Evidence

[质询]具体PSU型号（如2600W/5000W钛金）及价格区间（$500-$800）属于高度依赖具体供应商、采购时间和市场波动的经验事实，且不同厂商（Dell vs NVIDIA DGX）的电源架构差异巨大，无法从第一性原理推导，缺乏来源支持时存在较大不确定性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVIDIA DGX H100 power supply unit 4x 2600W price 4U server PSU cost
