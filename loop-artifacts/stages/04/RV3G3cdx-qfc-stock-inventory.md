# 阶段 04 A3 — RV3G3cdx-queue-format-contract · 存量备料清单（r151）

> 边界声明（02.5 X4 裁定）：本文件 = **备料件，非 diff**——逐行表含「当前形态摘录 + 改写预览」，不含实际执行动作。改写本身需成璐裁定范围（契约 §4 选项 (i)/(ii)），导出候选承接执行轮。
> 行号基准 = r151 阶段 04 A2 后工作区版本（62 行，含尾空行；goal 行 48）。与 f7d3674 基准（61 行）差 = L4 指针行插入（L≥4 全部 +1）。
> 数字基线（02 S2/S3 锁定，本文件复核值须逐格一致）：低 pipe（≤1）= **15** / 严格 em-dash（零 pipe 且含 ` — `）= **8** / v1 标记 `**结果：` = **4** / v2 标记 = **20**。两集合交集为空（L8-L11 均 ≥2 pipe）。

## S1 — 三角验证记录（X6 操作约束第三遍：awk 独立实现）

| 口径 | python re 版 | awk 版 | 一致性 |
|---|---|---|---|
| goal 行总数（`^- \[` 前缀） | 48 | 48 | ✓ |
| 低 pipe（pipe ≤ 1） | 15 | 15 | ✓ |
| 严格 em-dash（零 pipe + ` — `） | 8 | 8 | ✓ |
| v1 标记 `**结果：` | 4 | 4 | ✓ |
| v2 标记（`**结果**：`/`**结果**:`） | 20 | 20 | ✓ |

v1 四行冒号 codepoint 独立核验：L8/L9/L10/L11 均为 U+FF1A（全角）——与契约 C5「v1 四行冒号同为全角」声明一致。

## S2 — 15 行低 pipe 简写行逐行表

风险标注：**⚠吸收登记行** = 短名跨区重复且 meta 括号内含「吸收」声明（C6 合法形态）——改写若移动声明位置将破坏 lint (a) SIGNAL 分支的既有实证，执行轮须 byte-stable 保留 meta 段原文。

### B 型：严格 em-dash（零 pipe ×8）

| 行号 | 短名 | 形态摘录（首 60 字） | 五段式改写预览 | 风险 |
|---|---|---|---|---|
| L18 | R5.2-evidence-packet | `(2026-10-30, r102: baff4b3) — 模板 v2 + packet v2（run1 M2=24…` | `- [x] R5.2-evidence-packet (2026-10-30, r102: baff4b3) \| 模板 v2 + packet v2（run1 M2=24/run2 M2=25/run3 null~45；M5 轮数 1/1/2 全带 basis）+ 对称性断言 67/0 exit 0；X2 错配登记（原 packet "run3 任务书25行"张冠李戴） \| 纯仓库内机判闭环，产投比中` | 无 |
| L19 | R5.2-packet-audit | `(2026-10-30, r103) — 原 v1 packet 单行摘要 12+1 原子断言…` | `- [x] R5.2-packet-audit (2026-10-30, r103) \| 原 v1 packet 单行摘要 12+1 原子断言全字段审计：8 confirmed / 3 mismatch / 1 unverified；新登记 X4/X5/X6/X7；机判脚本 assert-packet-audit.py 16/0/2 exit 0；未改任何冻结分 \| 纯仓库内审计，产投比中` | 无 |
| L20 | R5.2-sourcepath-hardening | `(2026-10-30, r104) — W1 收口：assert-packet-symmetry.py 删…` | `- [x] R5.2-sourcepath-hardening (2026-10-30, r104) \| W1 收口：assert-packet-symmetry.py 删 basename glob 兜底（严格模式）+ packet v2 十条 source_path 规范化 + 重跑 67/0 exit 0 基线维持 + 模板 v2 补填写规则 \| 纯仓库内脚本硬化，产投比中` | 无 |
| L21 | R5.2audit-C12-mechanize | `(2026-10-30, r105) — C12 "M1-M6 定义+" 形式性检查由 SKIP…` | `- [x] R5.2audit-C12-mechanize (2026-10-30, r105) \| C12 形式性检查由 SKIP(manual) 改机判信号输出（声称子串 + 正文正则，signal-only）；重跑 16 PASS / 0 FAIL / 1 SKIP + 1 SIGNAL exit 0；未改任何 verdict 与冻结分 \| 纯仓库内机判化，产投比中` | 无 |
| L44 | R5.2hard-EXEMPT-sentinel | `(2026-10-30, r106: 6fbd47b) — EXEMPT 非空哨兵警告落地…` | `- [x] R5.2hard-EXEMPT-sentinel (2026-10-30, r106: 6fbd47b) \| EXEMPT 非空哨兵警告落地，SELF-TEST 假豁免验证触发，67/0 exit 0 基线维持 \| 纯仓库内一行级加固，产投比高` | 无 |
| L51 | RV3G5-blocker-disposition-table | `(2026-10-30, 被 G6/r113 吸收) — 处置表已作为 AUDIT-report.md §7…` | `- [x] RV3G5-blocker-disposition-table (2026-10-30, 被 G6/r113 吸收) \| 处置表已作为 AUDIT-report.md §7 落地（12 blocker 逐条三态 + 16 major 按类点名 + 4 minor 逐条，消费 G5 3b L1/L2 分级）；本候选不再独立执行 \| 已被 G6 主 goal 吸收核销` | ⚠吸收登记行（meta 段「被 G6/r113 吸收」byte-stable 保留） |
| L53 | RV3G6-gmr-tiebreak-prereg | `(2026-10-30, 被队首同名 goal / r118 吸收) — gmr 主判据预注册…` | `- [x] RV3G6-gmr-tiebreak-prereg (2026-10-30, 被队首同名 goal / r118 吸收) \| gmr 主判据预注册冻结件已落盘（见上方待办区 r118 条目） \| 已被队首同名 goal 吸收核销` | ⚠吸收登记行 |
| L54 | RV3G6-o3-claim-list | `(2026-10-30, 被队首同名 goal / r120 吸收) — O3 claim 清单化…` | `- [x] RV3G6-o3-claim-list (2026-10-30, 被队首同名 goal / r120 吸收) \| O3 claim 清单化核心件已落盘（见上方待办区 r120 条目）；剩余部分另立候选见下 \| 已被队首同名 goal 吸收核销` | ⚠吸收登记行 |

