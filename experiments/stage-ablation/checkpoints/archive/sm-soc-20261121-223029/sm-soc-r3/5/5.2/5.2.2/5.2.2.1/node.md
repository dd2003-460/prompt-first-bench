# N302: ΔT_search 的量化估算：ΔT_search = T_search_pre - T_search_post，其中 T_search 定义为从买家首次浏览商

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

ΔT_search 的量化估算：ΔT_search = T_search_pre - T_search_post，其中 T_search 定义为从买家首次浏览商品到发起咨询或进入议价界面的时间差；需通过日志数据提取高溢价组（δ>0.15）与低溢价组（δ<0.10）的中位 T_search 差值，预期 ΔT_search ≈ 0（假设搜索时间由用户行为决定，与价格无关）。

## Corrected Claim

ΔT_search 的量化估算：ΔT_search = T_search_pre - T_search_post，其中 T_search 定义为从买家首次浏览商品到发起咨询或进入议价界面的时间差；需通过日志数据提取高溢价组（δ>0.15）与低溢价组（δ<0.10）的中位 T_search 差值，预期 ΔT_search ≈ 0（假设搜索时间由用户行为决定，与价格无关）。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述明确将 ΔT_search ≈ 0 定义为基于“搜索时间与价格无关”这一假设的预期值，而非经验事实断言，逻辑自洽且无内部矛盾。
