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

**终稿写法**：候选集定死为 **2 卡：RTX 3090（24GB）、V100 SXM2（32GB）**，可单机 2-4 卡，不得自行扩大或替换。

**为什么是这 2 卡**（不是 gold 全候选集 7 类）：
1. **winner 必须可由 ①类规格复算**。oracle（`gold_gpu_oracle.py`，commit d41ab1bf7）的 sweep
   只覆盖 calc.py HARDWARE 里有完整 ①类规格的卡 = 3090 + V100。gold 树其余候选
   （M2Ultra/L40S/A100，gold-tree.md L94 ①类）在 KB 缺 flops/price（null=[待核验]），
   不凭记忆填数（③类风险，oracle docstring 明示）。→ 定死 2 卡 = 定死在「规格可复算」的交集上。
2. **4090 必须排除**（敏感性已证，本轮 oracle 实跑复现）：`check_4090_flip()` →
   4090×4/W4/n=2 = 0.635 < 3090×4/W4/n=2 = 0.681，winner 翻转为 4090（盈亏平衡价 ≈ $1905，
   远高于 KB MSRP $1599 / NE street $1699-1899，`knowledge-base/hardware-staging/rtx-4090.json`
   ①类 conf 0.85）。T8b 题面「自行搜索」让模型自由纳入 4090 → 对照被污染（t8b-smoke-report.md §3.2）。
3. **M2Ultra/L40S/A100 排除**：规格不全（KB `mac-studio-m5-ultra.json`/`l40s.json`/`a100.json`
   ①类但 flops/price 为 null）。它们已被 gold 树 N-5.2 带宽门划掉（M2Ultra 448<774 fail、
   L40S 691<774 fail、A100×1/W16 1548<1574 fail，oracle `check_gold_judgments()` 6/6 实跑吻合），
   不影响 winner；T8c 不测「模型能否复现淘汰推理」，测的是「同预算下流程 vs 直接求解的 correctness」。

**每张卡的 ①类规格来源**（题面直接给出，模型不需自查）：

| 卡 | 显存 | 峰值带宽 | 峰值算力(FP16 non-tensor) | TDP | 单价(题面钉死) | 来源 |
|----|------|---------|--------------------------|-----|--------------|------|
| RTX 3090 | 24GB | 936 GB/s | 71 TFLOPS | 350W | **$1050** | calc.py L33 ①类（gold L4 口径）；KB `knowledge-base/hardware/rtx-3090.json` ①类 conf 0.5 二手价 $1500-2000（与 gold 口径不一致，题面取 gold 口径保 winner 复现） |
| V100 SXM2 | 32GB | 900 GB/s | 125 TFLOPS | 250W | **$2500** | calc.py L36 ①类（规格源 `datacenter-cards.json`；价格原文标 [待核验, 2026 市场价] → 本实验按 ③类假设钉死，见下方脆弱性披露） |

**⚠ 脆弱性披露（必须随题面一起读）**：winner 对 V100 价格假设敏感——本轮实跑（python 二分，
calc.py 同参数）：V100 单价 **< $2033** 时 V100×4/W4/n=2 反超 3090×4/W4/n=2 成为 winner；
V100=$2500（题面值）时 0.761 > 0.681，3090 稳赢。3090 一侧对价格极不敏感（>$5000 才被反超，
远超任何现实价）。→ **T8c 的 correctness 锚点 = 「题面钉死价格下的 winner」**，即
3090×4/W4/n=2；若后续 V100 实价核验（③→①升级）落在 $2033 以下，winner 锚点须重定，
T8c 数据作废重跑。此为已知限制，不掩盖。