B 型改写规则：`— <摘要>` → `| <摘要> | <产投比依据>`（产投比依据为执行轮从上下文提炼的补写段——**这是唯一需要人工判断的内容增量**，其余为机械替换）。

### C 型：单 pipe 混合（恰 1 pipe ×7）

| 行号 | 短名 | 形态摘录（首 60 字） | 五段式改写预览 | 风险 |
|---|---|---|---|---|
| L40 | R5.2audit-verdict-text-templatize | `(2026-10-30, r134: 6c18bc2, ralph/…) — assert-packet-audit.py VERDICT 段…` | `- [x] R5.2audit-verdict-text-templatize (2026-10-30, r134: 6c18bc2, ralph/r52audit-verdict-templatize) \| assert-packet-audit.py VERDICT 段硬编码事实快照同构缺陷处置：动态生成或注释标记'新增断言须同步' \| **结果**：选动态生成——AUDIT_CLS 显式分类表 + len() 推导；一致性守卫 exit 2；零漂移 + M1-M4 四变异实证；04.5 verdict pass（8 攻击 3 驳 3 部分处置） \| 纯仓库内脚本重构，产投比中` | 无 |
| L43 | R5.2audit-C4-assert-hardening | `(2026-10-30, r132: 8b2cc11, ralph/…) — assert-c4-timing.py W2/W3 健壮性落地…` | `- [x] R5.2audit-C4-assert-hardening (2026-10-30, r132: 8b2cc11, ralph/r52audit-c4-hardening) \| assert-c4-timing.py W2/W3 健壮性落地 \| **结果**：WS 缺失显式 FAIL + exit 1 + epoch() 时区剥离分派 + 未知格式 fail-loud；零漂移 + 三场景实证；04.5 verdict pass（导出 docsync 候选） \| 纯仓库内脚本加固，产投比中` | 无 |
| L45 | R5.2audit-C4-timing-reconstruct | `(2026-10-30, r130: dcdd7d8, ralph/…) — C4 "14m27s" 数值化机判…` | `- [x] R5.2audit-C4-timing-reconstruct (2026-10-30, r130: dcdd7d8, ralph/r52audit-c4-timing) \| C4 "14m27s" 数值化机判：解析 $WS/run2/loop-state.json channel 时间戳做差值重建耗时区间，与 14m27s 比对输出 SIGNAL \| **结果**：assert-c4-timing.py 落盘（signal-only exit 0）→ SIGNAL not-reconstructable；变异测试实证 reconstructable 分支可达；X5 升级机判实证；04.5 verdict pass（8 攻击 3 驳 5 登记）。导出 R5.2audit-C4-arena-export \| 纯仓库内机判化，产投比中` | 无 |
| L46 | R5.2audit-signal-counter | `(2026-10-30, r131: af8e15d, ralph/…) — assert-packet-audit.py 汇总行 SIGNAL 计数变量化…` | `- [x] R5.2audit-signal-counter (2026-10-30, r131: af8e15d, ralph/r52audit-signal-counter) \| assert-packet-audit.py 汇总行 SIGNAL 计数变量化 \| **结果**：signals 列表 + C12 三分支 append + 汇总行动态输出；零漂移 + 变异测试计数联动实证；exit code 语义不变；04.5 verdict pass（W2 残余耦合登记）。导出 R5.2audit-verdict-text-templatize \| 纯仓库内小修，产投比中` | 无 |
| L49 | RV3G4-prior-source-assert | `(2026-10-30, r135: d5899f4, ralph/…；核销轮——核心交付物 r130/0fedf42 已存在) — G4 强制机械化…` | `- [x] RV3G4-prior-source-assert (2026-10-30, r135: d5899f4, ralph/rv3g4-prior-source-assert；核销轮——核心交付物 r130/0fedf42 已存在) \| G4 强制机械化候选落地：assert 脚本校验 prior-estimates.json 必须记录 ≥N 个独立 p̃ 生成源（source 字段缺失/单源 = FAIL） \| **结果**：核销型收口——基线复验 8/8 PASS + M1-M3 防失效实证 + 队列四项核销表 + 尾行措辞修复；残余边界如实登记；04.5 verdict pass（8 攻击 4 败 3 部分处置 1 成立已处置） \| 核销型收口，产投比高` | 无 |
| L50 | RV3G4-kappa-receipt-assert | `(2026-10-30, r136: 26710e7, ralph/…) — G4 强制机械化候选落地：评分文件缺 κ 门禁…` | `- [x] RV3G4-kappa-receipt-assert (2026-10-30, r136: 26710e7, ralph/rv3g4-kappa-receipt-assert) \| G4 强制机械化候选落地：评分文件缺 κ 门禁执行回执 = FAIL 的断言脚本（回执格式定义 + 存在性检查） \| **结果**：assert-kappa-receipt.py 落盘——最小 schema 提案 + 三分支机判；当前 ablation 面实跑 = FAIL exit 1（预期行为）；M1-M7 七场景变异实证；04.5 verdict pass（8 攻击 2 驳 5 部分处置 1 成立已修）。闭环挂 RV3G4-kappa-gate-execution（外部阻塞） \| 纯仓库内机判化，产投比中` | 无 |
| L52 | RV3G6-draft-revision-batch1 | `(2026-10-30, 被队首同名 goal / r116 吸收) — DRAFT 修订清单第一批落地…` | `- [x] RV3G6-draft-revision-batch1 (2026-10-30, 被队首同名 goal / r116 吸收) \| DRAFT 修订清单第一批落地：R-01/R-02/R-03/R-06/R-10，产出新版 DRAFT 文件+修订 diff 记录（~14 回合） \| G6 AUDIT-report §9.1/§9.3 导出：开跑正式实验的前置条件，纯仓库内文本工作无外部依赖` | ⚠吸收登记行（meta 段「被队首同名 goal / r116 吸收」byte-stable 保留） |

