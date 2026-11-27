# N550: Intel Max 1550 48GB 在 INT8 量化下，Qwen3-27B 权重占用 27GB，框架及运行时开销约 1.5-2.5GB（基于 PyTorc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N192

## Claim

Intel Max 1550 48GB 在 INT8 量化下，Qwen3-27B 权重占用 27GB，框架及运行时开销约 1.5-2.5GB（基于 PyTorch/llama.cpp 典型开销），剩余可用显存 = 48 - 27 - 2 = 19 GB（取中值2GB开销）。

## Corrected Claim

Intel Max 1550 48GB 在 INT8 量化下，Qwen3-27B 权重占用 27GB，框架及运行时开销约 1.5-2.5GB（基于 PyTorch/llama.cpp 典型开销），剩余可用显存 = 48 - 27 - 2 = 19 GB（取中值2GB开销）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B在INT8下权重约27GB（27B*1Byte），PyTorch/llama.cpp运行时开销1.5-2.5GB符合典型量级，48-27-2=19GB计算正确。
