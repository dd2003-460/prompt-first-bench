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

## 2026-10-30 · RV3G3cdx-crossdomain-promptversion-mapping（r153）— C9-plain 归属推论复核 + 执行偏差备案

**操作**：`bench/rubric-v3/ablation/prompt-version-gold-map.json` 新建权威映射表，其中 `pre-v3/C9-plain` 条目的 status=`archived-reference` 及「C9-plain ≠ v3 变体矩阵成员」的归属判定为**推论**而非直接证据——L1 原始任务书不在本仓，推论锚点 = DRAFT-rubric-v3-v2.md §3.2 L180 #27 裁定原文（「V0 必须在 v3 题面上同批次重跑……L1 C9-plain 只作外部参照」把两者当不同对象处理）。

**理由**：04.5 A-1 攻击项复核结论为驳回（推论有裁定文本锚点支撑），但残余不确定性非零——若成璐知悉 C9-plain 实为 V0-baseline 旧名，则映射表存在重复登记。消费逻辑零影响（两条目 gold_nodes 相同，仅 label/status 一行 diff），故不阻塞收口，挂此供复核。

**影响面声明**：纯新增文件（git status `??`），冻结面零触碰；消费方 assert-goldrank-crossdomain.py 的 gold_map_check 对该条目只做 sorted-set 相等比较，label/status 字段机判零消费。

**回退方式**：`git revert <收口 commit>` 单步还原；或单行修改该条目 status/label 即可纠正归属，无需重建表。

**状态**：待成璐复核（不阻塞）。

**附 · 执行偏差备案（D-a~D-d，均已修复复验，无遗留）**：
- D-a：初版 domain 解析用 prompt_version 的 `/` 后缀查 versions dict，而映射表键为完整字符串 ⇒ 恒 miss 误落 T3 SIGNAL；修复 = 完整 pv 直查 + 多域期 prefix 路由过渡形态（升级条款预注册于代码注释，挂 queue 候选 RV3G3cdx-goldmap-multidomain-upgrade）。
- D-b：bound 类型违例分支引用已删除变量 `ver`（NameError 潜伏）⇒ 改 `pv`，T7b 实跑实证闭合。
- D-c：N6 样例初版 gold 成员 N-5.3 不在样例 nodes 键集被 Y1 先行拦截 ⇒ 改 N-5 并同步 nodes/hit-matrix，断言语义未变。
- D-d：主模式原无 --dir 参数 ⇒ main() 增 --dir 解析（无参行为 byte-exact 不变，A4(i) 实证）。
