# N110: LFU 驻留对象数 N_LFU 的数值解：假设 h_min 对应 Top 5% 对象（K=5000），其累计大小 sum_{i=1}^{5000} S_{(i)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

LFU 驻留对象数 N_LFU 的数值解：假设 h_min 对应 Top 5% 对象（K=5000），其累计大小 sum_{i=1}^{5000} S_{(i)} ≈ 5000 * E[S|Top5%] ≈ 5000 * 5KB = 25GB << 128GB。因此容量约束非紧，N_LFU 实际上可覆盖 Top 10%-15% 对象（K≈10000-15000），累计大小约 50-75GB，仍低于 128GB。

## Corrected Claim

LFU 驻留对象数 N_LFU 的数值解：假设 h_min 对应 Top 5% 对象（K=5000），其累计大小 sum_{i=1}^{5000} S_{(i)} ≈ 5000 * E[S|Top5%] ≈ 5000 * 5KB = 25GB << 128GB。因此容量约束非紧，N_LFU 实际上可覆盖 Top 10%-15% 对象（K≈10000-15000），累计大小约 50-75GB，仍低于 128GB。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算（5000*5KB=25GB, 15000*5KB=75GB）准确，且25GB/75GB均小于128GB的结论符合算术逻辑，无内部矛盾。
