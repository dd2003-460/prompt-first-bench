# N247: Qwen3-27B 在 RTX 3090 (24GB) 上运行 BF16 精度时，仅模型权重显存占用约为 54GB (27B * 2 bytes)，远超 24G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 RTX 3090 (24GB) 上运行 BF16 精度时，仅模型权重显存占用约为 54GB (27B * 2 bytes)，远超 24GB 显存容量，因此 BF16 单卡部署在物理上不可行，必须采用 INT8 或 INT4 量化。

## Corrected Claim

Qwen3-27B 在 RTX 3090 (24GB) 上运行 BF16 精度时，仅模型权重显存占用约为 54GB (27B * 2 bytes)，远超 24GB 显存容量，因此 BF16 单卡部署在物理上不可行，必须采用 INT8 或 INT4 量化。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 2字节/参数 = 54GB，远超24GB显存，物理上不可行。
