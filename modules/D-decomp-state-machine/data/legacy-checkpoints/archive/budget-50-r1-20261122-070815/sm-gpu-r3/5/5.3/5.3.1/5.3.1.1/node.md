# N352: vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 RTX 4090 (Ada Lovelace) 的推理吞吐量 (tokens/s) 提升幅度

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 RTX 4090 (Ada Lovelace) 的推理吞吐量 (tokens/s) 提升幅度约为 5-15%，主要得益于 cuDNN 和 TensorRT 对 FP8/INT8 内核的优化；具体数值需对比 vLLM v0.4.0 (CUDA 12.1) 与 v0.6.0+ (CUDA 12.4) 的官方基准测试报告。

## Corrected Claim

vLLM 在 CUDA 12.1 到 12.4 版本升级过程中，对 RTX 4090 的推理吞吐量通常会有所提升，主要得益于底层库（如 cuDNN）的优化，但具体提升幅度取决于模型架构、批处理大小及具体配置，需参考官方或社区基准测试报告。

## Evidence

[质询]该陈述包含具体的性能提升幅度（5-15%）和特定版本/硬件组合的基准测试结论，属于经验事实。由于缺乏外部来源支持，且不同环境配置下性能波动可能远超此范围，无法确认该具体数值区间的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM CUDA 12.4 vs 12.1 benchmark RTX 4090 performance improvement
