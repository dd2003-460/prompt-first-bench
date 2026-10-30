# 02 — RV3G3-threshold-crossdomain-reverify 核销轮 · 事实链核验

> goal: queue 队列卫生修复 + 核销验证 · 分支 ralph/rv3g3-threshold-crossdomain-reverify-close · 2026-10-30
> 定位：核销轮的 02 = 交付物完整性与 git 证据链核验（非信息研究）。全部结论带 commit/文件锚点。

## F1 — 交付物存在性（r140/f8c096b，经 96a89e7 合入 main）

`git show f8c096b --stat`：**3 files changed, 418 insertions(+)，0 deletions**——

| 文件 | 角色 | 状态 |
|------|------|------|
| `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（283 行） | 核心交付物：schema 预注册骨架 + DP tie 可达枚举器 | ✅ 存在于 main，本轮实跑通过（见 04） |
| `loop-artifacts/stages/04/RV3G3cd-execution-log.md`（63 行） | 阶段 04 执行日志（A3 18/18 + M0 50/50 + M1-M4） | ✅ 存在于 main |
| `loop-artifacts/stages/04.5/RV3G3cd-review.md`（72 行） | 阶段 04.5 八攻击复核（verdict pass） | ✅ 存在于 main |

**docstring 完整性抽查**（脚本 L1-L60 通读）：输入 schema 三文件（hit-matrix-batch2 / prior-estimates-batch2 / judge-blindtest-batch2）字段级预注册 ✅；方案权重合成协议「与第一域权威实现逐字同协议，assert-goldrank-threshold.py L90-99」✅；判定语义 D1-D5 段（S1 锚点集合 {W3-orig, W4-orig, W3-new} / (a) 三分支 / (b) DP 席位预算法 / exit code 0/1/2 语义）✅ byte-stable 于 docstring。**失败降级触发条件（脚本不存在 / docstring 缺 D1-D5 段）均不成立。**

## F2 — queue 漏翻 checkbox 的 git 证据链

1. **r138+（446f4cc）**：RV3G3-goldrank-threshold-proof 收口时导出本候选，初始形态 `- [ ] RV3G3-threshold-crossdomain-reverify | batch2 第二域数据到来后重验…`（queue L22，纯描述无结果注记）。
2. **r140 工作 commit（f8c096b）**：全部交付物落盘（F1），commit message 含「A3 回归锚点 18/18 + M0 fuzz 50/50 + M1-M4 变异全过 + 冻结面零修改 + 04.5 verdict pass」。
3. **r140 收口 commit（97d2adf）**：message = 「queue 划掉 + 结果注记 + 新导出闭环候选 RV3G3-batch2-arrival-closure」。实际 diff（`git show 97d2adf -- tasks/goal-queue.md`）= **2 insertions / 1 deletion**：
   - 插入 L23 新候选 `RV3G3-batch2-arrival-closure`（完整条目）；
   - 原 crossdomain 行 → 追加完整 **结果** 注记（A3/M0/M1-M4/SIGNAL 常态/冻结面/04.5/范围切割 N3 全量写入）；
   - **但行首 checkbox 仍为 `[ ]`**——`git show 97d2adf:tasks/goal-queue.md` L23 实证 `- [ ] RV3G3-threshold-crossdomain-reverify (2026-10-30, r140: f8c096b, …)`。
4. **当前 main（c0eba3b）**：L28 仍 `- [ ]`（r141-r144 各轮未触碰该行）。

**定性**：97d2adf 完成了收口的两个实质动作（结果注记 + 新候选导出）唯独漏了 checkbox 翻转，且 message 声称「划掉」与实际不符——属收口执行遗漏，非交付物缺失。与 r137 docsync 先例（r133 交付未收口）性质相同、程度更轻（连收口 commit 都有，只差一个字符位）。

## F3 — 外部阻塞状态未变（核销不改变 blocked-on-external 属性）

- `bench/rubric-v3/ablation/batch2/` **不存在**（ls 实证）→ 脚本常态分支 = SIGNAL blocked-on-external exit 0（docstring L7 预注册语义）。
- 核销对象是「assert 骨架这一交付物已完成并合入」，不是「跨域重验已执行」——后者仍是 RV3G3-batch2-arrival-closure（queue L27，blocked-on-external）的职责。两候选正交，翻转本条 checkbox 不影响 batch2 候选的状态。

## F4 — 冻结面基线（02 快照，04 复验）

`git diff main --stat`（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-run1..8.md 十件）= **0 行**。工作树在写 current-goal 前 clean。

## 负面结果声明

无——F1-F4 全部按预期核验通过，未发现交付物缺失或基线漂移。唯一异常即 F2 的 checkbox 漏翻本身（已被本 goal 定义为修复对象）。