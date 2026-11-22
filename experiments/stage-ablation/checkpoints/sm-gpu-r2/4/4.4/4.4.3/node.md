# N107: 若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s (受 PCIe 瓶颈限制，有效带宽可能降至 1.5x 单卡水平)。若采用 1x H100 (80GB)，显存充足，带宽 3350 GB/s。在 BF16 精度下，2x 4090 因显存不足不可行，除非降至 FP8 (27GB 权重 + 1GB KV = 28GB < 48GB)，此时 2x 4090 可行。

## Corrected Claim

若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s (受 PCIe 瓶颈限制，有效带宽可能降至 1.5x 单卡水平)。若采用 1x H100 (80GB)，显存充足，带宽 3350 GB/s。在 BF16 精度下，2x 4090 因显存不足不可行，除非降至 FP8 (27GB 权重 + 1GB KV = 28GB < 48GB)，此时 2x 4090 可行。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存24GB，2卡共48GB，带宽1008GB/s*2=2016GB/s；H100显存80GB，带宽3350GB/s；BF16下55GB需求超过48GB，FP8下28GB需求小于48GB，数值与逻辑均自洽。

## Search Query

2x RTX 4090 tensor parallel 48GB VRAM Qwen3-27B FP8 feasibility
