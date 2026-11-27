# N248: Qwen3-27B 在 RTX 3090 (24GB) 上运行 INT8 精度时，模型权重显存占用约为 27GB (27B * 1 byte)，仍超过 24GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 RTX 3090 (24GB) 上运行 INT8 精度时，模型权重显存占用约为 27GB (27B * 1 byte)，仍超过 24GB 显存容量，导致单卡 INT8 部署不可行，必须进一步量化至 INT4 或采用多卡/Offload 方案。

## Corrected Claim

Qwen3-27B 在 RTX 3090 (24GB) 上运行 INT8 精度时，模型权重显存占用约为 27GB (27B * 1 byte)，仍超过 24GB 显存容量，导致单卡 INT8 部署不可行，必须进一步量化至 INT4 或采用多卡/Offload 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8下权重占用约27GB，确实超过RTX 3090的24GB显存，单卡部署不可行的结论符合硬件规格与量化原理。
