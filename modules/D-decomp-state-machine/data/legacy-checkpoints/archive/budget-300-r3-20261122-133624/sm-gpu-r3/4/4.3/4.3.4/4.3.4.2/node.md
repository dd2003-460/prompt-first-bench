# N321: SmoothQuant INT8 推理在 RTX 4090 上的软件开销：SmoothQuant 将激活值量化至 INT8，权重保持 INT8，但需额外的 pe

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

SmoothQuant INT8 推理在 RTX 4090 上的软件开销：SmoothQuant 将激活值量化至 INT8，权重保持 INT8，但需额外的 per-channel scaling 和 dequantization 操作。相比 GPTQ，SmoothQuant 的 dequantization 开销更低（仅激活值需 dequantize），Prefill 阶段算力利用率降至 85-90%，吞吐量约为 720-760 tokens/s。

## Corrected Claim

SmoothQuant INT8 推理在 RTX 4090 上相比 GPTQ 具有更低的 dequantization 开销（仅激活值需 dequantize），Prefill 阶段算力利用率较高，具体吞吐量取决于模型配置与实现细节。

## Evidence

[质询]具体数值（85-90%利用率、720-760 tokens/s）高度依赖模型规模、序列长度及具体实现库（如vLLM/TensorRT-LLM版本），属于经验事实，缺乏通用性，且无来源支持该特定数值区间。 | 经验事实，逻辑自洽但缺来源支持
