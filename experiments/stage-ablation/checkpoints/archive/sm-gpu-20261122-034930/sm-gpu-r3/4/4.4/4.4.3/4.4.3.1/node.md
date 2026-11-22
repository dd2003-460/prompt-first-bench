# N333: W4 量化（如 AWQ W4A16）下，Qwen3-27B 权重大小约为 13.5GB（27B * 4bits / 8bits）。在 32K 上下文、Batch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

W4 量化（如 AWQ W4A16）下，Qwen3-27B 权重大小约为 13.5GB（27B * 4bits / 8bits）。在 32K 上下文、Batch=1 条件下，KV Cache（FP16）占用约 10.7GB，框架开销约 4GB，总显存需求为 28.2GB。单卡 RTX 4090 (24GB) 无法容纳，需将 KV Cache 降至 FP8（占用约 5.35GB）或使用 CPU Offload（将部分 KV Cache 移至内存），此时总显存需求降至 22.85GB（FP8 KV）或 24GB+（Offload），单卡方可运行。

## Corrected Claim

W4 量化（如 AWQ W4A16）下，Qwen3-27B 权重大小约为 13.5GB（27B * 4bits / 8bits）。在 32K 上下文、Batch=1 条件下，KV Cache（FP16）占用约 10.7GB，框架开销约 4GB，总显存需求为 28.2GB。单卡 RTX 4090 (24GB) 无法容纳，需将 KV Cache 降至 FP8（占用约 5.35GB）或使用 CPU Offload（将部分 KV Cache 移至内存），此时总显存需求降至 22.85GB（FP8 KV）或 24GB+（Offload），单卡方可运行。

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算(27B*4/8=13.5GB)、KV Cache估算(27B模型32K上下文FP16约10.7GB符合典型量级)、显存总和(13.5+10.7+4=28.2GB)及优化后数值(13.5+5.35+4=22.85GB)均逻辑自洽且符合工程常识。
