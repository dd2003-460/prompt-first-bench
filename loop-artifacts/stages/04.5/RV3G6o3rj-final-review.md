# 04.5 — RV3G6-o3-claim-rejudge-scaffold · 反方复核（八攻击）

> goal: claim 级独立重判的仓库内闭环骨架 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30
> 方法：从反方立场逐条攻击交付物；每条给出「驳 / 成立已修 / 成立登记」三态处置。数字层全部独立重算（不复用 04 日志结论）。

## 攻击 1 — 「变相产生 h 值」（预注册规则 1 红线）

**攻击**：sample-plan.json 的 `h_id_frozen` 字段 + P0/P1 分层是否构成对 (run, node) 的新判定？protocol 是否偷偷带了答案倾向？

**核查**：`h_id_frozen` 逐格 == 冻结 hit-matrix.json 现值（A1 独立复核 set 相等 + 逐格比对通过）——是只读镜像非新判定；P0/P1 标签由该镜像机械派生。protocol 全文 grep 无任何具体 cell 的 yes/no 判断（示例全为占位符）。assert 数据齐备分支只消费外部落盘结果，不代判。M1/M2 变异 fixture 中的 flip 构造是**测试输入**（测毕删除，git status 确认无残留），不是交付物内容。

**判定**：❌ 驳。零 h 值红线成立。

## 攻击 2 — 「evidence 子串检查空转或误杀」

**攻击**：(a) 子串检查能否被绕过（如 evidence 取 run 文件中与 claim 无关的任意句子 → 防编造形同虚设）？(b) 真实 judge 引用时是否必然大量误报？

**核查**：(a) 属实但属**协议语义边界非缺陷**——子串检查只保证「evidence 出自该 run」（防跨 run 张冠李戴 + 防凭空编造），**不保证「evidence 支持该 claim」**（语义相关性不可机判，同 r136 finding #15「打分过程合规性不可机判」先例）。protocol §3 硬约束 3 措辞为「防编造 evidence」未夸大为「防滥用」，04 负面结果 2 已声明从严方向。若未来要加「evidence 与 claim 相关」检查 = 需要 LLM 语义判断 = 超出机判边界，应导出而非暗改。(b) 误报风险：TASK-ablation 原协议本就要求「原样引用真实句子」，子串检查是该要求的直接机判化，未额外加严到「句子边界」级别（连续子串可跨标点，比整句匹配更宽松）——实际执行中误报率应低于直觉预期。

**判定**：⚠️ 部分成立——(a) 的能力边界已在 protocol/04 双向如实声明（非隐藏），无需修改；(b) 驳。登记为已知边界（见末尾边界清单 B1）。

## 攻击 3 — 「M1/M2 口径与 o3-claim-list §3.1 不一致」

**攻击**：assert 复算公式是否照抄定义式？gold strict 切片节点清单是否与冻结件同源？

**核查**：独立重算对照——§3.1 M1 = |{(r,v): h_claim==h_id}| / |V_judgeable|，V_judgeable = 全部 31 节点（零 NA）→ 分母 248 ✓ assert 用 248 常量（与 sample-plan total 断言联动）；M1 gold strict 限 5 节点 × 8 = 40 ✓；M2 = per-run 向量完全一致才计 1 ✓ assert 用 `per_run_all_agree` 布尔累积，语义等价。GOLD_STRICT 清单 = N-2.1/N-3.2.2/N-2/N-4/N-1.3，与 assert-gmr-recompute.py L13 / goldrank-threshold-proof L2.1 同源 ✓。M2 变异场景手工核算（8 run 各含 ≥1 flip → 0/8）✓。

**判定**：❌ 驳。口径零偏差。

## 攻击 4 — 「偏离不 FAIL 的语义预注册是自我豁免漏洞」

**攻击**：预注册规则 4 说「M1/M2 偏离本身不是 FAIL 条件」——这是否让 assert 在数据齐备后永远 exit 0，失去门禁功能？

**核查**：门禁功能已由 ② schema 分支承担（exit 2 拦截全部可信性错误：覆盖缺口/非二值/evidence 编造/h=0 带 evidence/固定字段漂移——M3a-c 实证可达）。③ 分支的职责是**报告**（偏离表是产出物不是异常）。类比：crossdomain 的 (b) FAIL 针对的是「过线集合 tie-sensitive」这一特定失效模式，本脚本对应的特定失效模式 = 「结果不可信」，已被 ② 封闭。若未来发现新的可信性维度（如 judge_family 与 judge_id 矛盾），扩展 ② 即可，③ 的 exit 0 语义不变。**残余风险**：schema 合法但整体系统性偏置（如同族判者集体漏判同一类 cell）无法被任何单批 assert 检出——这是 S2 限定语的存在理由，protocol §5 已叠加声明，非脚本职责。

