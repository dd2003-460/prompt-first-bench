# 原 r4 evidence packet 单行摘要全字段审计（R5.2-audit）

> origin: ai · 2026-10-30 · R5.2-packet-audit goal 交付物 1
> 审计对象：`r4/independent-scoring-deepseek.json` → `evidence_packet` 字段（逐字）：
> `M1-M6 定义 + 3 run 证据（run1 7锚点/5.11M累计未切分/无降级；run2 14m27s/10锚点/12,086 o200k重发/2降级；run3 7锚点/无网络/3模板缺陷/任务书25行）`
> WS = `/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3`
> verdict 口径：**confirmed** = 原始证据正向证实；**mismatch** = 与原始证据矛盾；**unverified** = 无法从本地证据重建（非矛盾）。所有断言按**字面口径**核验（语义辩护只作缓解注记，不翻转 verdict——02.5 A1 裁决）。

## 结果汇总

| verdict | 条数 | 编号 |
|---------|------|------|
| confirmed | 8 | C1 C2 C5 C6 C7 C8 C9 C10 |
| mismatch | 3 | C3 (X4) / C11 (X2 已知) / C12 (X7) |
| unverified | 1 | C4 (X5) |

另登记关联错配 X6（adjudication-step2.json "49/25/25"，packet 外同链路文档）。

## 逐条审计表

| # | run | packet 原文片段 | verdict | 证据定位（路径 + 原文） | 严重度 | X 登记 |
|---|-----|----------------|---------|------------------------|--------|--------|
| C1 | run1 | "7锚点" | **confirmed** | `$WS/run1/loop-state.json` `"anchors_count": 7, "gate_passed": 7`；佐证 `bench-r3.json` M7 "run1 7/7" | — | — |
| C2 | run1 | "5.11M累计未切分" | **confirmed** | `$WS/run1/token-ledger.json` `input_tokens_cumulative: 5108882`（≈5.11M）+ `run1_scope_note`："input 累计含 r1/r2 历史，run1 专属增量需按 requests 时间戳切分（待 R3.5 做）" | — | — |
| C3 | run1 | "无降级" | **mismatch** | `$WS/run1/loop-state-r1.json` `degraded` 数组 **3 项**（create_goal 不可用 / report_step 改用 loop-state 记录 / arena 通道全链路降级 conf-0.2）；`run1/execution-log.md` 有 "## 降级记录" 节。缓解注记：3 项降级全部如实留痕（M6 诚实性不受损），但字面 "无降级" 为假 | 中 | **X4** |
| C4 | run2 | "14m27s" | **unverified** | 唯一载体 = `$WS/run2/loop-state.json` channel 字段（转录件）；原始计时源 = arena 网页会话（外部不可复访）；pfb 内首次出现于 commit 3798b21；`r4/token-split.json` run2.arena_side 已注 "token 本地无账本"。无相反证据，只是无法正向重建 | 低 | **X5** |
| C5 | run2 | "10锚点" | **confirmed** | `$WS/run2/loop-state.json` `"anchors_count": 10`；佐证 `bench-r3.json` "run2 7/7(10锚点)" | — | — |
| C6 | run2 | "12,086 o200k重发" | **confirmed** | 数值：`$WS/run2/token-counts.txt` RULE LOAD TOTAL 行 `TOTAL 39858B o200k=12086`（L11）。机制："每 turn 重发" 见 `$WS/run2/04.5-review.md` L27 原文 + `02-research.md` E1（3 独立源 conf 0.8） | — | — |
| C7 | run2 | "2降级" | **confirmed** | `$WS/run2/loop-state.json` degraded 数组长度 = 2（main push→工作分支；ego-browser exit 1→web_search） | — | — |
| C8 | run3 | "7锚点" | **confirmed** | `$WS/run3/loop-state.json` `"anchors_count": 7` | — | — |
| C9 | run3 | "无网络" | **confirmed** | `$WS/run3/execution-log.md` M6 行 "无网络/无 arena 全程如实标注 unverified"；`r4/token-split.json` run3.note "subagent 独立 session，无网络" | — | — |
| C10 | run3 | "3模板缺陷" | **confirmed** | `$WS/run3/03-review.md` `^## 缺陷` 标题恰好 3 个（L8/L18/L29）；归属核对：packet 将其挂在 run3 名下，与文件位置一致 | — | — |
| C11 | run3 | "任务书25行" | **mismatch（已知）** | 即 R5.2 登记的 **X2**：25 = run2 task-brief 实测（`bench/self-opt-tester/run2-arena/task-brief.md` wc -l = 25）；run3 任务书为 Lead 派发消息文本，无落盘文件，唯一记载 = execution-log bench-row 自估 "~45 行"。packet v2 已修正（run3 P1=null/~45） | 高 | X2（引用） |
| C12 | 跨 run | "M1-M6 定义 +" | **mismatch（形式性）** | packet 字段全文不含任何 M1-M6 定义正文——"M1-M6" 仅出现在该自我声称处；指标含义靠缩写术语隐含传递。声称-内容不符 | 低 | **X7** |

