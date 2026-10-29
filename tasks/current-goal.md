# Goal: RV3G6-draft-revision-batch1 — rubric-v3 DRAFT 修订第一批

> 创建：2026-10-30 · ralph loop runner（queue 队首）
> 依据：`bench/rubric-v3/AUDIT-report.md` §9.1/§9.3（修订清单 R-01~R-15，第一批 = R-01~R-03 + R-06 + R-10，开跑前置条件）

## 【目标】
把 AUDIT-report §9.1 修订清单的第一批落地为**新版 DRAFT 文件**（`DRAFT-rubric-v3-v2.md`）+ **修订 diff 记录**（`revision-log-batch1.md`）+ **机判断言脚本**（C4 w2 公式断言 / C3 W3W4 复算断言）。具体五项：

1. **R-01 O1 拆账 + 计分统一**（B1/B7/#20/#21）：O1 只计「覆盖行为」（低先验候选是否纳入 + 三项检查各有可定位证据），不判语义正确性；每项二值 0/1、每候选满分 3、删 tier/w 概念；计入深度分的低先验候选 ≤3（预注册写死）；补四条机械防刷分判据（≥3 档含中间档 / 相邻档可测序数差 / 候选集 Jaccard<0.9 / 维度定义带时间戳先于搜索）；每候选 ≥1 URL + ≥1 数值 + ≥1 约束判断，缺一该候选深度分 0。
2. **R-02 全维尺度统一**（B6/#26）：每维拆 3-6 个 yes/no 条目，维度分 = 条目通过率（0-1 连续），κ 在条目层（二值）计算；权重与总分公式预注册写死，删「满分另定」。
3. **R-03 §4 题面去方向暗示 + V1-align 对照组 + Pr2/Pr3 判据替换**（B3/B11）：去掉「发布 ≥5 年旧选项」具体锚点 → 抽象「非默认可行区间（由任务画像定义）」；三问改域无关占位（由被测者实例化）；加 V1-align 对照组（只加结构规则不含价值判断）隔离「结构 vs 暗示」；Pr3 判据换外部真值（低先验候选在实测口径下确实优于 baseline 首选，「进入模型自己写的前 3」不算）；Pr2 降为 manipulation check 不作能力证据。
4. **R-06 §1-O3 加「宣称前置条件」硬条款**（B2 声明路径）：AUDIT-report §6 S2 限定语原文写入正式版 §1-O3「宣称前置条件」小节。
5. **R-10 变体矩阵冻结**（B10/#27）：冻结 V0/V1/V2/V3(+V-sham) 差异定义——所有变体共用同一题面；V2 = V1 精确删除 §4 段落（冻结 diff + 行号 + commit）；V3 = 边界类型声明段落等长中性 sham 替换；每处差异单独标注（删/替段落原文引用 + 行号 + 冻结 commit hash），无 diff 记录的变体不得开跑。

外加两条机判断言（G5 导出，消除 p̃ 层纸面协议零防护力）：
6. **C4 w2 断言**：assert 脚本校验 prior-estimates.json / judge-blindtest-r1.json 中每个节点的 w2 = 1 + min(−log₂ p̃, log₂(1/ε))（p̃=null → 1.0 根节点政策），逐节点复算比对。
7. **C3 W3W4 复算断言**：assert 脚本从 hit-matrix.json + prior-estimates.json 独立复算 W0-W4 全部 8 run 分数，与 stats-w3w4.json 落盘值比对（容差 5e-5，吸收 4 位小数舍入）。

## 【阶段】
rubric-v3 审计链的**修订落地环**。消费 AUDIT-report §2/§6/§7/§9 的处置结论，产出可开跑的新版 DRAFT + 冻结件 + 机判脚本。本 goal 不改任何冻结数据（hit-matrix/prior-estimates/gold-tree/stats-* 只读），不实施第二批修订（R-04/R-05/R-07~R-09/R-11~R-15 留 batch2）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00..04.5`（六阶段定义）
- `bench/rubric-v3/AUDIT-report.md`（上游定稿建议，§2 维度表 / §6 限定语 / §7 处置表 / §9 修订清单）
- `bench/rubric-v3/DRAFT-rubric-v3.md`（待修订对象，r59 原版）
- `bench/rubric-v3/ablation/{prior-estimates,judge-blindtest-r1,hit-matrix,stats-w3w4}.json`（断言脚本输入，冻结只读）
- `bench/rubric-v3/ablation/scripts/assert-g1-audit.py`（assert 脚本模式参考）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3B1-`
2. 新版 DRAFT 文件落盘（`DRAFT-rubric-v3-v2.md`），五项修订全部可见（grep 可查关键标记：O1 二值条目 / 条目通过率 / 宣称前置条件 / 非默认可行区间 / V1-align / 变体冻结表）
3. 修订 diff 记录落盘（`revision-log-batch1.md`）：每条修订 = AUDIT-report 出处（§x + finding 编号）→ 改动位置 → 改动前后对照
4. R-06 限定语与 AUDIT-report §6 原文逐字一致（diff 可验证）
5. R-10 变体冻结表含：每变体「删/替段落原文引用 + 行号 + 冻结 commit hash」；V-sham 段落给出等长中性替换文本
6. 两个 assert 脚本落盘 `ablation/scripts/` 且运行 exit 0（C4：双 judge 60/60 节点 w2 复算通过；C3：W0-W4 × 8 run = 40 分数复算通过）
7. 冻结数据零修改（git status 可查：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / stats-*.json 不在变更列表）
8. commit + push 分支 `ralph/rv3g6-batch1` + ls-remote 验证 + merge main + queue 划掉本 goal + 追加 ≥1 新候选

## 【失败降级】
- 新版 DRAFT 与 AUDIT-report 某条处置冲突无法调和 → 以 AUDIT-report 为准（它是上游定稿建议），冲突点在 revision-log 登记并标「需人工裁决」
- assert 脚本发现冻结数据不自洽（FAIL）→ 这是**有效负面结果**，如实报告 FAIL 详情，不修冻结数据，登记 APPROVALS 后继续收口其余项
- 04.5 verdict=fail → 回 04 修复后重审，不跳过
- merge 冲突 → 停手登记 APPROVALS，不 force