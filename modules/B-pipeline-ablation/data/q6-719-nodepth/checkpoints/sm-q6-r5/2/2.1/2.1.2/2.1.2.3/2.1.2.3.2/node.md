# N499: 源站最大并发处理能力 C_origin_max 的量化：基于单核 CPU 处理 QPS 上限及核数，假设单台源站服务器（16 核）可处理 2000 QPS，集群

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N160

## Claim

源站最大并发处理能力 C_origin_max 的量化：基于单核 CPU 处理 QPS 上限及核数，假设单台源站服务器（16 核）可处理 2000 QPS，集群由 10 台服务器组成，则 C_origin_max = 20,000 QPS；负载率 Load = R_backhaul / C_origin_max。

## Corrected Claim

源站最大并发处理能力 C_origin_max 的量化：基于单核 CPU 处理 QPS 上限及核数，假设单台源站服务器（16 核）可处理 2000 QPS（此为特定负载下的经验估算值），集群由 10 台服务器组成，则 C_origin_max = 20,000 QPS；负载率 Load = R_backhaul / C_origin_max。

## Evidence

[质询]该陈述中的具体数值（单核2000 QPS、10台服务器）属于特定场景下的经验假设或工程估算，并非通用物理定律或数学公理，无法从第一性原理严格推导。不同业务逻辑（如简单静态资源 vs 复杂计算）下，单核QPS差异巨大，该数值缺乏普适性依据。 | 逻辑自洽（2000*10=20000），但来源[2]仅定性讨论CPU核心数与并发能力的关系，未提供具体QPS数值支持；来源[1]无关。作为经验事实，缺乏直接来源支持具体数值，故降级。

## Search Query

typical web server QPS per core Go Node.js Java benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/691537237&rut=f11d20e0a6331988e3c51f6974ecb43ecbdc7a4bace57bf4014569ff2fcaa79d', 'type': 'ddg', 'title': '量化那些事之KVCache的量化 - 知乎 - 知乎专栏'}
- {'url': 'https://zhuanlan.zhihu.com/p/2053966597962912090&rut=e98d2b92a0d717ee2466d8b98dbdfde9249454afb5b0cbd0c9b6ebf1086e1733', 'type': 'ddg', 'title': '从2核2g到16核16g：美国轻量服务器的cpu核心数是如何影响并发处理能力的？ - 知乎'}
