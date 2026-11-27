# N278: T_save 的活跃度分层基准值：高频买家（月登录>10次）因熟悉平台，T_save_high = 8分钟/次；低频买家（月登录<3次）因需重新学习，T_sav

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

T_save 的活跃度分层基准值：高频买家（月登录>10次）因熟悉平台，T_save_high = 8分钟/次；低频买家（月登录<3次）因需重新学习，T_save_low = 22分钟/次；加权平均 T_save_avg = w_high*8 + w_low*22，假设 w_high=0.3, w_low=0.7，则 T_save_avg = 17.8分钟。

## Corrected Claim

T_save 的活跃度分层基准值：高频买家（月登录>10次）因熟悉平台，T_save_high = 8分钟/次；低频买家（月登录<3次）因需重新学习，T_save_low = 22分钟/次；加权平均 T_save_avg = w_high*8 + w_low*22，假设 w_high=0.3, w_low=0.7，则 T_save_avg = 17.8分钟。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.3*8 + 0.7*22 = 2.4 + 15.4 = 17.8，数值与逻辑自洽。

## Search Query

user search time reduction high frequency vs low frequency users e-commerce