## 关联错配面（packet 外、同一输入链路）

### X6：`r4/adjudication-step2.json` inputs "任务书 49/25/25 行"

- 原文：`inputs: "step2 追问（自估 18 分 + 3 条补充证据：任务书 49/25/25 行 / 3 run 均 1 轮完成 conf 0.9/0.8 / M4 三 run 独立源事实）"`
- 对照实测：run1 = **24**（X3 三源一致冻结）≠ 49；run2 = 25 ✓；run3 = null/~45 自估 ≠ 25（X2 同源错配再现）。
- 49 来源：全仓 grep 无第二出处，判定为 step2 追问时 Lead 侧笔误/口误（49 可能是其他文件的行数被误代入）。
- **对冻结分的传导核查**（A2）：step2 裁决 `run1_M2: winner=self, final=100, reason="49 行 ≤200 行满分"` → 该 100 进入 r4 冻结分 76.45±7.29 的 M2 均值。**关键事实：结论不变**——24 行同样 ≤200，M2=100 对正确值依然成立；错的是理由文本引用的数字，不是分值本身。同句 "3 run 均 1 轮完成" 与 packet v2 P2（run3=2 轮自述）口径不一，但未触任何裁决项（run3_M5 裁决理由是 conf 0.8 而非轮数）。
- 处置：分值不动（分数冻结纪律）；提请成璐裁决 caveat 注记方式 → `个人/APPROVALS.md` 条目 3（选项 3.1/3.2/3.3）。

## X4 对冻结分的传导核查（A2）

- DeepSeek `independent_scores` 三个 run 的 M6 均为 100，但 `key_reasons` **无任何 M6 条目**（M6 不在 |Δ|>15 分歧清单，走 "保留自估/盲打" 路径）；`items_without_adjudication_delta_le_15` 列明 run2 M6(100/95)、run3 M6(100/95) 保留自估。
- 即：packet 的 "无降级" 措辞**未被任何 key_reason 引用为打分依据** → X4 不传导进冻结分值，仅登记（措辞歧义风险供后续 packet 写作参考）。

## 对第三打分器（R5.2-third-scorer）的影响说明

1. **v1 packet 不应再作为第三打分器的输入**——它同时存在缺失（C12 定义句为空承诺）、错配（C3/C11/X6）与不可核验值（C4）三类问题。
2. **packet v2（`r5/evidence-packet-r4-v2.json`）已覆盖全部 mismatch 面**：C11 已修（run3 P1=null/~45 + basis）；C3 对应 P5 字段以完整降级条目列表呈现（run1 3 项如实列出，不再有 "无降级" 措辞）；C12 由 P1-P6 必填 schema 结构性消除；C4 在 v2 caveats 标注 unverified。对称性断言 67/0 通过（r102）。
3. 因此 third-scorer goal **直接用 packet v2 即可**，无需回读 v1；本审计的价值 = 排除 "v1 残余错配影响 κ 解释" 的风险（R5.1 的 4 项分歧归因于缺失字段，现已确认不存在第 5+ 项来自错配的隐性分歧源——C3 若被打分器采信只会影响 M6 措辞理解，而 M6 三 run 双打分器均给高分且无分歧）。

## 附录：机判脚本运行输出

见 `assert-packet-audit.py` 运行 stdout（同目录执行 `python3 assert-packet-audit.py`，exit 0）。