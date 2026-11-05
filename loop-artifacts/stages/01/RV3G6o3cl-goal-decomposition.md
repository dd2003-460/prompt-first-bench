# 阶段 01：目标分解 — RV3G6-o3-claim-list

> goal: O3 gold 节点转原子 claim 清单 · 分支 ralph/rv3g6-o3-claim-list · 2026-10-30
> 上游：tasks/current-goal.md（五字段）+ AUDIT-report.md §2-O3 L79 / §9.1 R-13 L293 / §9.3 L312

## F1 · 交付物结构分解（o3-claim-list.md 的节骨架）

| # | 节 | 内容来源 | 关键判读点 |
|---|----|----------|-----------|
| §1 | 背景与问题定义 | AUDIT §2-O3 L79（#13 处置原文）+ DRAFT v1 L58 / v2 L71（现行判据原文） | 「节点 ID 对得上才算命中」为何不可执行——三个具体失败模式（ID 幻觉匹配 / 无实质内容也算命中 / 方向错误也算命中），每条给冻结数据或 run 原文 evidence |
| §2 | 原子 claim 清单（31 节点） | gold-tree.md 全树 + prior-estimates.json reason 字段 + hit-matrix evidence 校准 | 每节点 1-2 句可判真假陈述；三属性逐条满足：自含 / 可二值 / 方向内嵌；SHARED 节点（N-1.3.2）与根节点（N-0）特殊处理显式声明 |
| §3 | 映射一致性指标定义 | AUDIT §2-O3「映射一致性本身作为可报效度指标」 | 主口径公式 + 分母声明（NA 节点处理）+ 辅助口径（节点级精确一致 vs run 级聚合）+ 冻结数据基线值（机算） |
| §4 | 多判者协议（≥2/3 文字化） | AUDIT §2-O3「≥2/3 独立判者一致」 | N=3 判者构成 / tie 处理（2/3 即过、1/3 即不过、无平票态）/ 与 R-02 κ 条目层门禁的关系（κ 在条目层算，本协议是条目判定后的聚合规则，两者不重复） |
| §5 | 使用边界与未决项 | G4 S2 + AUDIT §6 限定语 | claim 清单不消除同源偏置（S2 未闭环前同样带限定语）；claim 措辞人工审定状态登记 |
| §6 | 冻结声明 | — | 修改流程 = 新 goal + APPROVALS；gold-tree.md 本体零修改 |

**判读**：§2 是核心工作量（31 条 claim 起草 + 自检）；§3 需要判断（指标口径选择）+ 计算（基线值）；§1/§4/§5/§6 是机械固化。六节覆盖任务书四块要求 + 验收标准全部条目。

## F2 · 输入完备性盘点

| 输入 | 状态 | evidence |
|------|------|----------|
| AUDIT §2-O3（#13 处置：claim 清单 + ≥2/3 + 映射一致性指标） | ✅ 在仓 | AUDIT-report.md L79 |
| AUDIT §9.1 R-13 / §9.3 导出描述 | ✅ 在仓 | AUDIT-report.md L293/L312 |
| gold-tree.md（31 节点全树 + SHARE/BOUND/KIND 标注 + SHARED 表） | ✅ 在仓，只读 | bench/rubric-v3/ablation/gold-tree.md L10-57 |
| 现行命中判据原文（修订对象） | ✅ 在仓 | DRAFT-rubric-v3.md L58 + DRAFT-rubric-v3-v2.md L71 |
| TASK-ablation Step 1（h_v 判定协议：从严 + 黑盒算覆盖 + evidence 真实存在） | ✅ 在仓 | ablation/TASK-ablation.md L17-24 |
| hit-matrix.json（8×31 h 值 + evidence 片段 = claim 措辞校准材料） | ✅ 在仓，只读 | ablation/hit-matrix.json |
| prior-estimates.json nodes.*.reason（judge 对各节点「什么算提出这一刀」的自然语言理解） | ✅ 在仓，只读 | ablation/prior-estimates.json |
| gold strict 集（5 节点，指标基线用） | ✅ 在仓 | assert-gmr-recompute.py L13 + AUDIT §3.2 L100 |
| runs-C0-run1..8.md（claim 可判性抽查的对照原文） | ✅ 在仓，只读 | ablation/runs-C0-run*.md |
| 外部文献交叉验证 | ❌ 不需要 | 纯仓库内文本+计算工作，无外部依赖 |

