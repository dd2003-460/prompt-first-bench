# N20: 断言A3（干预代价）：最小干预措施M（强制披露近期成交价）对卖家利益的伤害量化为：卖家预期收益损失ΔR = (P_list - P_clear) * Q_los

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

断言A3（干预代价）：最小干预措施M（强制披露近期成交价）对卖家利益的伤害量化为：卖家预期收益损失ΔR = (P_list - P_clear) * Q_loss，其中Q_loss为因透明化导致的咨询量下降比例，若60%卖家降价后48h无咨询，则Q_loss ≈ 0.6 * (1 - P_consult_after_disclosure)，该式需代入P_consult_after_disclosure的估计值[待核验]

## Corrected Claim

断言A3（干预代价）：最小干预措施M对卖家利益的伤害量化为：卖家预期收益损失ΔR = (P_list - P_clear) * Q_base * Q_loss_ratio，其中Q_base为基准咨询量，Q_loss_ratio为因透明化导致的咨询量下降比例。若60%卖家降价后48h无咨询，需进一步估计P_consult_after_disclosure以推导Q_loss_ratio，当前公式量纲需修正。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 744)

## Search Query

price transparency intervention impact on seller inquiry rate second hand market 48 hour window
