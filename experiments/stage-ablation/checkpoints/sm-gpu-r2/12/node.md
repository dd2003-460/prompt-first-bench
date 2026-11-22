# N170: 候选硬件全集的显存容量档位界定：基于 Qwen3-27B 32K 上下文需求，显存 <24GB 的 GPU（如 RTX 4080S 16GB, RTX 3060

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件全集的显存容量档位界定：基于 Qwen3-27B 32K 上下文需求，显存 <24GB 的 GPU（如 RTX 4080S 16GB, RTX 3060 12GB）因无法容纳 FP8 权重+KV Cache 而被排除；24-32GB 档位（RTX 4090, RTX 5090, RX 7900 XTX）为消费级核心候选；48-80GB 档位（L40S, A100, H100）为专业/数据中心核心候选；>128GB 档位（MI300X, H100 NVL）仅在高并发或 BF16 全精度场景纳入。

## Corrected Claim

候选硬件全集的显存容量档位界定：基于 Qwen3-27B 32K 上下文需求，显存 <24GB 的 GPU（如 RTX 4080S 16GB, RTX 3060 12GB）因无法容纳 FP8 权重+KV Cache 而被排除；24-32GB 档位（RTX 4090, RTX 5090, RX 7900 XTX）为消费级核心候选；48-80GB 档位（L40S, A100, H100）为专业/数据中心核心候选；>128GB 档位（MI300X, H100 NVL）仅在高并发或 BF16 全精度场景纳入。

## Evidence

检索失败: no sources from any channel (all 5 failed)
