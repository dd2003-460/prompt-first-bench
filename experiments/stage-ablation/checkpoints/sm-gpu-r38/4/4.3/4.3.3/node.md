# N62: 2x RTX 4090 (96GB total VRAM) 的聚合内存带宽为 1.5 TB/s (2 * 1008 GB/s)，支持 NVLink 互联，其推理

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

2x RTX 4090 (96GB total VRAM) 的聚合内存带宽为 1.5 TB/s (2 * 1008 GB/s)，支持 NVLink 互联，其推理吞吐量理论上限约为 25-30 tokens/s

## Corrected Claim

2x RTX 4090 (96GB total VRAM) 的聚合内存带宽为 1.5 TB/s (2 * 1008 GB/s)，支持 NVLink 互联。其推理吞吐量取决于模型规模与精度，对于 70B 级别模型，理论解码速度通常在 100-200 tokens/s 量级，而非固定的 25-30 tokens/s。

## Evidence

[质询]推理吞吐量理论上限 25-30 tokens/s 严重低估且缺乏模型规模前提。对于 96GB 显存可承载的大模型（如 70B 参数），在 1.5 TB/s 带宽下，理论解码速度通常可达 100-200+ tokens/s（取决于具体架构和精度），25-30 tokens/s 更接近单卡或低带宽场景，或与特定小模型/高延迟场景混淆。 | source=knowledge，硬件规格（2x 4090, 96GB, 1.5TB/s, NVLink）逻辑自洽且符合先验知识；但吞吐量数值缺乏模型规模等关键前提，且与典型大模型推理性能量级不符，故降级。
