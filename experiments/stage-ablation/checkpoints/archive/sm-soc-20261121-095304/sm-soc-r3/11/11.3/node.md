# N201: 噪声对成交周期的非线性影响函数：成交周期 T_deal = T_base × (1 + λ_noise × σ_noise² / σ_signal²)，其中 λ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

噪声对成交周期的非线性影响函数：成交周期 T_deal = T_base × (1 + λ_noise × σ_noise² / σ_signal²)，其中 λ_noise 为噪声放大系数（估计值 1.5-2.5），σ_noise 为噪声标准差，σ_signal 为信号强度标准差。当 σ_noise > 5% 时，T_deal 增加幅度超过 20%。

## Corrected Claim

噪声对成交周期存在非线性影响，通常可用 T_deal = T_base × (1 + λ_noise × (σ_noise/σ_signal)²) 形式近似描述，其中 λ_noise 为经验估计的噪声放大系数，具体数值需根据市场微观结构实证确定。

## Evidence

[质询]该公式为特定经验模型，缺乏普适性理论支持；且参考来源仅讨论信噪比与观测窗口的关系，未提供该具体非线性影响函数及参数估计值（λ=1.5-2.5），属于无来源支持的特定经验断言。 | 逻辑上量纲自洽（σ²/σ²无量纲），但参考来源[1]仅涉及信噪比概念，未直接支持该具体公式及参数，属经验事实且缺直接来源支持。

## Search Query

noise impact on transaction time nonlinear function lambda coefficient empirical estimation

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7650287636393574964/&rut=47d3bc38536c296b9a95dcde76cc132ebada60bf5fad92fe705a9482daece4da', 'type': 'ddg', 'title': '华泰金工 | 时序cta方法论综述：市场状态、开仓信号与退出机制'}
