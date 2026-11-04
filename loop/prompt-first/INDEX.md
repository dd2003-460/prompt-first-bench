# Loop 阶段路由表

进入每个阶段前只读该阶段的文件，不要一次读全部 7 个。

| 当前阶段 | 必需文件 |
|---------|---------|
| 01-goal-decomposition | 00-common-review.md, 01-goal-decomposition.md, 02-information-research.md |
| 02-information-research | 00-common-review.md, 02-information-research.md, 02.5-cross-check.md |
| 02.5-cross-check | 00-common-review.md, 02.5-cross-check.md, 03-action-decomposition.md |
| 03-action-decomposition | 00-common-review.md, 03-action-decomposition.md, 04-execution-verification.md |
| 04-execution-verification | 00-common-review.md, 04-execution-verification.md, 04.5-final-review.md |
| 04.5-final-review | 00-common-review.md, 04.5-final-review.md |

**纪律**：进新阶段前重读本表，只读该阶段那 2–3 个文件。

**示例层（tier-3，真正按需）**：不在路由表中，不默认读取。仅当遇到以下卡点时才读对应文件：
- 不确定如何写某类工件（decomposition/research/cross-check/action/execution/review）→ 读该阶段的 `examples/<stage>-examples.md`
- 不确定 review verdict 怎么写 → 读 `examples/00-common-review-examples.md`
- 其余情况不读。读过一遍不重读。

**跨阶段豁免**（读产出，不读规则，按需单独取）：
- 02.5 取 01 的分解产出；04 取 03 的步骤表；04.5 取 01–04 全部产出。
- 这些是 `loop-artifacts/stages/` 下的产物，不并入阶段包，也不触发规则重载。

示例层已于 R7 压缩为「每阶段 top-1」，其余移入 `examples/archive/<同名>-extras.md`（原文保留，按需取）。

校验：`python3 bench/self-opt-tester/runs/r6/check-route-coverage.py`（须 exit 0）。
