# N125: 工作点 A（高保守阈值）：定义 x_med 为对象大小的中位数（P(S > x_med) = 0.5），r_95 为热度的第 95 百分位（P(R > r_95

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点 A（高保守阈值）：定义 x_med 为对象大小的中位数（P(S > x_med) = 0.5），r_95 为热度的第 95 百分位（P(R > r_95) = 0.05），计算 P_small_hot_A = ∫_{S<x_med}∫_{R>r_95} f(S,R) ds dr，此工作点代表最严格定义的'热门小对象'，预期占比最低，用于估算 LFU 容量损失的下界。

## Corrected Claim

工作点 A（高保守阈值）：定义 x_med 为对象大小的中位数（P(S > x_med) = 0.5），r_95 为热度的第 95 百分位（P(R > r_95) = 0.05），计算 P_small_hot_A = ∫_{S<x_med}∫_{R>r_95} f(S,R) ds dr，此工作点代表最严格定义的'热门小对象'，预期占比最低，用于估算 LFU 容量损失的下界。

## Evidence

先验知识/题面给定，逻辑校验通过：定义符合概率论基本公理，中位数与95百分位的组合确实界定了最严格的'小且热'区域，其积分值作为LFU容量损失下界的逻辑推导自洽。
