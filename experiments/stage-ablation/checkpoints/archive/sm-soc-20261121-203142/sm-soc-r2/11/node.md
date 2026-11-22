# N101: ‘60%无咨询’归因结论的敏感性分析置信度：该结论对算法降权系数 β_low 的敏感度为 ∂(P_no_inquiry)/∂β_low ≈ 0.4，若 β_lo

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

‘60%无咨询’归因结论的敏感性分析置信度：该结论对算法降权系数 β_low 的敏感度为 ∂(P_no_inquiry)/∂β_low ≈ 0.4，若 β_low 的 95% CI 为 [0.3, 0.7]，则结论的稳健性指数 Robustness_Index = 1 - (CI_width / β_low_mean) = 0.43，表明该结论对参数估计误差较为敏感，置信度标注为中等（Medium Confidence）。

## Corrected Claim

若 β_low 的 95% CI 为 [0.3, 0.7]，则结论的稳健性指数 Robustness_Index = 1 - (0.4 / 0.5) = 0.2，而非 0.43。

## Evidence

[质询]该陈述包含具体的数值参数（敏感度0.4、CI [0.3, 0.7]、稳健性指数0.43），这些属于特定模型或数据集的经验事实/计算结果，无法从第一性原理推导，且参考来源未提供这些具体数值，存在数值来源不明或虚构的风险。 | 逻辑校验通过：CI宽度为0.4，均值0.5，1-(0.4/0.5)=0.2，但文中称0.43，此处存在计算矛盾（0.4/0.5=0.8, 1-0.8=0.2 ≠ 0.43）。等等，重新计算：CI=[0.3, 0.7], width=0.4, mean=0.5. Robustness = 1 - (0.4/0.5) = 0.2. 文中说是0.43。这是一个硬逻辑/计算错误。因此 logic_ok 应为 false，status 应为 failed。

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/365205484&rut=7d1d5f27bbc6a0983977d193f2caaa504d7a0d7d84194abf07d91c246a4e8196', 'type': 'ddg', 'title': '写论文需要用到敏感性分析，有谁知道敏感性分析怎么用啊救救孩子吧!!!？ - 知乎'}
