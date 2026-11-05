# 01 — RV3G6-kappa-formula-adjudicate · goal 分解

> goal: U-K1 κ 公式裁定备料（三方案对照，不代裁）· 分支 ralph/rv3g6-kappa-formula-adjudicate · 2026-10-30

## 1. 为什么现在做

queue 待办区现状：R5.2-third-scorer / RV3G4-kappa-gate-execution / R5.2audit-C4-arena-export / RV3G1-semantic-rejudge / RV3G3-batch2-arrival-closure 全 blocked-on-external；RV3B1-jaccard-adjudicate / RV3G6-o3-claim-rejudge 为 [~] 待人工/待外部。纯仓库内可动项 = **RV3G6-kappa-formula-adjudicate**（r141 导出，~2 回合备料型）+ 新导出的 RV3G6-o3-claim-list-erratum-27（冻结件修改需成璐裁定改法——比本项多一道人工前置）。按产投比取 kappa-formula-adjudicate：它是 judge-protocol-batch1.md §4 UNRESOLVED 标记的直接上游，且 batch2/rejudge 执行体到来后 protocol 即刻需要该公式闭合——备料先行无浪费。

## 2. 缺口精确定位（预注册研究问题）

U-K1 = o3-claim-list §4.3「条目层 κ 门禁」只有**序关系**（判者间一致性须达阈值），没有**计算公式**。悬空链条：

```
o3-claim-list §4.3（κ 门禁，无公式）
  ├→ DRAFT v2 R-02/R5：阈值 0.6 引用了「条目层 κ」但口径未绑定到具体公式
  ├→ r141 judge-protocol-batch1.md §4：UNRESOLVED 登记处（回填目标）
  └→ assert-kappa-receipt.py：method 字段 schema 未约束取值域（任何字符串都过）
```

三个候选公式（材料需逐一定义 + N=3 适用性论证）：
- **F1 Cohen's κ**：二判者指标。N=3 时**不适用**于整体——只能两两配对（C(3,2)=3 对）后聚合，退化为 F3
- **F2 Fleiss'κ**：N≥2 判者原生指标，条目粒度 = 单 cell 跨判者计数矩阵。N=3 直接可用
- **F3 pairwise 平均 Cohen's κ**：3 对 Cohen's κ 的均值（或中位数）。N=3 可用，但对子集缺失敏感

关键裁定维度（对照表列）：定义式 / N=3 适用性 / 条目粒度（单 node 跨判者 vs 跨 cell 全量池化）/ 与 0.6 阈值的口径绑定 / 缺失标注处理 / 可机判性（给定 rejudge-results.json 能否零歧义复算）/ 计算成本。

## 3. 不做的事

- **不代裁**：推荐排序是给成璐的决策输入，不是结论（同 jaccard-m5 先例——材料落盘即本 goal 完成，裁定是人工动作）
- **不算真实 κ**：无 rejudge-results.json（blocked-on-external），数值自检只用手算小例验证公式引用正确性
- **不动冻结件**：o3-claim-list.md / DRAFT v2 / judge-protocol-batch1.md / assert-kappa-receipt.py 裁定前零触碰；裁定后执行清单只描述 diff 面不执行