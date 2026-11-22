# N286: 反制行为触发阈值：当预期收益损失 ΔR_seller > C_counter + C_reputation_loss 时，卖家才会采取反制行为；C_reputa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

反制行为触发阈值：当预期收益损失 ΔR_seller > C_counter + C_reputation_loss 时，卖家才会采取反制行为；C_reputation_loss = λ_reputation * P(Review_Negative | Countermeasure)，其中 λ_reputation 为声誉敏感系数，P(Review_Negative) 为负面评价概率，需结合历史数据估计。

## Corrected Claim

反制行为触发阈值：当预期收益损失 ΔR_seller > C_counter + C_reputation_loss 时，卖家才会采取反制行为；C_reputation_loss = λ_reputation * P(Review_Negative | Countermeasure)，其中 λ_reputation 为声誉敏感系数，P(Review_Negative) 为负面评价概率，需结合历史数据估计。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述构建了一个标准的理性决策模型，其中反制行为的触发条件（预期收益损失大于反制成本加声誉损失）符合经济学中的成本-收益分析逻辑，且声誉损失项的定义（敏感系数乘以负面评价概率）在量纲和逻辑上均自洽，无内部矛盾。

## Search Query

seller reputation loss threshold for countermeasure adoption
