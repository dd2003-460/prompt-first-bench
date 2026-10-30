# 阶段 04 — 执行验证（RV3G3cdx-queue-dedup-lint, r149）

> 执行顺序 A1→A5。所有实跑输出可复现（命令见各节）。

## A1 脚本落盘 ✓

`bench/rubric-v3/ablation/scripts/assert-queue-lint.py`（126 行）落盘。docstring 预注册判定语义与 02.5「判定语义定稿」节逐条对应：(a) 三分支（同区 FAIL / 跨区无吸收 FAIL / 跨区带吸收 SIGNAL）/ (b) B1+B2（`[~]` 豁免）/ (c) C1+C2 最小规则（无 pipe 下限，X2 裁定）/ X4 短名提取式（剥 `~~` + 截断括号）。exit 0/1/2 三分支 + `[SIGNAL]` stdout 前缀约定（r141）。

**过程注记（如实登记）**：本 goal 存在前序会话草稿版脚本（(a) 一律 SIGNAL + C2-only），其 (a) 无 FAIL 出口、(c) 无分隔符 FAIL 出口——负样例矩阵无法构造。本轮按 02.5 X1/X2 裁定重写为三分支版本，docstring 内保留取代声明（防双版本漂移误读）。

## A2 正样例实跑（当前 main queue）✓

```
[PASS] 解析 goal 行 46 行
[SIGNAL] (a) 跨区重复短名「RV3G6-draft-revision-batch1」@ L8(待办), L49(新导出候选)（含「吸收」声明，合法形态）
[SIGNAL] (a) 跨区重复短名「RV3G6-gmr-tiebreak-prereg」@ L9(待办), L50(新导出候选)（含「吸收」声明，合法形态）
[SIGNAL] (a) 跨区重复短名「RV3G6-o3-claim-list」@ L10(待办), L51(新导出候选)（含「吸收」声明，合法形态）
== queue-lint: 46 行 / 3 检查项 / 1 PASS / 0 FAIL / 3 SIGNAL ==
exit=0
```

与 03 A2 预期表逐格吻合（3 SIGNAL / 0 FAIL / exit 0）。**(b)(c) 零违例 = 当前 queue 静态结构健康**；3 条 SIGNAL 均为已知吸收登记行（L49/L50/L51），人工确认成本 ≈ 0。

## A3 负样例矩阵 ✓（7/7 符合预期）

样例落盘 `bench/rubric-v3/ablation/queue-lint-samples/`（随 commit 持久化——r148 N1/N2 tmp 分支污染教训，构造性样例显式标注不落 main 数据面）：

| 样例 | 触发 | 实跑 | 预期 | 判定 |
|---|---|---|---|---|
| neg-a-samezone-dup.md | (a) 同区 ×2 | FAIL 指名 L5+L6，exit 1 | FAIL exit 1 | ✓ |
| neg-a-crosszone-nomark.md | (a) 跨区无吸收 | FAIL 指名 L5+L8，exit 1 | FAIL exit 1 | ✓ |
| pos-a-absorb.md | (a) 跨区带吸收 | SIGNAL，exit 0 | SIGNAL exit 0 | ✓ |
| neg-b-done-unchecked.md | (b)B1 已完成区 [ ] | FAIL 指名 L8，exit 1 | FAIL exit 1 | ✓ |
| neg-b-result-note-unchecked.md | (b)B2 结果注记+[ ] | FAIL 指名 L5（97d2adf 形态），exit 1 | FAIL exit 1 | ✓ |
| neg-c-unparseable.md | (c)C2 无分隔符 | FAIL 指名 L5，exit 1 | FAIL exit 1 | ✓ |
| pos-full.md | 全合规三区 | 0 FAIL 0 SIGNAL，exit 0 | 全 PASS exit 0 | ✓ |

覆盖任务书要求 4 类违例（重复短名×2 形态 / 已完成区 [ ] / 结果注记+[ ] / 格式残缺）+ 2 正对照 + 1 SIGNAL 对照。

## A4 exit 2 双路径实证 ✓

- 路径 1（文件缺失）：`python3 assert-queue-lint.py /tmp/nonexistent-qlint.md` → `[ERROR] cannot read ... No such file or directory`，**exit 2** ✓
- 路径 2（零 checkbox 行）：空文件 → `[ERROR] no goal lines ... found`，**exit 2** ✓

## A5 回归基线 + 冻结面 ✓

**七脚本基线（仓库根执行，关键：脚本用相对路径定位数据，必须从 repo root 跑）**：

| 时点 | exit 序列 |
|---|---|
| r147 收口记录（0bb55ce） | [0,0,0,1,0,0,0] |
| 0bb55ce 全树 git archive 到 /tmp 实跑 | [0,0,0,1,0,0,0] |
| 当前分支仓库根实跑 | **[0,0,0,1,0,0,0] 零漂移** |

（kappa-receipt 常态 FAIL exit 1 = 已知项，闭环挂 RV3G4-kappa-gate-execution 外部阻塞。）

**cwd 陷阱登记**：首轮 spot check 在 `scripts/` 目录下执行得 [0,1,1,1,0,1,0]——系脚本相对路径（`../hit-matrix.json` 等）在错误 cwd 下解析失败所致，非代码漂移；换回 repo root 后与基线逐位一致。此陷阱对既有七脚本同样存在（r147 前从未在 scripts/ 目录内跑过），建议未来回归统一固定 cwd=repo root。

**冻结面**：`git diff main --stat -- hit-matrix.json prior-estimates.json gold-tree.md runs-C0-*` = **0 行** ✓

**改动面** ⊆ {assert-queue-lint.py, queue-lint-samples/×7, stages/{02,02.5,03,04,04.5}, current-goal.md}（queue 数据行本轮零修改）✓

## 负面结果声明

1. 02 S1 初稿「合计 58 行」为误计（grep 输出行号最大值 58 被误读为计数）——真实值 46 行（CSV 42 行为 02 首版枚举，含 4 行后续修正补入；最终权威值 = 脚本实跑 46 行，三区分布 6/5/35）。已在 02 工件勘误注记。
2. 02.5 X2 复核发现 02 S5 低 pipe 行枚举不完整（只举已完成区 4 例，漏候选区 11 例）——已修正并据此推翻「按区分派 pipe 下限」候选规则。
3. 前序草稿版脚本判定面不足（(a) 无 FAIL 出口）——已被本轮重写取代，非静默覆盖（docstring 留取代声明）。

## 判定

A1-A5 全部达标，验收标准 7/7（04.5 前）。**pass → 进 04.5**。