# N145: 若使用 FP32 存储 Scale/Zero Point，Overhead 翻倍至 1.698 GB，总权重显存 ≈ 15.29 GB，需重新评估 24GB 显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

若使用 FP32 存储 Scale/Zero Point，Overhead 翻倍至 1.698 GB，总权重显存 ≈ 15.29 GB，需重新评估 24GB 显存卡的可行性边界（来源：计算推导）

## Corrected Claim

若使用 FP32 存储 Scale/Zero Point，Overhead 翻倍至 1.698 GB，总权重显存 ≈ 15.29 GB，需重新评估 24GB 显存卡的可行性边界（来源：计算推导）

## Evidence

先验知识/题面给定，逻辑校验通过：FP32 为 4 字节，若原 Overhead 为 0.849 GB（对应 FP16/2字节），翻倍后为 1.698 GB，数值量级与计算逻辑自洽。

## Search Query

INT4 quantization FP32 scale zero point memory overhead
