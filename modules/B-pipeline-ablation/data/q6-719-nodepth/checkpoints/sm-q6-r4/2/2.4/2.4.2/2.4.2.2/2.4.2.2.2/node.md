# N669: 长尾区域回源流量成本精确计算：Cost_origin_tail = Tail_Traffic_GB × Miss_Rate_tail × Price_origi

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N231

## Claim

长尾区域回源流量成本精确计算：Cost_origin_tail = Tail_Traffic_GB × Miss_Rate_tail × Price_origin_GB，其中 Tail_Traffic_GB = 0.4 × 2000 GB = 800 GB/天，Miss_Rate_tail = 0.3，Price_origin_GB 为公有云回源单价（典型 ¥0.5-0.8/GB），月度成本 = 800 × 0.3 × 0.65 × 30 ≈ ¥46,800/月。

## Corrected Claim

长尾区域回源流量成本估算公式为 Cost = Tail_Traffic × Miss_Rate × Price_origin。若假设长尾流量为800GB/天，回源率30%，单价0.65元/GB，则月度成本约为¥46,800。实际成本需根据具体云厂商定价及真实流量分布确定。

## Evidence

[质询]该陈述中的具体数值（总流量2000GB、长尾占比0.4、回源单价0.65元/GB）均为经验假设或特定场景参数，并非通用物理定律或数学公理，无法从第一性原理严格推出；且参考来源仅提供了计费公式（流量×单价），未提供具体的单价数值或流量分布假设，因此缺乏直接来源支持具体计算结果。 | 逻辑推导成立（800*0.3*0.65*30=46800），来源[1]和[3]支持计费逻辑（流量×单价），但具体参数（单价0.65、流量分布）属于经验事实，缺来源直接支持，故降级。

## Search Query

Alibaba Cloud CDN origin pull price per GB 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/ask/652758&rut=95f5b6fe03c007ee15ae9f7b0f062a3f952446a4ef5892dd23e308ad6ee817ef', 'type': 'ddg', 'title': 'Cdn回源oss如何计算回源流量费用_问答-阿里云开发者社区'}
- {'url': 'https://cloud.tencent.com/document/product/436/53863&rut=50f1b4b2bd996c31d41d24905c69b9b24823f6228c6c3cf6dae07f8040315719', 'type': 'ddg', 'title': '对象存储 流量费用_腾讯云'}
- {'url': 'https://cdn.cloudflew.com/learn/cdn-cost-components&rut=5b2567058342724b8f9b852b14fde1ae42279bbc1bb9a982f51fe2b3d6c25b12', 'type': 'ddg', 'title': 'Cdn 成本构成：流量、请求、回源与附加功能'}
