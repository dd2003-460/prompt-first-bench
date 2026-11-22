# N164: σ_f > σ_f_crit 时 LFU 负增益的量化模型：ΔH_neg(σ_f) = -w * (σ_f - σ_f_crit)^2 * H_base，其中 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58, N59, N60

## Claim

σ_f > σ_f_crit 时 LFU 负增益的量化模型：ΔH_neg(σ_f) = -w * (σ_f - σ_f_crit)^2 * H_base，其中 w 为惩罚系数，需通过模拟不同 σ_f (1.0, 2.0, 3.0) 下的命中率变化拟合 w 的具体数值。

## Corrected Claim

在 σ_f > σ_f_crit 时，LFU 可能出现负增益，其量化模型可假设为 ΔH_neg(σ_f) = -w * (σ_f - σ_f_crit)^2 * H_base，其中 w 为需通过模拟拟合的惩罚系数，但该模型的有效性依赖于具体 workload 特征，非通用定理。

## Evidence

[质询]该量化模型（二次方惩罚函数）属于特定假设下的经验拟合公式，并非通用物理定律或数学恒等式，且参考来源未提供该具体公式或拟合系数 w 的推导/验证，存在模型过拟合或不适用于特定 workload 的风险。 | 逻辑自洽（量纲与符号合理），但参考来源 [1] 仅讨论 LRU/LFU 自适应的必要性，未涉及具体的负增益量化模型或拟合方法，属于经验事实且缺乏直接来源支持。

## Search Query

quantifying LFU performance degradation high frequency volatility penalty coefficient simulation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/679259506&rut=f013bbe63c240c69fef131a2de419b94200af7a6c469968c442400d1fc8a8540', 'type': 'ddg', 'title': 'Lru Lfu 自适应算法设计纲要 - 知乎'}
