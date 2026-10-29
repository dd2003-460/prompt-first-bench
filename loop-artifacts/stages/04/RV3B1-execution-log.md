# 阶段 04：执行日志 — RV3G6-draft-revision-batch1

> goal: rubric-v3 DRAFT 修订第一批 · 分支 ralph/rv3g6-batch1 · 2026-10-30
> 上游：stages/03 A-DAG（A1-A12）+ 四条预注册裁定规则

## A-DAG 执行表

| # | 行动 | 状态 | 产出 / 证据 |
|---|------|------|-------------|
| A1 | R-01 O1 重写 | ✅ | `DRAFT-rubric-v3-v2.md` §1-O1（L23-45）：覆盖行为 only + 每候选 3 条 yes/no（E1/E2/E3）+ ≤3 封顶 + 四条防刷分门禁（Jaccard 双口径标「需人工裁决」）。验证：grep「条目通过率」命中；O1 节内无 tier/w 计分残留 |
| A2 | R-02 横切尺度统一 | ✅ | v2 §0 原则 4 改写（L16）+ 新增原则 5（L17）；Outcome 总分 = 0.4×O3+0.25×O1+0.2×O2+0.15×O4（L98）；Process 总分 = 四等分（L167）。验证：grep「满分另定」仅 2 处，均为**删除声明句**（L17/L96），无操作性残留 |
| A3 | O2/O4/P1-P4 条目框架化 | ✅ | 各维 3-4 条 yes/no 直译过渡 + `[batch2: R-xx]` 占位（全文 6 处：R-12/R-14/R-08×2/R-09×2——P1 与 P3 共用 R-08，P4 用 R-09）。NA 档机制写入 P1/P3（通道不可用 ≠ 0 分） |
| A4 | R-06 宣称前置条件 | ✅ | v2 §1-O3 L75-77 新增小节。**逐字一致性已 diff 验证**：AUDIT-report.md L186（§6 引用块唯一正文行）与 v2 L77 **字节级相等**（python 比对 `a == b → True`，len=413）。附带状态声明（w2 experimental / 主公式 W1 / gmr 主判据 / 阈值不写死）在 L73 |
| A5 | R-03 §4 去方向暗示 | ✅ | v2 §4（L211-275）：锚点/价值断言/指向性三问全部删除；冻结块（D1 L219-236、sham L258-269）内 grep「≥5 年/保值性/性价比可能更高/老马区/kernel 支持到哪一代/二手价」= **0 命中**。Pr2 降级 manipulation check（L274）、Pr3 换外部真值判据（L275）。注：「≥5 年」在 v2 中仅存于 §4 设计变更声明（L217，描述 v1 病灶的元文本，非题面指令）——该保留是有意为之（审计可追溯性），不计为残留 |
| A6 | V1-align 对照组 | ✅ | v2 §4.2（L245-252）：与 4.1 逐处差异 3 条列明（删数量义务句 / 分区纯占位去「默认先验」字样 / 三问适用全部候选）；三层归因逻辑在 §3.2 L199 |
| A7 | R-10 变体矩阵冻结 | ✅ | v2 §3.2（L177-199）：V0/V1/V1-align/V2/V3/V-sham 六变体表 + 冻结 diff 登记表（D1=L219-L236 含围栏 / D2=L154-L161 含围栏 / sham 替换源=L258-L269，行号 sed 逐行核验过）+ 「无 diff 记录的变体不得开跑」门禁。V0 必须同批次重跑（L179）。commit hash 单元格处理见下方裁定 |
| A8 | C4 w2 断言脚本 | ✅ | `ablation/scripts/assert-w2-formula.py` **实际运行 exit 0**：`[orig-judge] PASS: 31/31 (tol=5e-05)` + `[new-judge] PASS: 31/31 (tol=0.0005)` + `SIGNAL: 双 judge 合计 0 mismatch`（M3 分侧容差落地） |
| A9 | C3 W3W4 复算断言脚本 | ✅ | `ablation/scripts/assert-w3w4-recompute.py` **实际运行 exit 0**：W0-W4 各 `PASS: 8/8 run 分数复算一致 (tol=5e-05)` + `SIGNAL: W0-W4 × 8 run 合计 0 mismatch` |
| A10 | revision-log-batch1.md | ✅ | `bench/rubric-v3/revision-log-batch1.md`：包含/不包含双清单 + 七项工作逐条前后对照 + M5「需人工裁决」登记 + 诚实保留 6 条 |
| A11 | 文头状态 + 通读校对 | ✅ | 文头 L3-4 标「v2 · batch1 落地 · batch2 未完成不可用于正式实验计分」。grep 检查清单全过（见下表）。typo 修复：O3 消融证据行「W4=w1+w4」→「W4=w1+w2」（本阶段发现并修复，修复后 grep「w1+w4」= 0 命中） |
| A12 | 04 日志 + 04.5 复核 | ✅ | 本文件 + `stages/04.5/RV3B1-review.md` |