**空缺**：无阻塞性空缺。一个非阻塞观察已登记为 F3-J2（hit-matrix evidence 覆盖率仅 ~30%，见 F4-R2）。

## F3 · 判断点识别

| # | 判断 | 选项空间 | 预注册倾向 |
|---|------|----------|-----------|
| J1 | claim 的粒度：每节点 1 条还是允许 2 条 | A 严格 1 条 / B 1-2 条（queue 描述原文「每节点 ≥2/3 独立判者可核验的实质内容条目」+ AUDIT §9.3「每节点 1-2 句」） | B（两处上游原文都写 1-2；复合节点如 N-3.2 decode 时间含 KV 带宽双机制，硬压成 1 条会丢失可判性） |
| J2 | 映射一致性基线的可用输入 | A 用 hit-matrix h 值做节点级一致率（claim 级重判 unverified 时的降级口径）/ B 拒绝给基线值（等独立 judge） | A + 显式声明口径局限（A 测的是「evidence 片段与 claim 语义兼容率」的下界代理，不是真 claim 级重判；B 会让指标只有定义没有锚点，违反研究级质量线「结论必须带 evidence」） |
| J3 | NA 档适用范围 | A 仅纯结构性节点（无实质内容可言）/ B 任何 judge 无法二值判的节点 | A（保守：先验估计只有 N-0 根节点候选——p̃=null 但 c_pass 定义本身是可判的实质内容，需逐节点检查后定，不在 01 预断） |
| J4 | DRAFT v2 修订范围 | A 只改 L71 判据行 / B 连带更新 L73 状态声明中的判据引用 | A（L73 提的是 gmr/阈值，与命中判据无关；最小 diff 防误伤 batch2 占位） |
| J5 | 多判者 N 取值 | A N=3（AUDIT 原文「≥2/3」的最小整数解）/ B N=5 | A（N=3 是「≥2/3」唯一无歧义的最小实现；N=5 引入 3/5 平票态需要额外 tie 规则，超出上游原文授权范围） |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|----|------|--------|------|
| R1 | claim 措辞把 gold 答案数值写死（如「KV 字节 ≈ 8GB」），使命中判定退化为数值背诵，重新引入 #13 类不可执行问题 | 高 | claim 只写**结构/机制/方向**（「产出给出每流 KV 缓存字节数的估算或区间」），不写具体数值；自检脚本检查 claim 中不含 gold-tree 专有数字（SHARED 表例外需人工确认） |
| R2 | hit-matrix evidence 覆盖率低（h=1 cell 才有 evidence，8 run 合计 ~100/248 cell），claim 校准样本不足 | 中 | 措辞校准只用 h=1 evidence（正例），h=0 方向的漏判检查导出 queue（与 RV3G1-semantic-rejudge 同通道）；04.5 显式声明该局限 |
| R3 | 映射一致性基线被误读为「claim 判据已验证有效」 | 高 | §3 强制口径声明（J2-A 的局限）+ §5 使用边界；assert 脚本输出行带口径标签 |
| R4 | 31 条 claim 中个别节点（SHARED 引用节点 N-1.3.2）claim 写成「见 N-1.1.1」不自含 | 中 | SHARED 节点 claim 必须展开为完整陈述（「故障损耗支引用的卡价与摊销支的卡价为同一参数」），禁交叉引用 |
| R5 | DRAFT v2 L71 替换后与 L66 权重公式行的 h_v 符号不一致 | 低 | 保留 h_v 符号不变（claim 命中 → h_v=1），只改判据定义；04 阶段 grep 核对 |

## 阶段 02 研究入口

- 第一批行动：通读 gold-tree.md 全树 31 节点（含 L59 图例 + L65-71 SHARED 表 + L75-125 OC-1 卡片样例），逐节点提取「该节点声称的实质内容」草稿
- 第二批行动：prior-estimates.json 31 条 reason 字段逐条对照（judge 视角的「这一刀是什么」）+ hit-matrix h=1 evidence 逐条对照（run 实际怎么写的）
- 第三批行动：runs-C0-run1..8.md 抽查 3 个节点（1 个高频命中 / 1 个零命中 gold / 1 个 SHARED），验证 claim 草案的可判性（能明确说出 yes/no 及依据）
- 失败备用路径：若某节点三源（tree/reason/evidence）信息不足以写出可二值 claim → 标 NA 候选进入 J3 裁决，不虚构