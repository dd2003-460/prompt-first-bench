# T8c 预注册（token-matched 对照 · 三歧义消解后）

# origin: ai · 2026-11-25 · 判据先 commit 再跑数据（预注册纪律）

> 取代并扩展 `prereg_t8c.md`（保留其 token-matched A' 臂 + power 前置思想，
> 补齐三歧义消解后的具体判据、power 结论、决策规则）。
> 本文件在 T8c 数据产生前 commit；跑数后只读不改（post-hoc 修订另开文件）。

## 0. 假设与指标

**H1（备择）**：在 token 预算匹配（两臂同为 24576 completion tokens）且题面无歧义（三歧义已消解）的条件下，
pfb 六阶段流程（Arm B'）在 **correctness** 上优于直接求解（Arm A'）。

**H0（原假设）**：两臂 correctness 无差异（p_B' = p_A'）。

**主指标 = correctness（三型判别）**，不是 coverage：
- 每样本一个标签 ∈ {A1, A2, A3, indeterminate}，由 J1 机械判别器
  （`correctness_layer_v0.py`，commits 92aa24a76→fb60263ac，selftest 11/11，无 LLM）给出。
  三型定义（`research/correctness-layer-design.md` §0/§3，①类）：
  - **A1 候选构建断点**：winner 卡型（3090）从未进入候选集（P_A1 = 1−C ≥ 0.7）。
  - **A2 候选集粒度断点**：3090 进了候选集，但 winner 配置（4×3090）从未被构造/评估（C2BP）。
  - **A3 排序/权重断点**：4×3090 被完整评估但排序垫底/未被选中（P_A3 = E1·R_low ≥ 0.5）。
  - **indeterminate**：都不命中——**含结论正确的情形**（winner 被评估且被选中时 R_low=0 → 不命中 A3）。
- **correctness 得分**：`score = 1[indeterminate] + 0[A1/A2/A3]`（三型=断点=错，indeterminate=未检出断点=对/无法判定）。
  注意 indeterminate 是「未检出断点」而非「确认正确」——报告时标注此口径，不夸大为 accuracy。
- **为什么不用 coverage**（已证陷阱）：J2 存量 17 条 Pearson(cov, CORR)=0.462（互补非冗余）；
  cov 最高样本 S5=0.389 恰是 A2 断点样本；cov 均值按 verdict 单调 A1 0.179 < A2 0.259 < A3 0.278
  （`research/joint-scores-20261125.md`，①类）——coverage 高 ≠ 结论对。

**次指标 = coverage（必要条件检查）**：judge_v1 cov 分数（frozen f6072397f）照算，
但只用于「B' 是否覆盖了 gold 结构」的必要条件核对（cov 低则 correctness 高分存疑），不进主判据。

## 1. token-matched 对照设计

**两臂同 token 预算 = 24576 completion tokens**（B' 臂 6 阶段 × 4096 的天然上限）。

**基线来源（T8b 实测，`raw_outputs_t8b.json` meta + usage，①类本轮读）**：
- Arm A（直接求解，max 16384）：3 run completion tokens = 7015 / 13276 / 12819，
  均值 11037，全部自然 stop（未撞顶）。
- Arm B（六阶段，6×4096）：3 run 总 tokens = 23645 / 21466 / 22779，
  均值 22630，cap 利用率 87-96%（撞顶 2/3：B1/B2 final finish=length）。

**取哪条 run 做基线**：取 **B 臂均值 22630** 向上取整到阶段对齐值 **24576**（=6×4096），
而不是 A 臂均值 11037——理由：① token-matched 的意义是「给直接求解臂同样的 token 预算」，
预算上限由 B 臂结构决定（6 阶段 × 4096 是 harness 的硬结构）；② 若按 A 臂均值 11037 设预算，
B 臂 6 阶段每阶段只有 ~1856 token，01 阶段连分解都写不完（T8a 已证 4096 截断 confound），
对照退化为「双截断」无信息量。

**两臂预算分配**：
- Arm A'（直接求解）：单次调用 `max_tokens=24576`。T8b A 臂自然收尾在 7K-13K，
  24576 下预期仍自然 stop（不截断）；若 stop 后实际用量 ≪ 24576，属正常（预算是上限不是配额），
  报告里同时记「预算」与「实际用量」。
- Arm B'（六阶段）：每阶段 `max_tokens=4096`，总预算 24576（同 T8b B 臂结构）。

**匹配容差**：
- **预算层面（硬）**：两臂名义预算严格相等 = 24576，无容差（这是设计的定义）。
- **实际用量层面（软，只报告不判死刑）**：若 A' 实际用量均值 < B' 实际用量均值 × 0.5
  （即直接求解臂远未花完预算），报告中必须标注「预算匹配但用量失衡」，
  此时主判据（§3）照常执行，但结论置信度降一档（token 预算相等 ≠ token 用量相等，
  余量本身是流程差异的一部分，不强行消除）。
- **截断处理**：任一臂样本 finish_reason=length（撞顶截断）→ 该样本主指标判
  **indeterminate（截断）**，单独计数，不进三型分布比较（截断样本的 correctness 不可判）。
  若某臂截断样本 > 50%，该臂数据作废重跑（预算 24576 下预期不发生；T8b B 臂撞顶 2/3 是
  24576 预算内的阶段分配问题，B' 沿用同结构，风险已知并接受——截断样本按上条处理）。

## 2. 样本量与 power analysis

<!-- SEC:power -->

## 3. 判据（可机械执行 · 先 commit 再跑）

<!-- SEC:criterion -->

## 4. 决策规则（smoke → 扩样，pre-commit）

<!-- SEC:decision -->
