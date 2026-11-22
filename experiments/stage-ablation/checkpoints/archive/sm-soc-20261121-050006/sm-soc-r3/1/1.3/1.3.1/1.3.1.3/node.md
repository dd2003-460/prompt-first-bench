# N142: λ_search 与在线时长 T_online 的非线性关系：模型设定为 λ_search = γ * T_online^δ，其中 δ 为弹性系数；若 δ < 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

λ_search 与在线时长 T_online 的非线性关系：模型设定为 λ_search = γ * T_online^δ，其中 δ 为弹性系数；若 δ < 1，表明搜索强度随在线时长增加而边际递减（疲劳效应），δ 的估计值需通过幂律拟合获得，预期 δ ∈ [0.5, 0.8]。

## Corrected Claim

模型设定为 λ_search = γ * T_online^δ，其中 δ 为弹性系数；若 δ < 1，表明搜索强度随在线时长增加而边际递减（疲劳效应），δ 的估计值需通过幂律拟合获得。

## Evidence

[质询]该陈述包含具体的经验参数范围（δ ∈ [0.5, 0.8]）和特定的模型设定，属于经验事实。参考来源 [1] 讨论的是强化学习中的 TD(λ) 算法，其中的 λ 是折扣/回溯参数，与搜索强度弹性系数 δ 无关，来源与事实主题完全不匹配，无法提供外部支持。 | 逻辑上幂律模型描述边际递减效应是自洽的，但参考来源 [1] 与搜索行为建模无关，且该事实属于经验参数设定，缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

user online duration search intensity power law decay e-commerce

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/1512.04087&rut=750ef2bc0e6d49b960528a5e07ffd40055dfbce0c7e7097f84e7b7efa72ec3df', 'type': 'ddg', 'title': '[1512.04087] True Online Temporal-Difference Learning'}
