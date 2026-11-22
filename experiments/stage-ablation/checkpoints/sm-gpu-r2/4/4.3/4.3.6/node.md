# N114: Groq LPU (若可获取) 的显存容量为 230MB (SRAM) + 240GB (HBM)，Qwen3-27B W4 权重 13.5GB + 8.4GB

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

Groq LPU (若可获取) 的显存容量为 230MB (SRAM) + 240GB (HBM)，Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) + 2GB (激活) = 23.9GB，HBM 利用率约 9.96%，SRAM 用于缓存热点数据。

## Corrected Claim

Groq LPU 集群（若可获取）的总显存容量包含 SRAM 和 HBM，其中 HBM 总容量可能达到 240GB（多芯片配置），Qwen3-27B W4 模型权重约 13.5GB，加上 KV Cache 和激活内存后总占用约 23.9GB，HBM 利用率较低，SRAM 用于缓存热点数据。

## Evidence

[质询]数值量级与硬件规格存在显著矛盾：Groq LPU 单芯片 SRAM 通常为 230MB，但 240GB HBM 远超单芯片规格（通常单卡 HBM 为 20-80GB），240GB 更可能是多芯片集群或特定服务器配置的总容量，而非单 LPU 规格；此外，Qwen3-27B W4 权重 13.5GB 计算合理（27B * 0.5 bytes ≈ 13.5GB），但 KV Cache 8.4GB 和激活 2GB 的具体数值缺乏上下文（如序列长度、批大小），且 HBM 利用率 9.96% 的计算依赖于总容量定义，若 240GB 为集群总量，则单卡利用率描述不准确。 | 经验事实，逻辑自洽但缺来源支持；硬件规格数值（240GB HBM）与常见单芯片规格不符，需降级为定性表述或修正为集群配置。