### A11 grep 检查清单（实际输出）

| 检查 | 命令 | 结果 |
|------|------|------|
| 「满分另定」无操作性残留 | `grep -n 满分另定` | 2 命中（L17/L96），均为删除声明句 ✅ |
| 冻结块无方向暗示词 | `sed -n '219,236p;154,161p;258,269p' \| grep ...` | 0 命中 ✅ |
| manipulation check 存在 | `grep -c "manipulation check"` | 1 ✅ |
| W4 typo 清零 | `grep -n "w1+w4\|W4=w1+w4"` | 0 命中 ✅ |
| batch2 占位齐全 | `grep -c "batch2: R-"` | 6 ✅ |
| 冻结行号锚点 | `sed -n '154p;161p;219p;220p;235p;236p;258p;269p'` | L154/L161/L219/L236/L258/L269 均为 ``` 围栏，L220=【候选集构造规则】首行 ✅（typo 修复为单行内替换，行号未漂移） |
| R-06 逐字一致 | python 字节比对 AUDIT L186 vs v2 L77 | `True`（413 字符）✅ |

## 预注册裁定规则执行情况（03 定义，逐条核对）

1. **逐字条款**：✅ 通过。diff 零差异（byte-exact，非手工重打）。
2. **越界红线**：✅ 通过。v2 中 batch2 内容仅以 `[batch2: R-xx]` 占位出现（6 处），无任何 R-04~R-15 实质实施。注意边界说明：D2 段落文本（L154-161）是本 goal 新写的 prompt 侧文本——其**作为冻结对象给出**属 R-10 范围（变体矩阵需要具体删除目标），而「写入 loop/prompt-first 并 commit 冻结」的流程动作属 R-09（batch2），本版不做。
3. **冻结数据红线**：✅ 通过。`git status --porcelain` 对 hit-matrix.json / prior-estimates.json / gold-tree.md / stats-*.json / judge-blindtest-r1.json = **空输出**（零修改）。本次改动全集 = 9 个新文件 + tasks/current-goal.md（goal 规格覆写）+ loop-artifacts/prompt-first/02-web-llm-cross-check.md（阶段 02 web-llm 回执更新，非冻结数据）。
4. **断言真实性**：✅ 通过。两脚本均实际运行并记录 exit code（0）与输出计数（62/62 节点、40/40 分数），非「应该通过」。

## 裁定记录（执行中新产生的决定）

**C-01 · 冻结 commit hash 的 chicken-and-egg 处理**：§3.2 冻结表的「冻结 commit」列不能指向包含本表的 commit 本身（hash 在 commit 产生前不存在）。裁定：**该行回填为收口 commit 的完整 hash，且该行所在的文件版本即冻结版本**——即冻结语义 = 「本表所在 commit 的文件快照」，hash 是定位符而非自指。执行方式：收口 commit 产生后，追加一个 fixup commit 回填 hash（fixup 只改这一列，不改任何冻结段落文本；冻结段落的行号与内容以第一个收口 commit 为准，fixup 不移动它们——回填发生在表格行内，位于冻结段落之外）。若 fixup 导致行号漂移风险，则改为在 revision-log 中登记「冻结版本 = <第一收口 commit hash>」，表格列保持「见 revision-log 回填状态」。**最终采用后者**（零行号漂移风险，冻结段落区域完全不动）。

**C-02 · 「≥5 年」元文本保留**：§4 设计变更声明中引用 v1 锚点原文属审计可追溯性需要（说明删了什么），不是题面指令，不计为 A5 验收的残留。此裁定记入 revision-log 诚实保留。

## 诚实保留（负面结果与弱点）

1. **web-llm 三 provider 全失败**（登录过期，与 AUDIT-report 附录 B 一致）——V1-align 切分与 sham 等长设计的**外部第二意见缺失**，只有仓库内自证（unverified）。
2. **Jaccard 双口径是兜底不是裁定**（M5）——待人工裁决，v2 内已标注。
3. **权重数值（0.4/0.25/0.2/0.15 与 process 四等分）是本 goal 的预注册选择**，AUDIT-report 只要求「预注册写死」未给具体值——取值理由写在 v2 对应位置，供人工审。
4. **batch2 占位条目是过渡态**——O2/O4/P1/P3 的二值化直译大概率在 R-08/R-12/R-14 落地时重构；本版保证 pilot 设计期可用，不是终态。
5. **D2 段落文本未经 prompt 侧实测**——它是按 B9 意图新写的冻结对象，实际消融效果要等 V3-noboundary 跑出来才知道（这正是它存在的意义，但当前是纸面设计）。

verdict: **pass** — 12/12 行动完成，四条预注册规则全部机判通过，进入 04.5 反方复核。