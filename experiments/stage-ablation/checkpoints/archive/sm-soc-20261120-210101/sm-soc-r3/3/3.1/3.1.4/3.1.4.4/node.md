# N231: 搜索路径截断效应修正：若买家在点击第 k 次后直接下单，则 L_search 被低估；需引入‘有效点击’定义（排除返回/刷新），并计算截断比例 R_trunc 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

搜索路径截断效应修正：若买家在点击第 k 次后直接下单，则 L_search 被低估；需引入‘有效点击’定义（排除返回/刷新），并计算截断比例 R_trunc = (总点击 - 有效点击) / 总点击，若 R_trunc > 10%，则 L_search 需修正为 L_adj = L_raw / (1 - R_trunc)。

## Corrected Claim

搜索路径截断效应修正：若买家在点击第 k 次后直接下单，则 L_search 可能被低估；需引入‘有效点击’定义（排除返回/刷新），并计算截断比例 R_trunc。若 R_trunc > 10%，建议通过敏感性分析或基于转化概率加权的模型来修正 L_search，而非简单使用 L_adj = L_raw / (1 - R_trunc)。

## Evidence

[质询]该修正公式 L_adj = L_raw / (1 - R_trunc) 隐含假设了“被截断的点击（返回/刷新）与有效点击具有相同的转化概率”，这在逻辑上是不成立的。通常，返回/刷新行为往往暗示用户犹豫或不满，其转化概率可能低于有效点击，或者这些点击本身并不构成完整的搜索路径，直接除以 (1-R) 可能会高估或低估真实的搜索路径长度，缺乏理论依据。 | 经验事实/方法论假设，逻辑自洽但缺乏来源支持，且修正公式的假设存在争议

## Search Query

click path truncation bias correction e-commerce user behavior
