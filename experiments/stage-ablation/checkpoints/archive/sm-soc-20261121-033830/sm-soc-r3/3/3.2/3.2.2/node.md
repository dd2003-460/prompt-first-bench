# N61: “低咨询容忍度”的量化定义：卖家在挂价 P_high 下，若 48 小时内咨询数 N_consult < N_threshold，则不降价；N_threshol

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

“低咨询容忍度”的量化定义：卖家在挂价 P_high 下，若 48 小时内咨询数 N_consult < N_threshold，则不降价；N_threshold 应基于卖家时间成本 λ_s * 48h 与降价损失 (P_high - P_low) * P(sale|low) 的边际平衡点计算。

## Corrected Claim

“低咨询容忍度”可被建模为卖家在特定时间窗口（如48小时）内，当咨询量低于由时间成本与预期降价损失边际平衡决定的阈值 N_threshold 时，选择不降价的行为模式；该阈值的具体数值需结合卖家个体成本参数与市场动态确定。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 126 (char 192)

## Search Query

seller patience threshold second hand market listing duration consultation rate price reduction trigger
