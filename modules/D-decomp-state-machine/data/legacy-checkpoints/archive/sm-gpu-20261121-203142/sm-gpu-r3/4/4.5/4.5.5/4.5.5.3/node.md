# N297: FP8 与 INT4 在 RTX 4090 (Ada Lovelace) 上的硬件支持差异：Ada 架构原生支持 FP8 Tensor Cores，而 INT4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

FP8 与 INT4 在 RTX 4090 (Ada Lovelace) 上的硬件支持差异：Ada 架构原生支持 FP8 Tensor Cores，而 INT4 需通过软件库 (如 TensorRT-LLM) 模拟或特定指令，FP8 的实际算力效率通常高于 INT4，因此在相同显存带宽下，FP8 的有效 TPS 可能略高于同等显存占用的 INT4 方案。

## Corrected Claim

FP8 与 INT4 在 RTX 4090 (Ada Lovelace) 上的硬件支持差异：Ada 架构原生支持 FP8 Tensor Cores，而 INT4 需通过软件库 (如 TensorRT-LLM) 模拟或特定指令，FP8 的实际算力效率通常高于 INT4，因此在相同显存带宽下，FP8 的有效 TPS 可能略高于同等显存占用的 INT4 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：Ada Lovelace架构确实原生支持FP8 Tensor Cores，而INT4通常依赖软件模拟或特定指令，FP8在硬件层面的算力效率通常优于INT4，符合硬件架构常识。
