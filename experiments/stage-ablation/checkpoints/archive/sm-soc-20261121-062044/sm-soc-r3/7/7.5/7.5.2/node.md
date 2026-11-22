# N260: 定义独立用户数 (Unique Users) 为在特定时间窗口 (T_window) 内去重后的访问用户 ID 集合大小，即 |{User_ID_i | Acc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

定义独立用户数 (Unique Users) 为在特定时间窗口 (T_window) 内去重后的访问用户 ID 集合大小，即 |{User_ID_i | AccessTime_i ∈ T_window}|，作为咨询率分母时需确保 User_ID 的唯一性标识符（如设备指纹或登录ID）在统计周期内保持稳定。

## Corrected Claim

定义独立用户数 (Unique Users) 为在特定时间窗口 (T_window) 内去重后的访问用户 ID 集合大小，即 |{User_ID_i | AccessTime_i ∈ T_window}|，作为咨询率分母时需确保 User_ID 的唯一性标识符（如设备指纹或登录ID）在统计周期内保持稳定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

unique user definition e-commerce analytics deduplication logic
