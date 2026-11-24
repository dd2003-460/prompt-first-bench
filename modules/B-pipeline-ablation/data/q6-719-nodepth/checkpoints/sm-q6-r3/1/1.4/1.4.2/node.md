# N51: Total Requests (R) = DAU × Avg_Requests_Per_User_Day，其中 DAU = 5,000,000，Avg_Requ

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Total Requests (R) = DAU × Avg_Requests_Per_User_Day，其中 DAU = 5,000,000，Avg_Requests_Per_User_Day 由平台类型决定（图片+短视频平台典型值 20-50 次/人/天）[待核验]

## Corrected Claim

Total Requests (R) = DAU × Avg_Requests_Per_User_Day，其中 DAU = 5,000,000，Avg_Requests_Per_User_Day 由平台类型决定（图片+短视频平台典型值 20-50 次/人/天）[待核验]

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2本质上是同一参数（人均请求数）在不同假设下的取值，属于参数敏感性分析而非正交维度，存在冗余；子节点3是约束校验，与前两者维度不同，但前两者的结构导致整体分解逻辑不清晰。）

## Search Query

average daily API requests per user social media platform
