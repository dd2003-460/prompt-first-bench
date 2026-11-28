# N91: 分块处理策略的阈值判定：当SSRB实测Recall@1 < 0.5时，启用滑动窗口分块（Window=8k, Step=4k），分块后整体召回率提升ΔR = R

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

分块处理策略的阈值判定：当SSRB实测Recall@1 < 0.5时，启用滑动窗口分块（Window=8k, Step=4k），分块后整体召回率提升ΔR = R_chunked - R_flat，预期ΔR ≥ 0.2，需通过A/B测试验证分块边界处的实体截断误差E_trunc < 5%。

## Corrected Claim

分块处理策略的阈值判定：当SSRB实测Recall@1 < 0.5时，启用滑动窗口分块（Window=8k, Step=4k），分块后整体召回率提升ΔR = R_chunked - R_flat，预期ΔR显著为正（具体阈值需根据基线数据校准），需通过A/B测试验证分块边界处的实体截断误差E_trunc处于可接受范围（如<5%）。

## Evidence

[质询]预期提升幅度 ΔR ≥ 0.2 缺乏普遍适用的理论或经验支撑，属于高度依赖具体数据集分布的经验性假设，不同场景下实际提升可能远低于此阈值。 | 先验知识/题面给定，逻辑校验通过（流程自洽），但具体数值阈值（ΔR≥0.2, E_trunc<5%）为经验参数，无外部来源支持，故降级。
