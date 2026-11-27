# N10: ‘降价无响应’机制：主动降价触发‘柠檬市场’逆向选择信号。买家模型更新：P(Defective | Price_Drop) > P(Defective | Pr

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

‘降价无响应’机制：主动降价触发‘柠檬市场’逆向选择信号。买家模型更新：P(Defective | Price_Drop) > P(Defective | Price_Stable)。具体表现为，降价后48小时内新咨询量 ΔQ_consult ≈ -β * (P_drop / P_initial)，其中 β 为价格敏感度系数，且 β 在二手非标品中显著大于标准化品。

## Corrected Claim

‘降价无响应’机制：主动降价可能触发‘柠檬市场’逆向选择信号，导致买家对商品缺陷概率的后验估计上升（P(Defective | Price_Drop) > P(Defective | Price_Stable)）。在二手非标品市场中，这种负面信号效应通常比标准化品更显著，可能导致咨询量或成交意愿下降，但具体下降幅度取决于价格敏感度及市场结构，无统一固定公式。

## Evidence

[质询]该陈述将‘柠檬市场’的定性逆向选择机制强行量化为具体的线性公式（ΔQ_consult ≈ -β * (P_drop / P_initial)）及特定时间窗口（48小时），且声称β在二手非标品中显著大于标准化品。这种具体的数学形式和参数比较缺乏通用的经济学理论支持，属于过度精确化的经验断言，极易因具体市场情境、品类差异而失效，存在将复杂非线性行为简化为单一线性模型的逻辑风险。 | 先验知识/题面给定，逻辑校验通过（定性机制符合柠檬市场理论，但定量公式缺乏普适性来源支持，故降级）

## Search Query

price drop negative signal lemon market second-hand goods consultation drop
