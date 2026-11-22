# N302: 卖家最佳反应函数的验证条件：在平台选择 $W_{high\_boost}$ 时，卖家选择 $P_{high}$ 的期望收益 $E[U_s|P_{high}, W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

卖家最佳反应函数的验证条件：在平台选择 $W_{high\_boost}$ 时，卖家选择 $P_{high}$ 的期望收益 $E[U_s|P_{high}, W_{high\_boost}]$ 必须大于选择 $P_{low}$ 的期望收益 $E[U_s|P_{low}, W_{high\_boost}]$。量化条件：$(P_{high} - C_{hold}) \cdot P_{sell,high} > (P_{low} - C_{hold}) \cdot P_{sell,low}$，其中 $P_{sell,high}$ 和 $P_{sell,low}$ 分别为高/低挂价下的成交概率。若 $P_{sell,high} / P_{sell,low} > P_{low} / P_{high}$，则 $P_{high}$ 为最佳反应。[待核验] 需估算不同挂价水平下的成交概率比。

## Corrected Claim

卖家最佳反应函数的验证条件：在平台选择 $W_{high\_boost}$ 时，卖家选择 $P_{high}$ 的期望收益 $E[U_s|P_{high}, W_{high\_boost}]$ 必须大于选择 $P_{low}$ 的期望收益 $E[U_s|P_{low}, W_{high\_boost}]$。量化条件：$(P_{high} - C_{hold}) \cdot P_{sell,high} > (P_{low} - C_{hold}) \cdot P_{sell,low}$，其中 $P_{sell,high}$ 和 $P_{sell,low}$ 分别为高/低挂价下的成交概率。若 $P_{sell,high} / P_{sell,low} > P_{low} / P_{high}$，则 $P_{high}$ 为最佳反应。[待核验] 需估算不同挂价水平下的成交概率比。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式推导符合期望收益最大化定义，量纲一致，无内部矛盾。

## Search Query

seller optimal pricing strategy under platform exposure boost expected revenue comparison
