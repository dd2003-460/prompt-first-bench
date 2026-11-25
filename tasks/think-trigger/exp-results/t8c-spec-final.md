# T8c 题面终稿（token-matched 对照 · 三歧义消解版）

# origin: ai · 2026-11-25 · T8c 硬前置产出（不跑数据，只产判据）

> 定位：T8c 是 token-matched 对照（多阶段 vs 直接求解，同 token 预算）。
> 本文件消解 T8b 暴露的三处题面歧义（① 上下文 ② 候选集 ③ c_pass 口径），
> 使两臂在同一题面上求解，correctness 探针才能区分「模型错」与「题面分叉」。
> 每个数字带来源标注：①文件路径 / ②推导 / ③[待核验]。

## 0. 三歧义消解结论（速览）

| 歧义 | T8b 题面 | T8c 终稿 | 依据（一句话） |
|------|---------|---------|--------------|
| ① 上下文 | ≥32K 容量下限 | **64K 定值**（KV 按 64K 计） | gold 锚点 @64K（gold-tree.md L123）+ 本地统计 32K/64K 均为松约束（construct-mismatch 台账 11-25 条目） |
| ② 候选集 | 自行搜索 | **定死 2 卡**：3090、V100（规格 ①类齐全） | 4090 敏感性已证候选集含 4090 则 winner 翻转（oracle `check_4090_flip()` 实跑）；定死后 oracle 实跑 winner=3090×4/W4/n=2 ✅ |
| ③ 目标函数 | 性价比最优（宽） | **c_pass ¢/task 最小化**（公式+参数全列，与 calc.py 同构） | gold 树 N-0 口径；calc.py 4/4 验收锚已过（本轮实跑） |

附加消解（T8b 正向对照暴露的第 4 处）：**并发约定 n = n_cards//2**（2 卡/流，部署惯例非自由变量）
写入题面——否则模型按 free-n 会错选 n=3（t8b_positive_control 实跑验证，oracle commit d41ab1bf7 预言）。

## 1. 歧义① 消解：上下文长度定值 64K

**终稿写法**：「上下文窗口定值 64K tokens（KV 缓存按 64K 计，27B 单流 KV≈24.7GB）」——不再写 '≥32K 下限'。

依据链（全部 ①类，本轮从实际文件读）：
1. **gold 锚点 @64K**：`bench/rubric-v3/ablation/gold-tree.md` L123「token 画像…@64K」；
   `bench/rubric-v3/tasks/T0-local-27b/reference/calc.py` L50 `KV_PER_STREAM = 24.7 GB/流 @64K`。
   gold 的 N-5.2 带宽准入下限 774/1034/1574 GB/s 由 @64K 画像推导（=20×(W+24.7)，三点残差 0.000，
   t8b-smoke-report.md §3.1 已验证 6/6 gold 判断吻合）。
2. **32K/64K 均为松约束**：`modules/B-pipeline-ablation/research/construct-mismatch-20261123.md`
   11-25 条目——本地统计（14056 user 轮次/2007 session，字符÷2 粗估 token，未扣压缩=上界）：
   P10≈38.5K，P50≫64K，≥32K 占 91.3%，≥64K 占 87.3%。→ 取 64K 不引入额外可行性约束，
   取值任意但必须自洽；自洽对象 = gold 锚点。
3. **T8b 的教训**：题面 '≥32K 下限' 被 6/6 输出取下限（KV@32K≈12.35GB），带宽门推导前提
   （64K 画像 + 20 tok/s 目标）不在题面内 → N-5.2 门 0/6 实例化，correctness 0/6
   （t8b-smoke-report.md §3.1/§3.2，归因 conf 0.8）。

**对两臂的约束**：KV 计算必须 @64K（24.7GB/流，来源 calc.py L50 ①类）；
带宽准入下限随之固定为 W4=774 / W8=1034 / W16=1574 GB/s（②推导：20×(W_bytes+24.7)，
W_bytes∈{14,27,54} 来自 calc.py L49 ①类；r=20 tok/s 即 ④ 解码吞吐目标，见 §3）。

## 2. 歧义② 消解：候选集显式定死

<!-- SEC:candset -->

## 3. 歧义③ 消解：c_pass 口径（公式 + 参数 + 同构性）

<!-- SEC:cpass -->

## 4. T8c 题面正文（冻结版，两臂共用）

<!-- SEC:prompt -->

## 5. 执行清单（跑 T8c 前 checklist）

<!-- SEC:checklist -->
