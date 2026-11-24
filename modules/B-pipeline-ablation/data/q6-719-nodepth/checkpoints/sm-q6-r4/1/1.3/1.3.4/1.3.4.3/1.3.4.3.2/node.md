# N515: 双峰混合分布下 s_median 的计算：s_median 无法直接由加权平均得到，需通过累积分布函数 CDF(s) = p_img × CDF_img(s) 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N173

## Claim

双峰混合分布下 s_median 的计算：s_median 无法直接由加权平均得到，需通过累积分布函数 CDF(s) = p_img × CDF_img(s) + p_vid × CDF_vid(s) = 0.5 求解，若 s_img 中位数 1.5MB, s_vid 中位数 7MB，则 s_median ≈ 2.8MB，与父节点声称的 3.2MB 存在偏差，需核验原始分布参数

## Corrected Claim

双峰混合分布下 s_median 无法直接由加权平均得到，需通过累积分布函数 CDF(s) = p_img × CDF_img(s) + p_vid × CDF_vid(s) = 0.5 求解；具体数值取决于各子分布的完整参数（如方差、偏度）及混合比例，仅凭中位数无法精确确定，需核验原始分布参数。

## Evidence

[质询]数值 2.8MB 和 3.2MB 的具体计算结果依赖于两个子分布的具体形状（如方差、偏度）以及混合比例 p_img 和 p_vid，仅凭中位数无法唯一确定混合分布的中位数，存在参数缺失导致的计算不确定性。 | 先验知识/题面给定，逻辑校验通过：双峰混合分布的中位数确实不能通过加权平均直接计算，需通过 CDF 求解，逻辑自洽；但具体数值 2.8MB 缺乏完整分布参数支持，且无外部来源验证，故降级。
