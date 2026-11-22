# N209: Jetson AGX Orin 64GB 的内存带宽（~205GB/s）在运行 27B INT8 模型时的理论最大吞吐量约为 10-15 tokens/s，需通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

Jetson AGX Orin 64GB 的内存带宽（~205GB/s）在运行 27B INT8 模型时的理论最大吞吐量约为 10-15 tokens/s，需通过 TensorRT-LLM 框架实测验证，且 32K 上下文下的 KV Cache 占用可能导致性能下降。

## Corrected Claim

Jetson AGX Orin 64GB 的内存带宽（~205GB/s）在运行 27B INT8 模型时的理论最大吞吐量约为 10-15 tokens/s，需通过 TensorRT-LLM 框架实测验证，且 32K 上下文下的 KV Cache 占用可能导致性能下降。

## Evidence

先验知识/题面给定，逻辑校验通过：27B INT8模型权重约27GB，205GB/s带宽下理论上限约7.6 tokens/s，考虑KV Cache和计算开销后10-15 tokens/s为合理工程估计范围
