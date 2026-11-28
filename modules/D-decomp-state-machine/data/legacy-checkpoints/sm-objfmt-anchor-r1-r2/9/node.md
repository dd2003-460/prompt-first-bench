# N32: 多卡方案 (如 2x RTX 4090) 的有效吞吐量并非单卡的 2 倍，由于 PCIe 通信开销和负载不均衡，实际加速比 (Speedup Factor) 通

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡方案 (如 2x RTX 4090) 的有效吞吐量并非单卡的 2 倍，由于 PCIe 通信开销和负载不均衡，实际加速比 (Speedup Factor) 通常仅为 1.6-1.8x。计算 TCO 时需将 'Effective_Throughput' 替换为 'Nominal_Throughput * 1.7'，这会导致多卡方案的单位 token 成本比单卡高 15-25%。

## Corrected Claim

多卡方案 (如 2x RTX 4090) 的有效吞吐量并非单卡的 2 倍，由于 PCIe 通信开销和负载不均衡，实际加速比 (Speedup Factor) 通常仅为 1.6-1.8x。计算 TCO 时需将 'Effective_Throughput' 替换为 'Nominal_Throughput * 1.7'，这会导致多卡方案的单位 token 成本比单卡高 15-25%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
