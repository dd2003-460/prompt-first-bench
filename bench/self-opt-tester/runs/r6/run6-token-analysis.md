# R6 · Token 消耗分析（阶段门控加载 vs run2 全量注入）

> 任务书：`tasks/TASK-r6-arena-token-optimization.md`（origin/main `7502348`）
> run 协议：9 步链路（与 run2/run5 同协议，新题面防复读）
> 计量工具：o200k_base（js-tiktoken，离线 ranks）→ `count-rule-tokens.js`（可复跑）
> 账本：`token-ledger-run6.json` ｜ 打分：`run6-m1-score.json`
> 生成：2026-11-04（Asia/Shanghai）

---

## 0. 一句话结论

**单 turn 规则负载 12,086 → 3,023 o200k（−75.0%），M1 = 78.2 ≥ 70（达标）；但换成「单会话走完 6 阶段」的保守口径，均值只降 43.1%、末态只降 8.9%，M1 = 62.0（不达标）。两个数字都成立，差别全在「规则读进上下文后会不会被卸载」。**

附带一个会改结论的发现：**v1.0 路由表漏掉了 7 个 `examples/*.md`（合计 4,211 tok），"降 74%"里有一部分是把它悄悄切掉了**；补上后才是 69%——与任务书目标巧合到几乎一致（见 §3）。

---

## 1. 基线（run2）

| 项 | 值 | 出处 |
|---|---|---|
| 每 turn 规则负载 | **12,086 o200k / 39,858 B** | `r5/packet-audit-r4-v1.md` C6：`TOTAL 39858B o200k=12086` |
| 构成（本轮实测拆分） | SOP 6,426 + 6 个阶段文件 5,243 + run2 任务书 417 | `count-rule-tokens.js` |
| 机制 | 全量内联进任务书 → **每轮重发** | `run2-arena/04.5-review.md` L27 |
| M1 | 量化 14.3 / 人工 25（S=0.0, R=0.0, G=0.57） | 任务书 §背景 |

✓ 拆分校验：6,426 + 5,243 + 417 = **12,086**，与 run2 实测逐 token 相等 —— 说明本轮口径与 run2 同源，不是另起一套。

---

## 2. 文件级实测（o200k）

| 文件 | tok | 文件 | tok |
|---|---|---|---|
| `00-common-review.md` | 1,099 | `examples/00-common-review-examples.md` | 210 |
| `01-goal-decomposition.md` | 1,755 | `examples/01-examples.md` | 660 |
| `02-information-research.md` | 1,237 | `examples/02-examples.md` | 528 |
| `02.5-cross-check.md` | 471 | `examples/02.5-examples.md` | 622 |
| `03-action-decomposition.md` | 565 | `examples/03-examples.md` | 883 |
| `04-execution-verification.md` | 653 | `examples/04-examples.md` | 678 |
| `04.5-final-review.md` | 562 | `examples/04.5-examples.md` | 630 |
| **`INDEX.md`（新增）** | **458** | 示例合计 | **4,211** |
| 7 个核心文件合计 | 6,342 | | |

阶段包（INDEX + 必需 + 本阶段示例）：

| 阶段 | 必需 | +示例 | 含 INDEX |
|---|---|---|---|
| 01 | 4,091 | 870 | **5,419** |
| 02 | 2,807 | 738 | **4,003** |
| 02.5 | 2,135 | 832 | **3,425** |
| 03 | 2,317 | 1,093 | **3,868** |
| 04 | 2,314 | 888 | **3,660** |
| 04.5 | 1,661 | 840 | **2,959** |

均值 3,709（= 任务书目标「~3,700」，非巧合，见 §3 的修正过程）。

---

## 3. 关键发现：路由表 v1.0 漏了 examples 层

检测器 `check-route-coverage.py`（本轮新写，见 §5）对 v1.0 路由表首跑：

