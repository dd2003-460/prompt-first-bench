# N314: 计算高挂价策略 $S_{high}$ 的期望收益项 $E[Revenue|S_{high}]$。公式为 $E[Revenue|S_{high}] = P_{se

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

计算高挂价策略 $S_{high}$ 的期望收益项 $E[Revenue|S_{high}]$。公式为 $E[Revenue|S_{high}] = P_{sell}^{high} \times P_{success}^{high}$，其中 $P_{sell}^{high} = 1.2 P_{ref}$，$P_{success}^{high}$ 为高挂价下的成交概率。需量化 $P_{success}^{high}$ 与 $P_{success}^{mut}$（正常定价）的比值，若比值 $< 1/1.2$，则收益项不足以支撑 ESS。[待核验] 需基于历史数据估算不同溢价率下的成交率曲线。

## Corrected Claim

计算高挂价策略 $S_{high}$ 的期望收益项 $E[Revenue|S_{high}]$。通常公式为 $E[Revenue|S_{high}] = Price_{high} \times P_{success}^{high}$。若 $Price_{high} = 1.2 \times Price_{ref}$，则需量化 $P_{success}^{high}$ 与 $P_{success}^{mut}$ 的比值。若比值 $< 1/1.2$，则期望收益低于正常定价策略，不足以支撑 ESS。需基于历史数据估算不同溢价率下的成交率曲线。

## Evidence

[质询]公式定义存在量纲与逻辑混淆：期望收益（Revenue）通常应为 价格 × 成交概率，而陈述中将其定义为两个概率的乘积（P_sell × P_success），且 P_sell 被定义为参考概率的倍数，这在经济学直觉上是不成立的（概率不能直接作为收益的乘数，除非 P_sell 实际指代价格倍数，但符号命名具有误导性）。此外，缺乏具体数据支持 1/1.2 这一阈值的有效性。 | 无可用外部证据；逻辑校验发现公式量纲/定义不自洽（收益项不应仅为概率乘积，且 P_sell 定义模糊），属于经验/模型设定事实，缺乏来源支持且存在内部逻辑瑕疵。

## Search Query

used goods market transaction probability vs asking price premium empirical data
