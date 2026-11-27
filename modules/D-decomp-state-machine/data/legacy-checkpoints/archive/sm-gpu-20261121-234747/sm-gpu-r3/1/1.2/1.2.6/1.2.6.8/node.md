# N197: AMD MI300X 192GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量（tokens/s）：MI300X 的 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

AMD MI300X 192GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量（tokens/s）：MI300X 的 FP16 Tensor Core 算力（~1300 TFLOPS）极高，Prefill 速度预计远超 Decode，约为 1000-2000 tokens/s，但受限于 ROCm 生态中 FlashAttention 等算子的优化程度，实际性能可能低于理论值

## Corrected Claim

AMD MI300X 192GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Prefill 阶段吞吐量预计较高，具体数值取决于 ROCm 生态中 FlashAttention 等算子的优化程度，理论上限受限于 FP16 Tensor Core 算力（~1300 TFLOPS），实际性能可能低于理论峰值。

## Evidence

[质询]该陈述包含具体的硬件算力参数（~1300 TFLOPS）和性能预测数值（1000-2000 tokens/s），属于经验事实。虽然MI300X的FP16算力确实在此量级，但Prefill吞吐量受模型架构、序列长度、内存带宽及软件栈（ROCm/FlashAttention）优化程度影响极大，缺乏具体基准测试数据支持，1000-2000 tokens/s仅为粗略估算，可能因实际优化不足而显著偏低或偏高。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMD MI300X Qwen3-27B INT8 prefill throughput tokens per second ROCm
