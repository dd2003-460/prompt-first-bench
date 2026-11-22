# N393: Qwen3-27B NVFP4量化版本的MMLU准确率Acc_NVFP4，由于NVFP4是较新的格式，需特别关注NVIDIA TensorRT-LLM或相关推理

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N131

## Claim

Qwen3-27B NVFP4量化版本的MMLU准确率Acc_NVFP4，由于NVFP4是较新的格式，需特别关注NVIDIA TensorRT-LLM或相关推理引擎的官方文档中是否提供针对Qwen3系列的NVFP4精度损失报告；若无，需标记为[待核验]并建议通过本地TensorRT-LLM部署实测。

## Corrected Claim

Qwen3-27B NVFP4量化版本的MMLU准确率Acc_NVFP4需通过本地TensorRT-LLM部署实测或查阅最新官方文档确认，因NVFP4为较新格式，目前缺乏公开可靠的官方精度损失报告。

## Evidence

[质询]该陈述包含具体的经验性技术细节（Qwen3-27B 的 NVFP4 量化版本存在性、MMLU 准确率的具体数值或状态、TensorRT-LLM 对 Qwen3 系列 NVFP4 的官方支持情况），这些属于硬件/软件规格及模型性能数据，无法从第一性原理推导，且当前无可用来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证 Qwen3-27B NVFP4 的具体性能数据及官方文档覆盖情况）

## Search Query

Qwen3-27B NVFP4 quantization MMLU benchmark
