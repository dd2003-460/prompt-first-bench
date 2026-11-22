# N172: 工作点 A（头部集中）：假设 LFU 保留前 1% 最热门对象（N=1000），其总字节量 S_head1 = Σ_{i=1}^{1000} s_i。基于 Pa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

工作点 A（头部集中）：假设 LFU 保留前 1% 最热门对象（N=1000），其总字节量 S_head1 = Σ_{i=1}^{1000} s_i。基于 Pareto(α=1.1) 和负相关 ρ=-0.3，头部对象平均大小 E[S|top1%] 约为 0.5KB，则 S_head1 ≈ 500KB，远小于 128GB，此工作点下 LFU 集合确定准则退化为纯频率排序，容量约束不起作用。

## Corrected Claim

工作点 A（头部集中）：假设 LFU 保留前 1% 最热门对象（N=1000），其总字节量 S_head1 = Σ_{i=1}^{1000} s_i。基于 Pareto(α=1.1) 和负相关 ρ=-0.3，头部对象平均大小 E[S|top1%] 约为 0.5KB，则 S_head1 ≈ 500KB，远小于 128GB，此工作点下 LFU 集合确定准则退化为纯频率排序，容量约束不起作用。

## Evidence

先验知识/题面给定，逻辑校验通过：1000个对象 * 0.5KB = 500KB，远小于128GB，容量约束确实不起作用，LFU退化为纯频率排序符合逻辑。
