# APPROVALS — 待用户裁定的不可逆/越权操作队列

> runner 遇到「不可逆且偏好不明」或「冻结数据修改」时登记于此，跳过继续做可逆工作。成璐裁定后销账。

## 2026-10-30 · RV3G4-prior-source-assert（r130）

**操作**：`bench/rubric-v3/ablation/prior-estimates.json` 追加顶层键 `p_tilde_provenance`（independent_sources 两条 + note + n_min_referenced）。

**理由**：G4 交付物「给 G5 的导出」第一类授权机械化落地（g4-vulnerability-crosscheck.md L100）——provenance 语义上属于本文件自身元数据，拆新文件会造成双源漂移二义性（RV3B1psf 02.5 A4 同款论证）。

**影响面声明**：纯新增顶层键；nodes.* / epsilon / weight_formula / source_baseline_commit 等全部既有字段零触碰。消费侧回归 assert-w2-formula.py + assert-w3w4-recompute.py 重跑 exit 0（见 04 日志 A5）。

**回退方式**：`git revert <收口 commit>` 单步还原，无级联影响。

**状态**：已执行（runner 按 J4 预注册处置：登记 + 纯新增 + 回归证明三重保障）。若成璐认为应走开新文件路径，revert 后按新方案重做。

## 2026-10-30 · RV3G3-goldrank-threshold-proof（r138+）— freeze doc 回填备案

**操作**：`bench/rubric-v3/gmr-criterion-freeze.md` 修改 3 行——§2.1 引用行（占位符 `threshold_top10 := RV3G3-goldrank-threshold-proof 产出值` → 双轨阈值表述 + 指向 goldrank-threshold-proof.md）、§2.1 说明行（「不得写死数值」禁令 → 回填状态声明）、§2.3 门禁行（❌ 未完成（queue 中）→ ✅ 完成（2026-10-30, goldrank-threshold-proof.md））。

**理由**：freeze §7 规定「修改本文件 = 开新 goal + APPROVALS.md 登记」。本 goal 即该引用机制预留的回填通道（§2.1 占位符为 r118 预注册授权），属机制内操作；04.5 攻击 3 复核维持该裁决，按 current-goal 失败降级条款补事后备案（非事前审批）。

**影响面声明**：改动面限 3 行，diff 全量落盘 `loop-artifacts/stages/01/RV3G3thr-stages01-03.md` J2 节；freeze §1/§3/§4/§5/§6/§7 零触碰；防漂移断言 assert-goldrank-threshold.py exit 0（31 PASS）+ 变异测试 4/4 FAIL。

**回退方式**：`git revert <收口 commit>` 单步还原。

**状态**：已执行（事后备案）。若成璐认为 §2.1 回填应走其他形式（如拆独立阈值文件），revert 后按新方案重做。
