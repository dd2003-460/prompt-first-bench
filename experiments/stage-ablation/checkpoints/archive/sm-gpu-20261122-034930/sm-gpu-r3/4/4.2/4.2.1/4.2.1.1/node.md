# N314: RTX 4090 (48GB) 在 INT8 精度下，当上下文长度从 4K 增加到 32K 时，KV Cache 显存占用从 0.67GB 线性增加至 10.7

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N111

## Claim

RTX 4090 (48GB) 在 INT8 精度下，当上下文长度从 4K 增加到 32K 时，KV Cache 显存占用从 0.67GB 线性增加至 10.7GB，导致总显存需求从 31.7GB 增加至 41.7GB，单卡 24GB 显存均无法满足，必须启用 CPU Offload 或双卡方案。

## Corrected Claim

RTX 4090 (24GB) 在 INT8 精度下，当上下文长度从 4K 增加到 32K 时，KV Cache 显存占用从 0.67GB 线性增加至 10.7GB，导致总显存需求从 31.7GB 增加至 41.7GB，单卡 24GB 显存无法满足，必须启用 CPU Offload 或双卡方案。

## Evidence

[质询]硬件规格错误：NVIDIA RTX 4090 的标准显存容量为 24GB，不存在 48GB 版本的 RTX 4090（48GB 通常对应 RTX 6000 Ada 或 A6000 等专业卡，或虚构配置）。 | RTX 4090 显存为 24GB，题干中 'RTX 4090 (48GB)' 存在事实性错误，且后续 '单卡 24GB 显存均无法满足' 与前提 '48GB' 自相矛盾（若为 48GB 卡，41.7GB 需求本可满足，无需 Offload 或双卡）。
