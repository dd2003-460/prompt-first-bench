# N143: W4 (NVFP4/INT4) 精度的 QF 值估算：基于 N14 的描述，长上下文下精度损失极小 (<0.5%)，故 QF_W4 取值范围 [0.995, 1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

W4 (NVFP4/INT4) 精度的 QF 值估算：基于 N14 的描述，长上下文下精度损失极小 (<0.5%)，故 QF_W4 取值范围 [0.995, 1.0] [待核验]，但需确认短上下文或代码生成任务上的潜在波动。

## Corrected Claim

W4 (NVFP4/INT4) 精度在长上下文场景下表现良好，QF 值预计接近 1.0，但在短上下文或代码生成等对细节敏感的任务中可能存在波动，具体数值需依赖实际基准测试确认。

## Evidence

[质询]该陈述将‘长上下文下精度损失极小’直接外推为‘QF值在[0.995, 1.0]区间’，忽略了短上下文、代码生成等特定任务场景下量化误差可能显著放大的风险，且缺乏具体基准测试数据支持该数值区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于具体量化精度经验参数，不适用第一性原理推导）

## Search Query

Qwen3 INT4 NVFP4 quantization accuracy loss benchmark
