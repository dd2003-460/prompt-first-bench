# 01 — RV3G6-o3-claim-rejudge-evidence-audit · goal 分解

> goal: hit-matrix 98 个 h=1 evidence 的 verbatim 合规审计 · 分支 ralph/rv3g6-o3-claim-rejudge-evidence-audit · 2026-10-30

## 1. 为什么这是 queue 空扫后的最高产投比项

queue 待办区现状：R5.2-third-scorer（blocked-on-external）/ RV3G3-batch2-arrival-closure（blocked-on-external）/ RV3B1-jaccard-adjudicate（待成璐裁定 [~]）/ RV3G4-kappa-gate-execution（blocked-on-external）/ R5.2audit-C4-arena-export（blocked-on-external）/ RV3G1-semantic-rejudge（blocked-on-external）/ RV3G6-kappa-formula-adjudicate（r141 刚导出，裁定型备料）。按协议阶段 A.1 兜底路径自找——扫冻结数据已知缺陷面。

**缺口定位**：o3-claim-list §3.2 口径声明 4 声称「已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token」——该核查只覆盖了**数值泄漏方向**（evidence 是否携带 gold 答案数值）。TASK-ablation Step 1 的另一半硬约束——「evidence 必须是 run 文件里真实存在的句子（不许改写）」——**从未被机判验证过**。r141 骨架把子串性确立为 rejudge 新结果的 schema 硬约束，形成标准不对称：新数据受检、旧数据免检。而 M1 identity 锚点（1.0 基线）与 FM-2 补数分母都建立在旧 hit-matrix 上——旧数据 evidence 若含改写/拼接，锚点可信度受损且当前无证据排除。

**产投比**：纯仓库内（读 1 JSON + 8 md），~1 个 assert 脚本 + 实跑 + 变异；产出 = 验证链补环（PASS）或负面结果清单（FAIL）——两种结果都有信息量，无外部依赖。

## 2. 判定语义预注册（FAIL vs SIGNAL 边界）

| 检查 | 条件 | 判定 | 依据 |
|------|------|------|------|
| C1 非空 | h=1 cell evidence 为 null/空串 | **FAIL** | TASK-ablation「每个 h=1 必须附 evidence」硬约束 |
| C2 verbatim 子串 | evidence ∉ run 全文连续子串 | **FAIL** | 「必须是 run 文件里真实存在的句子（不许改写）」硬约束；r141 protocol §3 硬约束 3 同源标准 |
| C3 长度惯例 | len(evidence) > 40 字符 | **SIGNAL**（不 FAIL） | TASK-ablation 原文「≤40字」是填写惯例非验收门禁；超长者可能是合理长句——暴露事实留人工裁量，同 r131 signal-counter 先例 |
| C4 跨 run 张冠李戴 | evidence 在所属 run 不存在但在其他 run 存在 | **FAIL**（C2 的子类，单独报出定位） | 张冠李戴比改写更严重（出处错误），单列便于处置 |
| C5 h=0 cell | evidence 应为 null（若有值） | **SIGNAL** | TASK-ablation 只要求 h=1 附 evidence；h=0 带值是冗余非违规 |

exit code：0 = 无 FAIL（含 SIGNAL）/ 1 = 存在 FAIL。stdout `[SIGNAL]` 前缀义务继承全局约定。

## 3. 不做的事

- 不判 evidence 是否**支持**对应 claim/node 的命中语义（语义相关性不可机判，r141 攻击 2 B1 同款边界）
- 不修改 hit-matrix.json（冻结红线；发现违规 → APPROVALS 登记 + 导出修复候选）
- 不复算 h 值本身（那是 RV3G6-o3-claim-rejudge 执行体的职责，blocked-on-external）