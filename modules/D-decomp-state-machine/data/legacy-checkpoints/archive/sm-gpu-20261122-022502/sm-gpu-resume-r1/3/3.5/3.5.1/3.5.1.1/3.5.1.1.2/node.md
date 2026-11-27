# N747: 在 vLLM nightly build (CUDA 12.8+) 上运行 Qwen3-27B (BF16) 时，RTX 5090 的单卡吞吐量 (tokens

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N230

## Claim

在 vLLM nightly build (CUDA 12.8+) 上运行 Qwen3-27B (BF16) 时，RTX 5090 的单卡吞吐量 (tokens/s) 与 RTX 4090 (CUDA 12.6) 的实测比值，以及因驱动/内核未优化导致的额外内存带宽利用率损失百分比 [待核验: 需引用具体 benchmark 报告或社区实测数据]

## Corrected Claim

在 vLLM nightly build (CUDA 12.8+) 上运行 Qwen3-27B (BF16) 时，RTX 5090 的单卡吞吐量通常高于 RTX 4090 (CUDA 12.6)，但具体比值及因驱动/内核未优化导致的额外内存带宽利用率损失百分比需引用具体 benchmark 报告或社区实测数据确认。

## Evidence

[质询]该陈述包含具体的硬件性能比值和内存带宽利用率损失百分比，属于高度依赖具体驱动版本、内核优化状态及测试环境的经验事实，且参考来源为空，无法验证具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM RTX 5090 vs RTX 4090 throughput benchmark Qwen 27B
