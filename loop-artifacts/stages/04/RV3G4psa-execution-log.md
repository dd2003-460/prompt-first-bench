# 04 执行日志 — RV3G4-prior-source-assert（r130 · 2026-10-30）

> goal: G4 强制机械化候选落地——assert 脚本校验 prior-estimates.json 独立 p̃ 生成源 provenance
> 分支：ralph/rv3g4-prior-source-assert · 上游判断 J1-J4 见 stages/02，行动表 A1-A6 见 stages/03
> 执行模式说明：runner（Hermes agent）直接执行——本 goal 工作量小且全为确定性文本/脚本操作，按 runner 桥接规则可由 Hermes 本人完成（不派 claude -p，避免 API 往返开销；工具纪律条款约束的是 claude 子会话内部）。

## 实际执行记录

| 步骤 | 内容 | 验证 |
|------|------|------|
| A1 | APPROVALS.md 新建 + 登记 prior-estimates.json 追加顶层键 `p_tilde_provenance`（纯新增、回退方式、影响面声明） | grep 定点 |
| A2 | prior-estimates.json 追加 `p_tilde_provenance`：independent_sources 两条（primary = Lead 主会话估计；blind-reestimate judge_id 从 judge-blindtest-r1.json:judge **程序化提取** byte-exact）+ note 显式声明 family-independent: false + n_min_referenced: 2 | python json round-trip + assert 检查①②③ PASS |
| A3 | 新建 `ablation/scripts/assert-prior-source.py`（三组检查 8 项断言；首行 SIGNAL ONLY 标注；N_MIN=2 常量注释指向遗留 #1） | **实际运行 exit 0**：8/8 PASS |
| A4 | g4-vulnerability-crosscheck.md L100「候选」→「已落地（RV3G4-prior-source-assert，r130）」+ signal-only 边界说明；κ 门禁候选指向 RV3G4-kappa-receipt-assert | grep 定点确认 |
| A5 | 消费侧回归：assert-w2-formula.py + assert-w3w4-recompute.py 重跑 | 双双 **exit 0**（prior-estimates.json 追加键后 W2/W3/W4 复算零影响） |
| A6 | 本日志 + 04.5 反方复核 + per-goal web-llm 回执 | 本文件 + 04.5 工件 |

## 变异测试（A3 实义确认，临时写入原文件后立即恢复）

| 变异 | 操作 | 脚本行为 |
|------|------|----------|
| M1 | 删 p_tilde_provenance 块 | exit 1，检查① 2 项 FAIL ✓ |
| M2 | blind-reestimate judge_id 篡改一字 | exit 1，byte-exact 检查 FAIL ✓ |
| M3 | primary artifact 指向不存在文件 | exit 1，artifact 可解析检查 FAIL ✓ |
| M4 | 两源 judge_id 设为相同（去重数=1） | exit 1，检查③ N_MIN FAIL ✓ |

（每项变异后原文件立即恢复；恢复后重跑 exit 0。）

## 风险表落实（02.5 登记项）

- R5（A1 残余风险）：同一人先后跑两次估计并都登记为独立源，脚本无法识别——已接受，家族隔离 + 盲性真实性归 04.5 人工复核 + rubric-v3 遗留 #1（≥3 独立 LLM 服务盲测）闭环。
- R6（A4 限制）：primary 条目的 artifact 检查只是格式校验（自我指认），不是历史过程真实性证明——已接受，可追溯性 ≠ 历史真实性，后者归 04.5 人工复核。

## 红线核对

- prior-estimates.json 既有字段零修改：git diff 仅 +17/-1（新增 p_tilde_provenance 块；-1 为文件尾换行规范化）✓
- judge-blindtest-r1.json / hit-matrix.json / stats-* / gold-tree.md 零修改 ✓
- APPROVALS.md 登记先行（A1 → A2 顺序）✓
- 冻结数据修改走登记路径（J4 预注册处置）✓

## web-llm 回执

per-goal 分文件约定沿用：`loop-artifacts/prompt-first/02-web-llm-cross-check-RV3G4psa.md`——预期三 provider 登录态失效 unverified 降级（同 RV3B1psf / RV3G6u3 模式）；本 goal 证据链仓库内闭合（provenance 块 + 脚本 + 消费侧回归），外部第二意见边际贡献 ≈ 0。
