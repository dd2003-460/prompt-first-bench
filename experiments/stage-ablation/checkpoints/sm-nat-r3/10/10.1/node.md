# N79: LRU 对突发访问的敏感度量化：定义突发因子 B 为短期请求率与长期平均请求率的比值。LRU 命中率在突发下的波动幅度 ΔH_LRU ≈ B * (1 - H_

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

LRU 对突发访问的敏感度量化：定义突发因子 B 为短期请求率与长期平均请求率的比值。LRU 命中率在突发下的波动幅度 ΔH_LRU ≈ B * (1 - H_LRU_steady) * exp(-λ_burst * T_burst)，其中 T_burst 为突发持续时间。

## Corrected Claim

LRU命中率在突发访问下的波动幅度受突发因子B、突发持续时间T_burst以及工作负载局部性特征（如缓存大小、参考串长度）共同影响，具体量化关系需结合特定工作负载模型（如Markov链或特定拟合公式）确定，不存在通用的单一解析公式 ΔH_LRU ≈ B * (1 - H_LRU_steady) * exp(-λ_burst * T_burst)。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点之间存在明显的公式矛盾（父节点含指数衰减项，子节点2为线性/无指数项），且子节点3讨论的'恢复时间'超出了父节点仅定义'波动幅度'的范围，导致逻辑不连贯且覆盖不精准。）

## Search Query

LRU cache hit rate volatility under bursty traffic

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/679259506&rut=a26cf25bce37b887450157027fc322372845ddf6f5fd547679e5983603084287', 'type': 'ddg', 'title': 'Lru Lfu 自适应算法设计纲要 - 知乎'}
- {'url': 'https://www.sohu.com/a/696456696_827544&rut=703ee36dc72ba9d44e6bc4adf6bd89d7edaf9ede8555a52455303896146f562d', 'type': 'ddg', 'title': '深入解析Redis的LRU与LFU算法实现_数据库_访问_缓存 - 搜狐'}
