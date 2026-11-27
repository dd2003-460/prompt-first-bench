# N147: RTX 3090 Ti 的 350W TDP 对应 P_avg 约为 245W，其能效比 (tokens/s per watt) 在 INT4 推理下约为 25

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

RTX 3090 Ti 的 350W TDP 对应 P_avg 约为 245W，其能效比 (tokens/s per watt) 在 INT4 推理下约为 25-28 / 245 ≈ 0.10-0.11 tokens/s/W，高于 RTX 4090 的 11.5-15 / 315 ≈ 0.036-0.048 tokens/s/W (BF16)，但低于 4090 在 FP8 下的能效比。

## Corrected Claim

RTX 3090 Ti 的 TDP 通常为 450W，RTX 4090 的 TDP 为 450W。具体能效比需基于实际功耗和吞吐量数据重新计算，原陈述中的功率数值有误。

## Evidence

[质询]RTX 3090 Ti 的 TDP 通常为 450W 而非 350W，且 RTX 4090 的 TDP 为 450W 而非 315W，陈述中的功率数值与主流硬件规格存在显著偏差，导致能效比计算基础错误。 | 经验事实，逻辑自洽但缺来源支持，且关键硬件参数（TDP）与已知事实不符，无法验证具体能效比数值。

## Search Query

RTX 3090 Ti vs RTX 4090 energy efficiency LLM inference tokens per second per watt
