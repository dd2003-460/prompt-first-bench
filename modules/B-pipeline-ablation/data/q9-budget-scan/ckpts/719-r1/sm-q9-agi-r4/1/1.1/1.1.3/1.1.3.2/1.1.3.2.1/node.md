# N361: k_order = 0.03 的波动幅度需分解为示例内容相似度的方差项与位置偏差项，其中位置偏差（primacy/recency effect）贡献约 60% 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N115

## Claim

k_order = 0.03 的波动幅度需分解为示例内容相似度的方差项与位置偏差项，其中位置偏差（primacy/recency effect）贡献约 60% 的波动，需通过控制变量实验分离这两个正交因素

## Corrected Claim

k_order = 0.03 的波动幅度需分解为示例内容相似度的方差项与位置偏差项，其中位置偏差（primacy/recency effect）通常占据显著比例，需通过控制变量实验分离这两个正交因素以量化具体贡献。

## Evidence

[质询]「位置偏差贡献约 60% 的波动」是一个具体的经验量化数值，缺乏通用理论支撑，不同数据集和实验设置下该比例差异巨大，不能视为普适常数。 | 先验知识/题面给定，逻辑校验通过（分解框架合理），但具体数值 60% 属经验事实且无来源支持，故降级。
