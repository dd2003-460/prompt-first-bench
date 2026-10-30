# 阶段 01：目标分解 — RV3B1-prompt-side-freeze（batch2 R-09 前置）

> goal: D2 边界类型声明段写入 loop/prompt-first/02.5 并 commit 冻结 + V3 sham 化联动设计 · 分支 ralph/rv3b1-psf · 2026-10-30
> 上游：tasks/goal-queue.md 候选条目 + batch1 revision-log 诚实保留 #5 + DRAFT-rubric-v3-v2.md L154-161（D2 冻结 diff 段）/ §3.2 变体矩阵 / §4.3 sham 段

## F1 · 交付物结构分解

| # | 交付物 | 内容 | 关键判读点 |
|---|--------|------|-----------|
| D1 | D2 段写入 `loop/prompt-first/02.5-cross-check.md` | 独立小节「【边界类型声明】sham 消融专用」，正文 = DRAFT v2 L154-161 代码块内文本逐字抄录（不改动一字）+ 来源标注（DRAFT v2 L154-161 冻结快照） | 与 DRAFT v2 源文本 byte-exact（机判 diff）；落点选择见 J1 |
| D2 | V3-sham 联动设计 | §3.2 变体矩阵新增 V3-sham 行（或等价登记）：V3-noboundary 的删除目标 = 本 D1 小节；sham 替换段 = DRAFT v2 §4.4（与 §4.3 对称设计的等长中性段） | V3-noboundary 定义本身零改动（冻结件不动）；只补「删除什么、换成什么」的执行侧定义 |
| D3 | assert 脚本 | assert-psf-freeze.py：① 02.5 文件含 D2 段且与 DRAFT v2 L154-161 逐字一致；② §3.2 表含 V3-sham 行；③ §4.4 sham 段存在且与 §4.3 等长约束满足（行数相等 + 字符数偏差 ≤10%） | exit 0 + 变异测试 |
| D4 | 六阶段工件 | 本文件 + 02/02.5/03/04/04.5（前缀 RV3B1psf）+ per-goal web-llm 回执 | 02 含 DRAFT v2 相关段落全量盘点 evidence |

## F2 · 输入盘点

| 输入 | 状态 | evidence |
|------|------|----------|
| D2 段源文本（DRAFT v2 L154-161 代码块） | ✅ 已读 | DRAFT-rubric-v3-v2.md L154-161 |
| §3.2 变体矩阵（V0-V3 + V-sham 行现状） | ✅ 已读 | DRAFT v2 §3.2（L194-196 D1/D2 freeze-diff 表附近） |
| §4.3 sham 替换段（既有先例） | ✅ 已读 | DRAFT v2 L255-269 |
| `[batch2: R-09]` 占位符位置 | ✅ 已定位 | DRAFT v2 L164 |
| 02.5 目标文件现状（25 行通用流水线节） | ✅ 已读 | loop/prompt-first/02.5-cross-check.md |
| revision-log 诚实保留 #5（范围切割依据） | ✅ 已读 | DRAFT v2 revision-log |

## F3 · 判断点识别

| # | 判断 | 选项空间 | 预注册倾向 |
|---|------|----------|-----------|
| J1 | D2 段落点：A `loop/prompt-first/02.5-cross-check.md` 独立小节 / B `03-action-decomposition.md` / C 新文件 | A（queue 描述明写「02.5（或 03）」取首选；02.5 是交叉核对阶段，边界类型声明属「核对前先声明比对对象类型」的前置信息，语义贴合；C 会碎片化 prompt 文件集） |
| J2 | V3-sham 段来源：A 新建 §4.4 与 §4.3 对称 / B 复用 §4.3 同段 | A（§4.3 服务于既有 V-sham；V3-sham 需要自己的等长中性段，否则两变体共享替换文本会让「删除 vs sham」对照失去独立性——对称设计原则） |
| J3 | 等长判定标准 | 行数相等 + 总字符数偏差 ≤10%（沿用 batch1 V-sham 的等长约定口径；若 DRAFT v2 有显式数值标准则从其标准） |
| J4 | §3.2 表改动幅度 | 最小 diff：只加 V3-sham 一行，不改任何既有行（V3-noboundary 定义冻结不动） |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|----|------|--------|------|
| R1 | 手抄 D2 段引入差异 → byte-exact 声明变假声明 | 高 | 用脚本从 DRAFT v2 提取 L154-161 原文写入 02.5（不手敲）；assert 检查① diff 验证 |
| R2 | 改 §3.2 表误伤冻结的 V3-noboundary 定义行 | 高 | J4 最小 diff + assert 对 V3-noboundary 行做定点不变断言 |
| R3 | 02.5 文件被 prompt-first 工作流机械进程（Stop Hook/Reviewer）并发修改 | 中 | 写入前 git status 确认干净；写入后 assert 复验；若冲突则登记 APPROVALS 不阻塞 |
| R4 | 「commit 冻结」语义歧义（commit ≠ 不可变） | 低 | 冻结 = 后续 goal 不得改动该段（由 assert 防漂移承担），commit 只是留痕动作；在 02 工件写明此语义 |
| R5 | web-llm 登录态失效 | 低 | per-goal 分文件回执记录 unverified，不阻塞（纯仓库内文本工作） |