# N246: 2×RTX 4090 运行 Qwen3-27B (BF16/FP8) 的实测单流推理吞吐量（tokens/s），需区分 vLLM 与 TensorRT-LLM 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

2×RTX 4090 运行 Qwen3-27B (BF16/FP8) 的实测单流推理吞吐量（tokens/s），需区分 vLLM 与 TensorRT-LLM 框架，以修正 N97 中估算的 28 tokens/s。

## Corrected Claim

2×RTX 4090 运行 Qwen3-27B (BF16/FP8) 的实测单流推理吞吐量需区分 vLLM 与 TensorRT-LLM 框架，具体数值需参考对应框架的官方基准测试或最新实测报告，现有来源未提供直接数据。

## Evidence

[质询]参考来源均指向 Qwen3.5/3.8 或不同量化/框架（llama.cpp/单卡），缺乏针对 Qwen3-27B 在 2×RTX 4090 上运行 vLLM 与 TensorRT-LLM 的 BF16/FP8 实测吞吐量数据，无法直接验证具体数值。 | 来源 [1][2][3] 主题相关但模型版本（Qwen3.5/3.8）或硬件配置（单卡/量化）不匹配，未提供 Qwen3-27B 双卡 vLLM/TRT-LLM 的实测 tokens/s 数据，属经验事实且缺直接来源支持。

## Search Query

Qwen3-27B 2x RTX 4090 inference throughput tokens per second vLLM TensorRT-LLM benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2302_79462688/article/details/159615336&rut=70b8514c1a0796cbc6a47be8794b32b18ac6b9aa076aaa25d90ea90f50e5f96e', 'type': 'ddg', 'title': 'Qwen3.5-27B 双RTX 4090部署实战：从环境配置到性能调优全记录_tensorrt-llm qwen3.5'}
- {'url': 'https://dashen-tech.com/ai-tech/qwen38-27b-deployment-guide/&rut=aaf906668f1b8fafbac7f3c6d54d6c9103a71d8c17508fb461dc08b547b4e001', 'type': 'ddg', 'title': 'Qwen3.8 27B 本地部署：RTX 4090 单卡运行+6方案对比（2026） | Dashen-Tech'}
- {'url': 'https://blog.csdn.net/pkyang2004/article/details/164110922&rut=ed3c7b7f1dfdd87c1c11f0af63868b8817ae04cbe66049a0196c503d9b8cfb44', 'type': 'ddg', 'title': 'RTX 4090D-48G本地部署 Qwen3.8-27B 经验总结_qwen3.5-27b-fp8的单请求tps-CSDN博客'}
