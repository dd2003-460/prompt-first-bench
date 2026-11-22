# N427: RTX 4090 (Ada) 的 INT8 Tensor Core 吞吐量约为 BF16 Tensor Core 的 2 倍，因此运行 AWQ INT8 量化模

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148

## Claim

RTX 4090 (Ada) 的 INT8 Tensor Core 吞吐量约为 BF16 Tensor Core 的 2 倍，因此运行 AWQ INT8 量化模型时，计算密集型的 Prefill 阶段吞吐量预计提升约 1.8-2.0 倍，而 Decode 阶段受显存带宽限制，提升幅度较小（约 10-20%），具体 tokens/s 数值需实测确认。

## Corrected Claim

RTX 4090 (Ada) 的 INT8 Tensor Core 理论吞吐量约为 BF16 的 2 倍。在运行 INT8 量化模型时，计算密集型的 Prefill 阶段理论上可获得接近 2 倍的算力提升，但实际吞吐量受软件栈优化、内存访问模式等因素影响，需实测确认；Decode 阶段主要受显存带宽限制，提升幅度通常较小。

## Evidence

[质询]该陈述包含具体的硬件性能比率（INT8 vs BF16 为 2 倍）及特定量化模型（AWQ）在特定阶段（Prefill/Decode）的性能提升幅度（1.8-2.0 倍 / 10-20%），属于经验事实。虽然逻辑上 INT8 算力高于 BF16 且 Decode 受带宽限制是合理的，但具体的倍数和百分比缺乏来源支持，且 AWQ 通常指 4-bit 量化，此处用于 INT8 场景可能存在术语或场景混淆（尽管 AWQ 也有 8-bit 变体，但性能提升幅度高度依赖具体实现和硬件驱动优化，不能仅凭理论算力比直接得出 1.8-2.0 倍的实测预期）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。INT8 理论算力约为 BF16 的 2 倍符合 NVIDIA 架构常识，但具体到 AWQ 模型在 RTX 4090 上的实际吞吐量提升幅度属于需实测的经验数据，无法从第一性原理严格推出具体数值区间。

## Search Query

RTX 4090 INT8 vs BF16 inference throughput vLLM Qwen3 benchmark
