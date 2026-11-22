# N81: 加权平均更新失效概率 P_invalidate_avg 的计算：P_invalidate_avg = ∫ [1 - exp(-λ_update / q)] * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

加权平均更新失效概率 P_invalidate_avg 的计算：P_invalidate_avg = ∫ [1 - exp(-λ_update / q)] * f_freq(q) dq，其中 f_freq(q) 是 Pareto(β=0.9) 的频率分布密度。由于 Pareto 分布尾部较长，低频对象（q 小）的 P_invalidate 较大，但权重也较小；需数值积分求解。

## Corrected Claim

加权平均更新失效概率 P_invalidate_avg 的计算公式为 P_invalidate_avg = ∫ [1 - exp(-λ_update / q)] * f_freq(q) dq，其中 f_freq(q) 为 Pareto(β=0.9) 分布密度。该模型假设失效概率随访问频率 q 变化，需数值积分求解。

## Evidence

[质询]该陈述描述的是特定缓存/存储系统中的失效概率模型，属于经验性工程假设或特定论文结论，而非通用物理/数学定律。参考来源[1]讨论的是深度学习中的EMA（指数移动平均）权重平滑技术，与缓存失效概率、Pareto频率分布及数值积分完全无关，无法提供外部支持。此外，'低频对象P_invalidate较大'这一结论依赖于λ_update与q的具体关系定义（通常失效概率随访问频率降低而降低，除非模型定义特殊），存在逻辑歧义风险，但主要问题是缺乏来源支持。 | 参考来源[1]主题为深度学习EMA，与本事实（缓存失效概率计算）主题无关，无可用外部证据；该事实为经验性模型公式，逻辑上自洽（积分形式正确，Pareto分布特性描述合理），但缺乏来源直接支持，依据经验事实排除条款判为degraded。

## Search Query

Numerical integration of Pareto distribution beta 0.9 with exponential decay term

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42744466/article/details/151153583&rut=6a278c7cafcdc79193fa8dd17e3046887391f6bbeaa2efded3397c3d9b2e15a1', 'type': 'ddg', 'title': '【Optimization】深入解析模型权重平均（EMA）技术_ema of weights-CSDN博客'}
