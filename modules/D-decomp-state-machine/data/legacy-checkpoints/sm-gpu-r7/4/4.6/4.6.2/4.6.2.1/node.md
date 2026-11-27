# N231: Qwen3-27B 在 RTX 4090 上的 INT8 量化权重显存占用为 27GB (27B * 1 byte)，超出 RTX 4090 24GB 物理显存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

Qwen3-27B 在 RTX 4090 上的 INT8 量化权重显存占用为 27GB (27B * 1 byte)，超出 RTX 4090 24GB 物理显存，导致 vLLM 和 llama.cpp 均必须启用 CPU Offload 或 FP16 KV Cache 混合策略，这是吞吐量差异的架构性前提。

## Corrected Claim

Qwen3-27B 在 RTX 4090 上的 INT8 量化权重显存占用为 27GB (27B * 1 byte)，超出 RTX 4090 24GB 物理显存，导致 vLLM 和 llama.cpp 均必须启用 CPU Offload 或 FP16 KV Cache 混合策略，这是吞吐量差异的架构性前提。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8下占用约27GB显存，确实超过RTX 4090的24GB物理显存，因此必须启用CPU Offload或混合策略，逻辑自洽且符合硬件规格常识。
