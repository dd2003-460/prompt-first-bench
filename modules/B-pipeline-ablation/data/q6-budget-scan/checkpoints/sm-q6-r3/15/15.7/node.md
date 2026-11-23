# N371: P99 超标单请求赔付成本 C_penalty_per_req 的估计：C_penalty_per_req = P_compensation_per_user 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

P99 超标单请求赔付成本 C_penalty_per_req 的估计：C_penalty_per_req = P_compensation_per_user * (N_users_affected / N_req_affected)，其中 P_compensation_per_user 为单用户赔付标准（¥1-10），N_users_affected 为受影响用户数，N_req_affected 为受影响请求数

## Corrected Claim

P99 超标单请求赔付成本 C_penalty_per_req 的估计：C_penalty_per_req = P_compensation_per_user * (N_users_affected / N_req_affected)，其中 P_compensation_per_user 为单用户赔付标准（¥1-10），N_users_affected 为受影响用户数，N_req_affected 为受影响请求数

## Evidence

先验知识/题面给定，逻辑校验通过
