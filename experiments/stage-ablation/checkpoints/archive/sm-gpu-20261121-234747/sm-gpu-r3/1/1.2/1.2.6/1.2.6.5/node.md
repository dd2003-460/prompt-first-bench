# N194: L40S 48GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量（tokens/s）：L40S 的 FP16/BF16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

L40S 48GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量（tokens/s）：L40S 的 FP16/BF16 Tensor Core 算力（~91 TFLOPS）虽低于 H100，但在 Prefill 阶段仍具有优势，预计约为 Decode 的 15-25 倍（即 300-750 tokens/s），具体数值需验证 GDDR6 带宽对大矩阵乘法的制约

## Corrected Claim

L40S 48GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量受 GDDR6 带宽制约，具体数值需实测验证，预计显著高于 Decode 阶段。

## Evidence

[质询]该陈述包含具体的硬件性能预测数值（300-750 tokens/s）和倍数关系（15-25倍），属于经验事实。L40S 的 GDDR6 带宽（~864 GB/s）在 32K 上下文 Prefill 阶段可能成为瓶颈，导致实际吞吐量远低于纯算力理论值，且 Qwen3-27B 的具体模型架构参数（如层数、隐藏层维度）未提供，无法通过第一性原理严格推导出该具体数值范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体吞吐量数值无法仅凭逻辑推导得出，需实测或可靠基准测试数据支持）

## Search Query

L40S Qwen3-27B INT8 prefill throughput tokens per second
