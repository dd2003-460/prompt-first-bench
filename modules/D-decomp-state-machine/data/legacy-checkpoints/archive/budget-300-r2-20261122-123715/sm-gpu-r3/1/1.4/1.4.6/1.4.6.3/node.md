# N191: 混合并行策略 (TP+PP) 的可行性评估：在 2 卡限制下，TP=2 是常见选择，但需验证 vLLM/TensorRT-LLM 是否支持 TP=2 在 PCI

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

混合并行策略 (TP+PP) 的可行性评估：在 2 卡限制下，TP=2 是常见选择，但需验证 vLLM/TensorRT-LLM 是否支持 TP=2 在 PCIe 互联下的优化路径，以及是否存在比纯 TP 更优的通信模式（如 AllGather 替代 AllReduce）。

## Corrected Claim

在 2 卡限制下，TP=2 是常见的并行策略选择。理论上，需评估 vLLM/TensorRT-LLM 在 PCIe 互联下对 TP=2 的支持情况及通信优化潜力（如 AllGather 与 AllReduce 的效率对比），但具体框架的实现细节需查阅官方文档或实测验证。

## Evidence

[质询]该陈述包含具体的工程实现细节（vLLM/TensorRT-LLM 对 PCIe 下 TP=2 的优化路径支持情况、AllGather 替代 AllReduce 的具体可行性），属于经验事实。在缺乏外部来源支持的情况下，无法确认这些特定框架在 PCIe 互联下的具体优化行为或通信模式选择是否如陈述所述，存在将理论可能性误判为已验证工程事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM tensor parallelism PCIe 4.0 optimization Qwen3-27B
