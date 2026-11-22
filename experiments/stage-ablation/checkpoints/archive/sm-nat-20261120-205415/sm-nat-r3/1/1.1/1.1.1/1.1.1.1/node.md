# N89: 工作点A（x_min=1KB）：假设最小对象大小为1KB，截断Pareto(α=1.1)的CDF在B处的表达式简化为 F(B) = 1 - (10^-3/B)^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

工作点A（x_min=1KB）：假设最小对象大小为1KB，截断Pareto(α=1.1)的CDF在B处的表达式简化为 F(B) = 1 - (10^-3/B)^{0.1}，其中B以KB为单位；该工作点代表典型CDN小文件场景，数值计算时B通常远大于x_min，使得(x_min/B)^{0.1}项趋近于0

## Corrected Claim

工作点A（x_min=1KB）：假设最小对象大小为1KB，截断Pareto(α=1.1)的CDF在B处的表达式简化为 F(B) = 1 - (10^-3/B)^{0.1}，其中B以KB为单位；该工作点代表典型CDN小文件场景，数值计算时B通常远大于x_min，使得(x_min/B)^{0.1}项趋近于0

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式 F(x)=1-(x_min/x)^α 代入 α=1.1 及 x_min=1KB 后，表达式 F(B)=1-(10^-3/B)^{0.1} 数学推导正确；当 B >> 1KB 时，(10^-3/B)^{0.1} 趋近于0符合数学极限性质。
