# N692: 双活架构中，主备集群需保持完全同步，其网络同步带宽需求 B_sync = W_avg_write * k_replication，若温数据日均写入量为 5TB，

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N287

## Claim

双活架构中，主备集群需保持完全同步，其网络同步带宽需求 B_sync = W_avg_write * k_replication，若温数据日均写入量为 5TB，同步流量峰值约为 5TB/8h ≈ 0.625GB/s，需预留千兆或万兆专线，其年租赁成本约为 ¥20,000-¥50,000/年，该成本独立于电力冗余系数，需单独计入 TCO。

## Corrected Claim

双活架构中，主备集群需保持完全同步，其网络同步带宽需求 B_sync = W_avg_write * k_replication，若温数据日均写入量为 5TB，同步流量峰值约为 5TB/8h ≈ 0.625GB/s，需预留千兆或万兆专线，其年租赁成本需根据具体地区和运营商报价单独计入 TCO。

## Evidence

[质询]年租赁成本数值（¥20,000-¥50,000/年）缺乏来源支持，且不同地区/运营商差异巨大，属于经验事实而非第一性原理可推导内容。 | 逻辑推导部分（带宽计算 5TB/8h ≈ 0.625GB/s）自洽，但成本部分为经验事实，无来源支持，故降级。

## Search Query

active-active datacenter network bandwidth cost synchronization