C 型改写规则：现有单 pipe 两侧内容已是「一句话目标 | 结果注记」结构——改写 = 在结果注记段后追加第三段 `| <产投比依据>`（同样为执行轮提炼的补写段），并把 em-dash 连接符统一为 pipe。**注意 L40/L43/L45/L46/L49/L50 六行已含标准 `**结果**：` 注记（v2 形态）**——C 型 7 行无一命中 v1 标记变体，与 S3 对账一致。

## S3 — 4 处 v1 结果注记变体逐行表

| 行号 | 短名 | 现状片段 | 归一改写预览 | 备注 |
|---|---|---|---|---|
| L8 | RUBRIC-V3-FULL-AUDIT | `**结果：`（U+FF1A 全角） | `**结果**：`（半角 U+003A） | 长行，仅标记位 2 字符改动 |
| L9 | RV3G6-draft-revision-batch1 | 同上 | 同上 | 同上 |
| L10 | RV3G6-gmr-tiebreak-prereg | 同上 | 同上 | 同上 |
| L11 | RV3G6-o3-claim-list | 同上 | 同上 | 同上 |

v1 归一 = 纯机械替换（`**结果：` → `**结果**：`），零内容增量、零人工判断。lint (b) 现行宽松匹配对两代写法免疫 ⇒ 归一前后 exit 行为不变（回归取证覆盖）。

## S4 — 对账与高风险项汇总

- 15 + 4 = 19 触碰行，交集为空（L8-L11 均 ≥2 pipe，不在 15 之列）✓ 与契约 §4 声明一致。
- 「19」口径勘误重申：19 = 格式维（15 低 pipe）∪ 标记维（4 v1）并集大小，**不是**「em-dash 简写行数」（该口径实数 = 严格 8 / 低 pipe 15，视口径而定）——详见契约 §4 数字勘误登记节。
- 高风险项 = 4 个吸收登记行（L51/L52/L53/L54）：改写预览已保证 meta 段（含「吸收」声明）byte-stable 原位保留；执行轮实施后须复跑 assert-queue-lint (a) 确认 3 组跨区重复仍走 SIGNAL 分支（不升级为 FAIL）。
- 执行轮验收建议（供导出候选引用）：(1) 19 行改写后 queue 总行数不变（48 goal 行）；(2) assert-queue-lint 实跑 0 FAIL / 3 SIGNAL exit 0（SIGNAL 组数不变）；(3) 八脚本基线零漂移；(4) 可选同批落地契约 §3 R1+R2（激活条件 = 成璐裁「顺手统一排版」）。