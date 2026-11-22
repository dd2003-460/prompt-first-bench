# N128: RTX 5090 32GB 显存在 FP8 精度下运行 Qwen3-27B 且上下文为 32K 时，可用显存余量为 1.41GB (计算式: 32GB - 27

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

RTX 5090 32GB 显存在 FP8 精度下运行 Qwen3-27B 且上下文为 32K 时，可用显存余量为 1.41GB (计算式: 32GB - 27.18GB权重 - 12.88GB KV Cache [基于N32 BF16值减半] + 2GB 激活值/框架开销预留)，该余量低于安全阈值 (通常需 >2GB 以防止 OOM 或频繁 Swap)，表明单卡 32K 上下文 FP8 推理存在显存溢出风险，需启用 KV Cache 量化 (如 INT8 KV) 或限制最大并发 Batch Size 为 1。

## Corrected Claim

RTX 5090 32GB 显存在 FP8 精度下运行 Qwen3-27B 且上下文为 32K 时，权重占用约 13.5GB (27B * 1 byte)，KV Cache 占用约 1-2GB (取决于具体架构参数)，加上激活值/框架开销约 2-4GB，总占用约 16-19GB，显存余量充足（>10GB），单卡 32K 上下文 FP8 推理不存在显存溢出风险，无需强制启用 KV Cache 量化或限制 Batch Size 为 1。

## Evidence

[质询]KV Cache 显存占用计算存在严重逻辑错误：Qwen3-27B 的 KV Cache 在 32K 上下文下，即使使用 BF16 也远小于 12.88GB（通常约为 1-2GB 量级，取决于层数和头数），FP8 下更小；陈述中声称 '12.88GB KV Cache [基于N32 BF16值减半]' 暗示 BF16 下为 25.76GB，这远超 32GB 显存卡能承载的合理 KV 大小，且与 27B 模型的架构参数不符，导致总显存占用计算（27.18 + 12.88 + 2 = 42.06GB）远超 32GB 物理显存，结论中的 '1.41GB 余量' 在数学上不可能成立（32 - 42.06 = -10.06GB）。 | 逻辑校验失败：KV Cache 数值量级严重违背模型架构常识，导致总显存需求超过物理显存上限，计算式内部矛盾。
