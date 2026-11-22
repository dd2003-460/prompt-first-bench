# N154: 软件栈版本对 INT4 吞吐量的影响：vLLM 0.6.2 相比 0.5.4，INT4 推理吞吐量提升 15%（因优化了 Kernel Fusion），Tens

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

软件栈版本对 INT4 吞吐量的影响：vLLM 0.6.2 相比 0.5.4，INT4 推理吞吐量提升 15%（因优化了 Kernel Fusion），TensorRT-LLM 8.5 相比 8.3 提升 8%（因改进了 Dequantization Pipeline）

## Corrected Claim

软件栈版本更新通常能提升INT4推理吞吐量，例如vLLM和TensorRT-LLM在后续版本中通过优化Kernel Fusion和Dequantization Pipeline等机制实现了性能提升，但具体提升幅度（如15%或8%）需依据特定基准测试报告确认。

## Evidence

[质询]具体数值（15%和8%）及特定版本对比（0.6.2 vs 0.5.4, 8.5 vs 8.3）属于经验事实，参考来源未提供这些精确数据，且来源[2]主要讨论v0.6.0的CPU优化而非INT4 Kernel Fusion的具体吞吐提升幅度，存在数据无据可依的风险。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为项目主页无具体数据，来源[2]仅提及v0.6.0性能优化方向，未覆盖具体版本对比数值）

## Search Query

vLLM TensorRT-LLM INT4 inference performance improvement version comparison

## Retrieval Sources

- {'url': 'https://github.com/vllm-project/vllm&rut=3c1b72c23523dd9a980755bcb2d4e67d3ada258432470eb78015fd3ff0c47818', 'type': 'ddg', 'title': 'GitHub - vllm-project/vllm: A high-throughput and memory-efficient ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/19992486933&rut=3f679fe9f58ed72e37b6945797be67b852d3f26971ec4c601e75bbb6a4113d2e', 'type': 'ddg', 'title': '解读vLLM v0.6.0官方blog - 知乎'}
