# N190: A100 80GB 在 Qwen3-27B BF16, batch=1 下的 Decode 阶段显存带宽瓶颈量化：理论最大吞吐 T_decode_max = H

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

A100 80GB 在 Qwen3-27B BF16, batch=1 下的 Decode 阶段显存带宽瓶颈量化：理论最大吞吐 T_decode_max = HBM_Bandwidth / (P_params * bytes_per_param) = 2039 GB/s / (27e9 * 2 bytes) ≈ 37.7 tokens/s，实际 52 tokens/s 超出此理论值，表明 A100 在此配置下并非纯带宽受限，或实际权重加载采用了稀疏/缓存优化 [待核验]。

## Corrected Claim

A100 80GB 在 Qwen3-27B BF16, batch=1 下的 Decode 阶段理论带宽瓶颈约为 37.7 tokens/s。若实测吞吐超过此值，需确认是否采用了量化、稀疏加载或 KV Cache 优化等非标准全量权重加载策略，否则该实测数据与硬件带宽极限存在矛盾。

## Evidence

[质询]陈述中声称“实际 52 tokens/s 超出此理论值”，但 52 tokens/s 这一具体实测数据缺乏来源支持，且若该数据属实，其超出理论带宽极限（37.7 tokens/s）的解释（稀疏/缓存优化）在标准 BF16 全量加载场景下缺乏物理直觉支持，存在将特定优化场景误判为通用瓶颈或数据错误的可能。 | 先验知识/题面给定，逻辑校验通过：理论带宽瓶颈计算（2039 GB/s / 54 GB ≈ 37.7 tokens/s）符合 A100 80GB 硬件规格与 Qwen3-27B 模型参数量级，数学推导自洽；但“实际 52 tokens/s”为经验事实，无来源支持且超出理论极限的解释存疑，故降级。

## Search Query

A100 HBM2e bandwidth 2039 GB/s LLM decode throughput limit formula
