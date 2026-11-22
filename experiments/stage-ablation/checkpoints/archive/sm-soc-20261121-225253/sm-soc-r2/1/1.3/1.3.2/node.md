# N23: $P_{mkt}$ 稳定性的量化定义：需计算同类商品近期成交价的标准差 $\sigma_{mkt}$ 与均值 $\mu_{mkt}$ 的比值（变异系数 $CV 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

$P_{mkt}$ 稳定性的量化定义：需计算同类商品近期成交价的标准差 $\sigma_{mkt}$ 与均值 $\mu_{mkt}$ 的比值（变异系数 $CV = \sigma_{mkt}/\mu_{mkt}$），当 $CV < 0.1$ 时，认为 $P_{mkt}$ 稳定，此时买家对挂价虚高的容忍度提高，具体表现为成交周期 $T_{deal}$ 与 $|P_{ask} - P_{mkt}|$ 的相关性 $\rho$ 显著降低（$\rho < 0.2$）。

## Corrected Claim

在特定交易模型中，可定义市场稳定性为同类商品近期成交价的变异系数（CV = σ/μ）。当 CV < 0.1 时，视为市场稳定，此时买家对挂价虚高的容忍度提高，表现为成交周期 T_deal 与 |P_ask - P_mkt| 的相关性 ρ 显著降低（如 ρ < 0.2）。

## Evidence

[质询]该陈述将‘市场稳定性’量化为变异系数（CV），并设定具体阈值（CV<0.1, ρ<0.2），这属于特定业务场景下的经验性定义或模型假设，而非通用的金融或统计学第一性原理。参考来源均讨论风控中的PSI（群体稳定性指标），与CV定义及交易行为相关性无关，无法提供外部支持。 | 逻辑上自洽（CV是衡量离散程度的标准统计量，且市场稳定时价格波动小、买家对偏离度容忍度高的经济直觉合理），但参考来源[1][2][3]均关于PSI指标，与该事实主题（CV定义及交易行为）无关，属于经验事实且缺来源支持。

## Search Query

market price stability coefficient of variation impact on buyer tolerance for high asking prices

## Retrieval Sources

- {'url': 'https://blog.csdn.net/zkw54334/article/details/147513724&rut=2288a6626658d4311ce21e438a0b0730295b0d5f328b618a2f118d88708f50e6', 'type': 'ddg', 'title': '【风控】稳定性指标psi - Csdn博客'}
- {'url': 'https://edu.51cto.com/article/note/53899.html&rut=17011a479930fdc17ea41bed8771d2467d778923f156ca35ce161b842587246b', 'type': 'ddg', 'title': '模型上线后效果变差？PSI指标实战详解与数据分布漂移监控_51CTO学堂_专业的IT技能学习平台'}
- {'url': 'https://cloud.tencent.com/developer/article/2365865&rut=827cf800e5b2a7ef934f66b3b2c816d832da141a8163bb6e75fa67a941d0cd8c', 'type': 'ddg', 'title': '风控模型：PSI 稳定性指标详解 (Python)-腾讯云开发者社区-腾讯云'}
