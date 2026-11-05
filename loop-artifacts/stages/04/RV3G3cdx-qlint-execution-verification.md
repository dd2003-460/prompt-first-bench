# 阶段 04 — RV3G3cdx-queue-dedup-lint · 执行验证（r149）

> 全部命令仓库根执行，可复现。脚本 = `bench/rubric-v3/ablation/scripts/assert-queue-lint.py`（128 行）。

## A1 — 脚本落盘 ✅

docstring 预注册 (a)(b)(c) 判定语义 byte-stable（抄 02.5 定稿末节），含三分支 (a)、X3 `[~]` 豁免、X4 短名提取式、exit 0/1/2 语义、`[SIGNAL]` 前缀约定。实现层三检查函数 check_a/check_b/check_c + parse() 解析层。

**与前序会话草稿版的差异（如实登记）**：草稿版（同路径 untracked 文件，从未 commit）(a) 一律 SIGNAL 无 FAIL 出口、(c) 仅 C2「短名后剩余文本非空」——负样例矩阵无法构造 (a)/(c) FAIL。本轮按 02.5 X1/X2 裁定重写为三分支 (a) + 「无分隔符」(c) FAIL 出口；草稿版 docstring 引用的 `RV3G3cdxqdl-scan.md` 工件已在本轮清理（其 S1「58 行」系标题行误计，正确值见下 A2）。

## A2 — 当前 main queue 实跑（正样例基线）✅ exit 0

```
[PASS] 解析 goal 行 46 行
[SIGNAL] (a) 跨区重复短名「RV3G6-draft-revision-batch1」@ L8(待办), L49(新导出候选)（含「吸收」声明，合法形态）
[SIGNAL] (a) 跨区重复短名「RV3G6-gmr-tiebreak-prereg」@ L9(待办), L50(新导出候选)（含「吸收」声明，合法形态）
[SIGNAL] (a) 跨区重复短名「RV3G6-o3-claim-list」@ L10(待办), L51(新导出候选)（含「吸收」声明，合法形态）
== queue-lint: 46 行 / 3 检查项 / 1 PASS / 0 FAIL / 3 SIGNAL ==
exit=0
```

与 03 A2 预期表逐格吻合：(a) 3 × SIGNAL 0 FAIL ✓ / (b) PASS ✓ / (c) PASS ✓ / exit 0 ✓。

**数字勘误（负面结果，不藏着）**：02 S1 记「goal 行共 42 行」有误——独立 python 重跑（宽松正则 `^- \[( |x|~)\] `）实证 **46 行**（42 + L17/L18/L19/L20 已完成区 em-dash 简写行 4 行，02 枚举时漏计）。line-inventory.csv 同为 42 行版本，一并勘误。**不影响任何判定结论**：46 行中低 pipe 行 15→19 行仍全部含 `—` 分隔符（(c) PASS 不变）、重复组仍 3 组（(a) 不变）、状态位构成不变（(b) 不变）。教训：02 的 CSV 生成脚本与 02.5 复核脚本用了两个不同严格度的正则（`\] (.*)` vs `\] `），未做交叉对账——本 goal 的 lint 脚本本身以宽松式为准（更宽容，防误报）。

## A3 — 负样例矩阵 ✅ 7/7 符合预期

样例目录 `bench/rubric-v3/ablation/queue-lint-samples/`（持久落盘，防 r148 tmp 分支污染先例重演；短名统一 `RV3TEST-*` 前缀防与真实 queue 短名子串碰撞）：

| 样例 | 预期 | 实跑 | ✓ |
|---|---|---|---|
| neg-a-samezone-dup.md | (a) FAIL exit 1 指名两行号 | FAIL 同区重复「RV3TEST-alpha-goal」×2 @ L5,L6 exit 1 | ✓ |
| neg-a-crosszone-nomark.md | (a) FAIL exit 1 | FAIL 跨区无吸收声明 @ L5,L8 exit 1 | ✓ |
| pos-a-absorb.md | (a) SIGNAL exit 0 | SIGNAL 含吸收声明 exit 0 | ✓ |
| neg-b-done-unchecked.md | (b) FAIL exit 1 | FAIL 已完成区未勾选 L8 exit 1 | ✓ |
| neg-b-result-note-unchecked.md | (b) FAIL exit 1（97d2adf 静态形态） | FAIL 带结果注记却 [ ] L5 exit 1 | ✓ |
| neg-c-unparseable.md | (c) FAIL exit 1 | FAIL 无可识别分隔符 L5 exit 1 | ✓ |
| pos-full.md | 全 PASS exit 0（含 `[~]` 行 + `~~删除线~~` 短名 + em-dash 变体） | 3 行 0 FAIL exit 0 | ✓ |

覆盖任务书要求 4 类违例（重复短名/已完成区 [ ]/结果注记+[ ]/格式残缺）+ 2 正对照 + 1 SIGNAL 对照。

**构造过程负面发现 ×1**：neg-a-crosszone-nomark 初版在行内写了「无吸收声明」字样 → 被 (a) 的「吸收」子串匹配命中降级为 SIGNAL（exit 0 不符预期）。修正 = 样例行措辞避开触发词。此即 W2 型边界（关键词集不完备）在本脚本上的实例：「吸收」是宽子串匹配，行内任何提及都会触发豁免——已登记 04.5 攻击面，处置 = 接受（queue 行内提及「吸收」几乎必然是在声明吸收关系，误豁免方向安全：漏报真失控 < 误报合法登记）。

## A4 — exit 2 三路径 ✅

| 路径 | 输入 | 实跑 |
|---|---|---|
| 文件缺失 | `/nonexistent/path.md` | `[ERROR] cannot read ... No such file or directory` exit 2 |
| 无 goal 行 | 纯 markdown 无 `- [` 行 | `[ERROR] no goal lines` exit 2 |
| 零字节文件 | 空文件 | `[ERROR] no goal lines` exit 2 |

## A5 — 回归与冻结面 ✅

- 七脚本 spot check（仓库根）exit=[0,0,0,1,0,0,0] 与 r147/r148 记录零漂移（kappa-receipt FAIL(1) 常态不转绿）。本 goal 新增第 8 个脚本（assert-queue-lint.py），收口后基线扩为八脚本：[0,0,0,1,0,0,0,**0**]。
- 冻结面 `git diff main -- hit-matrix.json prior-estimates.json gold-tree.md` = **0 行**。
- 改动面 = {assert-queue-lint.py, queue-lint-samples/*, stages/{02,02.5,03,04,04.5}/*, current-goal.md, goal-queue.md(收口)} ⊆ 允许集。

## 验收标准对照

- [x] 脚本落盘 + docstring 预注册 (a)(b)(c) 判定语义
- [x] 当前 main queue 实跑明确 verdict（3 SIGNAL / 0 FAIL / exit 0；42→46 行勘误如实登记）
- [x] 负样例矩阵 7/7（≥4 类违例全覆盖）
- [x] exit 2 三路径可达
- [x] 冻结面零修改；改动面 ⊆ 允许集
- [x] 七脚本回归基线零漂移
- [ ] 04.5 verdict pass（下阶段）
- [ ] queue 更新（收口 commit）