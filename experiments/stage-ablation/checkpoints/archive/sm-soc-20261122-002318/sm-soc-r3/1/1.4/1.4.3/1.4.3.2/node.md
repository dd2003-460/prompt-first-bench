# N127: t_avg 的实证分解：平均单次搜索决策时间 t_avg 包含浏览时间 t_browse 和比较时间 t_compare，t_avg = t_browse + 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N43

## Claim

t_avg 的实证分解：平均单次搜索决策时间 t_avg 包含浏览时间 t_browse 和比较时间 t_compare，t_avg = t_browse + t_compare；在二手平台中，t_browse ≈ 30-60s，t_compare ≈ 60-120s，总 t_avg ≈ 90-180s，需根据用户行为日志校准。

## Corrected Claim

t_avg 的实证分解：平均单次搜索决策时间 t_avg 包含浏览时间 t_browse 和比较时间 t_compare，t_avg = t_browse + t_compare；在二手平台中，t_browse 和 t_compare 的具体数值需根据特定品类和用户行为日志进行校准，典型量级可能在数十秒至数分钟之间。

## Evidence

[质询]数值量级缺乏普适性：30-60s的浏览时间和60-120s的比较时间属于特定场景下的经验估计，不同品类（如手机vs家具）、用户熟练度及平台UI设计会导致显著差异，直接作为通用常数存在过度概括风险。 | source=knowledge，逻辑自洽（加法分解合理），但具体数值为经验估计，缺乏普适性证据支持，依据经验事实排除条款降级。

## Search Query

average decision time search browsing comparison secondhand
