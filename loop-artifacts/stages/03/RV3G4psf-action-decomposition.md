# 阶段 03：行动分解 — RV3G4-prior-source-assert

> 依据：02 §2 判断确认 + 02.5 verdict pass（A1/A4 登记并入 04）· 分支 ralph/rv3g4-prior-source-assert

## 行动表

| # | 行动 | 对象 | 具体改动 | 验证方式 |
|---|------|------|----------|----------|
| A1 | APPROVALS 登记 | `APPROVALS.md`（新建，仓库根） | 条目：prior-estimates.json 追加顶层键 `p_tilde_provenance`（纯新增，nodes.* 零触碰；理由 = G4 导出授权的机械化落地必需；消费侧回归见 A5） | grep 定点 |
| A2 | prior-estimates.json 补 provenance | `bench/rubric-v3/ablation/prior-estimates.json` | 追加顶层键 `p_tilde_provenance`：independent_sources 两条（primary: judge_id="lead-main-session (original judge, TASK-ablation.md L27)" artifact="bench/rubric-v3/ablation/prior-estimates.json" role="primary"；blind-reestimate: judge_id 从 judge-blindtest-r1.json:judge **程序化提取** byte-exact，artifact="bench/rubric-v3/ablation/judge-blindtest-r1.json" role="blind-reestimate"）+ note 显式声明 family-independent: false（双源均 Qwen 家族，跨家族隔离待 rubric-v3 遗留 #1）+ n_min_referenced: 2 | python json round-trip + assert 检查①②③ |
| A3 | assert 脚本 | `bench/rubric-v3/ablation/scripts/assert-prior-source.py`（新建） | 三组检查：① p_tilde_provenance 存在 + independent_sources 非空 list；② 每条 source：judge_id 非空 str + artifact 相对 ROOT 可解析 is_file() + blind-reestimate 条目 judge_id == judge-blindtest-r1.json:judge（byte-exact）；③ judge_id 去重数 ≥ N_MIN=2。首行输出 SIGNAL ONLY 标注；exit 0/1 语义同 R5.2 系列 | exit 0 + 变异测试 M1-M4 |
| A4 | g4 文档状态更新 | `bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md` L100 | 「候选」→「已落地（RV3G4-prior-source-assert）」+ signal-only 边界说明一行 | grep 定点 |
| A5 | 消费侧回归 | assert-w2-formula.py + assert-w3w4-recompute.py | 重跑两脚本，确认 prior-estimates.json 追加键后消费侧零影响 | 双双 exit 0 |
| A6 | 六阶段工件收口 | stages/{01,02,02.5,03,04,04.5}/RV3G4psa-* + per-goal web-llm 回执 | 04 执行日志（含变异测试 M1-M4 + 风险表 R5/R6 落实）+ 04.5 反方复核 + web-llm 回执（预期 unverified 降级沿用） | 文件存在性 |

## 明确不做

- 不改 prior-estimates.json 任何既有键/节点值（nodes.* / epsilon / weight_formula 等全量不变）
- 不实现 verdict 模式（J1 定 signal-only；verdict 留后续候选）
- 不实现家族隔离机判（J3：归人工声明 + 遗留 #1 另开 goal）
- 不动 judge-blindtest-r1.json（只读引用其 judge 字段）
- 不碰 hit-matrix.json / stats-* / gold-tree.md

## 顺序依赖

A1（登记先行）→ A2（数据侧）→ A3（脚本锚定最终文本）→ A4（文档状态）→ A5（回归证明）→ A6（收口工件）。
