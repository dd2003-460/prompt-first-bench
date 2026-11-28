# N307: KL 散度衰减斜率的实证基础：在 100 个标准科研 QA 对上，KL 散度随迭代次数 i 的衰减符合指数模型 KL(i) = KL_0 * exp(-λi)，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

KL 散度衰减斜率的实证基础：在 100 个标准科研 QA 对上，KL 散度随迭代次数 i 的衰减符合指数模型 KL(i) = KL_0 * exp(-λi)，需通过最小二乘法拟合 λ 值，验证 λ 是否稳定在 0.22（对应每次迭代降低 20%）

## Corrected Claim

在特定科研QA数据集上，KL散度随迭代次数的衰减可能符合指数模型 KL(i) = KL_0 * exp(-λi)，具体衰减系数 λ 需通过最小二乘法拟合确定，不同数据集和设置下 λ 值可能存在差异。

## Evidence

[质询]该陈述包含具体的经验参数（100个QA对、λ=0.22、20%衰减率），属于特定实验条件下的经验事实，无法从第一性原理推导，且参考来源均未提供此具体数值支持。 | 逻辑上指数衰减模型自洽，但参考来源[1][2]仅讨论KL散度的定义、估计器方差及一般性质，未涉及具体迭代衰减斜率或λ=0.22的实证数据，属经验事实缺来源支持。

## Search Query

KL divergence convergence rate iterative refinement LLM scientific reasoning

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1938191691510186931&rut=1f9e55574af7560e72033303ecad82f7143d7271f45026b210d6eafa613fb0a6', 'type': 'ddg', 'title': '从 RL for LLM 视角重新理解 KL 估计：读《Approximating KL Divergence》笔记'}
- {'url': 'https://zhuanlan.zhihu.com/p/1950257135775642370&rut=c046762fecb5e927661213d77f2f72e6fd2fc0ca8663d8102b89def68fa323ad', 'type': 'ddg', 'title': '深入理解 KL 散度（Kullback-Leibler Divergence）：从直觉、数学到前沿应用的全方位解析'}
