# N65: 重新挂价频率阈值量化：定义降价后重新挂价频率 R_relist = (降价后48h内修改价格或重新上架次数) / (总降价次数)。需确定基准阈值 Thresho

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

重新挂价频率阈值量化：定义降价后重新挂价频率 R_relist = (降价后48h内修改价格或重新上架次数) / (总降价次数)。需确定基准阈值 Threshold_relist，若 R_relist > 0.2 且显著高于未降价卖家的 R_relist，表明卖家在主动进行价格试探（Price Probing）而非被动等待。

## Corrected Claim

重新挂价频率阈值量化：定义降价后重新挂价频率 R_relist = (降价后48h内修改价格或重新上架次数) / (总降价次数)。需通过历史数据分布确定基准阈值 Threshold_relist（例如取未降价卖家 R_relist 分布的 P90 或固定经验值如 0.2），若 R_relist 显著高于该阈值（需结合统计显著性检验），表明卖家在主动进行价格试探（Price Probing）而非被动等待。

## Evidence

[质询]阈值 0.2 缺乏实证数据支持，属于经验性设定，且未定义“显著高于”的统计检验标准（如 p 值或置信区间），可能导致误判。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

seller price probing behavior relist frequency threshold second hand
