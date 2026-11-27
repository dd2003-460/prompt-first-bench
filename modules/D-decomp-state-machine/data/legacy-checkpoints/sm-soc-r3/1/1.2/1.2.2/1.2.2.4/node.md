# N127: 禀赋溢价对成交周期的负向反馈机制：高 π_endow 导致 P_ask 偏离 P_market 增大，进而通过降低匹配概率 P_match 延长 T_close

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

禀赋溢价对成交周期的负向反馈机制：高 π_endow 导致 P_ask 偏离 P_market 增大，进而通过降低匹配概率 P_match 延长 T_close；量化关系为 T_close ≈ T_base / (1 - π_endow/π_threshold)，其中 π_threshold 为买家容忍上限（约 30%），当 π_endow > π_threshold 时，T_close 趋向无穷（无成交）。

## Corrected Claim

禀赋溢价对成交周期存在负向反馈机制：高 π_endow 导致 P_ask 偏离 P_market 增大，进而通过降低匹配概率 P_match 延长 T_close；当 π_endow 超过买家容忍上限时，成交概率显著下降，T_close 显著延长甚至无成交。

## Evidence

[质询]该量化公式 T_close ≈ T_base / (1 - π_endow/π_threshold) 缺乏经济学或市场微观结构理论支持，属于任意构造的数学模型，且将复杂的匹配概率简化为单一禀赋溢价的线性倒数关系，忽略了流动性、搜索成本等多重因素，存在过度简化和因果归因谬误。 | 经验事实/理论模型，逻辑自洽但缺来源支持（检索无可用来源，且该具体公式非公认第一性原理推论）

## Search Query

endowment effect impact on time to sell negative feedback loop price deviation matching probability
