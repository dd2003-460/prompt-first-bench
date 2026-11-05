# 阶段 03 — RV3G3cdx-queue-dedup-lint · 动作分解（r149）

> 依据：02 现状扫描 + 02.5 裁定 X1-X4。判定语义定稿见 02.5 末节，byte-stable 落入 docstring。

## A1 — 脚本落盘 `bench/rubric-v3/ablation/scripts/assert-queue-lint.py`

结构参照 assert-closure-checklist.py（r148 模式）：
- docstring：用途 / 用法 `python3 assert-queue-lint.py [path]`（默认 `tasks/goal-queue.md`，参数化供负样例沙盒消费——同 r147 lint-only 参数化先例）/ (a)(b)(c) 判定语义全文（抄 02.5 定稿，含三分支 (a) 与 X3/X4 子句）/ exit code 语义 / `[SIGNAL]` 前缀约定。
- 解析层：逐行正则 `^- \[( |x|~)\] (.*)$`；区归属 = 最近 `## ` 标题；短名提取 = 首空白 token → 剥 `~~` → 截断至首个 `（`/`(`。
- 检查层三函数 check_a/check_b/check_c，各自返回 (status, detail) 列表；汇总打印 PASS/FAIL/[SIGNAL] 逐条 + 末尾计数行。
- exit 2 路径：文件不存在 / 空文件 / 无任何 goal 行。

## A2 — 当前 main queue 实跑（正样例基线）

预期 verdict（由 02/02.5 实证数据直接推出，实跑须逐格吻合）：
- (a)：3 组跨区重复全部含「吸收」声明 ⇒ **3 × SIGNAL**，0 FAIL；
- (b)：**PASS**（已完成区无 `[ ]`；全文件无「结果注记+[ ]」行）；
- (c)：**PASS**（42 行全部可解析——含 L55 剥 `~~` 后短名非空、15 行 em-dash 行含 ` — ` 分隔符）；
- 总 exit **0**（SIGNAL 不拦截）。若实跑与此表任何一格不符 ⇒ 回 02.5 查规则实现偏差，不带病进 A3。

## A3 — 负样例矩阵（构造性，沙盒目录 `bench/rubric-v3/ablation/queue-lint-samples/`，随 commit 落盘防 tmp 分支污染先例重演——r148 N1/N2 教训：构造性样例放独立持久位置并显式标注）

| 样例 | 构造内容 | 预期 |
|---|---|---|
| neg-a-samezone-dup.md | 同区两行同短名（复刻 r105c 父版本形态） | (a) FAIL exit 1，指名两行号 |
| neg-a-crosszone-nomark.md | 跨区两行同短名且均无「吸收」 | (a) FAIL exit 1 |
| pos-a-absorb.md | 跨区两行，候选区行含「被…吸收」（复刻 L49 形态） | (a) SIGNAL exit 0 |
| neg-b-done-unchecked.md | 「已完成」区一行 `[ ]` | (b) FAIL exit 1 |
| neg-b-result-note-unchecked.md | 待办区 `[ ]` 行含 `**结果**：` | (b) FAIL exit 1（97d2adf 静态形态复刻） |
| neg-c-unparseable.md | `- [ ] ` 后仅短名无分隔符 | (c) FAIL exit 1 |
| pos-full.md | 合规小 queue（三区各 1 行标准五段） | 全 PASS exit 0 |

7 样例 ≥ 任务书要求 4 类违例全覆盖（重复短名/已完成区 [ ]/结果注记+[ ]/格式残缺）+ 2 正对照 + 1 SIGNAL 对照。

## A4 — exit 2 双路径实证

- 路径 1：传不存在路径 → exit 2 + `[ERROR]`；
- 路径 2：空文件（或无 `- [` 行的 md）→ exit 2 + `[ERROR]`。

## A5 — 回归与冻结面核验

- 七脚本基线 spot check（仓库根）exit=[0,0,0,1,0,0,0] 零漂移（本 goal 只加新脚本不改既有脚本，理论零风险，仍实跑留痕）；
- `git diff main --stat -- hit-matrix.json prior-estimates.json gold-tree.md runs-C0-*` = 0 行；
- 改动面 ⊆ {assert-queue-lint.py, queue-lint-samples/*, stages/{02,02.5,03,04,04.5}/*, current-goal.md, goal-queue.md(收口)}。

## A6 — 收口

queue L26 `[ ]`→`[x]` + 结果注记 + 新导出候选 ≥1（预登记方向：queue 排版统一候选——em-dash 简写行 vs 五段式统一，02.5 X2 明确划出本 goal 范围外；或 queue-lint 门禁接入候选，与 closure-gate-integration 同源待成璐裁定）。merge main + push。