# N21: 纯本地档位的边际科研产出速率：基于 Qwen3.8-27b 在 TP=4 下 max-num-seqs=8 的并发吞吐，估算每小时可完成的“假设-验证”循环次数

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

纯本地档位的边际科研产出速率：基于 Qwen3.8-27b 在 TP=4 下 max-num-seqs=8 的并发吞吐，估算每小时可完成的“假设-验证”循环次数（假设单次循环平均 token 消耗 5k，KV cache fp8 优化下 batch 8 的 tokens/s 约为 1500-2000 [待核验]），得出每 1 元电费对应的循环次数增量

## Corrected Claim

基于 Qwen3.8-27b 在 TP=4 下 max-num-seqs=8 的并发吞吐，估算每小时可完成的“假设-验证”循环次数（假设单次循环平均 token 消耗 5k，需根据具体硬件实测 KV cache fp8 优化下的实际 tokens/s 进行计算），得出每 1 元电费对应的循环次数增量

## Evidence

[质询]核心数值（batch 8 下 1500-2000 tokens/s）缺乏来源直接支持，且该吞吐量高度依赖具体硬件型号（如 H100 vs A100 vs 消费级卡）及序列长度分布，不同硬件下量级差异巨大，无法仅凭模型名和 TP 设置确定唯一数值。 | 来源 [1][2][3] 均涉及 Qwen3.8-27B 的部署与量化，但未提供 TP=4 且 max-num-seqs=8 时的具体吞吐率数据，属于经验事实且缺来源直接支持。

## Search Query

Qwen 27B vLLM throughput tokens per second TP4 V100 batch size 8

## Retrieval Sources

- {'url': 'https://juejin.cn/post/7692742889197633536&rut=a7555eee9c2fe193fa65d8f9936b997b03ad987bddd71d5350cc78f21d11cbfd', 'type': 'ddg', 'title': '# 从 0 部署 Qwen3.8-27B：量化档位怎么选，终端配置怎么配以 Qwen3.8-27B 为样本梳理 20 余 - 掘金'}
- {'url': 'https://blog.csdn.net/lovely_yoshino/article/details/163828474&rut=0195b4e5dfa5b7cbba63f90a812f0c8467f62f911b6ca0d420433cf38557f270', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 部署实践：从原理到生产 - CSDN博客'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=bda3e56cedaae6d181b34928fb38fcb861fc1a3501752c8004812fefcc730ed4', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
