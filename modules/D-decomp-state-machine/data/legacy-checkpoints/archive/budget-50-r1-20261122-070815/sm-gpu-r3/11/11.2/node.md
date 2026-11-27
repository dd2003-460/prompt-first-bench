# N431: RTX 4090 的 INT4 Tensor Core 吞吐量约为 BF16 的 4 倍，而 RTX 3090 无原生 INT4 Tensor Core 支持（

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N149

## Claim

RTX 4090 的 INT4 Tensor Core 吞吐量约为 BF16 的 4 倍，而 RTX 3090 无原生 INT4 Tensor Core 支持（需软件模拟），因此运行 INT4 模型时，RTX 4090 的 Prefill 速度优势远超 15%，可能在 2-3 倍以上；Decode 阶段因带宽瓶颈，优势收窄至 10-20% 区间，具体数值需对比两卡在 Qwen3-27B INT4 下的实测 tokens/s。

## Corrected Claim

RTX 4090 原生支持 INT4 Tensor Core，而 RTX 3090 需软件模拟，因此在运行 INT4 模型时，RTX 4090 在 Prefill 阶段通常具有显著的速度优势（可能远超 15%），而在 Decode 阶段因受显存带宽瓶颈限制，优势相对收窄。具体性能提升倍数需依据 Qwen3-27B INT4 的实测 tokens/s 数据确定。

## Evidence

[质询]该陈述包含具体的硬件规格（INT4 Tensor Core支持情况）和性能预测数值（2-3倍、10-20%），属于经验事实。虽然RTX 4090确实支持INT4 Tensor Core而RTX 3090不支持（需软件模拟）这一硬件差异是成立的，但具体的性能提升倍数（Prefill 2-3倍，Decode 10-20%）高度依赖于具体的模型架构、量化方法（如GPTQ/AWQ）、Batch Size以及内存带宽的实际利用率，无法仅凭硬件规格从第一性原理严格推导出如此精确的区间，且缺乏实测数据支持。 | 经验事实，逻辑自洽（硬件差异导致Prefill优势大，带宽瓶颈导致Decode优势小符合直觉）但缺来源支持，且具体数值缺乏实测依据。

## Search Query

RTX 4090 vs RTX 3090 INT4 inference throughput Qwen3 benchmark
