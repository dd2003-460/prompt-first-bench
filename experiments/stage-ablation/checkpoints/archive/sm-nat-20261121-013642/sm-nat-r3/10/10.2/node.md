# N92: 当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_res

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_residence 失效，需采用指数衰减模型 f_update = exp(-U_rate * T_residence) 或精确的稳态陈旧占比模型 C_steady = 1 - exp(-U_rate * T_residence) 来计算有效命中率折损。

## Corrected Claim

当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_residence 失效，需采用指数衰减模型 f_update = exp(-U_rate * T_residence) 或精确的稳态陈旧占比模型 C_steady = 1 - exp(-U_rate * T_residence) 来计算有效命中率折损。

## Evidence

父节点级核验未通过：有冗余（子节点实质上是同一数学关系（线性 vs 指数）在不同参数取值（T_residence=50, 100, 200）下的实例化。虽然它们在数值上覆盖了不同区间（有效、阈值、失效），但在知识分解的粒度上，这属于‘参数扫描’而非‘概念正交’。三个节点的核心逻辑完全一致，仅变量不同，导致信息密度低且存在结构性冗余。）
