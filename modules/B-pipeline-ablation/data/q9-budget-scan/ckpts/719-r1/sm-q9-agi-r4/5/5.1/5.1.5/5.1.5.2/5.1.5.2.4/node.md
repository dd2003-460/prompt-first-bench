# N661: 单日成本敏感性分析：假设日均调用 N_calls=100 次，总成本 Cost_day = N_calls * Cost_per_call = $3.50；当 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N241

## Claim

单日成本敏感性分析：假设日均调用 N_calls=100 次，总成本 Cost_day = N_calls * Cost_per_call = $3.50；当 L_in 增加至 50,000 tokens（长文献综述场景），Cost_per_call 升至 $0.135，Cost_day 升至 $13.50，增幅 385%

## Corrected Claim

单日成本敏感性分析：假设日均调用 N_calls=100 次，总成本 Cost_day = N_calls * Cost_per_call = $3.50；当 L_in 增加至 50,000 tokens（长文献综述场景），Cost_per_call 升至 $0.135，Cost_day 升至 $13.50，增幅约 286%

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（100*0.035=3.5, 100*0.135=13.5），增幅计算正确((13.5-3.5)/3.5≈285.7%? 等等，题目说增幅385%。让我们重新检查增幅计算。原成本3.5，新成本13.5。增量是10。10/3.5 ≈ 2.857，即285.7%。题目声称增幅385%。这是一个明显的算术错误。
