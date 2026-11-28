# N162: 当请求序列数 N_req 超过 N_max 时，vLLM 的实际吞吐量下降比例并非简单的线性 (1 - N_max/N_req)，而是受限于显存带宽竞争导致的单

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

当请求序列数 N_req 超过 N_max 时，vLLM 的实际吞吐量下降比例并非简单的线性 (1 - N_max/N_req)，而是受限于显存带宽竞争导致的单序列解码速度降低；在 N_req=8, N_max=4 的场景下，由于 L2 Cache 命中率下降和 HBM 带宽饱和，实测吞吐量下降比例通常高达 60%-70%。

## Corrected Claim

当请求序列数 N_req 超过 N_max 时，vLLM 的实际吞吐量会因显存带宽竞争和 L2 Cache 命中率下降而受到限制，单序列解码速度降低，具体下降比例取决于硬件配置和负载特征，并非简单的线性关系。

## Evidence

[质询]具体数值（60%-70%）缺乏通用性，高度依赖硬件型号、模型大小及序列长度分布，属于特定实验条件下的经验数据，不能概括为“通常”情况；且来源中未包含此具体性能衰减比例的实测数据。 | 逻辑上，并发数增加导致显存带宽竞争和缓存命中率下降从而降低单序列速度是合理的（符合GPU推理瓶颈原理），但参考来源[1][2][3]仅讨论了max_num_seqs的参数定义、调度机制及一般性调优建议，均未提供N_req=8, N_max=4场景下吞吐量下降60%-70%的具体实证数据，属于经验事实且缺来源直接支持。

## Search Query

vLLM throughput degradation when batch size exceeds max concurrent sequences HBM bandwidth saturation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42437253/article/details/155252757&rut=a03b0e4c30632eab6c4204f1728ab2511e1dc43ef4165fa8dd93145fad87d49b', 'type': 'ddg', 'title': 'vLLM如何设置最大并发请求数？防过载保护-CSDN博客'}
- {'url': 'https://blog.csdn.net/qq_41956187/article/details/157440232&rut=5684f63b9a524539279ee1f60d9be765416540d275ecb22542b0e097a34ea62a', 'type': 'ddg', 'title': '[AI][vLLM] max_num_seqs 参数详解 - CSDN博客'}
- {'url': 'https://docs.vllm.ai/en/v0.6.2/models/performance.html&rut=89b370d70841fb09cd7c8e8004c368a3109ba04e9e4e7c795d6d352bbd538319', 'type': 'ddg', 'title': 'Performance and Tuning — vLLM'}
