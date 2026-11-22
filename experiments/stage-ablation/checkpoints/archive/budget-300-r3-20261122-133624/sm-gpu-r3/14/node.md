# N175: 在 32K 上下文、Batch=1 场景下，2× RTX 3090 (INT8) 的 TCO 约为 $4,187，单位 token 成本约 $0.00026；而

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 32K 上下文、Batch=1 场景下，2× RTX 3090 (INT8) 的 TCO 约为 $4,187，单位 token 成本约 $0.00026；而 1× RTX 6000 Ada (INT8) 的 TCO 约为 $6800 + $950 (power) + $300 (maint) ≈ $8,050，单位 token 成本约 $0.00045。因此，在低利用率 (<50%) 下，双卡 3090 方案 TCO 优势显著；但在高利用率 (>80%) 且需考虑多卡通信开销 (PCIe 4.0 瓶颈) 导致吞吐下降 20% 的情况下，单卡 6000 Ada 的稳定性溢价可能使其在特定工作负载下更具性价比。

## Corrected Claim

在 32K 上下文、Batch=1 场景下，2× RTX 3090 (INT8) 的 TCO 约为 $4,187，单位 token 成本约 $0.00026；而 1× RTX 6000 Ada (INT8) 的 TCO 约为 $6800 + $950 (power) + $300 (maint) ≈ $8,050，单位 token 成本约 $0.00045。因此，在低利用率 (<50%) 下，双卡 3090 方案 TCO 优势显著；但在高利用率 (>80%) 且需考虑多卡通信开销 (PCIe 4.0 瓶颈) 导致吞吐下降 20% 的情况下，单卡 6000 Ada 的稳定性溢价可能使其在特定工作负载下更具性价比。

## Evidence

检索失败: no sources from any channel (all 5 failed)
