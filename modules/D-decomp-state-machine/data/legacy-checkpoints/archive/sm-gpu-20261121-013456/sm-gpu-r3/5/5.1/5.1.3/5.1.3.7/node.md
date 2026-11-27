# N226: vLLM 0.5.x 版本在 H100 上运行 Qwen3-27B FP8 的吞吐量为 85 tokens/s，TensorRT-LLM 2.0 版本为 92 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88, N89, N90

## Claim

vLLM 0.5.x 版本在 H100 上运行 Qwen3-27B FP8 的吞吐量为 85 tokens/s，TensorRT-LLM 2.0 版本为 92 tokens/s，llama.cpp (CUDA) 为 78 tokens/s，三栈间吞吐量方差为 0.12x（(92-78)/85），低于 0.2x 阈值，无需采用保守估计。

## Corrected Claim

vLLM、TensorRT-LLM 和 llama.cpp 在 H100 上运行 Qwen3.8-27B（或 Qwen3-27B）的吞吐量差异较小，具体数值需查阅基准测试详细结果文件以确认。

## Evidence

[质询]参考来源中明确提到的模型是 'Qwen3.8-27B'，而陈述中是 'Qwen3-27B'，存在模型版本/名称不匹配的风险；此外，来源摘要未直接展示具体的吞吐量数值（85/92/78 tokens/s），无法确认具体数值是否准确，仅能确认存在相关基准测试。 | 来源 [1][2][3] 确认存在 H100 上 Qwen3.8-27B 的多框架基准测试，但摘要未提供具体吞吐量数值，且模型名称存在细微差异（Qwen3.8 vs Qwen3），属于间接支持且存在不确定性。

## Search Query

vLLM TensorRT-LLM llama.cpp Qwen3-27B FP8 H100 benchmark tokens/s

## Retrieval Sources

- {'url': 'https://github.com/winderai/llm-inference-benchmark&rut=58dd54b2e5c87c423326ee757fd3302548f3fa9ccd563c6e5f2979f1dfc4c22a', 'type': 'ddg', 'title': 'GitHub - winderai/llm-inference-benchmark: A reproducible benchmark of ...'}
- {'url': 'https://github.com/winderai/llm-inference-benchmark/tree/main/results/qwen3.8-27b&rut=c9a1c9ffb1611a947cf37e30ffd1fd5a1a862a23fc609c8380e3972e4d42c109', 'type': 'ddg', 'title': 'llm-inference-benchmark/results/qwen3.8-27b at main - GitHub'}
- {'url': 'https://github.com/winderai/llm-inference-benchmark/blob/main/results/qwen3.8-27b/h100.md&rut=a868731d9aaf21269cd135676694b4c2161626527cbfcfc8350a704ad65bb20d', 'type': 'ddg', 'title': 'llm-inference-benchmark/results/qwen3.8-27b/h100.md at main - GitHub'}
