# N328: 策略切换阈值 $R_{switch}$ 的求解方程为 $C_{self}(R_{switch}) = C_{cloud}(R_{switch})$，即 $C_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N122

## Claim

策略切换阈值 $R_{switch}$ 的求解方程为 $C_{self}(R_{switch}) = C_{cloud}(R_{switch})$，即 $C_{fixed}^{self} + MC_{self} \cdot R_{switch} = MC_{cloud} \cdot R_{switch}$，若 $MC_{self} \approx 0$，则 $R_{switch} = C_{fixed}^{self} / MC_{cloud}$，需代入具体成本参数计算该临界请求量。

## Corrected Claim

策略切换阈值 $R_{switch}$ 的求解方程为 $C_{self}(R_{switch}) = C_{cloud}(R_{switch})$，即 $C_{fixed}^{self} + MC_{self} \cdot R_{switch} = MC_{cloud} \cdot R_{switch}$，若 $MC_{self} \approx 0$，则 $R_{switch} = C_{fixed}^{self} / MC_{cloud}$，需代入具体成本参数计算该临界请求量。

## Evidence

先验知识/题面给定，逻辑校验通过：该方程基于成本函数定义（固定成本+可变成本）推导，量纲一致（成本=成本），且当边际成本为0时临界点公式符合代数逻辑。
