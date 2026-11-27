# N134: 工作点2（高延迟/低成功）：假设 T_origin=150ms, T_timeout=200ms，比值 r=0.75。根据 N49 假设的线性/阈值模型，P_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点2（高延迟/低成功）：假设 T_origin=150ms, T_timeout=200ms，比值 r=0.75。根据 N49 假设的线性/阈值模型，P_revalidate_success ≈ 0.75。此时 H_eff 额外损失为 (1-0.75) * P_stale = 0.25 * P_stale。在 P_stale=0.15% 时，额外损失 0.0375 个百分点，显著高于工作点1。

## Corrected Claim

工作点2（高延迟/低成功）：假设 T_origin=150ms, T_timeout=200ms，比值 r=0.75。根据 N49 假设的线性/阈值模型，P_revalidate_success ≈ 0.75。此时 H_eff 额外损失为 (1-0.75) * P_stale = 0.25 * P_stale。在 P_stale=0.15% 时，额外损失 0.0375 个百分点，显著高于工作点1。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (1-0.75)*0.15% = 0.0375% 准确，且符合线性模型假设下的推导逻辑。
