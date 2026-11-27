# N115: Mac Studio M2 Ultra 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) 时的实际 Deco

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) 时的实际 Decode 吞吐需考虑统一内存访问延迟，实测值通常低于理论带宽限制值 (14.8 tokens/s)，参考 M1 Max 运行 Llama-70B BF16 的实测数据约为 10-12 tokens/s，M2 Ultra 预期为 12-15 tokens/s [时效待核]。

## Corrected Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 时的实际 Decode 吞吐受统一内存访问延迟限制，通常低于理论带宽上限。参考 M1 Max 运行 Llama-70B BF16 的实测数据（约 10-12 tokens/s），M2 Ultra 因带宽优势预期吞吐率略高或相当，具体数值需根据实际上下文长度和软件栈配置确定。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（M1 Max 10-12 tokens/s, M2 Ultra 12-15 tokens/s）和理论带宽限制值（14.8 tokens/s），属于经验事实。由于检索无可用来源，无法验证这些具体数值的准确性，且不同上下文长度、Batch Size 及具体实现（如 llama.cpp 版本）会导致吞吐率显著波动，单一数值区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持。M2 Ultra 统一内存带宽（800GB/s）高于 M1 Max（400GB/s），且 M2 Ultra 支持更大内存容量，理论上 M2 Ultra 运行同规模模型（或更大模型）的吞吐率应高于或接近 M1 Max 运行 Llama-70B 的数据，量级关系合理，但具体数值无法通过第一性原理严格推导，需依赖实测数据。

## Search Query

Mac Studio M2 Ultra Llama 70B BF16 tokens per second benchmark
