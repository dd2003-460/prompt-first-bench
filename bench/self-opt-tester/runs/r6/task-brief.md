# origin: ai — R6 run6 任务书（arena 通道 · 阶段门控加载对照 run）

> 本任务书是 [R6] 模板（`tasks/_TEMPLATE-arena-task-brief.md`）的首次实跑应用。
> 与 run2/run5 的差异：**规则不再全量内联**，按 `loop/prompt-first/INDEX.md` 阶段门控加载。

## 【强制段】

你是 arena agent，工作仓库 = `dd2003-460/prompt-first-bench`，分支你的 arena 工作分支。
先 `git fetch` + `git ls-remote` 记录 HEAD。严格按步骤执行，产出落盘路径见【交付物】。
任何通道故障报告 Lead，不得静默跳过、不得伪造数据。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份。

## 【规则加载 · 阶段门控】

| 项 | 内容 |
|---|---|
| 路由表 | `loop/prompt-first/INDEX.md`（必读，482 o200k） |
| 当前阶段 | `01-goal-decomposition` |
| 本阶段规则包 | `00-common-review.md` + `01-goal-decomposition.md` + `02-information-research.md` = 4,091 o200k |
| 后续阶段 | 进入时**重读 INDEX.md**，只读该阶段的 2–3 个文件；已读文件不重读 |

纪律：不要一次性读全部 7 个 loop 文件。校验命令：`node bench/self-opt-tester/runs/r6/count-rule-tokens.js --stage 01`。

## 【目标】

回答一个 P0 上线前必须回答的问题：**阶段门控加载（INDEX 路由）会不会漏载跨阶段依赖？**
具体要求：
1. 把「漏载」拆成可判定的失效模式（正交分解，≤10 行）；
2. 给出一个**可机器执行**的漏载检测机制，并真跑一次（不是设计文档）；
3. 用实测 token 数据判断：P0 单独是否足以支撑 M1 ≥ 70，还是必须上 P1（规则压缩）。

## 【背景】≤10 行

- run2 每轮重发 7 个 loop 文件 + SOP = 12,086 o200k；T=30 turns 时规则重发 ≈ 362,580 tok。
- R6 实施 P0：INDEX 路由 + 阶段包（2–3 文件），目标单 turn 规则负载 12,086 → ~3,700。
- 风险：路由表把「规则文件」的依赖画对了，但**跨阶段真正需要的是上游产出**（loop-artifacts/stages/<N>/）。
  若 INDEX 只画规则依赖，agent 可能进入 02.5 时手里没有 01 的分解产出。
- 本 run 的任务 = 把这层风险变成可检测的断言。

## 【执行分解】9 步（每步挂不可伪造锚点）

1. `git fetch` + `git ls-remote` 记录远端 HEAD（anchor: 哈希）
2. 读 `INDEX.md`，用 `count-rule-tokens.js` 实测本阶段包 token（anchor: 脚本输出）
3. 目标分解：漏载失效模式正交分解 → `loop-artifacts/stages/01/R6-01-decomp.md`
4. 信息调研：≥2 独立来源查「progressive disclosure / context engineering」的既有实践（anchor: URL + 原文摘句）
5. 交叉核验：矛盾点记录 → `loop-artifacts/stages/02.5/R6-02.5-crosscheck.md`
6. 行动分解：漏载检测机制设计（检查什么、怎么判、exit code）→ `loop-artifacts/stages/03/R6-03-actions.md`
7. 执行+验证：写出并**真跑**检测脚本 → `bench/self-opt-tester/runs/r6/check-route-coverage.py` + 输出
8. 终检：`git ls-remote` 验证 push 落点
9. 汇总：9 步锚点清单 + M1–M8 自评 + token 账本 → `run6-token-analysis.md` / `run6-m1-score.json`

## 【交付物】

- `loop/prompt-first/INDEX.md`（已由 Lead 落地，本 run 校验）
- `bench/self-opt-tester/runs/r6/`：`run6-token-analysis.md` / `run6-m1-score.json` / `token-ledger-run6.json` / `check-route-coverage.py`
- `loop-artifacts/stages/01,02,02.5,03,04,04.5/R6-*.md`
- 回执：repo URL + branch + commit_sha + 自报模型身份

## 【失败降级】

- 无服务端 per-request 日志 → 用 o200k tokenizer 实测规则文件，逐 turn 记账本，标注 conf。
- 通道故障 → 停在当前步骤，回执注明完成到哪一步。
- 若 M1 < 70 → 如实报告，不要凑数。