```
X-miss (rule refs not in route): 7
  - 00-common-review.md:30 -> examples/00-common-review-examples.md  missing in ['01','02','02.5','03','04','04.5']
  - 01-goal-decomposition.md:60 -> examples/01-examples.md  missing in ['01']
  - 02-information-research.md:65 -> examples/02-examples.md  missing in ['02']
  - 02.5-cross-check.md:25 -> examples/02.5-examples.md  missing in ['02.5']
  - 03-action-decomposition.md:22 -> examples/03-examples.md  missing in ['03']
  - 04-execution-verification.md:33 -> examples/04-examples.md  missing in ['04']
  - 04.5-final-review.md:24 -> examples/04.5-examples.md  missing in ['04.5']
RESULT: FAIL (exit 1)
```

- 7 个规则文件里有 6 个明文写着「操作示例见 `examples/xx.md`」，而 v1.0 路由表一个都没排进去。
- 后果：只按 v1.0 读，agent 会**静默不读示例**。规则负载当然更低（3,012），但那是**靠少读东西换来的**，不是靠切分换来的。
- 修正：INDEX.md 升 v1.1，加第三列「示例（按需，tier-3）」。复跑 `X-miss = 0, exit 0`。

**这条是本轮最重要的结论**：门控动作本身会制造漏载，而漏载只能靠机检发现——7 个文件互相指引的引用关系人肉 review 不现实。

---

## 4. 逐 turn 账本（9 步）

| turn | 步骤 | 新加载 | Model A（阶段包口径） | Model B（单会话累计） |
|---|---|---|---|---|
| 1 | fetch + ls-remote | INDEX | 458 | 458 |
| 2 | 读 INDEX + 实测 | — | 458 | 458 |
| 3 | 01 目标分解 | 00,01,02 + ex00,ex01 | 5,419 | 5,419 |
| 4 | 02 信息调研 | 02.5 + ex02 | 4,003 | 6,418 |
| 5 | 02.5 交叉核验 | 03 + ex02.5 | 3,425 | 7,605 |
| 6 | 03 行动分解 | 04 + ex03 | 3,868 | 9,141 |
| 7 | 04 执行+验证 | 04.5 + ex04 | 3,660 | 10,381 |
| 8 | 04.5 复核 | ex04.5 | 2,959 | 11,011 |
| 9 | 汇总 | — | 2,959 | 11,011 |
| | **均值** | | **3,023（−75.0%）** | **6,878（−43.1%）** |

两个口径的定义差异：

- **Model A**：harness 每 turn 只注入当前阶段包（任务书按阶段重写/重置）。
- **Model B**：arena agent mode 的实际行为——单会话，读进上下文的规则**不会被卸载**，每轮重发的是累积上下文。
- 末态：Model B 收敛到 11,011，对基线 12,086 **只省 8.9%**。因为 9 步走完了全部 6 个阶段，最终必然触达全部文件（02.5 的 C3 早已预警）。

---

## 5. M1 量化

公式：`M1 = 100 × (0.4·S + 0.35·R + 0.25·G)`

| 分量 | 定义（本轮口径） | Model A | Model B |
|---|---|---|---|
| S | 有 per-request 日志且可切分到 run 窗口 → 1.0 | 0.6 | 0.6 |
| R | x = 每 turn 规则负载均值 / 12,086；`R = clamp((1−x)/0.9, 0, 1)` | x=0.250 → **0.833** | x=0.569 → **0.479** |
| G | g = 末 turn / 首个完整阶段包 turn；`G = clamp((5−g)/3.5, 0, 1)` | g=0.55 → **1.000** | g=2.03 → **0.848** |
| **M1** | | **78.2** | **62.0** |

S=0.6 的依据：本轮有 9/9 行逐 turn 账本、token 数可第三方用同脚本复算，但**是执行侧自产、非服务端日志**，且「turn→文件」映射来自任务书设计而非抓包。run2 是 0.0（完全无账本），本轮不应拿满分。

敏感性（S 取 0.5/0.6/0.7/1.0）：

| 口径 | S=0.5 | S=0.6 | S=0.7 | S=1.0 |
|---|---|---|---|---|
| Model A | 74.2 | 78.2 | 82.2 | 94.2 |
| Model B | 58.0 | 62.0 | 66.0 | 78.0 |

