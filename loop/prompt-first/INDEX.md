# Loop 阶段路由表

> 用途：**阶段门控加载**。进入每个阶段前只读该阶段需要的 2–3 个文件，不要一次性读全部 7 个。
> 生成于 R6（2026-11-04）；规则正文零改动，只改「读什么」的路由。
> **v1.1（R6 自检修正）**：v1.0 漏画了各阶段文件的 `examples/` 引用，被
> `bench/self-opt-tester/runs/r6/check-route-coverage.py` 判出 7 条 X-miss，现补第三列「示例（按需）」。
> 校验：`python3 bench/self-opt-tester/runs/r6/check-route-coverage.py`（须 exit 0）。

| 当前阶段 | 必需文件（每轮加载） | 示例（按需，规则文件指到才读） |
|---------|----------------------|--------------------------------|
| 01-goal-decomposition | 00-common-review.md, 01-goal-decomposition.md, 02-information-research.md | examples/00-common-review-examples.md, examples/01-examples.md |
| 02-information-research | 00-common-review.md, 02-information-research.md, 02.5-cross-check.md | examples/00-common-review-examples.md, examples/02-examples.md |
| 02.5-cross-check | 00-common-review.md, 02.5-cross-check.md, 03-action-decomposition.md | examples/00-common-review-examples.md, examples/02.5-examples.md |
| 03-action-decomposition | 00-common-review.md, 03-action-decomposition.md, 04-execution-verification.md | examples/00-common-review-examples.md, examples/03-examples.md |
| 04-execution-verification | 00-common-review.md, 04-execution-verification.md, 04.5-final-review.md | examples/00-common-review-examples.md, examples/04-examples.md |
| 04.5-final-review | 00-common-review.md, 04.5-final-review.md | examples/00-common-review-examples.md, examples/04.5-examples.md |

**纪律**：每次进入新阶段前，先读 INDEX.md 确定需要哪些文件，只读那些文件。不要一次性读全部 7 个。
示例文件属 tier-3：阶段规则文件没指到就不读；指到了再读，读完整阶段不再重读。

**跨阶段依赖豁免**：以下依赖读的是**产出**不是**规则**，按需单独取，不并入阶段包
（详见 `loop-artifacts/stages/04.5/R6-04.5.md` §漏载风险）：
- 02.5 需要 01 的分解产出（`loop-artifacts/stages/01/`），不是 01 的规则文件；
- 04 需要 03 的步骤表（`loop-artifacts/stages/03/`），不是 03 的规则文件；
- 04.5 复核需要 01–04 全部**产出**，不是全部**规则**——只读产出即可，规则不再重载。
