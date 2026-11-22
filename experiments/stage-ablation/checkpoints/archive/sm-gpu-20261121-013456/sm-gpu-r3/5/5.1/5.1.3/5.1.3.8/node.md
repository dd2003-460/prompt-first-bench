# N227: TensorRT-LLM 2.0 在 RTX 4090 上运行 Qwen3-27B INT8 的吞吐量为 22 tokens/s，vLLM 0.5.x 为 19

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88, N89, N90

## Claim

TensorRT-LLM 2.0 在 RTX 4090 上运行 Qwen3-27B INT8 的吞吐量为 22 tokens/s，vLLM 0.5.x 为 19 tokens/s，llama.cpp 为 17 tokens/s，三栈间吞吐量方差为 0.24x（(22-17)/19），超过 0.2x 阈值，TCO 计算中必须采用保守估计（取最小吞吐量 17 tokens/s），否则可能高估性能导致选型错误。

## Corrected Claim

TensorRT-LLM 2.0、vLLM 0.5.x 和 llama.cpp 在 RTX 4090 上运行 Qwen3-27B INT8 的吞吐量存在差异，若方差超过 0.2x 阈值，TCO 计算中建议采用保守估计（取最小吞吐量）以避免高估性能。

## Evidence

[质询]具体吞吐量数值（22/19/17 tokens/s）及方差计算属于特定硬件与模型配置下的经验事实，参考来源仅涉及部署流程或不同模型（Qwen3-Omni），未提供该特定组合（Qwen3-27B INT8 on RTX 4090）的精确基准测试数据，无法验证具体数值的准确性。 | 逻辑推导自洽（(22-17)/19≈0.26>0.2），但具体性能数值为经验事实，参考来源[1][2]未直接覆盖该特定模型与量化配置的吞吐量数据，缺乏直接外部证据支持。

## Search Query

TensorRT-LLM vLLM llama.cpp Qwen3-27B INT8 RTX 4090 benchmark tokens/s

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32389853/article/details/152304789&rut=5c685e0059d9ad3dfd4d5453434d619051cf1a2fd08e23151407f2eeda9f44f4', 'type': 'ddg', 'title': 'RTX4090 云 GPU 的 TensorRT-LLM 优化步骤 - CSDN博客'}
- {'url': 'https://blog.csdn.net/2302_79462688/article/details/159615336&rut=70b8514c1a0796cbc6a47be8794b32b18ac6b9aa076aaa25d90ea90f50e5f96e', 'type': 'ddg', 'title': 'Qwen3.5-27B 双RTX 4090部署实战：从环境配置到性能调优全记录_tensorrt-llm qwen3.5'}
