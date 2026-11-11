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