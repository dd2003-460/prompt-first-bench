# SM 修改日志（T53 D2 · 每次改目标函数/状态转移的原因 + 前后对比）

> origin: ai (T53-D2, 成璐要求"所有相关错误、修改路径放在项目里")
> 格式：日期 / 改了什么 / 为什么 / 证据。append-only，不删历史条目。

---

## 2026-11-11 r1 — S_α recall 型 → F_β 型（necessary 过滤接入）

**改了什么**（`experiments/stage-ablation/s5_state_machine.py`）：
1. `ObjectiveConfig` 加 `fbeta_beta=0.5`、`stop_criterion="necessary"`。
2. 新增 `judge_necessary(claim, parent_claims, confirmed, cfg)`：LLM 二元裁决该节点是否引入父 claim/已确认事实中不存在的新变量、新约束或新可检索事实；失败保守返回 False（宁可少拆不多拆）。
3. 主循环 DECOMPOSE 后、进树前：每个候选节点过 necessary 裁决，不通过直接丢弃并计入 `dropped_redundant`。
4. J_stop 判据从纯 n-gram gain streak 切到 necessary 饱和 streak（`stop_criterion="gain"` 可回退旧行为做消融对照）。

**为什么**：v17 的 Goodhart 根因是 S_α = Σ[n·ln(kₙ)+α·kₙ·ln(n)] 对节点数单调增、只奖"覆盖"不罚"多余"→ 模型堆 1930 个同义变体刷分。T-PR-15 survey（Lead 验收 commit `76e64c4e`）给出修法依据：Ryu et al. 2026（arXiv:2610.33512）——recall 型奖励很快饱和而 precision 持续降，改成 F_β 后回答长度降 2.6×、胜率 10.6%→68.0%。本改动就是给 decomp 侧加 precision 项：不引入新信息的节点不再进树。

**预期 vs v17**：GPU 题节点数 1930 → 几十~百级（AC1 ≤200），正交维度保持 6-8。

**验证状态**：smoke run `proc_aeb63c95fd0d`（gpu 题，全链路含真实检索+核验+necessary 判定），日志 `runs-s5-sm-gpu-fbeta.log`。结果出来填下方。

**风险/已知局限**：
- necessary 判定本身也是 LLM 裁决（文字代理），理论上可被"措辞新颖但信息冗余"的节点骗过——n-gram dedup（0.7 阈值）仍在前一道挡着，双层防线。
- 每候选节点一次额外 LLM 调用，成本上升；若 smoke 显示太慢，下一版改成批量判定（一次 prompt 判一批）。

## 2026-11-11 r2 — 核验不再豁免 knowledge/given（AC3 修复）

**改了什么**：`_verify_batch` 原来对 source=given/knowledge 直接标 verified + evidence="模型先验/题面给定"，只有 search 节点走 LLM 核验。r1 smoke 暴露：145/170 节点是这种免检 verified，evidence 全是占位文本——AC3（≥90% 节点有真实 evidence）名存实亡。现在所有节点都过 `verify_node`（LLM 逻辑+外部核验），只是 given/knowledge 不触发联网检索。`--no-verify` 模式也改成"跳过检索但过核验"。

**为什么**：AC3 的意图是"每个进树的节点都被核验过"，不是"每个节点都有个 status 字段"。v17 的诊断里"knowledge 节点未抽查"本来就是留的坑，r1 等于把它原样搬过来了。

**代价**：每节点一次 LLM 调用（~2s），单题总时长上升（r1 全链路约 30min → r2 预计 40-60min）。可接受：bench 只有 5-10 题。

**验证状态**：smoke run `proc_4c3b399c9772`（gpu 题），日志 `runs-s5-sm-gpu-fbeta-r2.log`。

## 2026-11-11 r1b — parent_ids 索引 bug 修复

r1 里 `par_claims` 用 `int(id.lstrip("N"))-1` 当列表下标取父节点 claim——id "N81" 会取到第 80 个节点而不是 id 为 N81 的节点，necessary 判定的参照系是错的。改成 `{n.id: n.claim}` 查表。单独测了 judge_necessary：新变量节点 True / 同义变体 False，裁决方向正确（各 ~1.5s/次）。


## 2026-11-11 r3 — 可靠性三件套（E6 静默死修复）

**背景**：r2 smoke 再次静默死在 L1 之后（log 停在 `[SM] L1: 25 nodes`，无 Traceback 无 EXIT）。单发/连发 verify_node 前台全过、8787 proxy 活着——说明不是某条 claim 触发异常，是后台长进程 + LLM 调用组合下的环境性死亡。这正是成璐点名的"微信会断，状态机要可靠"。

**改了什么**（commit 见下）：
1. **每轮 checkpoint 落盘**：`run()` 每轮结束写 `checkpoints/sm-{qid}-r{rnd}.json`（完整节点树 + 计数器）。死了不丢已完成的轮次。
2. **`--resume <ckpt>`**：CLI 支持从 checkpoint 加载继续跑，NodeRecord 反序列化已验证（假 ckpt 测试通过）。
3. **call_llm retries 1→2**：proxy 抖动多扛一次（timeout 本来就是 600s，不动）。

**没改的**：启动方式仍建议走 `scripts/launch.sh`（tee + EXIT code），这样即使再死，log 最后一行有 exit code，不再是 4 行无头尸体。

**待验证**：用 launch.sh 起 r2 重跑（proc_0df18a438c91 还在前台复现 _verify_batch 25 节点，结果出来对照）。若 launch.sh 下仍静默死且 EXIT≠0 → 死因可定位；若 EXIT=0 但 log 截断 → 是日志层问题不是进程问题。
