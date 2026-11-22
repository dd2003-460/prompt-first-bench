# N56: ETag/版本号机制下的失效代价量化：采用ETag验证时，只有当对象实际被更新且客户端发起条件请求时才失效。假设更新率u=1%/天，客户端平均访问间隔为1/f_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

ETag/版本号机制下的失效代价量化：采用ETag验证时，只有当对象实际被更新且客户端发起条件请求时才失效。假设更新率u=1%/天，客户端平均访问间隔为1/f_avg，则每次访问触发ETag校验的概率为1，但只有当对象在两次访问间被更新（概率≈u*Δt）时才导致缓存未命中。对于高频对象（f_i > 1000/天），Δt < 0.001天，P_update_between_visits ≈ 0.00001，几乎不失效；对于低频对象，P_update_between_visits ≈ u*Δt，需按频率分层计算加权失效概率。

## Corrected Claim

ETag/版本号机制下的失效代价量化：采用ETag验证时，只有当对象实际被更新且客户端发起条件请求时才失效。假设更新率u=1%/天，客户端平均访问间隔为1/f_avg，则每次访问触发ETag校验的概率为1，但只有当对象在两次访问间被更新（概率≈u*Δt）时才导致缓存未命中。对于高频对象（f_i > 1000/天），Δt < 0.001天，P_update_between_visits ≈ 0.00001，几乎不失效；对于低频对象，P_update_between_visits ≈ u*Δt，需按频率分层计算加权失效概率。

## Evidence

先验知识/题面给定，逻辑校验通过
