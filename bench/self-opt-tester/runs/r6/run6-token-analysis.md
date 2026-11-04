# R6 · Token 消耗分析（阶段门控加载 vs run2 全量注入）

> 任务书：`tasks/TASK-r6-arena-token-optimization.md`（origin/main `7502348`）
> run 协议：9 步链路（与 run2/run5 同协议，新题面防复读）
> 计量工具：o200k_base（js-tiktoken，离线 ranks）→ `count-rule-tokens.js`（可复跑）
> 账本：`token-ledger-run6.json` ｜ 打分：`run6-m1-score.json`
> 生成：2026-11-04（Asia/Shanghai）

---

## 0. 一句话结论

**单 turn 规则负载 12,086 → 3,913 o200k（阶段包均值，−67.6%；9 turn 加权 3,047 / −74.8%），M1 = 78.1 ≥ 70（达标）。但换成「单会话走完 6 阶段」的实际口径，均值只降 42.9%、末态只降 8.7%，M1 = 61.9（不达标）。三个数字都成立，差别全在「规则读进上下文后会不会被卸载」。**

附带一个会改结论的发现：**v1.0 路由表漏掉了 7 个 `examples/*.md`（合计 4,211 tok），"降 74%"里有一部分是把它悄悄切掉了**。补上后才是 67.6%，且 INDEX 自身从 458 涨到 482 tok（见 §3）。

---

## 1. 基线（run2）

| 项 | 值 | 出处 |
|---|---|---|
| 每 turn 规则负载 | **12,086 o200k / 39,858 B** | `r5/packet-audit-r4-v1.md` C6：`TOTAL 39858B o200k=12086` |
| 构成（本轮实测拆分） | SOP 6,426 + 6 个阶段文件 5,243 + run2 任务书 417 | `count-rule-tokens.js` |
| 机制 | 全量内联进任务书 → **每轮重发** | `run2-arena/04.5-review.md` L27 |
| M1 | 量化 14.3 / 人工 25（S=0.0, R=0.0, G=0.57） | 任务书 §背景 |

✓ 拆分校验：6,426 + 5,243 + 417 = **12,086**，与 run2 实测逐 token 相等 —— 说明本轮口径与 run2 同源，不是另起一套。

注：基线**未**包含 `examples/`（run2 内联的是 SOP + 7 个规则文件正文）。本 run 的 v1.1 路由把示例列为 tier-3，实际会读——这个不对称在 §4.5 单独处理。

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
| **`INDEX.md`（新增）** | **482**（1,678 B） | 示例合计 | **4,211** |
| 7 个核心文件合计 | 6,342 | | |

阶段包 = INDEX + 00 + 本阶段 + 下一阶段 + (ex00 + ex本阶段)：

| 阶段 | 必需（核心） | 示例 | 含 INDEX | 对 12,086 |
|---|---|---|---|---|
| 01 | 4,091 | 870 | **5,443** | −55.0% |
| 02 | 2,807 | 738 | **4,027** | −66.7% |
| 02.5 | 2,135 | 832 | **3,449** | −71.5% |
| 03 | 2,317 | 1,093 | **3,892** | −67.8% |
| 04 | 2,314 | 888 | **3,684** | −69.5% |
| 04.5 | 1,661 | 840 | **2,983** | −75.3% |

**均值 3,913**（中位 3,888，范围 2,983–5,443），均值降幅 **−67.6%**。

任务书估的是「~3,700 / −69%」，实测高 5.8%：任务书按「INDEX + 本阶段文件」估，漏算了每个阶段都要带 `00-common-review.md` 与示例。差 6% 不影响结论，但数字以实测为准。

---

## 3. 关键发现：路由表 v1.0 漏了 examples 层

检测器 `check-route-coverage.py`（本轮新写，见 §8）对 v1.0 路由表首跑：

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
- 后果：只按 v1.0 读，agent 会**静默不读示例**。规则负载当然更低，但那是**靠少读东西换来的**，不是靠切分换来的。
- 修正：INDEX 升 v1.1，加第三列「示例（按需，tier-3）」，并把说明段砍到只剩路由表 + 纪律 + 3 条豁免，把 INDEX 从初稿 707 tok 压回 **482 tok**。复跑 `X-miss = 0, exit 0`。

