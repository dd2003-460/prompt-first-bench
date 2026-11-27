# N293: 流量-咨询转化弹性 η_comp 的估计公式为 η_comp = log(1 + ΔQ_obs / Q_base) / log(1 + I_comp / I_b

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

流量-咨询转化弹性 η_comp 的估计公式为 η_comp = log(1 + ΔQ_obs / Q_base) / log(1 + I_comp / I_base)，需通过平台 A/B 测试中处理组（补偿曝光）与控制组（无补偿）在 48 小时窗口内的咨询率差值回归校准，当前缺乏具体实证值，标记为 [待核验]。

## Corrected Claim

流量-咨询转化弹性 η_comp 的一种估计方法为 η_comp = log(1 + ΔQ_obs / Q_base) / log(1 + I_comp / I_base)，需通过平台 A/B 测试中处理组与控制组在 48 小时窗口内的咨询率差值回归校准；该公式为特定业务场景下的经验模型，当前缺乏通用实证值支持，标记为 [待核验]。

## Evidence

[质询]该公式属于特定业务场景下的经验性计量模型，并非通用物理或数学定律，其具体形式（如对数线性关系、48小时窗口、特定回归校准方法）缺乏普适性理论支撑，且‘当前缺乏具体实证值’这一状态描述属于动态经验事实，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该公式为特定业务经验模型，不适用第一性原理推导条款）

## Search Query

A/B test traffic compensation inquiry rate elasticity C2C marketplace
