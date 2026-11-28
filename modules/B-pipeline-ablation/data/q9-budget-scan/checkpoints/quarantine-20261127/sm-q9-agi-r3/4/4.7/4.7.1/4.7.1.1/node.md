# N235: 分层抽样的基础公式为 n_i = n_total * (p_i * sqrt(e_i)) / Σ(p_j * sqrt(e_j))，其中 p_i 为第 i 阶段

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

分层抽样的基础公式为 n_i = n_total * (p_i * sqrt(e_i)) / Σ(p_j * sqrt(e_j))，其中 p_i 为第 i 阶段的历史错误率，e_i 为该阶段单位样本验证成本（Token消耗+人工时间），n_total 为总抽样预算（10%总样本量）。

## Corrected Claim

分层抽样的基础公式为 n_i = n_total * (p_i * sqrt(e_i)) / Σ(p_j * sqrt(e_j))，其中 p_i 为第 i 阶段的历史错误率，e_i 为该阶段单位样本验证成本（Token消耗+人工时间），n_total 为总抽样预算（10%总样本量）。

## Evidence

先验知识/题面给定，逻辑校验通过
