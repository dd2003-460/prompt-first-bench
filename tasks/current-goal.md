# Goal: RV3G6-o3-claim-rejudge-scaffold — claim 级独立重判的仓库内闭环骨架（schema + assert + 采样清单）

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选 RV3G6-o3-claim-rejudge 的仓库内可执行切片）
> 依据：o3-claim-list.md §4.4「在独立重判完成前，本清单只定义判据、不产生任何新的 h 值」+ §5.2 U1（unverified，禁 subagent → arena 通道）。原 goal 的执行主体（fresh-context judge 盲读 248 cell）依赖外部通道（arena 会话），当前不可达——同 r136 kappa-receipt / r140 crossdomain 先例：**执行体 blocked-on-external，但 schema 预注册 + 消费侧 assert + 采样清单属纯仓库内工作，先行落盘**。

## 【目标】
为 claim 级独立重判落三件仓库内交付物（全部新文件，冻结面零修改）：
1. `bench/rubric-v3/ablation/rejudge/judge-protocol-batch1.md` — 判者协议 v1：blind-packet 结构（每 cell 只见 run 原文 + 对应行 claim 文本，不见 gold-tree 全文/hit-matrix 现值/他判者结论，§4.1 独立性定义的机判化）、输入输出 schema（JSON 字段集 byte-stable）、§4.2 聚合规则引用、κ 条目层门禁顺序引用（§4.3：先 κ 后聚合）、S2 限定语叠加声明（§5.1）。
2. `bench/rubric-v3/ablation/rejudge/sample-plan.json` — 采样清单：全量 248 cell 枚举（run×node 完整覆盖，无抽样）+ 优先级分层（P0 = h_id=0 的 150 cell，FM-2 漏判方向优先；P1 = h_id=1 的 98 cell）+ 切片定义（gold strict 40 cell 标记）——供未来 judge 批次按 P0→P1 顺序消费。
3. `bench/rubric-v3/ablation/scripts/assert-o3-claim-rejudge.py` — 消费侧断言（三分支，byte-stable 于 docstring）：rejudge 结果 JSON 缺失 → SIGNAL blocked-on-external + exit 0（常态，不伪造转绿）；schema 违例 → ERROR fail-loud exit 2；数据齐备 → 复算 M1/M2 实际读数（§3 口径：cell 级一致率 + run 级聚合一致率 + gold strict 切片）与 1.0 identity 锚点的偏离量逐格报告 + 防泄漏检查（judge evidence 不得含 gold-tree 数值 token 之外的越界内容——沿用 assert-o3-claim-list.py 黑名单机制思路）+ verdict exit 0/1。

**范围定位**：纯仓库内推导（协议文字化自 o3-claim-list §2/§3/§4 + 脚本实现 + 变异测试），零外部依赖。judge 实际执行导出 queue 候选（arena 通道到来后零改动接入，同 r140 模式）。

## 【阶段】
01 分解 → 02 研究（o3-claim-list §2-§5 + assert-o3-claim-list.py 既有机制精读）→ 02.5 交叉核对（hit-matrix 分布 vs §3.2 注记一致性）→ 03 行动分解 → 04 执行验证（三件落盘 + 实跑 + 变异测试 ≥3 场景）→ 04.5 反方复核

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 协议参考（只读）：`bench/rubric-v3/o3-claim-list.md`（§2 claim 清单 / §3 M1-M2 口径 / §4 多判者协议 / §5.1 S2 限定语）
- 事实源（只读冻结）：`ablation/hit-matrix.json`（248 cell h 值）/ `ablation/gold-tree.md`（31 节点）
- 脚本参考（只读）：`ablation/scripts/assert-o3-claim-list.py`（防泄漏黑名单机制）/ `assert-kappa-receipt.py`（schema 预注册 + 三分支写法）/ `assert-goldrank-crossdomain.py`（SIGNAL blocked-on-external 先例）

## 【验收标准】
- [ ] 三件交付物落盘（judge-protocol-batch1.md / sample-plan.json / assert-o3-claim-rejudge.py）
- [ ] assert 脚本当前 ablation 面实跑 = SIGNAL blocked-on-external + exit 0
- [ ] schema 预注册（输入 JSON 最小字段集 + 判定语义 + exit code 约定）byte-stable 于脚本 docstring
- [ ] sample-plan.json 与 hit-matrix 冻结数据零 mismatch（248 cell 全覆盖 / P0=150 / P1=98 / gold strict=40，机算比对）
- [ ] 变异测试 ≥3 场景实证分支可达：伪造 rejudge 结果（部分 cell 翻转）→ M1/M2 偏离量正确计算路径 / schema 违例 → exit 2 fail-loud / 缺文件 → SIGNAL exit 0
- [ ] 冻结数据零修改（git status 验证：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* 零 diff）
- [ ] 04.5 verdict pass；queue 更新（RV3G6-o3-claim-rejudge 标注仓库内骨架已完成 + 剩余 = judge 实际执行仍 blocked-on-external + 追加新候选）

## 【失败降级】
- 若 o3-claim-list §4 协议存在未文字化的歧义（如 κ 计算的具体公式未在冻结件中定义）→ 登记边界，协议文件只引用不发明，歧义项显式标 UNRESOLVED 并导出裁定候选
- 若防泄漏检查与 assert-o3-claim-list.py 黑名单机制不可复用（作用对象不同）→ 独立实现最小检查（evidence ⊆ run 原文子串），不强行统一