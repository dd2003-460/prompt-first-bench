# N247: 数据中心级 GPU (H100/A100) 的年度故障率 (AFR) 约为 0.5-1%，但由于拥有 ECC 和 RAS 特性，主要维护成本为远程监控和定期固件

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

数据中心级 GPU (H100/A100) 的年度故障率 (AFR) 约为 0.5-1%，但由于拥有 ECC 和 RAS 特性，主要维护成本为远程监控和定期固件更新，C_maint_annual ≈ $75 (中值)，且无需计入数据损坏的额外风险溢价。

## Corrected Claim

数据中心级 GPU (H100/A100) 的年度故障率 (AFR) 通常在 0.5-1% 左右，主要维护成本涉及远程监控和固件更新，年度维护成本中值约为 $75，但需考虑潜在的数据损坏或业务中断风险。

## Evidence

[质询]具体数值 $75 和 0.5-1% 的 AFR 属于特定经验数据，缺乏通用标准，且“无需计入数据损坏风险溢价”这一结论过于绝对，忽略了硬件故障导致数据丢失或业务中断的潜在隐性成本。 | 先验知识/题面给定，逻辑校验通过，但具体数值缺乏外部来源直接支持，且风险溢价表述存在争议。

## Search Query

datacenter GPU annual failure rate maintenance cost ECC
