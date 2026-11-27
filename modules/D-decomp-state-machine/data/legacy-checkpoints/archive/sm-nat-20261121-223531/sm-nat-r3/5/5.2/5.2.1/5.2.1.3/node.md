# N184: LFU 增益 $\Delta H$ 的下界估计：即使 LFU 无法完美区分热度，只要其保留策略优于随机，在 $\beta=0.9$ 的极偏斜分布下，LFU 至少

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

LFU 增益 $\Delta H$ 的下界估计：即使 LFU 无法完美区分热度，只要其保留策略优于随机，在 $\beta=0.9$ 的极偏斜分布下，LFU 至少保留前 $K\%$ 对象。若 $K=1\%$，请求覆盖率 $P_{req} = 1 - 0.01^{0.1} \approx 36.9\%$（修正 N73 错误），结合负相关 $\rho=-0.3$，字节命中率下界约为 $36.9\% \times (E[S|Top1\%]/E[S])$。

## Corrected Claim

LFU 增益 $\Delta H$ 的下界估计：即使 LFU 无法完美区分热度，只要其保留策略优于随机，在 $\beta=0.9$ 的极偏斜分布下，LFU 至少保留前 $K\%$ 对象。若 $K=1\%$，请求覆盖率 $P_{req} = 1 - 0.01^{0.1} \approx 36.9\%$（修正 N73 错误），结合负相关 $\rho=-0.3$，字节命中率下界约为 $36.9\% \times (E[S|Top1\%]/E[S])$。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - 0.01^0.1 ≈ 36.9% 正确，且 LFU 在偏斜分布下优于随机保留前 K% 对象的逻辑自洽。
