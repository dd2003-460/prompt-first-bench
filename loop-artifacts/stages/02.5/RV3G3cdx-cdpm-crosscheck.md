# origin: ai — 阶段 02.5：交叉核对（RV3G3cdx-crossdomain-promptversion-mapping · r153）

> 交叉核对对象 = 02 工件的关键裁定 vs 仓库内独立证据源；web-llm 三 provider 登录态失效（r126/r129 先例），
> 外部第二意见 unverified 降级——本 goal 全部裁定有仓库内 byte-exact 锚点，外部边际贡献 ≈ 0（同 RV3B1psf A4 先例）。

## X1 · B10 推论的独立重读（防单源误读）

02 A3 主张「六变体 gold 清单 = domain1 gold（B10 机械推论）」。独立重读 DRAFT v2 §3.2 全节 + §3.1：
- §3.1 L176：「第一格沿用 decomp 27B 硬件域（gold 现成……）」——域不变
- §3.2 L180：「所有变体共用同一题面（v3 基础题面）」+ 变体表七行差异列全部是「删除/替换某指令段」，无一行改域或改 gold
- §4 补丁区（L217-283）：D1/D2/sham 段内容全部是流程指令（分区搜索/边界声明/格式规范），零 gold 语义

**裁定维持**：B10 推论成立，六变体占位条目 gold_nodes = domain1 清单合法。
残余边界：若未来 batch2 修订引入「换域」变体（§3.1 第二格），须新 domain 条目——映射表 schema 已支持（domains 为 dict），无需改消费逻辑。

## X2 · T4 收窄条件的反例搜索

02 A6 T4：仅当 M[P] ≠ GOLD_DOMAIN1（排序后）时 SIGNAL。反例搜索：是否存在「M[P]==GOLD_DOMAIN1 但缺省 G 仍危险」的场景？
- 缺省路径语义（load_batch2 L224-225）：G=None ⇒ gold := GOLD_DOMAIN1（硬编码常量）
- 若 M[P]==GOLD_DOMAIN1，则缺省值 == 声明版本绑定值 ⇒ 对照结论恒 PASS，SIGNAL 无信息量 ✓
- 若 M[P]≠GOLD_DOMAIN1，缺省值 ≠ 绑定值 ⇒ 静默错配风险（正是 Y1 前「静默漏计」缺陷的 prompt_version 维度镜像）⇒ SIGNAL 必要 ✓
**裁定维持**。注意：T4 是 SIGNAL 非 FAIL——即使真错配也留人工裁决空间（数据提供方可能正在迁移期），
与 T2（显式声明且错配 = 确定性错误 = FAIL exit 2）的强度差是有意的：显式声明 = 提供方已做选择，错配即 bug；
缺省 = 未做选择，提示而非定罪。

## X3 · T6 降级条款 vs fail-loud 原则的冲突检验

goal 标题是「fail-loud 协议承接」，T6 却是「表缺失降级 INFO」——是否自相矛盾？
- fail-loud 的对象 = **数据错配**（换题面未声明/错配），不是**工具能力缺失**
- 表缺失时断言无法执行对照 = 能力缺失，此时 fail-loud（exit 2）会把「没装对照器」误报为「数据错了」，方向性错误
- 先例：assert-kappa-receipt.py 对 kappa-receipt.json 缺失输出 FAIL（那是 verdict 型——回执缺失本身就是被检事实）；
  本场景表缺失不是被检事实而是检查器组件，类比 --lint-only 模式「目录不存在 = 数据未落盘 SIGNAL」（既有 docstring 先例）
**裁定维持**：T6 = INFO + exit 0，与 fail-loud 目标正交不冲突。挂 04.5 攻击项复核。

## X4 · 命名空间碰撞扫描

`pre-v3/C9-plain`、`v3/V0-baseline`… 等版本标识 vs 仓库既有字符串：
- grep `prompt_version` 全仓 → 仅 assert-goldrank-crossdomain.py（docstring+L233）+ batch2-lint-samples 样例（"DRAFT-v2-frozen"）
- 样例值 "DRAFT-v2-frozen" 是本 goal 之后才进入映射表的候选吗？**否**——样例是 lint 自验用假数据，
  其 prompt_version 值不在映射表中 ⇒ 跑 --lint-only --dir <sample> 时会触发 T3 SIGNAL。
  **这是预期行为还是回归？** 判定：预期——lint 模式只查 schema（T6/T7 域），gold-map 对照只在主模式 load_batch2 生效；
  若把对照放进 lint 模式，现有 11 个样例目录的实跑输出会漂移（byte-exact 回归违规）。⇒ **对照检查放主模式不放 lint 模式**（03 动作约束）。
  但需实证：改动后 11 样例 --lint-only 输出必须逐字节不变（04 验收项）。

## X5 · 冻结面影响面预扫

改动文件清单预测：
1. `bench/rubric-v3/ablation/prompt-version-gold-map.json`（新建）
2. `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（load_batch2 + docstring）
3. `bench/rubric-v3/ablation/batch2-lint-samples/`（新增负样例 ×2-3，不动既有用例）
4. loop-artifacts + tasks/goal-queue.md（收口）
冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / judge-blindtest-r1.json / stats-*.json / rejudge/*）= 零触碰。
**注**：prior-estimates.json 不加 prompt_version 字段（K6：第一域数据早于约定，回填 = 冻结面修改需 APPROVALS——不做，
第一域回归走「无参调用 byte-exact」验证而非数据回填）。

## X6 · 04.5 攻击项预登记（供反方复核消费）
A-1 O1 C9-plain 归属推论（A9.2）｜A-2 r71b vs r71 事件选择（A9.3）｜A-3 T4 收窄是否漏报（X2 已自检，反方再攻）
A-4 T6 降级 vs fail-loud（X3 已自检）｜A-5 对照检查放主模式导致 --lint-only 用户失去对照能力（X4 取舍）
A-6 排序后集合相等 vs 顺序敏感（O2）｜A-7 映射表 _schema 版本号机制是否过度设计｜A-8 六变体占位条目是否应入表（vs 只登记 C9-plain）

verdict: pass（六项交叉核对全闭合，矛盾三条已登记不隐藏）
