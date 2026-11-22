# N125: RTX 4090 (Ada Lovelace) 的显存带宽为 1008 GB/s，HBM3 带宽为 3.35 TB/s (H100) 或 5.3 TB/s (M

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (Ada Lovelace) 的显存带宽为 1008 GB/s，HBM3 带宽为 3.35 TB/s (H100) 或 5.3 TB/s (MI300X)；在 Memory-Bound 的 Decode 阶段，TPS 与显存带宽呈正相关，公式为 TPS ≈ (Effective_Bandwidth × Utilization) / (Bytes_Per_Token)，其中 Bytes_Per_Token 包含权重读取和 KV Cache 读取。

## Corrected Claim

RTX 4090 (Ada Lovelace) 的显存带宽为 1008 GB/s，HBM3 带宽为 3.35 TB/s (H100) 或 5.3 TB/s (MI300X)；在 Memory-Bound 的 Decode 阶段，TPS 与显存带宽呈正相关，公式为 TPS ≈ (Effective_Bandwidth × Utilization) / (Bytes_Per_Token)，其中 Bytes_Per_Token 包含权重读取和 KV Cache 读取。

## Evidence

检索失败: no sources from any channel (all 5 failed)
