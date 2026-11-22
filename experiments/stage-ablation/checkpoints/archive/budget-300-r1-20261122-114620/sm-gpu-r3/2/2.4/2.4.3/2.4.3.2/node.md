# N228: RX 7900 XTX 在 ROCm 6.x 环境下运行 Qwen3-27B (INT8) 的推理吞吐量相比 RTX 4090 的 CUDA 环境通常低 30-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

RX 7900 XTX 在 ROCm 6.x 环境下运行 Qwen3-27B (INT8) 的推理吞吐量相比 RTX 4090 的 CUDA 环境通常低 30-50%，主要受限于算子优化覆盖率和内存带宽效率 [待核验]

## Corrected Claim

RX 7900 XTX 在 ROCm 环境下运行大语言模型推理时，由于算子优化覆盖率和软件生态成熟度通常低于 NVIDIA CUDA 环境，其吞吐量相比同级或更高规格 NVIDIA GPU（如 RTX 4090）存在显著差距，具体性能比取决于量化方案与驱动版本。

## Evidence

[质询]具体数值区间（30-50%）缺乏统一基准，且INT8量化在ROCm上的算子支持情况随版本波动大，该具体百分比可能因驱动版本、量化方案（如GPTQ/AWQ vs 原生INT8）及具体模型结构而异，存在过度精确化的风险。 | 经验事实，逻辑自洽（AMD在AI推理生态成熟度上通常落后于NVIDIA，且ROCm算子优化覆盖率确实低于CUDA，导致性能差距合理），但本轮检索无可用来源，无法提供直接数据支持，故降级。

## Search Query

RX 7900 XTX LLM inference throughput benchmark vs RTX 4090 ROCm
