# Goal: R5.2-evidence-packet — evidence packet 模板固化 M2 行数 + M5 轮数字段

> 创建：2026-10-30 · ralph loop runner（goal-queue 队首）
> 依据：`bench/self-opt-tester/bench.md`「R5.1 打分器间一致性」节 R5.2 建议 + `loop-artifacts/stages/04.5/R5.1-review.md` W1/W2 风险项
> 注：`sop/goal-template.md` 在仓库内不存在（grep 全仓仅被引用），本文件按 runner 协议 §A2 五字段格式落盘。

## 【目标】
消除 R5.1 定位的**结构性分歧源**：r4 给 DeepSeek 的 evidence packet 缺「任务书行数（M2）」与「达 conf≥0.7 所需轮数（M5）」两个字段，导致第二打分器（Claude Code）与第一打分器（DeepSeek）在 M2/M5 上 |Δ|>15 共 4 项分歧（run1/run2 M2 各 −50、run1/run3 M5 各 −30/−35）。本 goal 交付：
1. **evidence packet 模板 v2**（`bench/self-opt-tester/r5/evidence-packet-template-v2.md`）：固化 M2 行数 + M5 轮数字段为必填项，含字段 schema + 填写规则 + 防虚构约束；
2. **r4 三 run 补齐版 packet**（`bench/self-opt-tester/r5/evidence-packet-r4-v2.json`）：按 v2 模板把 run1/run2/run3 的 M2 行数与 M5 轮数从原始证据一手提取填入，每条带来源路径+时间戳；
3. **可重放性验证**：用补齐后的 packet 重算两打分器分歧预期——证明 4 项 |Δ|>15 分歧中 M2×2 + M5×2 全部由输入不对称造成（非判断尺度差异），给出"补齐后预期 κ 变化方向"的可验证断言（不虚构新打分，只断言输入对称性）。

## 【阶段】
bench 度量基础设施修复（已知缺陷 #5 的后续闭环）。前置事实已定：R5.1 已完成（κ=0.55 moderate，4 项分歧全归因于 packet 缺字段，见 scorer-agreement-r1.json systematic_pattern + R5.1-review.md A4/H2）。本 goal 不改任何已有分数值，只修输入面。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口；§4 loop 六阶段速览）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义，逐段读）
- `bench/self-opt-tester/bench.md`（指标定义表 M1-M7 固定口径 + R5.1 节）
- `bench/self-opt-tester/r4/independent-scoring-deepseek.json`（原 packet 内容 = 其 evidence_packet 字段 + key_reasons）
- `bench/self-opt-tester/r5/scorer-agreement-r1.json`（4 项分歧对照 + systematic_pattern）
- run 原始证据（workspace `projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3/{run1,run2,run3}/` + pfb `bench/self-opt-tester/run2-arena/` + `r4/token-split.json`）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带 goal 短名前缀 `R5.2-*`
2. 01：因素分解 + 字段 schema 草案 + 空缺清单（哪些字段可从现有证据一手提取、哪些不可得需降级标注）
3. 02：每个待填字段的原始证据定位（文件路径 + 原文摘录 + 观察时间戳）；web-llm 强制步骤执行并留回执（预期三 provider 仍 error → 记录失败继续）
4. 02.5：矛盾登记（如 run1 任务书行数的两处记载是否一致）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent
6. 04：模板 v2 + packet v2 JSON 落盘且 json.load 通过；字段完整性断言脚本 exit 0（9 个必填字段 × 3 run 全非空或有显式 null+原因）
7. 04.5：反方复核 verdict + repair_stage 落 `stages/04.5/`
8. bench.md 追加 R5.2 节（模板位置 + 补齐结果 + 对第三打分器的使用说明）
9. commit + push 到分支 `ralph/r5.2-evidence-packet` + ls-remote 验证落点

## 【失败降级】
- web-llm 三 provider 均不可用 → 按 02 规则记录失败回执后继续本地一手证据提取，conf 相应降档，不阻塞
- 某 run 的 M5 轮数在原始证据中无直接记载 → 取最接近的间接证据（loop-state 状态/conf 标注）+ 显式标注"间接推断"，禁虚构精确轮数
- run3 任务书未独立落盘（派发消息文本）→ M2 行数标 null + 原因（沿用 R5.1 A6 先例：≤200 口径下方向确定但精度缺失）
- arena 通道不可用 → 本 goal 即 Lead 本地自答（conf-0.2 标注，同 T7.1/T8r1 先例）