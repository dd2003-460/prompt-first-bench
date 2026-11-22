# N262: H100 SXM 的 3350 GB/s 带宽相比 A100 的 2039 GB/s 提升 64%，但在 Qwen3-27B 单卡推理中，由于计算密度（FLOP

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

H100 SXM 的 3350 GB/s 带宽相比 A100 的 2039 GB/s 提升 64%，但在 Qwen3-27B 单卡推理中，由于计算密度（FLOPS）提升更大，带宽不再是主要瓶颈，吞吐量提升主要来源于 Tensor Core 加速，预期吞吐量可达 40-60 tokens/s。

## Corrected Claim

H100 SXM 的 3350 GB/s 带宽相比 A100 的 2039 GB/s 提升约 64%，在 Qwen3-27B 单卡推理中，由于计算密度提升显著，带宽瓶颈缓解，吞吐量主要受 Tensor Core 加速驱动，具体吞吐量取决于推理框架与量化策略，通常在数十 tokens/s 量级。

## Evidence

[质询]吞吐量数值（40-60 tokens/s）缺乏具体推理框架、Batch Size 及量化策略（如 FP16/INT8）的限定，属于高度依赖工程实现的经验事实，且不同优化方案下差异巨大，无法仅凭硬件参数推导。 | source=knowledge，硬件带宽与算力提升比例逻辑自洽，但具体吞吐量数值为经验事实，缺乏来源支持且受工程变量影响大，故降级。
