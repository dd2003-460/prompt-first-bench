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

父节点级核验未通过：有冗余（子节点1和子节点2本质上是同一参数（R_per_user）在不同假设下的取值，属于冗余分解；子节点3引入了新的约束维度（缓存/对象大小），与前两者正交，因此整体正交性成立。完备性方面，覆盖了参数范围估算及关键矛盾校验，基本完整。）

## Search Query

average daily API requests per user social media platform
