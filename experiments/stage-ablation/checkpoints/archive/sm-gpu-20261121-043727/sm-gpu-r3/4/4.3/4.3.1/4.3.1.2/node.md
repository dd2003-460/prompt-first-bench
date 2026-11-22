# N180: 核实 RTX 4090 在 Prefill 阶段 (Compute-Bound) 的 MFU：查阅 llama.cpp 或 vLLM 在 RTX 4090 上运

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

核实 RTX 4090 在 Prefill 阶段 (Compute-Bound) 的 MFU：查阅 llama.cpp 或 vLLM 在 RTX 4090 上运行 7B-70B 模型的 Prefill 基准。由于 Tensor Core 利用率受限于矩阵尺寸 (Batch Size) 和内核启动开销，实测 MFU 通常在 30%-50% 之间，取决于 Batch Size (Batch>1 时 MFU 更高)。

## Corrected Claim

RTX 4090 在 Prefill 阶段的实测 MFU 通常受限于 Batch Size 和内核开销，具体数值需参考 llama.cpp 或 vLLM 的官方基准测试报告，一般认为在合理 Batch Size 下可达 30%-50% 区间。

## Evidence

[质询]参考来源仅提供了RTX 4090的硬件理论峰值算力（FP8/FP16 TFLOPS），完全未涉及llama.cpp或vLLM在Prefill阶段的实际MFU（Model FLOPs Utilization）基准测试数据，无法直接支持30%-50%这一具体经验数值范围。 | 经验事实，逻辑自洽但缺来源支持。来源[1]仅确认硬件峰值算力，未覆盖实际推理框架的MFU实测数据，无法排除其他可能性。

## Search Query

RTX 4090 llama.cpp prefill MFU utilization 7B 70B benchmark

## Retrieval Sources

- {'url': 'https://github.com/JustAResearcher/gpu-unlock-ada&rut=c201380e2781344ce5cbd04791c7f3e96b9c7b3ffb172e29e9a9d96a127dfadd', 'type': 'ddg', 'title': 'GPU unlock 1.1.1 — RTX 4090 and experimental Ada GPUs'}
