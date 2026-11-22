# N323: σ_function的估算公式为 σ_function = sqrt(Σ (P_config_i - P_avg_config)^2 / N_configs) 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

σ_function的估算公式为 σ_function = sqrt(Σ (P_config_i - P_avg_config)^2 / N_configs) * (1 / σ_total)，其中σ_total为总成交价标准差，该公式需通过特定商品类别的市场数据校准。

## Corrected Claim

σ_function 的估算可能涉及配置价格偏差与总价格波动的比值，但具体公式及校准方法需依据特定领域实证研究确定，当前表述缺乏通用理论或数据支持。

## Evidence

[质询]公式中除以 σ_total 的量纲和逻辑合理性存疑：σ_function 通常指函数/模型输出的标准差，若 P_config 是价格，其标准差量纲为货币单位，而 σ_total 也是货币单位，相除后无量纲，这与通常‘估算标准差’（应有货币单位）的直觉不符；且‘特定商品类别市场数据校准’属于经验性操作，缺乏通用理论支持。 | 经验事实，逻辑自洽但缺来源支持；公式量纲存在潜在矛盾（标准差除以标准差得到无量纲数，与‘估算标准差’的语义冲突），且无外部来源验证该特定校准公式。
