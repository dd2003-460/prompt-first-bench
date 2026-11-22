# N137: 替代方案推荐规则：若某精度在某任务上Δscore > 2%，则推荐回退到上一级精度（如W4→INT8→FP8→BF16），并计算回退后的显存需求增量和TCO增加

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

替代方案推荐规则：若某精度在某任务上Δscore > 2%，则推荐回退到上一级精度（如W4→INT8→FP8→BF16），并计算回退后的显存需求增量和TCO增加比例

## Corrected Claim

替代方案推荐规则：若某精度在某任务上Δscore > 2%，则推荐回退到上一级精度（如W4→INT8→FP8→BF16），并计算回退后的显存需求增量和TCO增加比例

## Evidence

先验知识/题面给定，逻辑校验通过
