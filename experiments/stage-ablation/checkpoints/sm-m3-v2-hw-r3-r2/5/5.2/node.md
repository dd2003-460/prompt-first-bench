# N25: 阶段二复杂度跃迁（Week 3-6）：引入多步推理任务（如文献综述合成）。定义边际贡献率 $MC_2 = \frac{\Delta S_2}{\Delta Co

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

阶段二复杂度跃迁（Week 3-6）：引入多步推理任务（如文献综述合成）。定义边际贡献率 $MC_2 = \frac{\Delta S_2}{\Delta Cost_2}$，其中 $\Delta S_2$ 为任务成功率提升，$\Delta Cost_2$ 为增加的Token消耗。预期 $MC_2$ 在 Prompt 优化初期较高（>0.1%/token），但在 Context Window 接近 262k 上限时急剧下降，此时需切换至分层摘要策略。

## Corrected Claim

阶段二复杂度跃迁（Week 3-6）：引入多步推理任务（如文献综述合成）。定义边际贡献率 $MC_2 = \frac{\Delta S_2}{\Delta Cost_2}$，其中 $\Delta S_2$ 为任务成功率提升，$\Delta Cost_2$ 为增加的Token消耗。预期 $MC_2$ 在 Prompt 优化初期较高（>0.1%/token），但在 Context Window 接近 262k 上限时急剧下降，此时需切换至分层摘要策略。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM long context degradation marginal cost token efficiency
