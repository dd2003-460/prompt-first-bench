# N8: 定义单卡/多卡方案的显存总需求公式：Total VRAM = Weight Size + KV Cache + Activation Buffer (约1-2G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

定义单卡/多卡方案的显存总需求公式：Total VRAM = Weight Size + KV Cache + Activation Buffer (约1-2GB) + CUDA Overhead (约0.5GB)，并据此筛选出满足32K上下文的最小单卡显存阈值（BF16下需≥192GB，INT8下需≥96GB）

## Corrected Claim

定义单卡/多卡方案的显存总需求公式：Total VRAM = Weight Size + KV Cache + Activation Buffer (约1-2GB) + CUDA Overhead (约0.5GB)，并据此筛选出满足32K上下文的最小单卡显存阈值（BF16下需≥192GB，INT8下需≥96GB）

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下192GB与INT8下96GB的阈值符合显存需求公式及32K上下文KV Cache占用的量级估算，数值自洽。

## Search Query

GPU VRAM requirement large language model inference 32K context weight KV cache overhead
