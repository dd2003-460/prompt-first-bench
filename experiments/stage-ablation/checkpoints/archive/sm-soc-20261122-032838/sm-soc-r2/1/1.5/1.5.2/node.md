# N49: 参数一致性检验的约束条件2：降价后无咨询的概率下限。根据 N8，若 $P_{low} > P_{threshold}$，则 $P_{inquiry} \appr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

参数一致性检验的约束条件2：降价后无咨询的概率下限。根据 N8，若 $P_{low} > P_{threshold}$，则 $P_{inquiry} \approx 0$。需验证在 60% 的降价案例中，$P_{low}$ 确实高于 $P_{threshold} \approx 0.9 P_{ref}$。假设卖家降价幅度 $\Delta P \sim U[5\%, 15\%]$，则 $P_{low} = P_{high}(1-\Delta P)$。若 $P_{high} = 1.2 P_{ref}$，则 $P_{low} \in [1.02 P_{ref}, 1.14 P_{ref}]$，均大于 $0.9 P_{ref}$，满足 $P_{inquiry} \approx 0$ 的条件。

## Corrected Claim

参数一致性检验的约束条件2：降价后无咨询的概率下限。根据 N8，若 $P_{low} > P_{threshold}$，则 $P_{inquiry} \approx 0$。需验证在 60% 的降价案例中，$P_{low}$ 确实高于 $P_{threshold} \approx 0.9 P_{ref}$。假设卖家降价幅度 $\Delta P \sim U[5\%, 15\%]$，则 $P_{low} = P_{high}(1-\Delta P)$。若 $P_{high} = 1.2 P_{ref}$，则 $P_{low} \in [1.02 P_{ref}, 1.14 P_{ref}]$，均大于 $0.9 P_{ref}$，满足 $P_{inquiry} \approx 0$ 的条件。

## Evidence

先验知识/题面给定，逻辑校验通过：基于假设条件（P_high=1.2P_ref, ΔP∈[5%,15%]），计算得出 P_low∈[1.02P_ref, 1.14P_ref]，确实均大于 0.9P_ref，推导自洽。
