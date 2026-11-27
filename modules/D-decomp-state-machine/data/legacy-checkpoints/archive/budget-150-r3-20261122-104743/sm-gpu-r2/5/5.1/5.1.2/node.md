# N147: RTX 4080 Super 显存带宽为 717 GB/s，显存容量 16GB，支持 FP8 计算单元，单卡 BF16/FP8 27B 模型推理不可行（显存不足

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

RTX 4080 Super 显存带宽为 717 GB/s，显存容量 16GB，支持 FP8 计算单元，单卡 BF16/FP8 27B 模型推理不可行（显存不足），仅支持 4-bit 量化或 CPU Offload 方案

## Corrected Claim

RTX 4080 Super 显存带宽为 717 GB/s，显存容量 16GB，支持 FP8 计算单元，单卡 BF16/FP8 27B 模型推理不可行（显存不足），仅支持 4-bit 量化或 CPU Offload 方案

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4080 Super 显存带宽 717 GB/s、容量 16GB 符合硬件规格；27B 模型在 BF16 下需约 54GB 显存，远超 16GB，故单卡推理不可行，逻辑自洽。
