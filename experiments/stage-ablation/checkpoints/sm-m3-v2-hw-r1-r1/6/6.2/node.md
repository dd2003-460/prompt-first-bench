# N37: 云端 API 边际成本：以 GPT-4o 为例，输入价格 $2.5/M tokens，输出价格 $10/M tokens；平均输入:输出比例 = 3:1，混合单

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

云端 API 边际成本：以 GPT-4o 为例，输入价格 $2.5/M tokens，输出价格 $10/M tokens；平均输入:输出比例 = 3:1，混合单价 C_cloud = (3*$2.5 + 1*$10) / 4 = $4.375/M tokens = $4.375e-6/token，是本地成本的 ~315 倍

## Corrected Claim

云端 API 边际成本：以 GPT-4o 为例，输入价格 $2.5/M tokens，输出价格 $10/M tokens；平均输入:输出比例 = 3:1，混合单价 C_cloud = (3*$2.5 + 1*$10) / 4 = $4.375/M tokens = $4.375e-6/token，是本地成本的 ~315 倍

## Evidence

先验知识/题面给定，逻辑校验通过：GPT-4o 定价符合公开数据，加权平均计算 (3*2.5+10)/4=4.375 正确，倍数关系基于隐含的本地成本基准（约$0.014/M tokens）在量级上合理。

## Search Query

GPT-4o API pricing input output cost per million tokens
