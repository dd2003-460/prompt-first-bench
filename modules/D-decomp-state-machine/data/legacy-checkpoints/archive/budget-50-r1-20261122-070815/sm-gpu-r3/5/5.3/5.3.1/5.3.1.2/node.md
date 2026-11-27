# N353: vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 A100 (Ampere) 的推理吞吐量提升幅度较小，约为 2-5%，因为 A100 缺乏原

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 A100 (Ampere) 的推理吞吐量提升幅度较小，约为 2-5%，因为 A100 缺乏原生 FP8 支持，主要受益于内存管理优化和 PagedAttention 算法改进，而非硬件加速指令集的更新。

## Corrected Claim

vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 A100 (Ampere) 的推理吞吐量提升幅度较小，主要受益于内存管理优化和软件栈改进，而非硬件加速指令集的更新，因为 A100 缺乏原生 FP8 支持。

## Evidence

[质询]具体数值幅度（2-5%）缺乏公开基准测试支持，且将PagedAttention（vLLM核心特性，非CUDA版本升级直接带来）归因于CUDA版本升级导致的性能提升存在因果归因混淆风险。 | 经验事实，逻辑自洽但缺来源支持；A100无FP8支持是已知硬件事实，但具体性能提升幅度及归因于CUDA版本升级的细节无法从第一性原理推出，且检索无可用来源。

## Search Query

vLLM CUDA version impact A100 Ampere inference throughput benchmark