**oracle 实跑验证（本轮，命令 `python3 tasks/think-trigger/exp-results/gold_gpu_oracle.py`，exit 0）**：
- winner = **3090×4/W4/n=2** ✅（期望一致）
- c_pass(winner) = 0.681 ≈ 0.679（calc.py 标定值，差 0.3% < 1% 容差）✅
- N-5.2 带宽门对 gold 6 个 pass/fail 判断 6/6 吻合 ✅
- 可行配置排序 top-3：3090×4/W4/n=2 (0.681) < V100×4/W4/n=2 (0.761) < 3090×4/W8/n=2 (0.764)
- 淘汰 5 配置：3090×2/W8、3090×2/W16、3090×3/W16、3090×4/W16（N-5.1 显存门）、V100×2/W16
- 4090 敏感性复现：4090×4/W4/n=2 = 0.635 → 若入候选集 winner 翻转（排除依据，见上）

## 3. 歧义③ 消解：c_pass 口径（公式 + 参数 + 同构性）

**终稿写法**：目标函数 = **最小化 c_pass（¢/task）**，公式与参数全部写进题面（模型不需自查口径）：

```
c_pass = c_hour / ( U × λ_raw × G )        [¢/task]
c_hour = 摊销 + 电费 + 故障                  [$ / 小时, 整机]
摊销   = (gpu_price + HOST_PRICE − gpu_price×RESID) / H_HOURS
电费   = (n_cards×TDP + 300) / 1000 × ELEC
故障   = P_FAIL × gpu_price / H_HOURS
λ_raw  = 3600 / t_task                       [task / 小时]
t_task = t_prefill + t_decode/n              [秒]
t_prefill = PREFILL_FLOPs / (n_cards × TF_peak × MFU × tp_eff)
t_decode  = OUT_TOK × (W_bytes + n×KV) / (n_cards × BW_peak × η_bw × tp_eff)
```

**参数取值（全部 ①类，来源 calc.py L38-50，逐条）**：

| 参数 | 取值 | 来源 |
|------|------|------|
| U（利用率） | 0.35 | calc.py L48 ①类（L5§2 黑盒取中位数） |
| G（通过率） | 0.68 | calc.py L48 ①类 |
| ELEC（电价） | $0.12/kWh | calc.py L48 ①类 |
| MFU | 0.45 | calc.py L48 ①类 |
| η_bw（带宽效率） | 0.80 | calc.py L48 ①类 |
| HOST_PRICE（4 卡主机） | $2000 | calc.py L39 ①类（L4） |
| RESID（残值率） | 0.40 | calc.py L40 ①类（L4 B8） |
| H_HOURS（摊销时长） | 26280 h（3 年） | calc.py L41 ①类（L4） |
| P_FAIL（3 年故障概率） | 0.20 | calc.py L42 ①类（L4 B8） |
| PREFILL_FLOPs | 594 TFLOP | calc.py L43 ①类（L4: 2×27e9×5898） |
| OUT_TOK（输出 token） | 655 | calc.py L44 ①类（L3: decode 655） |
| tp_eff（多卡互联效率） | 0.81 | calc.py L45 ①类（**标定值**：文档标 S-a 未钉数值，0.81 使点值对上 0.679；排名结论不依赖其绝对值——tp_eff 同乘 prefill/decode） |
| W_bytes | W4=14.0 / W8=27.0 / W16=54.0 GB | calc.py L49 ①类（27e9×bits/8） |
| KV（@64K 单流） | 24.7 GB/流 | calc.py L50 ①类（B7「我」口径 46 层/16 KV 头） |
| 卡规格（TF_peak/BW/mem/TDP/price） | 见 §2 表 | calc.py L33/L36 ①类 |

**与 calc.py 的同构性**：题面公式与 `calc.py` 的 `c_pass()`（L53-67）**逐行同构**——
同一公式、同一参数表、同一单位（c_hour 美元/小时 ÷ 吞吐 → 美元/task ×100 → ¢/task）。
模型按题面公式算出的 c_pass 应能对上 oracle 数值（winner 0.681），对不上即可机械判「算术/推导错」。
N-5.2 带宽门与 c_pass 的 decode 项**代数同构**（t8b-smoke-report.md §3.1 已证：
把目标每流速率 r=20 代入 t_decode 分子即得带宽准入下限 20×(W+n×KV)/n_cards），
故题面同时给出：带宽准入下限 W4=774 / W8=1034 / W16=1574 GB/s（每卡有效带宽 = BW_peak×0.80
须 ≥ 每卡需求 20×(W_bytes + n×24.7)/n_cards，一卡一流口径 n=n_cards）。