**这条是本轮最重要的结论**：门控动作本身会制造漏载；而漏载只能靠机检发现——7 个文件互相指引的引用关系，人肉 review 不现实。

---

## 4. 逐 turn 账本（9 步）

| turn | 步骤 | 新加载 | Model A（阶段包口径） | Model B（单会话累计） |
|---|---|---|---|---|
| 1 | fetch + ls-remote | INDEX | 482 | 482 |
| 2 | 读 INDEX + 实测 | — | 482 | 482 |
| 3 | 01 目标分解 | 00,01,02 + ex00,ex01 | 5,443 | 5,443 |
| 4 | 02 信息调研 | 02.5 + ex02 | 4,027 | 6,442 |
| 5 | 02.5 交叉核验 | 03 + ex02.5 | 3,449 | 7,629 |
| 6 | 03 行动分解 | 04 + ex03 | 3,892 | 9,165 |
| 7 | 04 执行+验证 | 04.5 + ex04 | 3,684 | 10,405 |
| 8 | 04.5 复核 | ex04.5 | 2,983 | 11,035 |
| 9 | 汇总 | — | 2,983 | 11,035 |
| | **均值** | | **3,047（−74.8%）** | **6,902（−42.9%）** |

两个口径的定义差异：

- **Model A**：harness 每 turn 只注入当前阶段包（任务书按阶段重写/重置）。
- **Model B**：arena agent mode 的实际行为——单会话，读进上下文的规则**不会被卸载**，每轮重发的是累积上下文。
- 末态：Model B 收敛到 11,035，对基线 12,086 **只省 8.7%**。因为 9 步走完了全部 6 个阶段，最终必然触达全部文件。

### 4.5 第三个口径：对称比较（去掉 examples 差异）

基线 run2 根本没读 examples，本 run 读了 4,211 tok。降幅里混进了「多读的东西」，不好直接比。补一个对称口径 **Model B′**——单会话累积，但 run6 也只读 7 个核心文件：

| | 均值 | 末态 | 对 12,086 |
|---|---|---|---|
| Model B′ | 4,769 | 6,824 | 均值 −60.5%，末态 **−43.5%** |

- 末态 6,824 = INDEX 482 + 7 核心 6,342。对基线 12,086 的 5,262 差值**全部来自 SOP 6,426 换成 INDEX 482**。
- 也就是说：**P0 的真实收益 ≈ 「SOP 不再重发」**，约 −44%（单会话末端）/ −61%（单会话均值）。阶段切分本身在单会话里几乎不产生额外收益，因为读过的规则不会被卸载。
- 这个口径 M1 = 72.5（略过线），但前提是「示例从不被读」——那正是 v1.1 要修的病。所以**不拿它当结论，只拿它解释降幅构成**。

---

## 5. M1 量化

公式：`M1 = 100 × (0.4·S + 0.35·R + 0.25·G)`

| 分量 | 定义（本轮口径） | Model A | Model B′ | Model B |
|---|---|---|---|---|
| S | 有 per-request 日志且可切分到 run 窗口 → 1.0 | 0.6 | 0.6 | 0.6 |
| R | x = 每 turn 规则负载均值 / 12,086；`R = clamp((1−x)/0.9, 0, 1)` | x=0.252 → **0.831** | x=0.395 → **0.673** | x=0.571 → **0.477** |
| G | g = 末 turn / 首个完整阶段包 turn；`G = clamp((5−g)/3.5, 0, 1)` | g=0.55 → **1.000** | g=1.49 → **1.000** | g=2.03 → **0.849** |
| **M1** | | **78.1** | **72.5** | **61.9** |

S=0.6 的依据：本轮有 9/9 行逐 turn 账本、token 数可第三方用同脚本复算，但**是执行侧自产、非服务端日志**，且「turn→文件」映射来自任务书设计而非抓包。run2 是 0.0（完全无账本），本轮不应拿满分。

敏感性（S 取 0.5/0.6/0.7/1.0）：

