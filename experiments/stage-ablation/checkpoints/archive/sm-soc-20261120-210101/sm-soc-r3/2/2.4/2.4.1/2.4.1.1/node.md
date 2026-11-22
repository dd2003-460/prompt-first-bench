# N201: ε_max 的量化公式：ε_max = f(Information_Asymmetry, Cognitive_Load)，具体形式为 ε_max = k_1 *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N55

## Claim

ε_max 的量化公式：ε_max = f(Information_Asymmetry, Cognitive_Load)，具体形式为 ε_max = k_1 * (1 - R_info) + k_2 * C_compute，其中 R_info 为信息完备度（0-1），C_compute 为认知负荷指数，k_1, k_2 为校准系数，需通过实验数据拟合。

## Corrected Claim

在特定认知负荷与信息不对称模型中，ε_max 可被建模为信息完备度缺失与认知负荷的线性组合：ε_max = k_1 * (1 - R_info) + k_2 * C_compute，其中系数需通过实验数据拟合。

## Evidence

[质询]该公式属于特定理论模型或假设性框架下的定义，并非通用的物理或数学第一性原理定律；具体形式（线性组合）及系数 k1, k2 的必要性缺乏普适性证明，可能仅是特定实验场景下的拟合结果而非通用量化公式。 | source=knowledge，逻辑自洽（量纲一致，变量定义清晰），但作为经验性/模型性公式，其具体形式（线性加权和）并非绝对真理，且无外部来源支持其普适性，故降级为定性/特定模型表述。

## Search Query

mixed strategy noise magnitude cognitive load information asymmetry calibration
