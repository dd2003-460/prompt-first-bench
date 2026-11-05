# 02.5 — RV3G6-o3-claim-rejudge-scaffold · 交叉核对

> goal: claim 级独立重判的仓库内闭环骨架 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30

## X1 — hit-matrix 分布 vs o3-claim-list §3.2 声明（逐项机算比对）

| 项 | §3.2 声明 | 冻结 JSON 机算 | 判定 |
|----|-----------|----------------|------|
| h=1 cell 总数 | 98/248（39.5%） | 98/248 | ✓ 零 mismatch |
| gold strict 切片规模 | 5 节点 × 8 run = 40 cell | 40 | ✓ |
| gold strict h=1 | 10/40（N-3.2.2×6 + N-4×4，N-2.1/N-2/N-1.3 零命中） | 10/40，同分布 | ✓ |
| M1/M2 identity 基线 | 248/248、40/40、8/8 = 1.000 | （identity 定义下恒等，无需数据） | ✓ 定义一致 |

**结论**：§3.2 注记与冻结数据零漂移；sample-plan.json 的分层数字（P0=150 / P1=98 / gold strict=40）可直接以机算值落盘，无文档-数据张力。

## X2 — 优先级分层的语义依据核对

queue 原文「优先 h=0 的 150 cell，检验 FM-2 漏判方向」vs o3-claim-list §3.2 口径声明 2「M1 对 h=0 方向无判别力：两判据同判 0 可能都是漏判（FM-2 方向），召回检验依赖独立重判补数」。

核对结果：两者指向同一机制——h_id=0 ∧ h_claim=1 的 cell 才是 FM-2 假漏判的直接证据；h_id=0 ∧ h_claim=0 不产生新信息（但仍是分母）。故 P0 = 全部 h_id=0 cell（150）而非仅「疑似漏判子集」（后者不可事前界定，等于让采样器预知答案 → 循环论证）。**全量枚举 + 优先级排序**是本设计对「无偏采样」与「成本排序」冲突的解法：采样面 = 全集（248，无抽样偏差），执行顺序 = P0→P1（成本优化，不影响统计口径）。

## X3 — exit code 语义 vs 先例的一致性检查

| 脚本 | 数据缺失常态 | 语义 |
|------|-------------|------|
| assert-kappa-receipt.py | FAIL exit 1 | 回执是「评分有效性声明」——缺失 = 现有评分无效（负向事实） |
| assert-goldrank-crossdomain.py | SIGNAL exit 0 | batch2 是「待生产数据」——缺失 = 条件未触发（中性状态） |
| **assert-o3-claim-rejudge.py（本 goal）** | **SIGNAL exit 0** | rejudge 结果是「待生产数据」——缺失 = judge 通道未执行（中性状态） |

对齐 crossdomain 先例。stdout `[SIGNAL]` 前缀分流义务继承（batch2-closure queue 项登记的全局约定：未来自动化门禁接入须按前缀分流，不能只看 exit code）。

## X4 — κ 公式缺口（UNRESOLVED 登记）

o3-claim-list §4.3 规定「先算 κ（条目层质检）→ 过门禁 → 再聚合」，但**κ 的具体计算公式未在冻结件中文字化**（Cohen's κ？Fleiss'κ？条目层 = 单 node 跨判者还是跨 cell？N=3 时 Cohen's κ 不适用需 Fleiss'κ 或 pairwise 平均——冻结件未裁定）。DRAFT v2 R-02 提及「κ 条目层」与阈值 0.6（R5），同样未给公式。

处置：protocol D1 只引用**顺序关系**（κ 在聚合前）+ 阈值语义（低于下限作废重判），公式标 `UNRESOLVED (U-K1)`；assert 脚本**不计算 κ**（无公式可机判），只在 schema 中预留可选字段 `kappa_receipt_ref`（指向 kappa-receipt.json 路径，存在性可查、数值不复核）。导出裁定候选见 03 A6。此处置符合 current-goal 失败降级条款第 1 条（歧义项显式标 UNRESOLVED，不发明）。

## X5 — evidence 子串检查的边界情形

TASK-ablation Step 1 要求 evidence「必须是产出中真实存在的句子（不许改写）」+ ≤40 字。机判化选择：**evidence 必须是 run 文件全文的连续子串**（`evidence in run_text`）。边界情形登记：
- 判者引多句拼接 → 子串检查 FAIL（正确行为：协议要求「一句」）
- 判者引句含空白规范化差异（如全角空格）→ 子串检查 FAIL → 判者须原样复制（协议明文要求「原样」，FAIL 是正确行为非误报）
- h_claim=0 的 cell 无 evidence 义务（§2.2 只要求 yes 附依据）→ schema 允许 evidence=null 当且仅当 h_claim=0