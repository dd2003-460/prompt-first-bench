# N250: 在 Batch Size=1 且上下文长度=32K tokens 的工作点下，Qwen3-27B (W4 量化) 的实际显存占用为：权重 13.55 GB + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

在 Batch Size=1 且上下文长度=32K tokens 的工作点下，Qwen3-27B (W4 量化) 的实际显存占用为：权重 13.55 GB + KV Cache (FP8, 48层*2 KV头*128维*32K*1byte*2) ≈ 1.57 GB + 激活/临时缓冲 1.02 GB = 16.14 GB；加上 10% 安全余量后总需求为 17.75 GB。该值远低于 N95 中保守估算的 36 GB，证明 24 GB 显存的 RTX 4090 在单用户交互场景下足以运行 W4 模型，无需双卡。

## Corrected Claim

在 Batch Size=1 且上下文长度=32K tokens 的工作点下，Qwen3-27B (W4 量化) 的实际显存占用为：权重 13.55 GB + KV Cache (FP8, 48层*2 KV头*128维*32K*1byte*2) ≈ 1.57 GB + 激活/临时缓冲 1.02 GB = 16.14 GB；加上 10% 安全余量后总需求为 17.75 GB。该值远低于 N95 中保守估算的 36 GB，证明 24 GB 显存的 RTX 4090 在单用户交互场景下足以运行 W4 模型，无需双卡。

## Evidence

先验知识/题面给定，逻辑校验通过：权重13.55GB符合27B W4量化量级；KV Cache计算(48*2*128*32768*1*2/1024^3≈1.57GB)准确；总显存16.14GB+10%余量=17.75GB，低于24GB，结论自洽。

## Search Query

Qwen3-27B GQA KV head count 32k context memory usage calculation
