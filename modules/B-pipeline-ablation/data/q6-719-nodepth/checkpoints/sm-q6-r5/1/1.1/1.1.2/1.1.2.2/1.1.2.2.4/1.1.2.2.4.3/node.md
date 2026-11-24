# N1283: 低码率工作点带宽成本对比：C_bw_low = 200GB/day * 30 * ¥0.2/GB = ¥1,200/月，比标准工作点节省 50%；但需验证低码率

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N438

## Claim

低码率工作点带宽成本对比：C_bw_low = 200GB/day * 30 * ¥0.2/GB = ¥1,200/月，比标准工作点节省 50%；但需验证低码率是否导致用户感知质量下降，引入 QoE 惩罚项 ΔQoE = 0.1 * (1 - s_low/s_std)。

## Corrected Claim

低码率工作点带宽成本对比：C_bw_low = 200GB/day * 30 * ¥0.2/GB = ¥1,200/月，比标准工作点节省 50%；但需验证低码率是否导致用户感知质量下降，引入 QoE 惩罚项 ΔQoE = 0.1 * (1 - s_low/s_std)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 200*30*0.2=1200 正确，50% 节省隐含标准成本为 2400，逻辑自洽；QoE 公式为定义式，无逻辑矛盾。