**判定**：❌ 驳（职责划分自洽）；系统性偏置盲区登记为 B2（S2 范畴，已有声明覆盖）。

## 攻击 5 — 「S2 byte-exact 引用实为伪验证」

**攻击**：04 声称 difflib 逐字比对 = True——提取窗口是否正确？是否比对了错误段落？

**核查**：现场重跑提取逻辑（o3-claim-list §5.1 blockquote 起点「> 本文引用的 O3 构念效度数字」到下一空行；protocol 同锚点同窗口）→ 再次比对 = True，且目视两段均为完整 S2 限定语（含 (i)(ii) 双闭环条件）。锚点字符串唯一性：`grep -c '本文引用的 O3 构念效度数字'` 两文件各 = 1，无歧义窗口。

**判定**：❌ 驳。byte-exact 真实有效。

## 攻击 6 — 「sample-plan 优先级设计引入采样偏差」

**攻击**：P0 优先执行 h_id=0 cell——若 judge 批次因成本只做完 P0 就停，M1 分母只剩 150，与 §3.1 全量口径矛盾，是否诱导截断报告？

**核查**：sample-plan `coverage_rule` 字段明文「full-enumeration-no-sampling: 全部 248 cell 无抽样；priority 只定执行顺序不定统计口径」；assert ② 分支强制 cells 覆盖 == 248 全集（缺一即 exit 2）——**部分完成的批次根本无法通过 assert**，不存在「只做 P0 就出报告」的路径。priority 仅优化通道可用时的成本排序。

**判定**：❌ 驳。截断路径被 schema 封闭。

## 攻击 7 — 「exit code 语义与先例冲突导致自动化误接」

**攻击**：r136 receipt 缺失 = FAIL exit 1，本脚本缺失 = SIGNAL exit 0——未来自动化门禁若统一按「非 0 = 异常」接入，会漏掉 rejudge 未执行状态吗？

**核查**：两脚本语义差异有实质依据（02.5 X3：负向事实 vs 中性状态），且 batch2-closure queue 项已登记全局约定「须按 stdout [SIGNAL] 前缀分流，不能只看 exit code」。本脚本 SIGNAL 行携带 `[SIGNAL]` 前缀 ✓（实跑输出确认）。**残余**：该分流义务依赖消费方遵守约定，脚本自身无法强制——属流程边界非代码缺陷。

**判定**：❌ 驳（机制已就位）；消费方义务登记为 B3（随 batch2-closure 跟踪）。

## 攻击 8 — 「U-K1 κ 缺口被静默绕过」

**攻击**：protocol 预留 kappa_receipt_ref 但 assert 不复核数值——单判者批次传 null 即可永久跳过 κ 门禁，§4.3「κ 低于下限作废重判」是否被架空？

**核查**：§4.3 的 κ 门禁对象是**多判者聚合前的条目层质检**——单判者批次不存在 inter-rater agreement 可算（κ 定义域为空），null 是正确值非逃逸。多判者阶段（≥2 批次落盘）聚合时必须走 κ 门禁，届时 kappa_receipt_ref 指向 kappa-receipt.json（其存在性/格式由 assert-kappa-receipt.py 独立把关，数值门槛 0.6 由该脚本执行）。本脚本「不复核数值」避免双源漂移（谁算 κ 以 receipt 为准），不是绕过。**真缺口** = κ 公式本身未裁定（U-K1），已导出 queue 候选，protocol §4 显式标 UNRESOLVED 未装懂。

**判定**：❌ 驳（单判者 null 语义正确）；公式缺口本身是真实未决项，已按失败降级条款登记并导出（B4）。

---

## verdict

**pass** — 8 攻击：6 驳 / 2 部分成立（均已在 protocol + 04 负面结果双向如实声明，无需返工修改）。数字层独立重算零 mismatch（M1/M2 变异核算 + S2 重比对 + sample-plan 计数三重验）。冻结面零修改维持（git status 复核）。

## 边界登记（随收口进 queue 注记）

| # | 边界 | 归属 |
|---|------|------|
| B1 | evidence 子串检查只防编造不防滥用（语义相关性不可机判） | 已知能力边界，protocol §3 已声明 |
| B2 | 单批 assert 无法检出系统性同源偏置 | S2 范畴，protocol §5 限定语覆盖 |
| B3 | [SIGNAL] 前缀分流义务依赖消费方 | 随 RV3G3-batch2-arrival-closure 全局约定跟踪 |
| B4 | U-K1 κ 公式未裁定 | 导出 queue 新候选（裁定型，~2 回合） |