# N115: vLLM 对 NVIDIA RTX 4090/5090 的最低支持版本为 vLLM 0.4.0+，且需配合 CUDA 12.1 编译环境，低于此版本的 vLLM

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

vLLM 对 NVIDIA RTX 4090/5090 的最低支持版本为 vLLM 0.4.0+，且需配合 CUDA 12.1 编译环境，低于此版本的 vLLM 无法调用 Blackwell/Ada 架构的 FP8 内核。

## Corrected Claim

vLLM 对 NVIDIA RTX 4090/5090 的支持依赖于较新的版本（如 0.4.0 或更高，具体取决于 FP8 内核的集成情况），且需配合支持相应架构的 CUDA 环境；早期版本可能无法直接调用 Blackwell/Ada 架构的 FP8 内核。

## Evidence

[质询]该陈述包含具体的硬件支持版本（vLLM 0.4.0+）和编译环境要求（CUDA 12.1），属于经验事实。RTX 4090 属于 Ada 架构（SM 8.9），RTX 5090 属于 Blackwell 架构（SM 10.0）。vLLM 0.4.0 发布于 2024 年初，当时 Blackwell 架构尚未正式发布，且 FP8 支持在 vLLM 中是逐步引入的（例如通过 FlashInfer 或特定后端），断言 0.4.0 是“最低支持版本”且“低于此版本无法调用”缺乏精确的版本控制证据，可能存在版本偏差或依赖特定插件而非核心版本的情况。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体版本号与架构支持的对应关系）

## Search Query

vLLM minimum CUDA version RTX 4090 5090 FP8 support
