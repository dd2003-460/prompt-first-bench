# N56: 推理成本增加倍数并非简单的 5x，而是 Cost_ratio = k * (1 + Overhead_penalty)，其中 Overhead_penalty 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

推理成本增加倍数并非简单的 5x，而是 Cost_ratio = k * (1 + Overhead_penalty)，其中 Overhead_penalty 源于并发请求导致的 KV Cache 显存竞争 (当 max-num-seqs=8 时，k=5 并发可能导致其他序列被抢占或 OOM)，需实测并发下的 P99 延迟退化系数。

## Corrected Claim

推理成本增加并非简单的线性倍数，受并发请求下 KV Cache 显存竞争影响（如高并发可能导致序列抢占或 OOM），实际成本比率和 P99 延迟退化需根据具体部署参数（如 max-num-seqs）进行实测评估。

## Evidence

[质询]该陈述提出了一个具体的经验性公式 `Cost_ratio = k * (1 + Overhead_penalty)` 以及特定的参数关联（max-num-seqs=8, k=5），这属于具体的工程实现细节和经验数据，无法从第一性原理推导。参考来源仅讨论宏观推理成本趋势和一般性优化，未提及此特定公式、vLLM 的具体参数配置或并发下的显存竞争量化模型，因此缺乏直接来源支持。 | 逻辑上，并发导致 KV Cache 显存竞争进而引发抢占或 OOM 从而增加成本/延迟是合理的工程直觉，但具体公式和参数值为经验事实，参考来源 [1][2] 均未覆盖此微观机制及具体数值，故降级。

## Search Query

vllm concurrent request latency degradation kv cache contention

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%8E%A8%E7%90%86%E6%88%90%E6%9C%AC/67480650&rut=6d7a0ad93db30cd61d639f2785031d823b44ac2fee8de5c741b6edc2e995e9d7', 'type': 'ddg', 'title': '推理成本_百度百科'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=7750121&rut=ec65f43d1d70b805616110375ba3f0cc3dcd7ef4b21da76d77de35b040468d2b', 'type': 'ddg', 'title': '大模型推理优化：2026年的技术突破与成本挑战-百度开发者中心'}
