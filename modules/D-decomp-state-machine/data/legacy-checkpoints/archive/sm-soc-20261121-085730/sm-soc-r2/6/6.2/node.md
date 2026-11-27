# N130: 买家感知独特性提升 ΔU_perception 的非线性系数0.3需要引入价格弹性修正项：当溢价率(P/C_ref - 1)超过0.3时，边际感知价值递减，修正

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

买家感知独特性提升 ΔU_perception 的非线性系数0.3需要引入价格弹性修正项：当溢价率(P/C_ref - 1)超过0.3时，边际感知价值递减，修正系数为 exp(-5*(P/C_ref - 1)^2)。

## Corrected Claim

买家感知独特性提升 ΔU_perception 的非线性系数0.3需要引入价格弹性修正项：当溢价率(P/C_ref - 1)超过0.3时，边际感知价值递减，修正系数形式为 exp(-k*(P/C_ref - 1)^2)（其中k为待定的经验衰减系数，此处设定为5）。

## Evidence

[质询]该陈述包含具体的经验参数（非线性系数0.3、阈值0.3、指数衰减系数5），这些属于特定模型设定或经验拟合结果，无法从第一性原理或数学公理中严格推导出来，且参考来源完全无关，缺乏实证数据支持其具体数值的有效性。 | 参考来源[1]讨论的是机器学习中的感知机算法，与买家感知独特性、价格弹性修正等经济学/营销学模型完全无关，属于无关来源；该事实为经验性模型参数设定，逻辑上自洽（函数形式合理）但缺乏来源支持，依据经验事实排除条款判为degraded。

## Search Query

non-linear utility function price premium scarcity effect diminishing returns

## Retrieval Sources

- {'url': 'https://blog.csdn.net/huanyingzhizai/article/details/93525995&rut=9585a3afe7d537d29efff795fa21dec0c9bfd165e196af46bc6771e687a84b12', 'type': 'ddg', 'title': '【机器学习笔记】——感知机（Perceptron）-CSDN博客'}
