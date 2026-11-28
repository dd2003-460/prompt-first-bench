# N21: 逻辑一致性自动评估指标：采用 LLM-as-a-Judge 方法，使用 GPT-4o-mini (API) 或本地 Qwen3.8-27B 作为评判者，评估 A

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

逻辑一致性自动评估指标：采用 LLM-as-a-Judge 方法，使用 GPT-4o-mini (API) 或本地 Qwen3.8-27B 作为评判者，评估 AI 生成研究结论的逻辑自洽性；定义指标 Score_logic ∈ [0, 1]，计算方式为 5 个独立维度的加权平均（前提一致性 0.3, 推导步骤有效性 0.3, 无矛盾性 0.2, 边界条件覆盖 0.1, 结论可证伪性 0.1）；人工标注一致性 Kappa 系数 κ≈0.75-0.85 (参考 AlphaProof 基准)，低于 0.8 视为评估不可靠，需增加人工抽查比例至 20%。

## Corrected Claim

逻辑一致性自动评估指标：采用 LLM-as-a-Judge 方法，使用 GPT-4o-mini (API) 或本地 Qwen3.8-27B 作为评判者，评估 AI 生成研究结论的逻辑自洽性；定义指标 Score_logic ∈ [0, 1]，计算方式为 5 个独立维度的加权平均（前提一致性 0.3, 推导步骤有效性 0.3, 无矛盾性 0.2, 边界条件覆盖 0.1, 结论可证伪性 0.1）；人工标注一致性 Kappa 系数 κ≈0.75-0.85 (参考 AlphaProof 基准)，低于 0.8 视为评估不可靠，需增加人工抽查比例至 20%。

## Evidence

先验知识/题面给定，逻辑校验通过
