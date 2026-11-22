# N103: 消费级显卡代际筛选：排除 RTX 3090 (24GB) 作为首选，因其在 BF16 下无法容纳 32K 上下文 (需 Offload)，且在 INT8 下显存

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

消费级显卡代际筛选：排除 RTX 3090 (24GB) 作为首选，因其在 BF16 下无法容纳 32K 上下文 (需 Offload)，且在 INT8 下显存利用率 (27GB/24GB) 溢出，必须依赖 CPU Offload 导致延迟不可控；仅保留 RTX 4090 (24GB) 和 RTX 5090 (32GB) 进入多卡/单卡对比池。

## Corrected Claim

消费级显卡代际筛选：排除 RTX 3090 (24GB) 作为首选，因其在 BF16 下无法容纳 32K 上下文 (需 Offload)，且在 INT8 下显存利用率 (27GB/24GB) 溢出，必须依赖 CPU Offload 导致延迟不可控；仅保留 RTX 4090 (24GB) 和 RTX 5090 (32GB) 进入多卡/单卡对比池。

## Evidence

检索失败: no sources from any channel (all 5 failed)
