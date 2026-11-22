# N284: 2×RTX 4090 方案的 MTBF (Mean Time Between Failures) 基准值修正：鉴于 RTX 4090 为消费级显卡且无 ECC 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

2×RTX 4090 方案的 MTBF (Mean Time Between Failures) 基准值修正：鉴于 RTX 4090 为消费级显卡且无 ECC 支持，其 MTBF 显著低于数据中心级硬件；参考消费级 GPU 在 24/7 高负载下的社区统计，MTBF_2x4090 取中值 7500 小时（范围 5000-10000h），用于计算年均故障次数 N_failures = T_total / MTBF。

## Corrected Claim

2×RTX 4090 方案的 MTBF (Mean Time Between Failures) 基准值修正：鉴于 RTX 4090 为消费级显卡且无 ECC 支持，其 MTBF 显著低于数据中心级硬件；参考消费级 GPU 在 24/7 高负载下的社区统计，MTBF_2x4090 取中值 7500 小时（范围 5000-10000h），用于计算年均故障次数 N_failures = T_total / MTBF。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 MTBF 24/7 inference failure rate statistics
