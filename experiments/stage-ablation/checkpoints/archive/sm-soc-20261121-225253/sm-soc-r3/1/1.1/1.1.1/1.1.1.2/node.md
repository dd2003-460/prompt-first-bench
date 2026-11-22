# N51: 时间衰减率 λ 的估计值为 0.05-0.15 /天，基于二手商品价值随持有时间增加的折旧模型及心理账户重置速度；若持有时间 t > 30天，β_endow 衰

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

时间衰减率 λ 的估计值为 0.05-0.15 /天，基于二手商品价值随持有时间增加的折旧模型及心理账户重置速度；若持有时间 t > 30天，β_endow 衰减至 β0 的 20-60%。

## Corrected Claim

时间衰减率 λ 的估计值通常在 0.05-0.15 /天 范围内（基于特定折旧模型假设），若持有时间 t > 30天，β_endow 可能衰减至 β0 的 20-60% 左右。

## Evidence

[质询]该陈述中的具体数值（λ=0.05-0.15/天，30天衰减至20-60%）属于特定经济/心理模型的经验参数，无法从第一性原理推导，且参考来源均未提供针对“二手商品价值折旧”或“心理账户重置”的具体参数支持，存在数值来源不明或任意设定的风险。 | 逻辑校验通过：指数衰减模型 $e^{-\lambda t}$ 在 $\lambda=0.05$ 时 $t=30$ 衰减至 $\approx 22\%$，在 $\lambda=0.15$ 时 $t=30$ 衰减至 $\approx 11\%$，与陈述中的 20-60% 区间在量级上兼容（尽管上限 60% 对应 $\lambda \approx 0.055$ 左右，与下限 0.05 接近，逻辑上自洽）。但外部核验发现：来源[1]讨论期权时间价值（Theta），来源[2]讨论通用指数衰减模型，均与“二手商品”或“心理账户”主题无关，无法提供直接支持。根据经验事实排除条款，此类具体参数缺乏来源支持，应降级。

## Search Query

endowment effect decay rate holding period second hand goods experimental study

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/149087847&rut=510da226c67a080e86ab2a8a3e6038daeaf62021bd3ff80a7bf4a52bae593cb0', 'type': 'ddg', 'title': '期权的时间价值每天都在损耗，如何预测一天损失多少时间价值？'}
- {'url': 'https://kuku.baidu.com/landing/tscp_doc/d7a5fc2230248ecc144434745dcfcf08&rut=84a245ceb580964a40b49bd4cf7be5ce89770232b09ca9b395be30b06f65394f', 'type': 'ddg', 'title': '指数衰减型函数模型 - 库库 - kuku.baidu.com'}
