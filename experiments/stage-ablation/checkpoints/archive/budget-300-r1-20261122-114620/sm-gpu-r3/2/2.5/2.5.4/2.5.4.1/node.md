# N247: AMD MI250X 单卡 LLM 推理框架支持度量化：当前主流推理框架（vLLM, llama.cpp, ExLlamaV2）对 MI250X 的官方支持状态

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

AMD MI250X 单卡 LLM 推理框架支持度量化：当前主流推理框架（vLLM, llama.cpp, ExLlamaV2）对 MI250X 的官方支持状态为：vLLM 支持 ROCm 后端但需手动编译且部分算子（如 FlashAttention）缺失，导致吞吐量较同等算力 NVIDIA 卡降低 20-40% [待核验]；llama.cpp 支持 ROCm 但优化程度低于 CUDA，实测 Qwen3-27B 推理速度约为 RTX 4090 的 70-80% [待核验]

## Corrected Claim

当前主流推理框架（vLLM, llama.cpp, ExLlamaV2）对 AMD MI250X 的官方支持状态为：vLLM 支持 ROCm 后端但需手动编译且部分算子（如 FlashAttention）支持不完善；llama.cpp 支持 ROCm 但优化程度低于 CUDA。具体吞吐量及推理速度较同等算力 NVIDIA 卡的损耗比例需根据具体模型、版本及测试环境实测确定，通常存在一定性能差距。

## Evidence

[质询]具体性能损耗数值（20-40%、70-80%）及特定模型（Qwen3-27B）的实测数据属于高度依赖硬件配置、软件版本及测试环境的经验事实，缺乏通用性，且当前无来源支持这些具体数值。 | 逻辑自洽（ROCm生态成熟度低于CUDA是公认事实），但具体量化指标为经验事实，且本轮检索无可用来源支持，依据经验事实排除条款降级。

## Search Query

AMD MI250X vLLM llama.cpp inference benchmark ROCm performance comparison Qwen 27B
