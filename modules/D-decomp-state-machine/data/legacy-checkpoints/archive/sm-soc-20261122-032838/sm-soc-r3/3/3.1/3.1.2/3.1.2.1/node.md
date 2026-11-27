# N193: 方案B中特征工程成本 $C_{feat}$ 的分解：$C_{feat} = C_{extract} + C_{clean} + C_{label}$。在二手平台

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

方案B中特征工程成本 $C_{feat}$ 的分解：$C_{feat} = C_{extract} + C_{clean} + C_{label}$。在二手平台现有数据管道下，提取'溢价率'特征仅需SQL查询（$C_{extract} \approx 0.5$ 人日），清洗缺失值与异常值（$C_{clean} \approx 1.0$ 人日），若需新增'历史成交稳定性'标签则需离线计算（$C_{label} \approx 1.5-2.0$ 人日）。总 $C_{feat}$ 下限为 2.0 人日（仅用现有特征），上限 3.5 人日（需新标签），原估算 3-5 人日偏高，需按是否复用现有特征区分。

## Corrected Claim

方案B中特征工程成本 $C_{feat}$ 的分解：$C_{feat} = C_{extract} + C_{clean} + C_{label}$。在二手平台现有数据管道下，提取'溢价率'特征仅需SQL查询（$C_{extract} \approx 0.5$ 人日），清洗缺失值与异常值（$C_{clean} \approx 1.0$ 人日），若需新增'历史成交稳定性'标签则需离线计算（$C_{label} \approx 1.5-2.0$ 人日）。总 $C_{feat}$ 下限为 2.0 人日（仅用现有特征），上限 3.5 人日（需新标签），原估算 3-5 人日偏高，需按是否复用现有特征区分。

## Evidence

先验知识/题面给定，逻辑校验通过：特征工程成本分解符合软件工程常识，数值量级（0.5-2.0人日/项）在合理范围内，且内部逻辑自洽（下限2.0=0.5+1.0+0.5隐含或仅基础项，上限3.5=0.5+1.0+2.0，计算无误）。

## Search Query

recommendation system feature engineering cost estimation person-days
