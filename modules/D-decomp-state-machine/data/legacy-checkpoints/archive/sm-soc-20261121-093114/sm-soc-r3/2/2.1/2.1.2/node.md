# N45: T_decision缩短机制：T_decision' = T_decision * (1 - η * S_signal)，其中η为信号敏感度系数，需验证η * 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N11

## Claim

T_decision缩短机制：T_decision' = T_decision * (1 - η * S_signal)，其中η为信号敏感度系数，需验证η * μ_S是否足以达到30%的缩短幅度，即η * μ_S ≈ 0.3，否则总周期不会变短。

## Corrected Claim

T_decision缩短机制：T_decision' = T_decision * (1 - η * S_signal)，其中η为信号敏感度系数。需验证η * μ_S是否足以达到预期的缩短幅度（如30%），即η * μ_S ≈ 0.3，否则总周期不会显著变短。

## Evidence

父节点级核验未通过：非正交（子节点4（P_dev）属于T_search延长机制，与父节点明确限定的T_decision缩短机制无关，导致子节点集合在逻辑范畴上不纯（非正交/越界）。虽然其他三个子节点覆盖了参数、系数校准和非线性修正，但包含无关变量破坏了分解的正交性。）

## Search Query

decision time reduction signal sensitivity coefficient eta market price signal
