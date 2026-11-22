# N266: A100 40GB 的 TDP 400W 与平均功耗 260W 之间的差异机制：源于 Memory-bound 推理中计算单元（CUDA Cores/Tenso

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

A100 40GB 的 TDP 400W 与平均功耗 260W 之间的差异机制：源于 Memory-bound 推理中计算单元（CUDA Cores/Tensor Cores）的空闲率，以及 HBM2e 访问延迟导致的流水线气泡，该比例（65%）在 Batch=1 时高于 Batch>1 场景（后者趋近 80-90%）。

## Corrected Claim

A100 40GB 的 TDP 400W 与平均功耗 260W 之间的差异机制：源于 Memory-bound 推理中计算单元（CUDA Cores/Tensor Cores）的空闲率，以及 HBM2e 访问延迟导致的流水线气泡，该比例（65%）在 Batch=1 时高于 Batch>1 场景（后者趋近 80-90%）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 TDP 400W 与典型推理功耗 260W 的差异符合 Memory-bound 场景下计算单元空闲及 HBM 延迟导致能效比下降的物理机制，Batch=1 时利用率低于 Batch>1 符合 GPU 调度常识。
