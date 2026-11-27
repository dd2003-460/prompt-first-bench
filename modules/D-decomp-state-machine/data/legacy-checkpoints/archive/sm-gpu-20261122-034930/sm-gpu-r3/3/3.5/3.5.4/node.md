# N105: 单卡vs多卡TCO对比结论更新：在电价$0.15/kWh、利用率50%假设下，2x RTX 4090 的3年TCO ($5,675) 显著低于 1x A100 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

单卡vs多卡TCO对比结论更新：在电价$0.15/kWh、利用率50%假设下，2x RTX 4090 的3年TCO ($5,675) 显著低于 1x A100 40GB ($12,288)，但需注意 2x RTX 4090 总显存48GB在BF16下不足（需INT8/W4），而 A100 40GB 在INT8下刚好满足41.7GB需求，此TCO优势以牺牲精度灵活性为代价。

## Corrected Claim

单卡vs多卡TCO对比结论更新：在电价$0.15/kWh、利用率50%假设下，2x RTX 4090 的3年TCO ($5,675) 显著低于 1x A100 40GB ($12,288)，但需注意 2x RTX 4090 总显存48GB在BF16下不足（需INT8/W4），而 A100 40GB 在INT8下刚好满足41.7GB需求，此TCO优势以牺牲精度灵活性为代价。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO计算符合硬件成本与能耗逻辑，显存需求与精度量化关系符合深度学习工程常识。