**验收锚（oracle 实跑，本轮）**：c_pass(3090×4/W4/n=2) = 0.681 ≈ 0.679（calc.py 标定值，
差 0.3%）；六弹性 6/6、prefill:decode=40:60、winner 排名 3090×4/W4/n=2 < 3090×2/W4/n=1
（calc.py `main()` 4/4 验收锚全过，t8b-smoke-report.md §3.1 已记录）。

## 4. T8c 题面正文（冻结版，两臂共用）

两臂共用以下题面（冻结版）。Arm A'（直接求解）= 单次调用喂此题面；Arm B'（六阶段）= 此题面作 01 阶段输入，harness 驱动 01→02→02.5→03→04→04.5（同 T8b `run_exp_t8b.py`）。

```
你要在本地工作站上部署 Qwen3-27B 模型推理。严格按以下约束与成本模型求解
（本题面已给出全部所需数字，不需要也不允许外部查询）：

【硬约束】
1. 上下文窗口定值 64K tokens（KV 缓存按 64K 计，27B 单流 KV ≈ 24.7 GB/流）。
2. 解码吞吐目标：每流 ≥20 tok/s（≈50 ms/token）。不达标的配置直接淘汰（带宽准入门，见下）。
3. 并发约定：n = floor(n_cards / 2)（2 卡/流，部署约定，不是自由优化变量）。
4. 目标函数：最小化 c_pass（每个通过任务的成本，¢/task）。c_pass 最低的配置为最优。

【候选硬件（固定，不得自行扩大或替换）】
  RTX 3090    显存 24 GB   峰值带宽 936 GB/s   峰值算力(FP16 non-tensor) 71 TFLOPS   TDP 350 W   单价 $1050
  V100 SXM2   显存 32 GB   峰值带宽 900 GB/s   峰值算力(FP16 non-tensor) 125 TFLOPS  TDP 250 W   单价 $2500
卡数：单机 2-4 卡。精度：W4/W8/W16 可选（权重体积 W4=14 GB / W8=27 GB / W16=54 GB），
需论证所选精度的质量损失是否可接受。

【两道准入门（不满足即淘汰）】
- 显存门：(W_bytes + n×24.7) / n_cards ≤ 单卡显存。
- 带宽门：每卡有效带宽 = 峰值带宽×0.80 ≥ 每卡需求 20×(W_bytes + n×24.7)/n_cards。
  等价固定阈值（一卡一流口径）：W4 ≥ 774 GB/s，W8 ≥ 1034 GB/s，W16 ≥ 1574 GB/s（峰值带宽口径）。

【c_pass 公式与参数（按此公式计算，勿自改口径）】
  c_pass = c_hour / (U × λ_raw × G) × 100          [¢/task]
  c_hour = 摊销 + 电费 + 故障                        [$ / 小时, 整机]
  摊销   = (gpu_price + 2000 − gpu_price×0.40) / 26280
  电费   = (n_cards×TDP + 300) / 1000 × 0.12
  故障   = 0.20 × gpu_price / 26280
  λ_raw  = 3600 / t_task                            [task/小时]
  t_task = t_prefill + t_decode / n                 [秒]
  t_prefill = 594e12 / (n_cards × TF_peak × 0.45 × 0.81)
  t_decode  = 655 × (W_bytes + n×24.7) / (n_cards × BW_peak × 0.80 × 0.81)
参数含义：U=0.35 利用率；G=0.68 通过率；2000$ 4卡主机；0.40 残值率；26280h 3年摊销；
0.20 三年故障概率；594 TFLOP prefill 算力；655 输出 token 数；0.45 MFU；
0.81 多卡互联效率；0.80 带宽效率；0.12 $/kWh 电价。

【输出要求】
1. 枚举所有通过两道门的可行配置（卡型×卡数×精度×n），逐个算出 c_pass。
2. 给出最优选卡方案（c_pass 最低者）：卡型×卡数×精度×n。
3. 逐项说明其余候选为何被淘汰（显存装不下 / 带宽不达标 / c_pass 更高）。
4. 论证所选精度的质量损失是否可接受。
5. 关键数字标来源（题面给定 vs 你推导的），不确定标 [待核验]。
```

