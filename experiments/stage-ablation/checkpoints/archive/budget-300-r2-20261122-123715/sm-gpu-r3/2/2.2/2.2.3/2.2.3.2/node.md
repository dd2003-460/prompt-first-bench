# N210: 未使用 SmoothQuant 时，Qwen3-27B 激活值离群值导致的 INT8 截断误差具体表现为：在特定层（如 Layer 0-10）的激活值标准差 σ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

未使用 SmoothQuant 时，Qwen3-27B 激活值离群值导致的 INT8 截断误差具体表现为：在特定层（如 Layer 0-10）的激活值标准差 σ_act 超过 INT8 安全范围 (±127) 的比例 [待核验]，该比例直接决定截断误差的幅度。

## Corrected Claim

未使用 SmoothQuant 时，Qwen3-27B 激活值离群值会导致 INT8 量化截断误差，尤其在 Layer 0-10 等早期层，激活值分布的长尾特性（标准差较大）会增加超出 INT8 安全范围的风险，从而显著影响量化精度，但具体超范围比例需通过实验测量确定。

## Evidence

[质询]该陈述包含具体的经验性数值断言（特定层激活值标准差超过INT8安全范围的比例），且标记为[待核验]，缺乏具体数据支撑；此外，'直接决定'这一因果表述过于绝对，截断误差还受量化算法（如PTQ/QAT）、校准数据分布及后续层误差累积的影响，并非仅由该比例单一决定。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体比例数值无法从第一性原理推导，属于需实验验证的经验参数）

## Search Query

Qwen3-27B activation outlier distribution INT8 quantization error rate
