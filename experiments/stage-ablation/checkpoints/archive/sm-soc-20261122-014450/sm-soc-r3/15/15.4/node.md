# N413: 降价导致 S_sig 暂时受损的幅度 ΔS_sig 需量化为 ΔS_sig = -γ * (ΔP/P)，其中 γ 为信号衰减系数，需基于历史数据回归确定，具体值

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N132

## Claim

降价导致 S_sig 暂时受损的幅度 ΔS_sig 需量化为 ΔS_sig = -γ * (ΔP/P)，其中 γ 为信号衰减系数，需基于历史数据回归确定，具体值需校准。

## Corrected Claim

降价可能导致 S_sig 暂时受损，其幅度 ΔS_sig 通常与价格变动率 (ΔP/P) 呈负相关，具体衰减系数 γ 需基于特定历史数据回归校准，不存在通用的固定公式。

## Evidence

[质询]该公式为经验性线性近似，缺乏第一性原理支持，且γ系数高度依赖具体市场环境和产品特性，无法通过逻辑推导确定其存在性或具体形式。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

signal decay coefficient gamma price drop S_sig reduction second hand seller
