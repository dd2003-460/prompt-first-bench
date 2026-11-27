# N399: 24/7 长期运行场景下的 TCO 交叉点分析：设 H100 方案 3 年 TCO 为 T_H100，Mac Studio 方案 3 年 TCO 为 T_Mac

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N165

## Claim

24/7 长期运行场景下的 TCO 交叉点分析：设 H100 方案 3 年 TCO 为 T_H100，Mac Studio 方案 3 年 TCO 为 T_Mac。T_H100 ≈ $95,000 (N289 修正后)。T_Mac ≈ $4,000 (Capex) + $1,500 (3yr Power) + $0 (Maint) - $2,000 (Residual) = $3,500。在纯成本视角，Mac Studio 方案 TCO 仅为 H100 的 3.7%。但在性能视角，H100 吞吐量约为 Mac 的 3-4 倍（假设 H100 为 150 tokens/s），单位成本吞吐量 (Cost_per_Token) H100 ≈ $95,000 / (150 * 8760 * 3) ≈ $0.0024/token，Mac ≈ $3,500 / (12.5 * 8760 * 3) ≈ $0.0001/token。结论：在 24/7 高负载场景下，Mac Studio 的能效比优势转化为极低的单位 Token 成本，远超 H100，N165 关于“Mac 可部分抵消 Capex 劣势”的说法保守，实际是 Mac 在单位成本上具有压倒性优势，前提是软件栈支持（llama.cpp/MLX）且模型精度满足要求。

## Corrected Claim

在假设 H100 吞吐量为 150 tokens/s 且 Mac Studio 为 12.5 tokens/s 的特定条件下，Mac Studio 的单位 Token 成本显著低于 H100。但实际 TCO 需计入 H100 的电力、冷却及运维成本，且吞吐量假设需根据具体模型和硬件配置重新校准，不能直接得出 Mac 具有'压倒性优势'的普适结论。

## Evidence

[质询]核心假设存在严重偏差：1. 吞吐量假设不合理，H100 在 24/7 高负载下通常远高于 150 tokens/s（取决于模型大小，但 150 偏低），而 Mac Studio (M2/M3 Ultra) 在同等模型下吞吐量通常低于 12.5 tokens/s 或接近，导致 3-4 倍的性能差距假设可能过于乐观或悲观，直接影响单位成本计算；2. 忽略了 H100 方案的运维、电力及冷却成本，仅对比 Mac 的电力成本，导致 T_H100 被低估，T_Mac 被高估（相对优势被夸大）；3. '24/7 高负载'下 Mac Studio 的散热和稳定性风险未计入 TCO。 | 逻辑推导在给定参数下自洽，但关键经验参数（吞吐量、TCO 构成）缺乏来源支持且存在明显简化，属于经验事实，逻辑自洽但缺来源支持，且假设条件（吞吐量倍数）存在较大不确定性。
