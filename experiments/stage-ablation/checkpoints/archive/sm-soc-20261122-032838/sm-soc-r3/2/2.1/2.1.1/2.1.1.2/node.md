# N157: 持有成本 $C_{hold}$ 的时间函数：$C_{hold} = C_{storage} + C_{opportunity} \cdot T_{sale}$。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

持有成本 $C_{hold}$ 的时间函数：$C_{hold} = C_{storage} + C_{opportunity} \cdot T_{sale}$。其中 $C_{storage}$ 为固定仓储/空间成本（元/月），$C_{opportunity}$ 为资金占用的机会成本率（年化无风险利率 $r_f$ 除以 365）。若 $r_f = 3\%$，则每延长 1 天持有，$C_{opportunity}$ 增加 $P_{ref} \times 0.03 / 365$。

## Corrected Claim

持有成本 $C_{hold}$ 的时间函数：$C_{hold} = C_{storage} + C_{opportunity} \cdot T_{sale}$。其中 $C_{storage}$ 为固定仓储/空间成本（元/月），$C_{opportunity}$ 为资金占用的机会成本率（年化无风险利率 $r_f$ 除以 365）。若 $r_f = 3\%$，则每延长 1 天持有，$C_{opportunity}$ 增加 $P_{ref} \times 0.03 / 365$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合持有成本定义，年化利率除以365转换为日利率的数学推导正确，量纲一致。
