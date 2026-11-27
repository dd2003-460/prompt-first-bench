# N38: 筛选效率函数：成交周期缩短量 ΔT_short = f(P_markup, C_signal, P_willing_high)。具体形式为 ΔT_short =

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N8

## Claim

筛选效率函数：成交周期缩短量 ΔT_short = f(P_markup, C_signal, P_willing_high)。具体形式为 ΔT_short = k * (P_markup - P_market) * C_signal * ln(P_willing_high)，其中 k 为市场匹配速度常数，需通过回归估计 k 的置信区间。

## Corrected Claim

筛选效率函数：成交周期缩短量 ΔT_short 受 P_markup, C_signal, P_willing_high 影响。具体形式需通过实证数据回归确定，初步假设可表示为 ΔT_short = f(P_markup, C_signal, P_willing_high)，其中参数需通过回归估计置信区间。

## Evidence

[质询]该公式为纯理论构造，缺乏实证支持。具体而言，将成交周期缩短量建模为对数函数 ln(P_willing_high) 且与 (P_markup - P_market) 线性相乘，缺乏经济学或市场微观结构理论依据；通常匹配效率与价格偏离度及信号强度的关系更为复杂，且 k 作为常数假设忽略了市场异质性。 | 经验事实/模型参数，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体函数形式及参数估计方法的合理性）

## Search Query

auction theory signaling mechanism transaction speed reduction high reserve price
