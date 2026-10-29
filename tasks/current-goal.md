# Goal: R5.2-packet-audit — 原 r4 evidence packet 单行摘要全字段审计

> 创建：2026-10-30 · ralph loop runner（goal-queue 新导出候选队首，R5.2-evidence-packet 04.5 W2/R6 导出）
> 依据：`loop-artifacts/stages/04.5/R5.2-review.md` R6 攻击裁决 + `tasks/goal-queue.md` 候选行
> 注：`sop/goal-template.md` 在仓库内不存在（grep 全仓仅被引用），本文件按 runner 协议 §A2 五字段格式落盘。

## 【目标】
R5.2 只修了 4 项 |Δ|>15 分歧点字段（M2/M5），原 r4 packet（`r4/independent-scoring-deepseek.json` evidence_packet 字段，单行摘要）的**其余摘要值未逐项复核**——虽未产生 |Δ|>15 分歧（scorer-agreement-r1.json disagreements 只有 4 项），但可能存在隐性错配（X2 "run3 任务书25行"张冠李戴即此类）。本 goal 交付：
1. **全字段审计表**（`bench/self-opt-tester/r5/packet-audit-r4-v1.md`）：把原 packet 单行摘要拆成原子事实断言（per-run 逐条），每条对照原始证据（pfb git 对象 / workspace run 工件）核验，判定 verdict = confirmed / mismatch / unverified；
2. **机判脚本**（`bench/self-opt-tester/r5/assert-packet-audit.py`）：对可机械核验的断言（行数 wc -l、锚点数 JSON 字段、降级条目数、token 数值 grep）自动比对，exit 0 = 全部无 mismatch；
3. **mismatch 处置**：发现的错配登记 X 系列矛盾（追加到 02.5 工件或审计表内），若影响已冻结分数 → 写 APPROVALS.md 不静默改分（分数冻结纪律，沿用 R5.2 先例）。

## 【阶段】
bench 度量基础设施修复（R5.2 的收口补强）。前置事实已定：packet v2 已交付且对称性断言 67/0 通过（r102, baff4b3）；本 goal 审计对象是**原 v1 单行摘要**（历史输入面），不改任何已有分数值与 packet v2。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口；§4 loop 六阶段速览）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义，逐段读）
- `bench/self-opt-tester/bench.md`（指标定义表 M1-M7 固定口径 + R5.1/R5.2 节）
- `bench/self-opt-tester/r4/independent-scoring-deepseek.json`（**审计对象** = evidence_packet 字段 + key_reasons 中的数值主张）
- `bench/self-opt-tester/r5/evidence-packet-r4-v2.json`（R5.2 已核验字段，避免重复劳动——P1/P2 直接引用其结论）
- run 原始证据：WS `projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3/{run1,run2,run3}/` + pfb `bench/self-opt-tester/run2-arena/` + `r4/token-split.json` + `gate-evidence-breakpoint-ABC.md`

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带 goal 短名前缀 `R5.2audit-*`
2. 01：原 packet 单行摘要拆解为原子断言清单（预计 ~12-15 条：run1×4 / run2×4 / run3×4 + 跨 run 定义句），标注每条的核验方法（wc -l / JSON 字段 / grep 原文 / 不可核验）
3. 02：web-llm 强制步骤执行并留回执（预期三 provider 仍 error → 记录失败继续）；每条断言的证据定位（文件路径 + 原文摘录 + 观察时间戳）
4. 02.5：矛盾登记（X 系列续号，从 X4 起）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent
6. 04：审计表 md + 断言脚本落盘；脚本 exit 0（可机判断言全 confirmed，无 mismatch）；不可机判断言人工核验留痕
7. 04.5：反方复核 verdict + repair_stage 落 `stages/04.5/`
8. bench.md 追加 R5.2-audit 小节（审计结果一句话 + mismatch 数 + 对第三打分器的影响说明）
9. commit + push 到分支 `ralph/r5.2-packet-audit` + ls-remote 验证落点

## 【失败降级】
- web-llm 三 provider 均不可用 → 按 02 规则记录失败回执后继续本地一手证据提取，conf 相应降档，不阻塞
- 某断言原始证据不可达（如 arena 侧时长 14m27s 的原始计时来源）→ verdict = unverified + 原因，禁升级为 confirmed/mismatch
- 发现 mismatch 且牵涉已冻结分数 → 登记 + 写 APPROVALS.md 提请成璐裁决，不静默改分（分数冻结纪律）
- arena 通道不可用 → 本 goal 即 Lead 本地自答（conf-0.2 标注，同 T7.1/T8r1 先例）