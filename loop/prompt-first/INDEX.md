# Loop 阶段路由表

进入每个阶段前只读该阶段的文件，不要一次读全部 7 个。示例列属 tier-3：规则文件指到时才读。

| 当前阶段 | 必需文件 | 示例（按需） |
|---------|---------|-------------|
| 01-goal-decomposition | 00-common-review.md, 01-goal-decomposition.md, 02-information-research.md | examples/00-common-review-examples.md, examples/01-examples.md |
| 02-information-research | 00-common-review.md, 02-information-research.md, 02.5-cross-check.md | examples/00-common-review-examples.md, examples/02-examples.md |
| 02.5-cross-check | 00-common-review.md, 02.5-cross-check.md, 03-action-decomposition.md | examples/00-common-review-examples.md, examples/02.5-examples.md |
| 03-action-decomposition | 00-common-review.md, 03-action-decomposition.md, 04-execution-verification.md | examples/00-common-review-examples.md, examples/03-examples.md |
| 04-execution-verification | 00-common-review.md, 04-execution-verification.md, 04.5-final-review.md | examples/00-common-review-examples.md, examples/04-examples.md |
| 04.5-final-review | 00-common-review.md, 04.5-final-review.md | examples/00-common-review-examples.md, examples/04.5-examples.md |

**纪律**：进新阶段前重读本表，只读该阶段那 2–3 个文件；示例读过一遍不重读。

**跨阶段豁免**（读产出，不读规则，按需单独取）：
- 02.5 取 01 的分解产出；04 取 03 的步骤表；04.5 取 01–04 全部产出。
- 这些是 `loop-artifacts/stages/` 下的产物，不并入阶段包，也不触发规则重载。

示例层已于 R7 压缩为「每阶段 top-1」，其余移入 `examples/archive/<同名>-extras.md`（原文保留，按需取）。

校验：`python3 bench/self-opt-tester/runs/r6/check-route-coverage.py`（须 exit 0）。
