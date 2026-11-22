# N319: TensorRT-LLM 静态图编译的部署复杂度量化指标：针对 Qwen3-27B 在 RTX 4090 上构建引擎的耗时通常为 30-60 分钟（取决于模型大

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113, N114, N115

## Claim

TensorRT-LLM 静态图编译的部署复杂度量化指标：针对 Qwen3-27B 在 RTX 4090 上构建引擎的耗时通常为 30-60 分钟（取决于模型大小和硬件算力），且每次修改 Batch Size 或 Max Sequence Length 需重新编译，而 vLLM 动态调整仅需重启进程（<1 分钟），此维护成本在频繁调整场景下构成隐性 TCO 增量。

## Corrected Claim

TensorRT-LLM 静态图编译的部署复杂度较高：针对大模型（如 Qwen3-27B）在消费级显卡（如 RTX 4090）上构建引擎通常需数十分钟，且修改 Batch Size 或 Max Sequence Length 等关键参数需重新编译；相比之下，vLLM 等动态调度框架调整此类参数通常仅需重启进程（<1 分钟），在频繁调整场景下，TensorRT-LLM 的维护成本构成隐性 TCO 增量。

## Evidence

[质询]具体数值（30-60分钟）属于经验事实，缺乏通用性，且不同模型架构、量化方式及TensorRT版本下编译耗时差异巨大，该区间可能仅适用于特定配置，存在以偏概全风险。 | 经验事实，逻辑自洽但缺来源支持
