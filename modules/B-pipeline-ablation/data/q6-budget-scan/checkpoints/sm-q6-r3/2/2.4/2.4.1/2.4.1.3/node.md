# N197: 核心区域回源带宽成本与公有云 CDN 成本的对比：自建节点回源带宽成本 = (1 - H_cache) × Daily_Traffic_TB × Price_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

核心区域回源带宽成本与公有云 CDN 成本的对比：自建节点回源带宽成本 = (1 - H_cache) × Daily_Traffic_TB × Price_per_TB_self_hosted。假设 H_cache=92%，日均流量 2TB，回源流量 0.16TB，自建回源单价 0.3元/TB，则月成本 0.16TB × 30 × 0.3 = 1.44元/节点，10 节点合计 14.4元/月。公有云 CDN 成本 = 2TB × 30 × 0.4元/TB = 24元/月。表明自建节点在核心区域回源成本上优势不明显，主要优势在于边缘带宽成本。

## Corrected Claim

核心区域回源带宽成本与公有云 CDN 成本的对比：自建节点回源带宽成本 = (1 - H_cache) × Daily_Traffic_TB × Price_per_TB_self_hosted。假设 H_cache=92%，日均流量 2TB，回源流量 0.16TB，自建回源单价 0.3元/TB，则月成本 0.16TB × 30 × 0.3 = 1.44元/节点，10 节点合计 14.4元/月。公有云 CDN 成本 = 2TB × 30 × 0.4元/TB = 24元/月。表明自建节点在核心区域回源成本上优势不明显，主要优势在于边缘带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算准确（0.16*30*0.3=1.44, 1.44*10=14.4, 2*30*0.4=24），结论符合逻辑推导。

## Search Query

CDN origin bandwidth cost comparison self-hosted vs cloud provider
