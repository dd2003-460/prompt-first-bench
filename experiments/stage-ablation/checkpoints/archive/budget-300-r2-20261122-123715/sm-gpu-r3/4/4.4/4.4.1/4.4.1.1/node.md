# N316: 分支1 (Budget < $3000) 的可行解集修正：由于 Qwen3-27B INT8 权重 (27GB) 超过 RTX 4090 显存 (24GB)，且

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

分支1 (Budget < $3000) 的可行解集修正：由于 Qwen3-27B INT8 权重 (27GB) 超过 RTX 4090 显存 (24GB)，且 Offload 导致吞吐降至 5-10 tok/s (k_offload ≈ 0.05-0.1)，该分支在 'Quality=Low' 但 'Latency无硬约束' 下唯一可行解为 '1x RTX 4090 + INT8 (AWQ) + CPU Offload (3GB权重)', 其有效吞吐上限为 40 tok/s * 0.1 = 4 tok/s。

## Corrected Claim

分支1 (Budget < $3000) 的可行解集修正：由于 Qwen3-27B INT8 权重 (27GB) 超过 RTX 4090 显存 (24GB)，且 Offload 导致吞吐降至 5-10 tok/s，该分支在 'Quality=Low' 但 'Latency无硬约束' 下唯一可行解为 '1x RTX 4090 + INT8 (AWQ) + CPU Offload (3GB权重)', 其有效吞吐上限为 5-10 tok/s。

## Evidence

[质询]数值量级与逻辑推导存在内部矛盾：若 Offload 导致吞吐降至 5-10 tok/s，则有效吞吐上限应为 5-10 tok/s，而非 4 tok/s；且 40 tok/s * 0.1 = 4 tok/s 的推导假设了基础吞吐为 40 tok/s 且 Offload 系数为 0.1，这与前文提到的 5-10 tok/s 范围不一致。 | 先验知识/题面给定，逻辑校验未通过（数值推导不一致）