## 5. 执行清单（跑 T8c 前 checklist）

跑 T8c 数据前逐条过（全部机械可验，任一不过 → 不跑）：

- [ ] **oracle 验证**：`python3 tasks/think-trigger/exp-results/gold_gpu_oracle.py` exit 0 且
      输出含 `winner=3090×4/W4/n=2 ✅`、`c_pass=0.681≈0.679 ✅`、`N-5.2 6/6 ✅`。
      oracle 种子 commit = `d41ab1bf7`（已核：`git show --stat d41ab1bf7`）。
- [ ] **题面自洽验证**：`python3 tasks/think-trigger/exp-results/t8c_spec_selfcheck.py` exit 0
      且打印 `PASS`（参数从 §4 题面独立转录、不 import calc.py，防题面笔误；
      2026-11-25 实跑 PASS：winner=3090×4/W4/n=2 ✅ c_pass=0.6807≈0.681 ✅ 淘汰 5/5 ✅）。
- [ ] **题面冻结**：§4 题面正文冻结 commit hash = `2c16f644f`（§3/§4/§5 落盘 commit；
      其后仅本清单 hash 行回填，题面正文未动）。
- [ ] **预注册冻结**：`t8c-preregistration.md` 判据 commit hash = `8c168c2a4`
      （§2 power + §3 判据 + §4 决策规则，先于 T8c 任何数据 commit）。
- [ ] **两臂 prompt 模板**：
  - Arm A'（直接求解）：单次调用，user message = §4 题面全文，`max_tokens=24576`
    （= 24K 预算，见预注册 §1），temp=0.7，model=qwen3.8-27b-mtp（endpoint 127.0.0.1:8787）。
  - Arm B'（六阶段）：01 阶段 user message = §4 题面全文，harness 同 `run_exp_t8b.py`
    （01→02→02.5→03→04→04.5，每阶段 max_tokens=4096，累积上下文），总预算 6×4096=24576。
  - 两臂 token 预算相等（24576）= token-matched 的定义；容差见预注册 §1。
- [ ] **V100 价格假设复核**：确认仍按题面 $2500（③类假设）；若期间 V100 实价核验落到
      <$2033（§2 脆弱性披露的翻转点），winner 锚点重定后再跑。
- [ ] **correctness judge 就绪**：J1 三型判别器（`correctness_layer_v0.py`，
      commits 92aa24a76→fb60263ac 链，selftest 11/11）可用；winner 锚 = 4×3090/W4/n=2。
- [ ] **runner 改造点（已核 2026-11-25）**：`run_exp_t8b.py` 硬编码旧题面（L14-18 `Q`=32K/自行搜索/
      宽性价比）与 `MAX_A=16384`（L10）——**T8c 须新建 `run_exp_t8c.py`**：`Q` 替换为 §4 冻结题面全文、
      `MAX_A=24576`、`MAX_B=4096` 不变、`STAGES` 六阶段指令复用不动。不得直接改 T8b 脚本（T8b 数据可追溯性）。
- [ ] **端点健康**：vLLM 127.0.0.1:8787 `/v1/models` 返回 qwen3.8-27b-mtp（本轮已核 ①类）。
