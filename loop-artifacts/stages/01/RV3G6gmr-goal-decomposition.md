# 阶段 01：目标分解 — RV3G6-gmr-tiebreak-prereg

> goal: gmr 主判据预注册冻结件 · 分支 ralph/rv3g6-gmr-tiebreak-prereg · 2026-10-30
> 上游：tasks/current-goal.md（五字段）+ AUDIT-report.md §3.2/§3.3/§8

## F1 · 交付物结构分解（gmr-criterion-freeze.md 的节骨架）

| # | 节 | 内容来源 | 关键判读点 |
|---|----|----------|-----------|
| §1 | tie-break 规则文字化 | AUDIT §3.2 L100 + §8 规则 3 | 节点 ID 字典序的精确定义 + 为何不用其他方案（拒绝表） |
| §2 | 过线阈值引用机制 | AUDIT §3.2 L100 定位声明 + G3 F3b | 三件套：引用机制（不写死）+ 锚点（超几何参考值）+ 门禁（RV3G3 前不得正式判定） |
| §3 | 退出条件 checklist | AUDIT §3.3 L122 | 逐条拆为触发条件+动作+机判方式（5 条 EC-1~EC-5） |
| §4 | §8 引用规则 byte-exact | AUDIT §8 L248-272 | 逐字抄录 + 本 goal 复核发现（数值勘误补充） |
| §5 | 权威参考值表 | 本 goal 独立复算 | Fraction 精确值，替代 AUDIT §8 表中有误的绝对值 |
| §6 | DRAFT v2 一致性核对 | DRAFT-rubric-v3-v2.md L73/L77/L81 | 确认无矛盾 |
| §7 | 冻结声明 | — | 修改流程 = 新 goal + APPROVALS |

**判读**：§1/§3/§4 是机械固化（抄录+拆解），§2 需要判断（门禁边界），§5 需要计算（复算+对比）。七节覆盖任务书四块要求 + 验收标准全部条目。

## F2 · 输入完备性盘点

| 输入 | 状态 | evidence |
|------|------|----------|
| AUDIT-report §3.2（gmr 定义 + tie-break 预注册） | ✅ 在仓 | AUDIT-report.md L98-110 |
| AUDIT-report §3.3（权重处置 + 退出条件） | ✅ 在仓 | AUDIT-report.md L112-122 |
| AUDIT-report §8（tie-sensitivity 引用规则全文） | ✅ 在仓 | AUDIT-report.md L248-272 |
| prior-estimates.json（orig judge w1/w2/p̃） | ✅ 在仓，只读 | bench/rubric-v3/ablation/prior-estimates.json |
| judge-blindtest-r1.json（new judge w3_full_ranking） | ✅ 在仓，只读 | bench/rubric-v3/ablation/judge-blindtest-r1.json |
| gold strict 集定义（5 节点） | ✅ 在仓 | AUDIT §3.2 L100 + stats-w3w4.json construct_validity |
| G3 超几何锚点（E[X]=1.61/P≥4=2.7%） | ✅ 在仓 | g3-w3w4-completion.md L51 |
| DRAFT v2 O3 节（一致性核对对象） | ✅ 在仓 | DRAFT-rubric-v3-v2.md L62-85 |
| 外部文献交叉验证 | ❌ 不需要 | 纯仓库内文本+计算工作，无外部依赖 |

**空缺**：无。所有输入均在仓内且可机判。

## F3 · 判断点识别

| # | 判断 | 选项空间 | 预注册倾向 |
|---|------|----------|-----------|
| J1 | gmr rank 方向（rank 0 = 最高权重 vs 最低权重） | A 最高权重=rank0 / B 最低权重=rank0 | A（「越小越好」+ W3-orig=5.40 tie-robust 只在 descending 下成立 → 唯一自洽解） |
| J2 | AUDIT §8 表数值不一致的处理 | A 用 AUDIT 原值 / B 用本 goal 复算值 / C 两者并列 | B（复算值可机判验证，AUDIT 值有算术错误；但保留 AUDIT 原文 byte-exact 不动） |
| J3 | 退出条件「跨方案排序反转」的精确定义 | A 任一方案对翻转 / B 整体 Spearman < 0.5 / C 最大位移 ≥ 2 位 | A（最严格、最保守、最易机判） |
| J4 | top-10 阈值是否在本文件给推荐值 | A 给推荐值（如 ≥4）/ B 只给引用机制不给值 | B（任务书明确「不写死数值」，给值 = 越权定稿） |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|----|------|--------|------|
| R1 | §8 byte-exact 抄录出错（多/少一个字符） | 高 | python 字节比对验证（已做 ✓） |
| R2 | gmr 复算公式理解错（rank 方向/分母/tie 处理） | 高 | 用 W3-orig=5.40 tie-robust 单值作为锚点校验（只有正确公式能得出此值） |
| R3 | 退出条件拆得过细导致不可执行 | 中 | 每条给具体机判命令/脚本入口 |
| R4 | 与 DRAFT v2 产生新矛盾 | 低 | §6 逐行核对（DRAFT v2 未写死任何 gmr 数值） |
| R5 | AUDIT §8 数值勘误引发下游困惑 | 中 | §4.1 明确标注「以本文件 §5 为准」+ 建议后续 goal 发 erratum |

## verdict

**pass** — 七节骨架覆盖任务书四块 + 验收标准全条目；输入零空缺；4 个判断点已预注册（J1 有唯一自洽解，J2/J3/J4 有明确倾向供 02.5 攻击）。进入 02。