**M1 的达标与否几乎完全由「harness 是否按阶段重写任务书」决定**，S 只在 ±4 分内摆动。

---

## 6. 验收判定

| 口径 | M1 | vs run2 人工 25 | 判定（≥70） |
|---|---|---|---|
| Model A（任务书目标量同口径） | **78.2** | +53.2 | **PASS** |
| Model B（单会话保守） | **62.0** | +37.0 | **FAIL** |

**取哪个当结论**：任务书写「降低单 turn 规则负载从 12,086 → ~3,700」，3,700 这个数就是 Model A 的量；同口径对比只有 Model A 可比。但 Model B 是**更保守、更接近 arena 实际**的数，不能藏。

→ 因此判 **CONDITIONAL-PASS**：P0 在任务书定义下达标；在单会话实际行为下达不到 70，缺口 ≈ 8 分，需要 P1（规则压缩）或 harness 支持「按阶段重写任务书/重置上下文」。

**不凑数声明**：本轮所有数字均由 `count-rule-tokens.js` 实测，没有调参凑 70。若把 S 调到 1.0，Model B 才刚好 78 —— 但那需要服务端日志，本轮没有。

---

## 7. 交付物清单

| 路径 | 内容 |
|---|---|
| `loop/prompt-first/INDEX.md` | 路由表 v1.1（1,678 B / 458 tok），含 examples 第三列 + 跨阶段豁免清单 |
| `sop/arena-loop-pipeline.md` §2 | 强制段从「全量注入」改为「阶段门控」+ 注入量对照 |
| `tasks/_TEMPLATE-arena-task-brief.md` | 新任务书模板（阶段包占位符 + 校验命令） |
| `bench/self-opt-tester/runs/r6/count-rule-tokens.js` | 规则负载计量器（o200k，缺依赖时降级字节估算） |
| `bench/self-opt-tester/runs/r6/check-route-coverage.py` | 漏载检测器（R/X/A/G 四类断言，exit code 可挂 CI） |
| `bench/self-opt-tester/runs/r6/token-ledger-run6.json` | 9 turn 账本 + 双口径聚合 + 4 条 caveat |
| `bench/self-opt-tester/runs/r6/run6-m1-score.json` | M1 打分（双口径 + 敏感性表 + 置信度） |
| `bench/self-opt-tester/runs/r6/task-brief.md` | 本轮任务书（模板首用） |
| `loop-artifacts/stages/{01,02,02.5,03,04,04.5}/R6-*.md` | 6 阶段产出（每阶段带 verdict） |

---

## 8. 复现

```bash
git checkout <this-branch>
node bench/self-opt-tester/runs/r6/count-rule-tokens.js --json    # 逐文件 + 6 阶段包
python3 bench/self-opt-tester/runs/r6/check-route-coverage.py     # 期望 exit 0
python3 bench/self-opt-tester/runs/r6/check-route-coverage.py --index <v1.0 副本>  # 期望 exit 1
```

依赖：`js-tiktoken`（`npm i js-tiktoken`，离线可用）。缺失时计量器降级为 `bytes/3.32` 并在输出里标 `tokenizer` 字段，不会静默改口径。

---

## 9. 遗留与建议

1. **P1 需要上**：单会话口径 62.0，缺口 8 分。压缩方向：`02-information-research.md`(1,237) 与 `01-goal-decomposition.md`(1,755) 是核心文件里最大的两个；示例层 4,211 也可再瘦。
2. **harness 行为待确认**：若 arena 支持「每阶段重写任务书 / 阶段间重置上下文」，Model A 成立，P0 已达标。这是本轮唯一的关键未知，建议下一轮用一次 2 阶段小 run 验证（成本 ~10 turn）。
3. **检测器应进 CI**：`check-route-coverage.py` 已可 exit code 门禁。以后任何 INDEX/规则改动都该先过它，否则漏载会静默发生（本轮就是这么发现的）。
4. **S 分量的天花板**：只要拿不到服务端 per-request 日志，S 就封顶在 0.6–0.7，M1 也封顶在 82 左右。要突破必须先解决日志可得性。
