# N111: 流量弹性系数 $\beta_1$ 的估计公式为：$\beta_1 = \frac{\ln(1 + \Delta T / T_{base})}{\ln(1 + \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

流量弹性系数 $\beta_1$ 的估计公式为：$\beta_1 = \frac{\ln(1 + \Delta T / T_{base})}{\ln(1 + \Delta E / E_{base})}$，其中 $\Delta T$ 和 $\Delta E$ 需基于平台历史A/B测试中“曝光权重变化”与“成交周期变化”的回归残差计算，以剔除季节性因素。

## Corrected Claim

流量弹性系数 $\beta_1$ 的估计公式为：$\beta_1 = \frac{\ln(1 + \Delta T / T_{base})}{\ln(1 + \Delta E / E_{base})}$，其中 $\Delta T$ 和 $\Delta E$ 需基于平台历史A/B测试中“曝光权重变化”与“成交周期变化”的回归残差计算，以剔除季节性因素。

## Evidence

先验知识/题面给定，逻辑校验通过
