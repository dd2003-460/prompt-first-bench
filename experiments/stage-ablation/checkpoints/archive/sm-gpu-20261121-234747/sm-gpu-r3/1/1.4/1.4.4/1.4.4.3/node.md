# N229: 在 $1.5-$2.5/GPU-hour 的租赁价格区间内，若选择 32K 上下文推理任务，实际有效吞吐量受限于 KV Cache 显存占用与计算瓶颈，需计算单

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54, N55, N56

## Claim

在 $1.5-$2.5/GPU-hour 的租赁价格区间内，若选择 32K 上下文推理任务，实际有效吞吐量受限于 KV Cache 显存占用与计算瓶颈，需计算单位 token 生成成本（$/token）= 租赁小时费 / (吞吐量 tokens/hour)，以对比自购方案的单位成本

## Corrected Claim

在 $1.5-$2.5/GPU-hour 的租赁价格区间内，若选择 32K 上下文推理任务，实际有效吞吐量受限于 KV Cache 显存占用与计算瓶颈，需计算单位 token 生成成本（$/token）= 租赁小时费 / (吞吐量 tokens/hour)，以对比自购方案的单位成本

## Evidence

先验知识/题面给定，逻辑校验通过：成本计算公式符合基本经济逻辑，KV Cache 对吞吐量的限制符合 LLM 推理工程常识，数值量级合理。
