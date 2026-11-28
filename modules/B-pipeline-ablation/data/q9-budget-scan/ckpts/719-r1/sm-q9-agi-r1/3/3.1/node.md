# N13: 4x V100-SXM2-16GB (TP=4) 运行 Qwen3.8-27B NVFP4 时的实际 Tokens/s/Worker 吞吐量，需扣除通信开销（A

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

4x V100-SXM2-16GB (TP=4) 运行 Qwen3.8-27B NVFP4 时的实际 Tokens/s/Worker 吞吐量，需扣除通信开销（AllReduce latency）后的净推理速度。

## Corrected Claim

4x V100-SXM2-16GB (TP=4) 运行 Qwen3.8-27B NVFP4 时的实际吞吐量受AllReduce通信开销影响，具体数值需实测获取，当前缺乏公开基准数据支持确切数值。

## Evidence

[质询]该陈述包含具体的硬件配置（4x V100）、模型版本（Qwen3.8-27B NVFP4）及量化后的具体吞吐量数值，属于高度依赖特定环境、软件栈和硬件拓扑的经验事实，无法从第一性原理推导，且参考来源中完全缺失该特定组合的性能数据。 | 逻辑上自洽（V100支持NVFP4需较新驱动/框架，TP=4通信开销存在），但参考来源[1][2]仅涉及V100通用LLM部署或14B模型性能，未提供Qwen3.8-27B NVFP4在4x V100 TP=4下的具体Tokens/s数据，属经验事实且缺直接来源支持。

## Search Query

vLLM 4x V100 TP=4 Qwen 27B throughput tokens per second net speed

## Retrieval Sources

- {'url': 'https://github.com/andrewleech/v100-llm-kit&rut=ad91f7c6bbeedf6a1f9afebecc27e12f4c8031013db29d8467d0eb0962def34c', 'type': 'ddg', 'title': 'GitHub - andrewleech/v100-llm-kit: Run local LLMs on a Tesla V100-SXM2 ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/1910043824199303266&rut=f987a0d9f0a84c0a1ecf2f576e87cb1f1b31b4e6034cb616d8eb895a2228e9f4', 'type': 'ddg', 'title': 'SXM2版V100显卡很麻烦但很香：14B大模型速度超50!附折腾攻略'}
