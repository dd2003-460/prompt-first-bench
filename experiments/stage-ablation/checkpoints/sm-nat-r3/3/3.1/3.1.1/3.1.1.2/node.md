# N173: 工作点 B（中尾平衡）：假设 LFU 保留前 10% 对象（N=10000），其总字节量 S_head10 = Σ_{i=1}^{10000} s_i。基于 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

工作点 B（中尾平衡）：假设 LFU 保留前 10% 对象（N=10000），其总字节量 S_head10 = Σ_{i=1}^{10000} s_i。基于 Pareto(α=1.1) 和负相关 ρ=-0.3，中尾对象平均大小 E[S|top10%] 约为 2KB，则 S_head10 ≈ 20MB，仍远小于 128GB，此工作点下 LFU 集合由频率阈值 f_threshold 决定，且 f_threshold 对应第 10000 个对象的请求频率。

## Corrected Claim

工作点 B（中尾平衡）：假设 LFU 保留前 10% 对象（N=10000），其总字节量 S_head10 = Σ_{i=1}^{10000} s_i。基于 Pareto(α=1.1) 和负相关 ρ=-0.3，中尾对象平均大小 E[S|top10%] 约为 2KB，则 S_head10 ≈ 20MB，仍远小于 128GB，此工作点下 LFU 集合由频率阈值 f_threshold 决定，且 f_threshold 对应第 10000 个对象的请求频率。

## Evidence

先验知识/题面给定，逻辑校验通过：10000个对象 * 2KB/对象 = 20MB，数值量级计算正确，且20MB远小于128GB的结论符合逻辑。
