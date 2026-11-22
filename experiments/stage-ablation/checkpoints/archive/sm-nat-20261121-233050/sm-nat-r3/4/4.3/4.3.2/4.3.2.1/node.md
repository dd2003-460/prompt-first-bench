# N125: 工作点1（ETag/强一致性）：H_dynamic_hit ≈ P_update_between_visits * P_reentry。对于高频对象（F_i=1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点1（ETag/强一致性）：H_dynamic_hit ≈ P_update_between_visits * P_reentry。对于高频对象（F_i=1000/天），Δt=0.001天，P_update ≈ 0.01*0.001 = 0.00001。P_reentry ≈ 1（因为下次访问立即重新缓存）。H_dynamic_hit ≈ 0.00001。对于低频对象（F_i=1/天），Δt=1天，P_update ≈ 0.01。P_reentry ≈ 0.1（假设10%概率在下次访问前被重新缓存）。H_dynamic_hit ≈ 0.001。加权平均 H_dynamic_hit ≈ 0.0005 (0.05%)。

## Corrected Claim

工作点1（ETag/强一致性）：H_dynamic_hit ≈ P_update_between_visits * P_reentry。对于高频对象（F_i=1000/天），Δt=0.001天，P_update ≈ 0.01*0.001 = 0.00001。P_reentry ≈ 1（因为下次访问立即重新缓存）。H_dynamic_hit ≈ 0.00001。对于低频对象（F_i=1/天），Δt=1天，P_update ≈ 0.01。P_reentry ≈ 0.1（假设10%概率在下次访问前被重新缓存）。H_dynamic_hit ≈ 0.001。加权平均 H_dynamic_hit ≈ 0.0005 (0.05%)。

## Evidence

先验知识/题面给定，逻辑校验通过
