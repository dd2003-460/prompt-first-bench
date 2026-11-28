# N29: 黑盒节点 B2：vLLM TP=4 在 MTP×4 投机解码下的实际加速比 Speedup_ratio，理论值为 4x，但受限于 V100 显存带宽和同步开销，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

黑盒节点 B2：vLLM TP=4 在 MTP×4 投机解码下的实际加速比 Speedup_ratio，理论值为 4x，但受限于 V100 显存带宽和同步开销，实测可能仅为 1.8-2.5x，需监控 GPU 利用率确定真实迭代周期 T_iter

## Corrected Claim

vLLM TP=4 在 MTP×4 投机解码下的实际加速比通常低于理论值 4x，具体数值取决于硬件带宽、同步开销及草稿模型接受率，需通过监控 GPU 利用率和迭代周期进行实测评估。

## Evidence

[质询]参考来源[1]讨论的是Gemma-4-12B在RTX 5070 Ti上的单卡MTP性能，与待核验事实中涉及的vLLM框架、TP=4多卡配置及V100硬件环境完全不符，无法提供外部支持；且'1.8-2.5x'的具体数值范围属于经验事实，缺乏通用理论推导基础。 | 逻辑上，MTP理论加速比受限于接受率和通信开销，实测低于理论值符合直觉；但来源[1]主题无关（不同硬件/框架/模型），无法提供直接支持，且具体数值区间为经验数据，故降级。

## Search Query

vLLM speculative decoding MTP speedup V100 tensor parallelism 4

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2049474364488292313&rut=83ba2148df5278183182e27526df4174283122201bb948463e5e7e660f1d9a39', 'type': 'ddg', 'title': 'Gemma-4-12B MTP 加速性能对比报告 - 知乎'}
