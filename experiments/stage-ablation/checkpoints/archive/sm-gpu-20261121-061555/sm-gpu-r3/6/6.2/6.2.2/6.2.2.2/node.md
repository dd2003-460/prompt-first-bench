# N316: eBay Sold Listings 中 NVIDIA A100 80GB 过去7天成交价格的变异系数 (CV = σ/μ)，用于量化供应稳定性/价格波动风险

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

eBay Sold Listings 中 NVIDIA A100 80GB 过去7天成交价格的变异系数 (CV = σ/μ)，用于量化供应稳定性/价格波动风险

## Corrected Claim

eBay Sold Listings 中 NVIDIA A100 80GB 过去7天成交价格的变异系数 (CV = σ/μ) 需基于实际抓取数据计算，当前无可用数据源支持具体数值，建议标注为‘数据缺失’或‘待计算’。

## Evidence

[质询]该陈述声称存在一个具体的数值（变异系数 CV），但参考来源显示检索失败，无可用数据支持该具体数值；且 eBay 上 A100 80GB 的成交量极低，7 天窗口内的样本量可能不足以计算具有统计意义的 CV，存在小样本偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

A100 80GB eBay sold price volatility coefficient of variation
