# N58: TensorRT-LLM 启用 In-Flight Batching 和 Layer Fusion 后，激活内存峰值降低约 30-40%，主要因为 FFN 中间

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

TensorRT-LLM 启用 In-Flight Batching 和 Layer Fusion 后，激活内存峰值降低约 30-40%，主要因为 FFN 中间层 (intermediate_size) 的激活被分块计算并立即释放，而非全层同时驻留显存

## Corrected Claim

TensorRT-LLM 启用 In-Flight Batching 和 Layer Fusion 后，通过分块计算和即时释放激活内存，显著降低了显存峰值占用（具体降低幅度取决于模型配置和负载，通常有显著优化效果），主要因为 FFN 中间层的激活被分块处理而非全层同时驻留显存。

## Evidence

[质询]数值量级缺乏直接证据支持：30-40%的激活内存峰值降低是一个具体的经验数值，参考来源仅定性描述了In-flight Batching和Kernel Fusion（Layer Fusion）的机制，未提供该特定百分比的基准测试数据或理论推导依据。此外，In-flight Batching主要优化的是调度延迟和吞吐，对激活内存峰值的影响通常取决于Batch Size和序列长度，并非固定的30-40%。 | 来源[1][2][3]均确认TensorRT-LLM使用In-flight Batching和Kernel Fusion进行优化，但均未提及具体的激活内存降低百分比（30-40%），属于经验事实且缺乏直接来源支持。

## Search Query

TensorRT-LLM activation memory optimization layer fusion in-flight batching

## Retrieval Sources

- {'url': 'https://blog.csdn.net/iymei4986533030/article/details/162529331&rut=9b0f1afc75b4624ebb468ef5a47cba38359451a22e9eb3929ae10a827a1dfd7f', 'type': 'ddg', 'title': 'TensorRT-LLM 实战部署：从模型编译到 In-flight Batching 的性能调优'}
- {'url': 'https://blog.csdn.net/weixin_42594427/article/details/169239044&rut=e1098d242c03382bde44ebdaef70e3dff35ad6df11aa7b46301242f3ddbf0724', 'type': 'ddg', 'title': 'TensorRT-LLM 实战部署：从 trtllm-build 模型编译到 In-flight Batching 的性能调优'}
- {'url': 'https://geek-doc.cn/chip-design/intermediate/tensorrt-llm-inflight-batching&rut=99a1eeb1d9a0732238d5385a98b1ebcd69f528066eb6a307fe638bfaad1b4648', 'type': 'ddg', 'title': 'TensorRT-LLM：in-flight batching 机制、executor 架构与 plugin 体系工程解析'}
