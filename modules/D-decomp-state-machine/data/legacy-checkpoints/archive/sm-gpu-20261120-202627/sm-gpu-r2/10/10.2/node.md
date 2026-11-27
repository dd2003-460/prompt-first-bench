# N146: 数据中心显卡 (A100/H100) 的 MTBF 量化：根据 NVIDIA 数据中心产品规格，A100/H100 的 MTBF 通常 > 200,000 小时

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

数据中心显卡 (A100/H100) 的 MTBF 量化：根据 NVIDIA 数据中心产品规格，A100/H100 的 MTBF 通常 > 200,000 小时，折算为年故障率 (AFR) 约为 1-2% [待核验]，显著低于消费级卡。

## Corrected Claim

数据中心显卡 (A100/H100) 的 MTBF 通常较高，行业估算其年故障率 (AFR) 约为 1-2%（对应 MTBF 约 50,000-100,000 小时），显著低于消费级卡。

## Evidence

[质询]MTBF > 200,000 小时与 AFR 1-2% 存在数值矛盾：200,000 小时约等于 22.8 年，对应的年故障率 (AFR) 约为 1/22.8 ≈ 4.4%，而非 1-2%。若 AFR 为 1-2%，则 MTBF 应约为 50,000-100,000 小时。此外，NVIDIA 官方规格书通常不直接标注 MTBF 或 AFR，此类数据多来自第三方可靠性研究或行业估算，直接归因于'NVIDIA 数据中心产品规格'可能不准确。 | 经验事实，逻辑校验发现 MTBF 与 AFR 数值不匹配（200k 小时对应 ~4.4% AFR，而非 1-2%），且无外部来源支持，故降级。

## Search Query

NVIDIA A100 H100 MTBF reliability annual failure rate
