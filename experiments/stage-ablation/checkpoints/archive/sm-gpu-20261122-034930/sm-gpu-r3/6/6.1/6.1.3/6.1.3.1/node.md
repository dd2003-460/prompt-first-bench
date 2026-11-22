# N366: NVIDIA A100 80GB (SXM/PCIe) 的官方平均无故障时间（MTBF）数据在公开文档中通常缺失或标注为'N/A'，行业基准通常引用数据中心级G

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131, N132, N133

## Claim

NVIDIA A100 80GB (SXM/PCIe) 的官方平均无故障时间（MTBF）数据在公开文档中通常缺失或标注为'N/A'，行业基准通常引用数据中心级GPU的年均故障率（AFR）约为 2%-5% [待核验：需检索NVIDIA A100 Service Manual或第三方可靠性报告如Uptime Institute数据]，对应5年累计故障概率约为 10%-23%，每次故障导致的停机时间（MTTR）通常需 4-8 小时。

## Corrected Claim

NVIDIA A100 80GB 的官方 MTBF 数据在部分公开文档中可能未明确列出或标注为 N/A。行业经验数据显示，数据中心级 GPU 的年均故障率（AFR）通常在 2%-5% 范围内，对应 5 年累计故障概率约为 10%-23%，单次故障的平均修复时间（MTTR）估计在 4-8 小时之间。

## Evidence

[质询]该陈述包含具体的经验性数值（AFR 2%-5%, MTTR 4-8h），属于硬件可靠性经验事实，无法从第一性原理推导。且‘通常缺失’这一断言缺乏公开文档的直接证据支持，可能存在特定版本或渠道提供了该数据的情况。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及文档缺失情况）

## Search Query

NVIDIA A100 MTBF mean time between failures annual failure rate AFR
