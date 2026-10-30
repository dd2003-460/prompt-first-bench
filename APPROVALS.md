# APPROVALS — 待用户裁定的不可逆/越权操作队列

> runner 遇到「不可逆且偏好不明」或「冻结数据修改」时登记于此，跳过继续做可逆工作。成璐裁定后销账。

## 2026-10-30 · RV3G4-prior-source-assert（r130）

**操作**：`bench/rubric-v3/ablation/prior-estimates.json` 追加顶层键 `p_tilde_provenance`（independent_sources 两条 + note + n_min_referenced）。

**理由**：G4 交付物「给 G5 的导出」第一类授权机械化落地（g4-vulnerability-crosscheck.md L100）——provenance 语义上属于本文件自身元数据，拆新文件会造成双源漂移二义性（RV3B1psf 02.5 A4 同款论证）。

**影响面声明**：纯新增顶层键；nodes.* / epsilon / weight_formula / source_baseline_commit 等全部既有字段零触碰。消费侧回归 assert-w2-formula.py + assert-w3w4-recompute.py 重跑 exit 0（见 04 日志 A5）。

**回退方式**：`git revert <收口 commit>` 单步还原，无级联影响。

**状态**：已执行（runner 按 J4 预注册处置：登记 + 纯新增 + 回归证明三重保障）。若成璐认为应走开新文件路径，revert 后按新方案重做。