| 口径 | S=0.5 | S=0.6 | S=0.7 | S=1.0 |
|---|---|---|---|---|
| Model A | 74.1 | 78.1 | 82.1 | 94.1 |
| Model B′ | 68.5 | 72.5 | 76.5 | 88.5 |
| Model B | 57.9 | 61.9 | 65.9 | 77.9 |

**M1 的达标与否几乎完全由「harness 是否按阶段重写任务书」和「是否必须读示例」决定**，S 只在 ±4 分内摆动。

---

## 6. 验收判定

| 口径 | 假设 | M1 | vs run2 人工 25 | 判定（≥70） |
|---|---|---|---|---|
| **Model A**（阶段包） | harness 每 turn 只注入当前阶段包 | **78.1** | +53.1 | **PASS** |
| **Model B′**（对称） | 单会话累积，且不读 examples | 72.5 | +47.5 | PASS（前提与 v1.1 冲突） |
| **Model B**（实际） | 单会话累积 + 读了 examples | **61.9** | +36.9 | **FAIL** |

**取哪个当结论**：任务书写「降低单 turn 规则负载从 12,086 → ~3,700」，这个量属 Model A 口径；同口径对比只有 Model A 可比。但 Model B 是**更保守、更接近 arena 实际**的数，不能藏。

→ 判 **CONDITIONAL-PASS**：按任务书定义达标（78.1）；按本轮实际加载行为不达标（61.9），缺口 8.1 分。拆解：
- **~6 分来自 examples（4,211 tok）**：v1.1 为保证不静默漏读而主动加的，属质量取舍不是浪费；
- **~2 分来自单会话不卸载**：harness 行为，需 P1 规则压缩或阶段重置。

**不凑数声明**：所有数字由 `count-rule-tokens.js` 实测，无调参凑 70。三个口径全部并列，不择优藏数。

---

## 7. 交付物清单

| 路径 | 内容 |
|---|---|
| `loop/prompt-first/INDEX.md` | 路由表 v1.1（1,678 B / 482 tok），含 examples 第三列 + 跨阶段豁免 |
| `sop/arena-loop-pipeline.md` §2 | 强制段从「全量注入」改为「阶段门控」+ 注入量对照 |
| `tasks/_TEMPLATE-arena-task-brief.md` | 新任务书模板（阶段包占位符 + 校验命令） |
| `bench/self-opt-tester/runs/r6/count-rule-tokens.js` | 规则负载计量器（o200k，缺依赖时降级字节估算并告警） |
| `bench/self-opt-tester/runs/r6/check-route-coverage.py` | 漏载检测器（R/X/A/G 四类断言，exit code 可挂 CI） |
| `bench/self-opt-tester/runs/r6/token-ledger-run6.json` | 9 turn 账本 + 三口径聚合 + caveats |
| `bench/self-opt-tester/runs/r6/run6-m1-score.json` | M1 打分（三口径 + 敏感性表 + 置信度） |
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

依赖：`js-tiktoken`（`npm i js-tiktoken`，离线可用）。缺失时计量器降级为 `bytes/3.32` 并在输出里打 `WARN`，不会静默改口径。

---

## 9. 遗留与建议

1. **P1 需要上**：单会话实际口径 61.9，缺口 8.1 分。压缩方向：`01-goal-decomposition.md`(1,755) 与 `02-information-research.md`(1,237) 是核心文件里最大的两个；示例层 4,211 也可再瘦。
2. **harness 行为待确认**：若 arena 支持「每阶段重写任务书 / 阶段间重置上下文」，Model A 成立，P0 已达标。这是本轮唯一的关键未知，建议下一轮用一次 2 阶段小 run 验证（成本约 10 turn）。
3. **检测器应进 CI**：`check-route-coverage.py` 已可 exit code 门禁。以后任何 INDEX/规则改动都该先过它，否则漏载会静默发生（本轮就是这么发现的）。
4. **S 分量的天花板**：只要拿不到服务端 per-request 日志，S 封顶在 0.6–0.7，M1 也封顶在 82 左右。要突破必须先解决日志可得性。
