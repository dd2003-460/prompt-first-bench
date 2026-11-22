# N238: 卖家目标函数中的‘声誉资本’约束：卖家的效用函数 U_seller = (P_sale - C_cost) * P_sale - λ_reputation * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

卖家目标函数中的‘声誉资本’约束：卖家的效用函数 U_seller = (P_sale - C_cost) * P_sale - λ_reputation * ΔReputation；在平台算法中，频繁降价会降低卖家信用分，导致未来曝光权重 W_rec 下降 5-10%；因此，理性卖家倾向于维持高挂价以保护声誉资本，而非立即降价。

## Corrected Claim

卖家目标函数中若包含声誉资本约束（即降价会损害声誉并导致未来曝光权重下降），理性卖家倾向于维持高挂价以保护声誉资本，而非立即降价。

## Evidence

[质询]该陈述包含具体的经验性参数（曝光权重下降5-10%）和特定的平台算法机制（频繁降价降低信用分），这属于特定平台（如淘宝、亚马逊等）的工程实现细节或经验观察，无法从微观经济学第一性原理或通用效用函数定义中严格推导出来。此外，参考来源仅涉及通用的效用最大化理论，未涉及具体的平台声誉机制或数值参数。 | 逻辑上，引入声誉成本项（λ_reputation * ΔReputation）确实会抑制卖家的降价冲动，符合经济学直觉；但具体的'5-10%'数值及'频繁降价降低信用分'的机制属于经验事实，参考来源[1]仅讨论通用效用最大化，未提供相关支持，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/660051503&rut=f6c517cf278ad522218d13d8888fbbc1f380b6293da9a8274fbc2069272bf791', 'type': 'ddg', 'title': '高级微观08：效用最大化问题 - 知乎'}
