# N20: 电力成本计算：RTX 4090 TDP=450W，A100 80GB TDP=400W，假设24/7运行，电价$0.10/kWh，5年电力成本 = TDP * 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

电力成本计算：RTX 4090 TDP=450W，A100 80GB TDP=400W，假设24/7运行，电价$0.10/kWh，5年电力成本 = TDP * 24h * 365d * 5y * $0.10/kWh

## Corrected Claim

电力成本计算：RTX 4090 TDP=450W，A100 80GB TDP=400W，假设24/7运行，电价$0.10/kWh，5年电力成本 = TDP * 24h * 365d * 5y * $0.10/kWh

## Evidence

父节点级核验未通过：不完备（子节点分别讨论了功耗修正（硬件/负载维度）和电价敏感性（经济/外部变量维度），两者正交且不重复。但父节点定义了一个具体的计算场景（包含特定TDP、时间、单价），而子节点仅提供了修正因子和敏感性分析，缺少基于原始参数或修正后参数的具体计算结果（即未给出最终的5年电力成本数值），导致分解未能完整覆盖父节点隐含的‘计算’目标。）

## Search Query

RTX 4090 TDP 450W A100 TDP 400W electricity cost calculation
