# N276: ROCm 生态中 vLLM/TensorRT-LLM 等主流推理框架对 Qwen3-27B 的兼容性问题：部分算子（如 GQA 优化）在 ROCm 上未完全移植

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

ROCm 生态中 vLLM/TensorRT-LLM 等主流推理框架对 Qwen3-27B 的兼容性问题：部分算子（如 GQA 优化）在 ROCm 上未完全移植，导致需使用回退路径，吞吐量额外损失 5-10%。

## Corrected Claim

ROCm 生态中 vLLM 等主流推理框架在部署 Qwen3 系列模型时存在兼容性或性能优化空间，部分算子可能需使用回退路径，导致吞吐量存在一定程度的损失（具体数值需实测验证）。

## Evidence

[质询]具体数值（5-10%吞吐量损失）及特定算子（GQA优化未完全移植）属于高度具体的经验事实，参考来源摘要仅提及部署与优化过程，未提供该具体性能损耗数据或算子缺失细节，存在过度具体化风险。 | 来源[1]和[2]证实了ROCm环境下vLLM部署Qwen3的可行性及优化背景，间接支持存在兼容性/性能调优需求，但未直接提供'5-10%损失'或'GQA未移植'的具体证据，属经验事实缺直接来源支持。

## Search Query

vLLM TensorRT-LLM ROCm Qwen3-27B compatibility issues

## Retrieval Sources

- {'url': 'https://www.modelscope.cn/posts/435060&rut=e9b093a41a92435720a96a96ce02d1f77b3cac7d41242559f3b75e5c749a14b2', 'type': 'ddg', 'title': 'AMD GPU 大模型推理优化实战：基于 ROCm 7 + vLLM 的 Qwen3 部署与性能调优手记'}
- {'url': 'https://blog.csdn.net/gitblog_00948/article/details/148505785&rut=ac5454095f92daf3224647ee772f2b4bf5ab21fa6dcfeec99410776e5ed00057', 'type': 'ddg', 'title': 'ROCm项目中LLM推理框架vLLM与TGI的实践指南 - CSDN博客'}
