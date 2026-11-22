# N285: 卖家首个咨询延迟 T_feedback 的分布参数：在闲鱼平台，T_feedback 服从对数正态分布，中位数 48小时，75分位数为 96小时，95分位数为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

卖家首个咨询延迟 T_feedback 的分布参数：在闲鱼平台，T_feedback 服从对数正态分布，中位数 48小时，75分位数为 96小时，95分位数为 240小时；该分布的右偏特征（skewness > 2）导致卖家在 T_adjust 决策窗口内无法获得有效反馈

## Corrected Claim

在闲鱼平台，卖家首个咨询延迟 T_feedback 通常呈现右偏分布特征（如近似对数正态分布），导致部分卖家在决策窗口内无法获得有效反馈；具体分布参数（如中位数、分位数）需依据实际平台数据实证确定。

## Evidence

[质询]具体数值（中位数48h、75分位96h、95分位240h）及偏度阈值（>2）属于特定平台经验统计数据，缺乏公开权威来源直接支持，且不同卖家群体或时间段可能存在显著差异，存在过拟合特定样本的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体分布参数）

## Search Query

Xianyu seller first inquiry delay distribution log-normal median 48 hours
