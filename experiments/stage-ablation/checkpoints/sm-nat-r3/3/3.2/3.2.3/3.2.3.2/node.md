# N125: 工作点 B 的剩余容量计算：C_remaining = C - Σ_{i=1}^{1000} E[S_i|Top1%]，若 Top1% 占用约 1.5MB，则 

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点 B 的剩余容量计算：C_remaining = C - Σ_{i=1}^{1000} E[S_i|Top1%]，若 Top1% 占用约 1.5MB，则 C_remaining ≈ 128GB，K_B_max = C_remaining / E[S|1%-10%]，由于 K_B_max >> 9000，说明容量足以容纳所有 1%-10% 对象，N53 中 '20,000 个' 的限制是虚构的，实际瓶颈在于对象总数而非容量。

## Corrected Claim

工作点 B 的剩余容量计算：C_remaining = C - Σ_{i=1}^{1000} E[S_i|Top1%]，若 Top1% 占用约 1.5MB，则 C_remaining ≈ 128GB，K_B_max = C_remaining / E[S|1%-10%]，由于 K_B_max >> 9000，说明容量足以容纳所有 1%-10% 对象，N53 中 '20,000 个' 的限制是虚构的，实际瓶颈在于对象总数而非容量。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB 远大于 1.5MB，剩余容量充足，K_B_max 远大于 9000 的推导符合算术逻辑，且结论与题面设定自洽。
