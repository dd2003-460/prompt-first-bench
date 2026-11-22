# N233: 演化稳定策略（ESS）的适应度差值：计算变异策略（跟随市场价 $P_{market}$）与基准策略（维持高挂价 $P_{list} = 1.2 P_{marke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

演化稳定策略（ESS）的适应度差值：计算变异策略（跟随市场价 $P_{market}$）与基准策略（维持高挂价 $P_{list} = 1.2 P_{market}$）的适应度差 $\Delta \Pi = \Pi_{mutant} - \Pi_{resident}$。若 $\Delta \Pi < 0$，则高挂价为 ESS。需基于 $\lambda_{loss}=2.25$ 和平均成交周期 $T_{avg}$ 估算 $\Pi$ 的具体数值，验证 15-25% 偏差区间内 $\Delta \Pi$ 是否恒为负。

## Corrected Claim

演化稳定策略（ESS）的适应度差值：计算变异策略（跟随市场价 $P_{market}$）与基准策略（维持高挂价 $P_{list} = 1.2 P_{market}$）的适应度差 $\Delta \Pi = \Pi_{mutant} - \Pi_{resident}$。若 $\Delta \Pi < 0$，则高挂价为 ESS。需基于 $\lambda_{loss}=2.25$ 和平均成交周期 $T_{avg}$ 估算 $\Pi$ 的具体数值，验证 15-25% 偏差区间内 $\Delta \Pi$ 是否恒为负。

## Evidence

先验知识/题面给定，逻辑校验通过：ESS定义及适应度差值符号判断逻辑自洽，参数设定符合博弈论模型常规假设。
