# N95: 权重w_1, w_2, w_3的A/B测试设计：通过随机分配卖家至不同权重组（如w_1=0.4/0.5/0.6），观测各组卖家的ΔP_anchor调整幅度及最终

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

权重w_1, w_2, w_3的A/B测试设计：通过随机分配卖家至不同权重组（如w_1=0.4/0.5/0.6），观测各组卖家的ΔP_anchor调整幅度及最终成交周期T_deal，以最小化T_deal为目标函数确定最优权重组合。

## Corrected Claim

权重w_1, w_2, w_3的A/B测试设计：通过随机分配卖家至不同权重组（如w_1=0.4/0.5/0.6），观测各组卖家的ΔP_anchor调整幅度及最终成交周期T_deal，以最小化T_deal为目标函数确定最优权重组合。

## Evidence

先验知识/题面给定，逻辑校验通过：A/B测试通过随机分组控制变量，观测因变量（ΔP_anchor, T_deal）并优化目标函数（最小化T_deal）是标准的实验设计与优化方法论，逻辑自洽且符合统计学基本原理。

## Search Query

A/B test anchor weight optimization pricing
