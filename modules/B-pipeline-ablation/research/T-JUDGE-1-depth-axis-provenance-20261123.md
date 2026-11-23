# T-JUDGE-1 · depth 轴出处核验（2026-11-23，动摇 finding #3 的完整性缺口）

## 结论
**论文 §4.3 的 depth 数（finding #3 预算-质量曲线，peak@150）来自 LLM judge
（judge_v2_depth），不是论文 §3 声称的机械 judge_v1。** 这是"mechanical, no LLM
in the scoring path"核心声明的完整性缺口。

## 证据链（全部源①，刚查）
1. §4.3 表：150 → 0.4743 [0.4300, 0.5184]
   = 旧 K7 150 三 rep（0.4300/0.4745/0.5184）均值/极差（results-budget-scan.json）
2. 批处理 budget_scan_batch.sh：从 synth json 读 `depth_score` 字段
3. synth 函数 s5_state_machine.py:1595-1597：
   `from judge_v2_depth import score_run; depth = score_run(qid, answer)["overall"]`
4. **judge_v2_depth.score_run（line 422）= `call_llm(prompt, max_tokens=2000,
   temperature=0)`** —— LLM judge（对 synthesis answer 按 GPU_RUBRIC 逐点 0/1）
5. 论文 §3 声称的机械 judge_v1 depth（judge_v1.py:129）= `min(max_depth/5, 1.0)`
6. 用 judge_v1 重算旧 K7 150：0.6000/0.8000/0.6000（均值 0.6667）
   ≠ 论文数 0.4743 → 论文数不是 judge_v1 算的

## 两个连带问题
1. **机械 depth 是树大小代理**：judge_v1 depth ~ n_nodes r=0.947（n=28），
   用它重算 28 棵 peak 跳到 719（非 150），无预算区分度（只量树大小）。
2. **rep-scan 复现缺 --synth**：rep_scan_queue.sh 跑 `s5_state_machine.py gpu
   --max-nodes $budget`（无 --synth），新 run 无 answer 字段 → judge_v2_depth
   算不了新 run。复现设计无法复现论文实际用的 depth 指标。
   （K7 批处理带 --synth，rep-scan 没带——两批实验条件不一致。）

## 对论文的影响
- finding #3（预算-质量曲线 peak@150）基于 LLM judge，与"mechanical, no LLM"声明矛盾
- 若改用机械 judge_v1：peak 变 719，且 depth 只是树大小代理 → finding #3 大幅弱化
- 可能的诚实重构（待 D 决策）：depth 轴 = LLM rubric judge（非机械），
  finding #3 是关于"LLM 判定的推理深度"而非"机械树深度"；
  或：承认 depth 轴有 LLM，修正 §3 声明

## 待 D 决策（不静默改）
1. depth 轴定位：LLM rubric judge（改 §3 声明）vs 机械 judge_v1（改 finding #3 数）
2. rep-scan 是否补 --synth 重跑（才能复现 LLM depth 指标）
3. §4.3 表是否标注 depth 数出处（judge_v2_depth，LLM）

## 补充（10:21）：self-judge bias 第三层
judge_v2_depth 的 call_llm 来自 ablation_harness（line 32 import），
LLM_URL=127.0.0.1:8787 / LLM_MODEL=qwen3.8-27b（ablation_harness.py:19-20）
= **生成答案的同一个模型**。depth 分数是 27B 给自己的 synthesis answer
按 rubric 打分 → self-judge bias（模型倾向给自己打高分/风格一致分）。
论文 §2 引用的 "LLM judges inject family bias" 论证正好适用于此：
用同族模型当 depth judge，family bias 是 100%（同模型）。
→ finding #3 的 peak@150 曲线还叠加了 self-bias 混淆。

## 补充2（10:24）：机械轴上无 peak@150（era-matched 28 棵）
用 judge_v1 机械轴重算 28 棵（K7 15 + rep-scan 13）：
- cov 轴（纯 embedding，无 LLM）随预算单调升：0.259/0.264/0.278/0.347/0.352
  （50/100/150/300/719），cov~n_nodes r=0.571
- depth 轴：depth~n_nodes r=0.947（树大小代理）
- composite（0.5d+0.5c）单调升：0.463/0.445/0.501/0.574/0.643，**无 150 峰**

→ finding #3 的"非单调 peak@150"是 LLM judge（judge_v2_depth, self-biased）
独有产物。机械轴要么单调升（被树大小驱动，trivial），要么无区分度。
**结论强化**：finding #3 的具体形状（peak@150）不 robust，
是 self-biased LLM depth judge 的 artifact。诚实重构方向：
(a) depth 轴如实标 LLM+self-bias，finding #3 降为"LLM 判定深度"的 suggestive 观察；
(b) 机械轴只保留 cov（单调、size-confounded，不作预算曲线主张）；
(c) 真正的预算-质量主张应建立在 L4 zero-convergence（0/15+0/6，机械、
    无 self-bias、跨 budget 稳定）上——这才是 robust 的那条。

## 补充3（10:26）：机械 depth 轴是 3 级阶梯，选项(b)不成立
28 棵 max_depth 分布：3→12棵(0.6) / 4→14棵(0.8) / 5→2棵(1.0)。
depth_score=min(max_depth/5,1.0) 只有 {0.6,0.8,1.0} 三个离散值，
26/28 棵挤在 0.8/1.0 → 无预算区分度。
（K7 批处理带 --max-depth 5，树深被硬限 5；rep-scan 虽不带但状态机
默认也止于 5，故两批 max_depth 都 ≤5。）

→ 报 D 的选项 (b)「改用机械 judge_v1 depth」**不成立**：
  3 级阶梯测不出 peak@150。
→ 决策空间收窄：depth 轴只能是 LLM rubric judge（judge_v2_depth）。
  finding #3 重定位为「LLM 判定的深度（self-biased）」的 suggestive 观察；
  robust 主张留在 L4 zero-convergence（机械/无self-bias/跨budget稳定 0/21）。

## 补充4（10:27）：爆炸半径 + 问题重新定性
**重新定性**：§6 line 113 已写"Self-judge bias: the depth axis is same-family"
→ 这不是新发现的缺口，是草稿**早已存在但内部矛盾**的：
  abstract/§3 说"no LLM in the scoring path"，§6 又说 depth 轴 same-family。
  问题 = 草稿内部不一致，不是新数据污染。

**爆炸半径（依赖 LLM depth 轴的声明）**：
- finding #3（四发现之一）：预算-质量非单调曲线 peak@150
- abstract (3)：depth score highest at 150 (0.474)
- contribution #2："a non-monotonic budget–quality curve"
- §4.3 表（0.4743）+ §4.3 正文（150 peak 0.9 run-sd）
- §5 point 3："the non-monotonic curve is a warning"
- §6 n=3/budget 条
→ finding #3 的**具体形状**（peak@150）全在 LLM depth 轴上。

**Robust 的（不依赖 LLM depth，机械/metacog）**：
- finding #1（monitoring/repair 分离）：metacog 轴（gold-free, 节点字段）✓
- finding #2（difficulty-calibrated gap marking）：gap_rate（节点字段）✓
- finding #4（checkpoint reuse）：metacog + vsr（有通道故障 caveat）✓
- L4 zero-convergence（0/21，机械，刚核验）✓
- 两轴框架本身 + metacog 轴跨域（83-run）✓
- coverage 轴（机械，但 size-confounded）✓

**结论**：塌掉的是 finding #3 的**形状**，不是论文核心。
两轴框架、metacog 轴、L4 zero-convergence 全活。
finding #3 可重定位为：
  "LLM-judged depth（self-biased）显示弱非单调；机械轴显示
   breadth（nodes/cov）随预算单调升；robust 的预算-质量主张是
   L4 zero-convergence（跨 budget 稳定 0/21）。"
→ 决策代价可控：改 finding #3 定位 + §3/abstract 的 no-LLM 声明
  （承认 depth 轴有 LLM），核心两轴框架不动。

## 补充5（10:30）：vsr 预算趋势未被通道故障污染（§4.4 机械轴发现站得住）
K7 14 棵逐棵核验：空源率 0-90% 随机分布，与 vsr 值无相关（cor=-0.181）；
通道健康组 vsr 0.697 vs 故障组 0.641（差 0.056，弱）。
预算档 vsr 均值：b50 0.761 → b100 0.673 → b150 0.603 → b300 0.533 → b719 0.541
（与 §4.4 声称的 0.76@50 → 0.53-0.54@300/719 一致，719 略超 300 已如实标注）。
→ §4.4 的 vsr 预算趋势是机械轴上 robust 的预算相关发现
  （不依赖 LLM depth，不受通道故障混淆），可作 finding #3 重定位后的
  预算-质量主张支撑之一（与 L4 zero-convergence 并列）。

## 补充6（10:31）：metacog 轴 budget-invariant（两轴分离的干净证据）
rep-scan 13 棵 metacog 轴按 budget 档：
  b100(n=5): gap 0.099 ret 0.349 hg 0.861 total 0.246
  b150(n=5): gap 0.100 ret 0.294 hg 0.895 total 0.247
  b300(n=3): gap 0.130 ret 0.321 hg 0.875 total 0.239
→ metacog total 跨 budget 平（0.246/0.247/0.239），无 150 峰；
  gap 分量微升（0.099→0.130）但 total 不升。
对照 83-run：gap 0.067（全语料）/ gpu 0.102，rep-scan gap 0.107 与 gpu 一致。

**意义**：这是两轴分离最干净的实证——
  quality/breadth 轴随预算单调升（cov 0.26→0.35），
  metacog 轴跨预算不变（total 0.24 平）。
  预算买 breadth，不买 metacognition。
→ 这条 robust 主张（metacog budget-invariant）不依赖 LLM depth 轴，
  可作 finding #3 重定位后的核心预算主张（与 L4 zero-convergence、
  vsr 趋势并列）。n=5/5/3，suggestive 但方向清晰。

## 补充7（10:33）：metacog budget-invariance 的通道故障稳健性
对 13 棵 rep-scan 按通道健康度（空源率<50%）分层重算：
- metacog total 按档：全棵 0.246/0.247/0.239 → 仅健康棵 0.265(n=4)/0.239(n=2)/0.247(n=1)
  → 跨档仍平，invariance 不被通道故障污染
- post 分量（受通道影响, 0.3 权重）健康组按档：0.386/0.362/0.389 → 平
- gap 分量（不依赖通道, 0.4 权重）全棵按档：0.099/0.100/0.130 → 微升
  （b300 略高，n=3 不显著，如实标注）
→ 补充6 的 metacog budget-invariance 发现 robust（通道故障稳健），
  可作 finding #3 重定位后的核心预算主张（与 L4 zero-convergence、
  vsr 趋势并列）。

## 补充8（10:36）：rep-scan 队列自动评分静默失败的根因
**根因**：队列脚本的 `python3` 解析到 Homebrew 3.14（/opt/homebrew/bin/python3），
该环境缺 sentence_transformers（PEP 668 externally-managed，--user/--break-system-packages
都不宜用）→ judge_v1.judge_run line 181 `from sentence_transformers import
SentenceTransformer` 抛 ModuleNotFoundError → 被 heredoc try/except 捕获 →
`[score-err]` 输出到**队列 stdout**（非 $LOG，tee 只给 echo 行）→ 不可见 →
rep-scan-scores.json 从未被队列写入（7h 静默）。
**对照**：手动评分用系统 python3（3.9，有 sentence_transformers）→ 正常。
**影响**：仅评分步骤；run 数据（rep-*.json）正常落盘，手动评分可补全（已做 13 棵）。
**下次队列的修法**（不碰正在跑的队列）：
  ① 队列脚本评分段显式用系统 python3（/usr/bin/python3 或 3.9 路径），或
  ② 建一个带 sentence_transformers 的 venv 并让队列评分段用 venv 的 python，或
  ③ 评分段 stderr 不吞（去掉 2>/dev/null）+ tee 到 $LOG（让 [score-err] 可见）。
  最小改动 = ③（可见性）+ ①（正确解释器）。

## 补充9: workshop 草稿数字一致性审计 (11-23 10:42)

草稿关键数字 vs 数据源逐一核验:

| 数字 | 草稿 | 数据源 | 结果 |
|---|---|---|---|
| 83-run 语料 | 83 | metacog-budget-scan-v1.1.json n=83 | ✓ |
| gap 跨域 | nat 0.028 < soc 0.058 < gpu 0.147 | 全语料 0.0254/0.0562/0.1020 (era-matched 口径 0.028/0.058/0.147) | ✓ 方向一致 |
| healthy_gap_rate | 0.938 | n=83 mean=0.938 | ✓ |
| vsr 臂差 r1-r2 | +0.205 (B 0.66 vs A 0.46) | A 0.458 / B 0.661 / +0.202 | ✓ |
| L4 | 0/21 | K7 0/15 + idea2 0/6 | ✓ |
| L2 | 50:24 = 2.08:1 | 14-tree | ✓ |
| rework | 1.6-2.1% | 36/2298=1.57% | ✓ |
| **55% unverified** | abstract 当 100+ runs 通用发现 | **stale**: 出自 8c266fc8e 的 18-run/5812 节点子集, 当前数据不可复现 (最近 18 棵重构=48%); 全语料 160 棵(去重)/21945 节点非verified=45.5% (9984/21945), gpu 66 棵=52.5% | ✗ stale, 已换 45.5% 全语料口径 |
| 19-tree corpus | 19 | source-verify.json 现 21 棵 (K7 15 + idea2 6); 19 = 15+4 (r1-r2, r3 contaminated 排除) | ✓ 口径确认 (r3 本就不该计入) |

**55% 已闭环 (11-23 10:55)**: 18-run 子集不可复现 (最近 18 棵重构=48%≠55%)。scope 判定: finding 1 限定 "Within the GPU domain", 故用 GPU 域口径 **52.5% (5630/10730, 33 棵去重 GPU 树)** 填 abstract; §4.4 用全语料 45.5% (9984/21945, 160 棵去重) 并注 18-run 55% 不可复现。两处均带分母总体。
- 域分布 (去重): gpu 33 棵/10730 节点 52.5%; nat 42 棵/3895 36.8%; soc 52 棵/7320 39.9%。
- 教训: 改百分比前先确认 finding 的 scope 限定词 (GPU domain vs full corpus), 别拿全语料数填 GPU 域声明。

## 补充10: rep_scan_analyze.py era 混淆修复 + 机械轴真实形状 (11-23 10:45)

**bug**: analyze 脚本 load_k7() 读 results-budget-scan.json 的旧 LLM depth (judge_v2_depth, self-biased), load_reps() 读 rep-scan 新机械 depth。两 era 混表 → 假 peak@150 (depth 0.6529, Welch p=0.119)。

**fix**: 改为单一源 era-matched-28.json (28 棵全用 frozen judge 机械 depth 重算)。

**机械轴真实形状** (28 棵, frozen judge):
```
 budget   n  depth_mean  sd      nodes_mean
    50   3   0.6667    0.1155   234
   100   8   0.6250    0.0707   154
   150   8   0.7250    0.1035   262
   300   6   0.8000    0.0000   380
   719   3   0.9333    0.1155   598
```
- **无内部 peak**: 单调升, 3 级阶梯 (0.6/0.8/1.0) 在 300/719 饱和到 0.8/1.0。脚本 "peak 719" 是阶梯顶档, 非真 peak。
- **depth~n_nodes r=+0.947** (n=28): 机械 depth 与树大小强混淆, 无法分离 budget 效应。
- 结论: finding #3 的 peak@150 确证为 LLM judge 独有产物; 机械轴既无 peak 又与 n_nodes 混淆, 不能作为 budget 主张。robust 主张仍押 L4 zero-convergence + metacog budget-invariance + vsr 趋势。

**r7/r8 落地后**: 重算 era-matched (加 2 棵) → 300 档 n=8, 719 档 n=5, 重跑 analyze 填 §4.3 最终表。

## 补充11: run 数口径钉死 — K7 ⊂ 83, 唯一 104 (11-23 10:58)

**问题**: abstract "across 100+ runs" 的构成不明, 且原句 "Within the GPU domain" 与跨域 finding(2) 自相矛盾。

**核验** (n_nodes 会碰撞, 83 内部 8 个重复值, 故用"不同值命中"而非"任意命中"):
- K7 budget-scan 15 棵的 15 个**不同** n_nodes (103/122/123/136/167/175/314/364/381/391/392/415/423/665/747) 15/15 全命中 83-run 的 gpu 34 棵 → **K7 ⊂ 83** (撞车概率≈0)。
- idea-2 6 棵 (n_nodes 316/394/401/402/411/435) 独立臂, 仅 316 与 83 碰撞 (不同 run)。
- rep-scan 15 棵 = r4–r8 (新 run, 延续 K7 的 r1–r3), 非重复。

**唯一 run 数 = 83 (含 K7) + idea-2 6 + rep-scan 15 = 104**。"100+" 成立。

**abstract 已改**: 去掉 "Within the GPU domain" 限定 (与跨域 finding 2 矛盾), 改为 "104 unique: 83 cross-domain (含 K7 15) + idea-2 6 + rep-scan 15; K7 是 83 的子集非加法项; finding 1/3/4 GPU 域, finding 2 跨域"。

**教训**: ① 百分比/run 数前先确认 finding 的 scope 限定词; ② n_nodes 匹配做重叠检测必须用"不同值命中" (n_nodes 非唯一, 83 内部 8 碰撞); ③ 同一数字改 2 次以上 = 重复计数红旗, 停手用数据钉死再写。

## 补充12: 检索通道 outage 根因诊断 (11-23 11:00)

**Blocked 项 "root cause 待诊断" 收口**。

**通道架构** (research_hook.py `research_hook`): local_corpus → wikipedia → **ddg** → webllm → arxiv, 每通道独立 cap, 总输出 ≤ max_results=8。

**根因 = DDG 间歇性站级封锁 × 单向熔断器放大**:
1. **DDG lite TLS 站级封锁** (2026-11-20 笔记, line 349-353): rc=35, 直连+7890 代理都死, 同代理下 wiki/arxiv 正常 → 站级非代理。间歇性 (有时活 9min, 有时 3min 就挂)。
2. **单向熔断器** (line 354-408): `_ddg_fail_streak >= 2` → 本进程内**永久跳过 DDG**, 无半开/无冷却重试。DDG 在 run 早期挂 → 该 run 后续 ~40min 只剩 wikipedia 兜底 → 空源率飙升。

**放大证据** (SITE-WL 行数 = 白名单过滤次数 = 检索有效调用数):
| run | SITE-WL | DDG 存活 |
|---|---|---|
| 100-r4 | 16 | ~9min (03:25→03:34) |
| 100-r5 | 3 | ~3min (03:42→03:45) |
| 150-r4 | 18 | 较长 |
| 150-r5 | 37 | 最长 |
→ 间歇性 (同 budget 档内 r4/r5 差异大), 非整夜全死。

**为什么核心 metacog 指标不被污染** (呼应 §8): gap/retrieval/healthy_gap 来自节点打标 (retrieval-independent), 只有 post_retrieval_accuracy + vsr 依赖检索返回。

**修复方案 (半开熔断, 待 rep-scan 队列跑完后实施)**:
- `_ddg_fail_streak >= 2` 后不再永久跳过, 改为每 ~10min 允许 1 次 probe 调用; probe 成功 → 重置 streak, 失败 → 继续跳过。
- 同理给 WEBLLM-BROKEN (line 733) 加半开。
- **为何现在不改**: r7 在跑 (旧代码), r8 是队列最后一个 (~1.5h)。现在改 → r7(旧)/r8(新) 在 300 档内形成通道混淆, 违反 pipeline 固化约束 (不碰 running 实验)。r8 跑完后改, 惠及后续 83-run 语料 + Q6-Q10 budget scan。
- 可逆性: git 可回滚; 只影响未来 run (Python 启动时加载代码, 不影响 running 进程)。

## 补充13: abstract 数字全量核验完成 (11-23 11:05)

abstract 全部关键数字逐一核验 (全过):
| 数字 | 数据源 | 结果 |
|---|---|---|
| 52.5% unverified | 5630/10730, 33 棵 GPU 域去重 | ✓ (原 55% stale, 已换) |
| 84% unverifiable | 4611/5495 search-degraded, 160 棵全语料去重 = 83.9% (contradicted 5.9%, ambiguous 10.2%) | ✓ |
| 1.6-2.1% rework | 36/2298 + 61/2919 | ✓ |
| gap 0.028/0.058/0.147 | era-matched 口径 (全语料 0.0254/0.0562/0.1020, 方向一致) | ✓ |
| 104 runs | 83(含K7 15) + idea2 6 + rep 15 | ✓ (K7⊂83, 补充11) |
| depth 0.474@150 | LLM judge_v2_depth (self-biased, 带 provenance note) | ✓ 口径已标 |
| vsr 0.66 vs 0.46 | idea2 r1-r2 channel-healthy | ✓ |
| 19-tree corpus | 15 K7 + 4 idea2(r1-r2), r3 contaminated 排除 | ✓ |

abstract 数字审计闭环。

## 补充14: r7 落地后 budget-invariance 重验 (11-23 11:00)

r7 (300 档, 通道故障 ret=0, metacog total 0.045) 落地后, "metacog budget-invariance" 主张重验 (rep-scan-scores.json 14 条):

**total 分量 (含 channel-dependent 的 post_retrieval_accuracy 权重 0.3)**:
- 全量: 100=0.246 (n=5), 150=0.247 (n=5), 300=0.190 (n=4, 含 r7) — r7 把 300 档从 0.239 拉到 0.190
- healthy 子集 (排除 7 个 FLAG): 100=0.265 (n=4), 150=0.239 (n=2), 300=0.247 (n=1) — spread 0.026, flat 成立但 n 极小

**gap_rate 分量 (retrieval-independent, 权重 0.4)**:
- 全量 (含 outage runs): 100=0.099, 150=0.100, 300=0.126 — spread 0.027, **通道故障下也 flat**

结论: budget-invariance 主张应表述为 **gap_rate 分量 (retrieval-independent) 全量 flat**, 而不是 metacog total (total 含 post 分量, outage 会拉低)。draft §4.3 provenance note 现在写的是 "metacognition axis's budget-invariance (rep-scan 13 runs: total 0.246/0.247/0.239)" — r8 落地后需改为 gap_rate 口径 (0.099/0.100/0.126, n=14) 或 healthy 子集 total 口径, 并标 n 极小 caveat。

## 补充15: source_verify cache "bug" 关闭 (11-23 11:02)

Blocked 项 "source_verify cache bug: cache=0 on second run" 重验: 当前 cache 文件 647 条 (03:26 仍在写), 19 棵树的 384 个 candidate key **100% 命中**。cache 机制正常 (load 开头/save 每棵树后), "cache=0" 是早期 cache 未积累时的观察, 非 bug。Blocked 项清除。

## 补充16: scope-mismatch 系统性错误模式 (11-23 11:05)

今日 3 次同模式错误 (跨域数字填进域限定声明):
1. 55% (18-run gpu 子集) 先换成全语料 45.5%, 再换成 GPU 域 52.5% (finding 1 限定 "Within the GPU domain")
2. "83+21" 双计 K7 (K7 15 ⊂ 83), 修正为 104 = 83+6+15
3. §7 "GPU, 104 unique runs: 34+6+15" — 104 是跨域总数, 34+6+15=55 才是 GPU 域数

**规则 (写百分比/run 数前必查)**:
- 声明的 scope 限定词 (Within X domain / per-domain / 全语料) 必须与数字的分母人群一致
- 加法分解必须自洽: "A+B+C = N" 逐项加起来要等于 N (104 ≠ 34+6+15)
- 跨域总数 (104) 和域内数 (55 GPU / 49 nat+soc) 是两个口径, 不能互相填
- 同一数字被改 2 次以上 = 双计/口径错红旗, 停手用数据验证再写

## 补充17: r7 metacog 记录纠错 (11-23 11:25)

**发现**: 用当前代码重算全部 14 条 rep-scan metacog, 13/14 与 scores 文件完全吻合, 仅 r7 不符——scores 记 total=0.045 (ret=0), 当前代码重算 total=0.2912 (ret=0.3119)。

**根因**: r7 是用**写入中途的 329 节点快照**评的, 不是最终 311 节点 run json。证据:
- 旧记录 gap=0.1125 → n_defensive/n_total=0.1125; 当前文件 37 个 defensive 节点 → 0.1125×n_total=37 → n_total=329 (旧); 0.119×311=37 (新)。
- judge 侧 (era-matched) r7 = 311 节点, total=0.5944, 与最终 run json 一致 → 最终产物是 311 节点。
- git 确认 retrieval_rate=n_search/n_total 自文件创建 (5465d6062, 11-22 22:23) 未变, 代码不是变量。
- 13/14 完全吻合 → 当前代码权威, r7 记录是 mid-write 快照。

**修正**: r7 metacog total 0.045→0.2912 (ret 0→0.3119, post 0→0.5, hg 0→0.9872)。已写入 scores 文件。

**对 budget-invariance 的影响**: r7 修正后 300 档 metacog total = 0.2520 (n=4), 不再被拉低。**total 现在也是平的**: 100=0.2456 (n=5), 150=0.2465 (n=5), 300=0.2520 (n=4), spread 0.006。补充14 的结论 ("total 掉 0.190, 只能声明 gap_rate") 被推翻。

**caveat (诚实边界)**: retrieval_rate=n_search/n_total 对通道故障**盲**——通道死时模型照样打 search 标签 (r7 标了 97 个, 只拿到 3 个 URL), 所以 outage run 的 total 平 partly 是度量盲点, 不是真"检索成功"。gap_rate (defensive/total) 才是构造上 retrieval-independent 的干净分量 (0.099/0.100/0.127, n=14)。draft 保留 gap_rate 为主声明, total 平作为修正后的补充事实。

## 补充18 (2026-11-23 11:47): r8 落地, 15/15 完成, 300 档 n=5 数据变化

### 落地

- r8 (300-r8, 20261123-104623) 59min 落地, 355 节点, **通道健康** (SITE-WL 32 行, 非 FLAG)
- land_rep_run.py 落地 (修了 line 54 met["total"]→met["metacog_total"] 漏改): judge=0.5944 (depth=0.8, cov=0.3889), metacog=0.1534 (gap=0.0282, ret=0.307, post=0.167)
- scores=15 records, era-matched=30 棵 (depth 分布 12@0.6 / 16@0.8 / 2@1.0)
- 队列 15/15 完成, 进程结束

### 数据变化 (r8 是真实数据点, 非错误)

| budget | n | gap 均值 | total 均值 |
|---|---|---|---|
| 100 | 5 | 0.0992 | 0.2456 |
| 150 | 5 | 0.1001 | 0.2465 |
| 300 | 5 (旧 4) | **0.1075** (旧 0.127) | **0.2323** (旧 0.2520) |

- r8 gap=0.0282 是同档离群低 (其余 0.103/0.113/0.119/0.175): 109 search 标签但只有 10 defensive 标记 — **真·过度自信 run**, 非通道故障 (32 SITE-WL 行健康)
- **gap_rate 声明不变且更紧**: 0.099/0.100/0.107, spread 0.008 (旧 0.028), 仍是三组件里最平的 — 承重结论强化
- **total-flat 被动摇**: spread 0.006→0.014, 300 档掉 0.014 (r8 驱动)。措辞从 "flat" 改 "flat-to-mildly-declining", 归因 r8 过度自信离群
- 机械 depth 轴: 300 档仍饱和 0.8 (sd=0), 无新 peak; depth~n_nodes r=+0.944 不变

### 草稿更新

§4.3 provenance: 29→30 棵, 14→15 runs, n=5/5/4→5/5/5, gap 0.099/0.100/0.127→0.099/0.100/0.107 (spread 0.008), total 0.246/0.247/0.252→0.246/0.247/0.232 (spread 0.014, flat-to-mildly-declining, r8 归因), 删 "n will become 5/5/5" 前瞻句。

### 待办

- DDG half-open patch (f60f01871) 现在可以 apply (队列已结束, channel-mixing 红线解除)
- abstract "n=8/tier" 前瞻兑现 (100/150/300 各 n=8 已成立)

## 补充19 (2026-11-23 12:05): §4.4 per-layer 解剖扩到 30 棵 — "链断裂"实为"浅树无 L4"

### 数据 (30 棵 = K7 15 + rep-scan 15, 8,767 节点, 表内自洽已核)

| layer | nodes | verified | degraded | pending | ver% |
|---|---|---|---|---|---|
| L1 | 162 | 11 | 0 | 151 | 6.8% |
| L2 | 855 | 364 | 328 | 163 | 42.6% |
| L3 | 2759 | 1327 | 1195 | 237 | 48.1% |
| L4 | 4230 | 2230 | 1943 | 57 | 52.7% |

- 旧 18-run 快照 (5,812 节点) 的 "18/18 无链断裂" 在 30 棵上变成 18/30
- **真实机制 (连错 3 次才到)**: 12 棵 "失败" 树的 max_depth=3, **根本没有 L4 层** (0 个 L4 节点), 不是"有 L4 但 0 verified"
  - 50 档 2/3 无 L4, 100 档 7/8 无 L4, 150 档 3/8, 300 档 0/8, 719 档 0/3
  - 12 棵里只有 1 棵 (100-r5) 在通道故障 FLAG 列表, 其余 11 棵通道健康 → 非 channel artifact
  - 18 棵 max_depth≥4 的树 18/18 都有 verified L4 节点 → "链断裂"是 depth 的函数, 不是 verification 的函数
- 这是 §4.3 已确立的 depth~budget (r=0.94) 关系的 per-layer 签名: 低预算→浅树→无 L4

### 连错 3 次的教训 (本会话第 6/7 类 scope 错 + 1 次粒度错)

1. 第一版写 "channel-outage over-represented" — 错 (12 棵里只有 1 棵故障)
2. 第二版写 "source-unverifiable / carry no verifiable citation" — 错 (status 是模型自评, 不是机械核验)
3. 第三版写 "model refuses to certify (evidence 读 无来源支持)" — 错 (12 棵失败 run 的 L4 层 0 节点, 没有 degraded L4 可读; 且 0/12 含该措辞)
4. 第四版 (正确): 先 dump 每棵 max_depth + L4 节点数, 才发现是"无 L4 层"
**规则: 树结构发现必须先 dump 每棵 max_depth/各层节点数, 再写解读; 不凭 status 计数反推机制**

### 与 obs 4 的关系

obs 4 (zero-convergence 0/21) 是 synthesis 答案的内容声明; obs 2 是树结构 L4 层的存在性声明。两个不同对象, 同一个 (a)→(b)→(c) closure gap: 即使有最终答案, 背后的树常常没有结论层来支撑它。

### 草稿更新

§4.4 表头 18-run/5,812 → 30 棵/8,767; 表体换新数; obs 1 "flat 43-49%" → "rises monotonically 42.6/48.1/52.7%"; obs 2 重写为"无 L4 层 + budget 依赖 + 非 channel artifact + depth 函数"; obs 3 删掉不可复现的 "55% 18-run subset" 括注。

## 补充20 (2026-11-23 12:18): gap_rate 预算不变是 era-scoped, 非 corpus-wide

### 发现

abstract 原句 "fills the mechanical axes (coverage, metacognition, L4) at n=8/tier" 是 scope 错:
- coverage / L4 确实扩到 n=8 (K7 3 + rep-scan 5)
- 但 metacog 的**不变发现**只在 rep-scan era 内部成立

### 数据 (同 compute_metacog 代码, source ①)

| era | budget 100 | 150 | 300 | spread |
|---|---|---|---|---|
| rep-scan (11-23) | 0.099 | 0.100 | 0.107 | 0.008 (紧) |
| K7 (11-22) | 0.134 | 0.047 | 0.075 | 0.087 (10倍) |

- K7 150 档逐条 0.024/0.026/0.090 全低, 非单点噪声 → 真 era 差异
- K7 与 rep-scan edge_types 相同 (cartesian/quotient), 都无 synth 树节点 (synthesis answer 是独立输出非树节点, 我之前"K7 有 synthesis"假设错)
- era 差异 (0.087) 和 budget 效应同量级 → 不能跨 era 合并算 n=8

### 结论

budget-invariance 声明必须 era-scoped (rep-scan n=5/5/5), 不能写成 corpus-wide n=8。
abstract 已修: "extends the coverage and L4 axes to n=8/tier, while the metacognition axis's invariance finding remains scoped to the rep-scan era (n=5/5/5, spread 0.008)"。
§4.3 的 gap_rate 声明本来就是 n=5/5/5 (rep-scan only), 口径一致; 只有 abstract 的 n=8 措辞 overstate。

### 待查 (未做)

era 差异的成因: K7 (11-22) vs rep-scan (11-23) 之间 pipeline 改了什么? 需 git log 对比两日间的 research_hook / s5_state_machine 改动。若 gap_rate 的 era 敏感, 则 83-run 语料的跨日 metacog 对比都需 era-matched (现有 finding #2 nat/soc/gpu 已 era-matched, 安全)。

## 补充21 (2026-11-23 12:22): gap_rate 预算不变 = ANOVA 不显著, 非"钉在 0.100±0.008"

### 统计澄清

"spread 0.008" 只描述三个层均值的接近度, 藏掉了层内 sd 的真实噪声。
正确读法 (rep-scan only, n=5/5/5, source ① 同 compute_metacog):

| tier | mean | 层内 sd | 逐条范围 |
|---|---|---|---|
| 100 | 0.0992 | 0.0679 | 0.028–0.184 |
| 150 | 0.1001 | 0.0364 | 0.036–0.124 |
| 300 | 0.1075 | 0.0524 | 0.028–0.175 |

- 层间均值差 0.0083, 合并层内 sd 0.0499, **比值 0.17** (层间差是层内噪声的 1/6)
- **单因素 ANOVA F(2,12)=0.036, p ≫ 0.05** → 预算效应在 run-to-run 噪声分辨率之内, 检测不到
- 正确声明: "预算效应在噪声分辨率内, 检测不到" (强声明), 不是 "gap_rate 钉在 0.100±0.008" (弱声明, 误导)

### 与补充20 的关系

补充20 说 era-scoped (K7 形状不同); 补充21 说即便在 rep-scan era 内部, "不变"也是统计不显著 (ANOVA), 不是精确平坦。
两者叠加: budget-invariance 声明 = era-scoped (rep-scan) + 统计不显著 (ANOVA F=0.036), 不是 corpus-wide + 精确 0.100。

### 草稿更新

§4.3 provenance + abstract finding (3): "spread 0.008" → "层间差是层内 sd 的 1/6, ANOVA F(2,12)=0.036 p≫0.05, 预算效应低于噪声分辨率"。

## 补充22 (2026-11-23 12:35): depth 轴定位重写 + §4.2 budget-scan 数字纠错

### 定位重写 (D 授权方向: 如实标 LLM rubric + robust 主张挪 L4)

- 标题: "Non-Monotonic Budget–Quality Curve" → "Breadth-without-Depth Budget Curve"
- §1 贡献2: "a non-monotonic budget–quality curve" → "robust (mechanical, bias-immune) claim is the L4 zero-convergence (0/21); non-monotonic depth peak confined to self-biased LLM rubric axis"
- abstract finding (3): 标题改为 "More budget buys breadth, not a more stable answer — the robust claim is mechanical"; peak 限定 LLM 轴 + self-bias 归因 caveat
- §5 implication 3: 从 "non-monotonic curve 是警告" 改为 "robust mechanical finding (L4 零收敛 + 3-level step 饱和) 是警告; peak 是 weaker self-biased n=3 信号, 不是 implication 基础"
- 自相矛盾检查: abstract 标题一度写 "peak is a self-bias artifact" (比 §4.3 caveat 说满) → 改为 "not reproduced on the bias-immune axis"
- 逐字重复检查: "719 buys ~700 nodes vs ~380" 一度出现 2 次 (abstract 首句+末句) → 删末句, 现 ×1

### §4.2 数字纠错 (跨轴 scope 错, 历史遗留)

line 66 budget-scan gap_rate 原值 "50→0.079, 100→0.209, 150→0.147, 300→0.082, 719→0.089" 与当前代码算出的 K7 值 (0.064/0.134/0.047/0.075/0.081) 不符。
铁证: 原值 150→0.147 = finding 2 的 gpu **难度轴**值 → 难度轴数字误填预算轴声明。
已修正 + 标注纠错说明。非单调定性结论不变 (100 最高 0.134, 150 最低 0.047)。

## 补充23 (2026-11-23 12:50): finding (2) 难度梯度 gpu 值 0.147 不可复现 → 修正为 0.1193

### 发现

D 问"数字都是什么含义"→ 我把速查表报给他后, 对凭记忆的 finding (2) 数字独立重算:
- 数据源: metacog-budget-scan-v1.1.json (83 runs, 11-22 22:25 创建, git 确认此后未改)
- era-matched 口径 = sm-era budget-150 runs (gpu 排除 K7 15 budget-scan, 用 n_total 精确子集减法)
- **可复现: nat 0.0254 (n=22) < soc 0.0562 (n=27) < gpu 0.1193 (n=19), KW H=37.77 p=6.3e-9, 三对 Mann-Whitney 全 p<0.0001 (nat<soc p=0.0003 与草稿精确一致)**
- **草稿的 gpu 0.1469 (n=18) 数学上不可复现**: 19 条 sm-era gpu 总和 2.2667 < 0.1469×18=2.6442, 去掉任何一条只会更低
- 子集搜索: soc 0.0576 可复现 (去掉 0.02 那条), nat/gpu 不可复现
- 0.147 只存在于 11-22 散文记录 (plan-layered-20261122.md line 29-30), 从未存进数据文件
- 11-22 记录里 0.147 同时出现在难度梯度 (gpu n=18) 和 budget-scan 序列 (150→0.147) — 两个不同统计量同值, 当时数字混淆的信号 (budget-scan 序列今天已证明是错的, K7 150 档实际 0.047)

### 结论

- 方向 + 显著性全部复现, finding (2) 成立
- gpu 值 0.147 → 0.1193 (n=18→19): 0.147 算在更早的语料快照上, 或当时算错
- draft 三处修正: §4.2 表 (22/27/19, 0.0254/0.0562/0.1193, H=37.8) + honest boundaries + abstract finding (2); 每处带 correction 注
- 教训: 11-22 的"质询修正"记录只存散文没存数据文件 → 数字无法复现。规则: 任何"修正后"的数字必须连同计算脚本/子集定义一起落盘, 散文记录不算证据

## 补充24 (2026-11-23 13:00): rep-scan wall time = 第二成本维度

队列 15 run 的 wall_s (rep-scan-queue.log, 已存工作区 data/rep-scan/):
- budget 100: mean 988s (16.5min) | 150: 2017s (33.6min) | 300: 2998s (50.0min)
- wall 随 budget 单调升, 与 node count 同向 (154/262/368 nodes)
- **per-node 成本随 budget 升: 6.4→7.7→8.1 s/node** = 边际节点越来越贵 (时间轴上的递减效应)
- 论文目前只用 realized node count 作成本代理; wall time 是补充成本维度, 非承重 (budget-invariance/L4 零收敛都不依赖它)
- 若要强化 "cost" framing 可加: budget 买广度也买时间, 且边际节点时间成本递增

## 补充25 (2026-11-23 13:10): 承重数字地基验证 — 0.147 是孤例, 非系统性

D 问"数字含义"触发对凭记忆数字的独立重算, 暴露 0.147 不可复现后, 把 abstract 第一句的三个承重数字全部对磁盘数据重跑:

| 数字 | abstract 声称 | 重算 | 数据源 | 结果 |
|---|---|---|---|---|
| 84% healthy gap | 84% of search-degraded 正确分类 unverifiable | unv/search-degraded = 4802/5702 = 84.2%; unv/(unv+con)=93.5% (不含 ambiguous) | metacog-budget-scan-v1.1.json (83 runs) | ✓ 两口径都对 |
| 52.5% unverified | 5,630/10,730, 33 棵 GPU 树 | 18 sm-era (archive/sm-gpu-*) + 15 K7 (archive/budget-*) = 33 树, 10,730 节点, 5,630 未验证 = 52.5% | 磁盘 run json 逐节点遍历 | ✓ 一字不差 |
| 1.6-2.1% rework | 修复率 | K7 36/2298=1.6%, sm-era 61/2919=2.1% | 磁盘 run json rework_count>0 且 status=verified | ✓ 一字不差 |

**结论: 0.147 是孤例 (11-22 散文记录算错/算在旧快照), 不是系统性数据完整性问题。** 三个承重数字全部可复现, 论文地基站得住。

**根因 (0.147 为何不可复现)**: 83-run 语料文件的 `file` 字段全是泛化名 (runs-s5-sm-gpu.json, 34 条 gpu 指向同一名字), 无法追溯到实际 run 文件; 11-22 的"质询修正"只存散文没存计算脚本+子集定义。52.5% 能复现是因为它的口径 (18+15=33 树) 在补充16 里钉死了具体文件集; 0.147 的口径 (n=18 sm-era gpu) 没钉死, 且 n=18 与当前 sm-era 19 条不符。

**规则 (固化)**: 任何承重数字必须 (a) 存计算脚本或可复现的逐节点遍历, (b) 口径钉死到具体文件集, (c) 散文记录不算证据。83-run 语料的 file 字段泛化名是隐患 — 后续若再算跨域统计, 应先重建 file→实际路径的映射。

## 补充26 (2026-11-23 13:20): "coverage monotone rise" 不成立 → 修正为 rise-to-plateau

### 发现

定位重写把 "coverage monotone rise" 列为 robust 机械发现, 但 30 棵 era-matched 数据:
- cov 按档: 0.259/0.264/0.278/0.358/**0.352** (50/100/150/300/719)
- 719 档 (598 节点均值) cov 比 300 档 (368 节点) **还低** — 不是单调升, 是升到 300 后 plateau
- cor(cov, n_nodes) = +0.563 (size-confounded, draft 已标)
- 719 档逐条: r1 (381节点) 0.333 / r2 (665) 0.417 / r3 (747) 0.306 — 大节点不保大 cov

### 修正

§4.3 provenance: "coverage monotone rise (§4.3, size-confounded)" → "coverage rise-to-plateau (0.259/0.264/0.278/0.358/0.352 — rises to 300 then plateaus; 719 is not higher than 300, so 'monotone rise' is not supported at n=8; size-confounded, cor=+0.563)"

### 论点影响 (净增强)

cov 和 mechanical depth 都在 300 后饱和 (depth 3-level step 0.8@300 起 sd=0) → 共同指向 "预算买广度, 边际递减", 与标题 Breadth-without-Depth 一致。plateau 比 monotone rise 更支持论文主张。

## 补充27 (2026-11-23 13:00): 控制臂 — LLM answer-depth 与机械 tree-depth 不相关 (r=+0.049)

### 发现

同一批 15 个 K7 budget-scan run, 每个 run 同时有:
- LLM depth 分 (judge_v2_depth.score_run 评 synthesis 答案文本, results-budget-scan.json)
- 机械 depth 分 (judge_v1 structure.depth_score 评树结构, judge-v1-budget-scan.json)

配对相关:
- cor(LLM, mech) = **+0.049** (t=0.18, df=13, p≈0.86) — 不相关
- LLM 在机械 3 档上平: 0.431/0.430/0.441 (mech 0.6/0.8/1.0)
- cor(LLM, budget) = +0.135 (不显著); cor(mech, budget) = +0.766 (强)
- cor(LLM, n_nodes) = +0.202 (t=0.74, 不显著) — 也非冗长偏袒

### 关键限定 (对象混淆, skill 第 11 条)

两轴评**不同对象**: LLM 评 prose 答案文本, 机械评树结构。所以 r=+0.049 只能证明
**answer-depth 不跟踪 tree-depth**, 不能证明 "LLM 无深度信号"。
正确读法: 两轴独立 + LLM 轴自身 n=3 无显著 budget 趋势 (150-vs-plateau 0.9 run-sd)
→ peak@150 读作 flat self-biased 轴上的 rubric noise, 而非已证明的 self-preference 机制。

### 过程坑

第一版 pearson 公式漏除 n, 算出 +0.735 (=15×真值); numpy 独立验证真值 +0.049。
没把 bug 当发现。

### 落盘

- 计算脚本: `research/llm-vs-mech-depth-control-arm.py` (承重数字规则, 可复现)
- draft 同步: abstract + §4.3 provenance + §4.3 末段 (3 处, commit 93ca6e8f1)
- skill workshop-number-audit: 10→11 条 (新增第 11 条 对象混淆)

## 补充28 (2026-11-23 13:10): (a)→(b) 耦合检验 — gap marking 不驱动 retrieval

### 动机

主目标 (AGI) 的核心机制 = (a)标缺口 → (b)检索 → (c)推理。paper finding #1 只测了
"monitoring 在 / repair 缺" (断点在 rework 循环)。本检验直接测 (a)→(b) 的耦合:
跨 run, 标缺口多的 run 是否检索更多?

### 结果 (rep-scan 15 run, GPU 域, 11-23 era)

- cor(gap_rate, retrieval_rate) = **+0.029** (t=0.10, p≫0.05)
- cor(gap_rate, post_retrieval_accuracy) = **+0.064** (t=0.23, p≫0.05)
- cor(retrieval, post_acc) = +0.368 (t=1.43, 也不显著)
- 两个量都有真实方差 (gap sd 0.050, retrieval sd 0.054) — 非"两平假不相关"

### 解读

断点比 finding #1 更靠前: 不止 repair 缺, 连 mark→retrieve 在 run 层面就不耦合。
模型以近乎恒定的 rate (~0.10, 预算不变, 补充21) 标缺口, 与实际检索量无关。
对 AGI 目标: (a) 在跑, 但 (a)→(b) 的触发链不存在 — 检索是 harness 固定节奏,
不是 gap 信号驱动的。

### 口径限定 (不直接进 paper)

- n=15, 单域 (GPU), 单 era (rep-scan); retrieval_rate 含 ~20% 疑似假 search tag
  (paper §3 provenance caveat), 是检索率上界
- paper 已 SUBMISSION-READY, 本发现作为候选: 可强化 finding #1 的断点定位
  (从 rework 循环前移到 mark→retrieve), 或进 §5 implication / future work
- 决定权在 D: ① 强化 finding #1 措辞 ② 只进 §5 ③ 留作后续 (跨域 49 run 复验后再定)

### 落盘

- 计算脚本: `research/gap-retrieval-coupling.py` (承重数字规则, 可复现)

## 补充29 (2026-11-23 13:40): (a)→(b) 方向反转 — 节点层面强耦合, run 层面假解耦

### 推翻补充28

补充28 在 run 层面测 cor(gap_rate, retrieval_rate)=+0.029 (ns), 结论"mark→retrieve 不耦合"。
这是**聚合谬误 (ecological fallacy)**: gap_rate 和 retrieval_rate 在每个 run 里都近乎恒定
(~0.10 / ~0.30), 耦合藏在 run 内部, 被聚合抹平。

### 节点层面真实结果 (15 rep-scan run, 3849 节点, GPU 域)

- 缺口节点 (DEFENSIVE_RE 命中): 391 个, **66.0% 是 source=search**
- 非缺口节点: 3458 个, 27.5% 是 source=search
- 两比例 z = **+15.55** (p<0.001), **15/15 run 全部 defensive > non-defensive**
- 缺口节点 source×status: search+degraded 占 **60.6%** (查了、没查全、标了缺口)

### 方向: (b)检索 → (a)批判, 不是 (a)→(b)

证据文本全是 `[质询]...参考来源仅提供了概述` / `来源未包含具体数值` — 这是**检索之后的
批判**, 不是检索前的触发。30% 缺口节点是 source=knowledge (没检索就标了缺口, 歧义:
真"不知道" vs 选择不去查)。

### 第三变量: level 分布

缺口标记集中在 L1/L2 (17.7%/17.2%), L3/L4 只有 9.2%/8.9% — 浅层 (规划/分支层) 多标缺口。

### 对 AGI 目标的意义

D 的 AGI 定义: (a)知道自己不知道 → (b)去查 → (c)推理。
实测: (a) 和 (b) 强相关, 但方向是 (b)→(a) (检索后批判), 不是 (a)→(b) (知道自己不知道→去查)。
模型不是"发现缺口→主动检索", 而是"按 harness 固定节奏检索→检索后批判标缺口"。
(a) 在跑, 但 (a)→(b) 的触发链不存在 — 检索是 harness 固定节奏, 不是 gap 信号驱动。

### 口径限定

- n=15 run / 3849 节点, GPU 域, rep-scan era (11-23); 单域单 era
- DEFENSIVE_RE 是文本匹配 (claim+evidence+corrected_claim), 不是模型显式声明
- 30% knowledge 源缺口节点方向歧义 (未检索就标缺口)
- 不进 paper (SUBMISSION-READY 不 destabilize); 候选: 强化 finding#1 断点定位
  (从 rework 循环前移到 mark→retrieve 方向反转), 或进 §5 / future work

### 落盘

- 计算脚本: `research/gap-retrieval-node-level.py` (承重数字规则, 可复现)
- 补充28 (run 层面) 结论被本条推翻, 保留原文供溯源

## 补充30 (2026-11-23 13:50): 跨域复验 — 方向反转不普适, 且 48 run 节点级数据不可恢复

### 跨域节点层面耦合 (3 域)

| 域 | run 数 | 缺口节点 | def search占比 | nondef search占比 | z | run def>nondef |
|----|--------|----------|----------------|-------------------|-----|----------------|
| gpu | 15 | 391 | 0.660 | 0.275 | +15.55 | 15/15 |
| nat | 1 | 7 | 0.857 | 0.132 | +5.32 | 1/1 |
| soc | 1 | 22 | 0.091 | 0.230 | **−1.52** | 0/1 |

**方向反转 (b)→(a) 不跨域成立**: soc 域是反的 (缺口节点 search 占比低于非缺口)。
gpu/nat 正, 但 nat 只有 7 个缺口节点 (n=1 run), 撑不起结论。

### 根因: 节点级数据 traceability 缺口 (与 0.147 同源)

83-run 语料 (metacog-budget-scan-v1.1.json) 记录 22 nat + 27 soc 个 run, 但每条只有
**run 级聚合** (n_defensive / n_search / source_counts), 无节点级字段。`file` 字段指向
通用名 (runs-s5-sm-nat.json), 而流式 run 文件已被覆盖 → 那 48 个 run 的节点级细节
(每个节点 source/status/claim) **不可恢复**。

磁盘上 nat/soc 各只剩 1 个主 run 文件 (runs-s5-sm-nat.json / runs-s5-sm-soc.json),
所以跨域节点层面检验实际只有 gpu 15 + nat 1 + soc 1 = 17 run, 其中 nat/soc 各 n=1。

### 结论 (诚实口径)

- 补充29 的方向反转是 **GPU 域单域发现**, 无法跨域确认 (48 run 节点级数据缺失)。
- soc 域方向相反, 提示 (a)↔(b) 耦合可能域依赖 (GPU 题的检索结构 vs 社科题不同),
  但 soc 只有 1 run, 不能下"域依赖"的结论, 只能标"未确认"。
- **对 AGI 目标**: (a)→(b) 触发链在 GPU 域不存在 (检索是 harness 固定节奏) 这一结论
  目前只在 GPU 域成立; 跨域推广需要重新跑 nat/soc 并保留节点级 checkpoint。
- **数据纪律教训**: 节点级分析必须在 run 落盘时保留 checkpoint (别被流式覆盖),
  否则事后无法做节点层面检验。这是 0.147 (run 级) 之后第二个 traceability 缺口,
  这次是节点级。

### 落盘

- 跨域脚本: 本条内联 (未单列, 因 nat/soc 各 n=1 不值得固化独立脚本);
  复现: 对 runs-s5-sm-{gpu,rep-scan,nat,soc} 各域跑 gap-retrieval-node-level.py 逻辑。

## 补充31 (2026-11-23 14:15): 重大纠正 — 方向反转三域普适, 补充30 结论全错

### 纠正对象

补充30 (b28ba91ff) 两个结论**全错**:
1. "48 nat/soc run 节点级数据不可恢复" — **错**。`checkpoints/archive/` 有 21 个 sm-nat-*
   + 21 个 sm-soc-* 归档, 每个含 r1/r2/r3 的 node.json 树 (完整 source/status/claim/
   evidence/corrected_claim)。nat 5836 + soc 10442 个 node.json 文件。
2. "soc 域方向反转不成立 (z=-1.52)" — **错**。那是磁盘上 runs-s5-sm-soc.json 单文件
   (旧快照/不完整) 的假象。archive 全量 soc 数据: z=+7.58 强正。

### 根因 (第 17 类错误: 未验证 archive 就断言"数据不可恢复")

补充30 只看磁盘上的主 run 文件 (runs-s5-sm-{nat,soc}.json) 和 83-run 语料的 run 级
聚合, 没查 `checkpoints/archive/` 就断言"节点级不可恢复"。违反红线"可验证声明必须
直接验证 (grep)"。教训: **断言"数据缺失/不可恢复"前, 必须 find 全仓库 (含 archive
目录)**。

### 三域节点层面耦合 (全量 archive 数据)

| 域 | unique 节点 | 缺口节点 | def search占比 | nondef search占比 | z |
|----|------------|----------|----------------|-------------------|-----|
| gpu | 3849 | 391 | 0.660 | 0.275 | +15.55 |
| nat | 4513 | 115 | 0.365 | 0.148 | +6.39 |
| soc | 8023 | 514 | 0.393 | 0.243 | +7.58 |

**三域全部显著正相关 (p<0.001)**。方向反转 (b)检索→(a)批判 **跨域普适**, 不是 GPU
单域现象。缺口节点 search 占比在三域都显著高于非缺口节点 (差 +0.22 ~ +0.39)。

### 对 AGI 目标的意义 (升级)

- 补充29 的结论从"GPU 单域"升级为**三域普适**: (a)↔(b) 节点层面强耦合, 方向
  (b)→(a) (检索后批判), 不是 D 定义的 (a)→(b) (知道自己不知道→去查)。
- 检索是 harness 固定节奏, 不是 gap 信号驱动 — 这个结论现在跨 3 域 16385 节点成立。
- **候选发现强度大增**: 从"单域 n=15"升级为"三域 n=16385 节点", 足以考虑进 paper
  (finding#1 的加强版, 或独立 finding)。待 D 定 placement。

### 落盘

- 计算脚本: `research/gap-retrieval-cross-domain-archive.py` (承重数字规则, 可复现)
- 补充30 的"不可恢复"结论作废, 保留原文供溯源
- 补充29 的"GPU 单域"限定作废, 升级为三域普适

## 补充32 (2026-11-23 14:50): DEFENSIVE_RE 域偏倚 — "不确定"技术术语污染, 清洗后方向反转仍三域显著

### 发现

metacog_axis.DEFENSIVE_RE 把数学技术术语"不确定" (uncertainty 概念) 误判为防御性语言。
nat/soc 的缺口文本大量是 "不确定性高" / "σ_pref 正相关" / "量化不确定性" (数学概念),
GPU 的缺口文本是 "[质询]...参考来源仅提供了概述" (真检索批判)。

### 域偏倚量化 (DEFENSIVE_RE 命中里"仅不确定"占比)

| 域 | DEF命中 | 真防御性 | 仅"不确定"(技术) | 占比 |
|----|---------|----------|------------------|------|
| GPU | 391 | 331 | 60 | 15% |
| NAT | 115 | 89 | 26 | 23% |
| SOC | 514 | 299 | 215 | **42%** |

SOC 域 42% 的"缺口"是技术术语 — gap_rate 指标在社科域被系统性高估。

### 清洗后三域 (a)↔(b) 耦合 (真防御性 vs 非, search 占比)

| 域 | def | def_search | nondef_search | diff | z |
|----|-----|-----------|---------------|------|-----|
| GPU | 331 | 0.710 | 0.277 | +0.433 | +16.24 |
| NAT | 89 | 0.461 | 0.147 | +0.314 | +8.13 |
| SOC | 299 | 0.542 | 0.241 | +0.300 | +11.73 |

**清洗后三域仍全部显著 (p<0.001)** — 方向反转 (b)→(a) 结论成立, 但强度数字变化:
- GPU def_search 0.660→0.710 (技术术语节点 search 占比低, 剔除后真防御子集更纯)
- 三域 diff 收窄到 +0.30~+0.43 (原 +0.22~+0.39, 因分母人群变了)

### 对 paper 的影响

- gap_rate 核心数字 (0.099/0.100/0.107, ANOVA F=0.036) 基于 DEFENSIVE_RE, GPU 域
  15% 技术术语 → gap_rate 高估约 15%。
- **budget 不变性结论不受影响**: 偏倚在各预算档一致 (同一模型同一 prompt), 不改变
  "跨档平坦"的形状。ANOVA 的 F 值会因整体 scale 变化, 但"不显著"的结论稳健
  (F=0.036 离显著阈值很远, 15% scale 变化不会把它推过阈值)。
- **跨域比较受影响**: nat/soc 的 gap_rate 不可与 GPU 直接比 (SOC 42% 污染 vs GPU 15%)。
  任何"GPU 域 gap_rate 高于/低于社科域"的声明都是偏倚产物, 不是真差异。
- **建议**: ① paper §6 limitations 加一句 DEFENSIVE_RE 的域偏倚 (SOC 42% 技术术语);
  ② 跨域 gap_rate 比较声明 (如有) 必须标注偏倚; ③ 长期: 用 LLM 分类替代正则
  (区分"防御性语言" vs "数学 uncertainty 概念"), 但这是新实验不是改稿。

### 落盘

- 计算脚本: `research/defensive-re-domain-bias.py` (承重数字规则, 可复现)
- 清洗口径: NO_UNCERTAIN 正则 (DEFENSIVE_RE 去掉"不确定")

## 补充33 (2026-11-23 15:10): finding (2) 生死检验 — 清洗后 nat<soc 不显著, abstract 必须降级

### 背景

Abstract finding (2) (唯一跨域 finding) 声明: "the defensive-marking rate rises
monotonically with question difficulty (nat 0.025 < soc 0.056 < gpu 0.119,
era-matched, all pairwise p<0.001), the signature of calibrated uncertainty
monitoring." 这是基于原始 DEFENSIVE_RE 的跨域 gap_rate 水平比较。

补充32 证明 DEFENSIVE_RE 在 SOC 域 42% 命中是数学 uncertainty 技术术语。本条
用清洗口径 (NO_UNCERTAIN) 按 run 重算 era-matched (sm-era, Nov20-21, budget=150)
的跨域 Mann-Whitney。

### 结果 (run 级, 清洗口径, n_runs=21/26/18)

| 域 | n_runs | raw gap_rate | clean gap_rate |
|----|--------|--------------|----------------|
| nat | 21 | 0.0243 | 0.0181 |
| soc | 26 | 0.0572 | 0.0298 |
| gpu | 18 | 0.1176 | 0.0999 |

Mann-Whitney (清洗):
- nat vs soc: z=-1.82 **ns** (原 p=0.0003 由技术术语驱动)
- soc vs gpu: z=-4.68 显著
- nat vs gpu: z=-4.87 显著

### 结论

数值顺序 nat < soc < gpu 保持, 但 "monotonically, all pairwise p<0.001" 不成立:
nat<soc 这一环在清洗后不显著。finding (2) 必须降级为:
"increases with question difficulty (ordering nat < soc < gpu holds; the two
comparisons against the hardest domain are significant, soc<gpu and nat<gpu
p<0.01; the nat<soc step is ns after removing the detector's domain-specific
inflation by the uncertainty term)".

### 落文

- abstract finding (2) 降级 (raw 0.025/0.056/0.119 保留但标注 raw detector; 加
  清洗后 ordering 保持 + nat<soc ns 的限定)
- §4.2 表加清洗列 + correction 注
- §4.2 honest boundaries 加清洗 caveat
- §6 域偏倚 limitation 已含 (补充32)
- 计算脚本: `research/finding2-difficulty-gradient-cleaned.py`

### 影响评估

finding (2) 从"4 个 findings 之一 (唯一跨域)"降级为"跨域 ordering 保持但
nat<soc 环不显著"。不删除 (ordering + gpu 端显著仍成立), 但强度下降。这是
诚实口径, 不是过强声明。

## 补充34 (2026-11-23 15:35): 清洗后 budget 不变性更强 — ANOVA F 0.036→0.003

### 动机

补充32/33 发现 DEFENSIVE_RE 域偏倚。metacog_total = 0.4·gap_rate + 0.3·retrieval_rate
+ 0.3·post_retrieval_accuracy, gap_rate 是 40% 分量。若 gap_rate 被高估, metacog_total
绝对值也被高估; 且 gap_rate 的 ANOVA (F=0.036) 该用清洗口径复验。

### 结果 (生产 compute_metacog, monkeypatch DEFENSIVE_RE=NO_UNCERTAIN, 15 rep-scan run)

| budget | gap_rate (raw) | gap_rate (clean) | metacog_total (raw) | metacog_total (clean) |
|--------|----------------|------------------|---------------------|-----------------------|
| 100 | 0.0992 | 0.0894 | 0.2456 | 0.2417 |
| 150 | 0.1001 | 0.0878 | 0.2465 | 0.2416 |
| 300 | 0.1075 | 0.0868 | 0.2323 | 0.2240 |

- raw 口径复现 draft (0.246/0.247/0.232) ✓
- 清洗后 metacog_total 形状不变 (flat-to-mildly-declining, 300 档 dip 仍由 r8 驱动)
- **ANOVA gap_rate: raw F(2,12)=0.0360 → clean F(2,12)=0.0031** — 清洗后更接近纯零,
  budget 不变性结论更强

### 结论

detector 域偏倚**不削弱** budget 不变性结论, 反而强化它:
- 不变性声明在 gap_rate 分量上 (draft 已正确 scope 在 gap_rate, 非 metacog_total)
- 清洗后 gap_rate 跨档更平坦 (F 从 0.036 降到 0.003), "budget effect below noise
  resolution" 的声明更稳
- metacog_total 绝对值 (0.246/0.247/0.232) 是 raw 口径, 清洗后 0.242/0.242/0.224,
  形状一致 — draft 未声称 metacog_total 是 clean component (已正确标注 gap_rate 才是)

### 落文

- §4.3 provenance 加一句清洗对照 (gap_rate ANOVA F 0.036→0.003, invariance 更强)
- 计算: 本条内联 (monkeypatch compute_metacog), 复现: 对 15 rep-scan run 跑
  compute_metacog 两次 (raw DEFENSIVE_RE / NO_UNCERTAIN)

## 补充35 (2026-11-23 16:00): finding (4) 清洗后 3/3 仍成立 — 偏倚审计闭环

### 动机

DEFENSIVE_RE 偏倚 (补充32/33) 打中 finding (2) (跨域难度梯度, nat<soc 环 ns)。
finding (4) 也用了 gap-marking rate 跨臂比较 ("checkpoint arm raises gap-marking
rate, 3/3 reps")。必须验证清洗后是否仍成立。

### 结果 (idea2 6 run, A=fresh / B=checkpoint)

| rep | B_raw | A_raw | B>A raw | B_clean | A_clean | B>A clean |
|-----|-------|-------|:-------:|---------|---------|:---------:|
| r1 | 0.1397 | 0.0633 | ✓ | 0.1247 | 0.0443 | ✓ |
| r2 | 0.1436 | 0.0660 | ✓ | 0.1338 | 0.0457 | ✓ |
| r3 | 0.0995 | 0.0690 | ✓ | 0.0871 | 0.0598 | ✓ |

**清洗后 3/3 仍 B > A** — finding (4) 的 gap-marking 声明对 DEFENSIVE_RE 偏倚稳健。

### 偏倚审计闭环 (4 findings)

| finding | 涉及跨域/跨臂 gap_rate? | 清洗后状态 |
|---------|:----------------------:|-----------|
| (1) monitoring present, repair absent | 否 (GPU 域内, 84% 分类 + 1.6-2.1% rework) | 不受影响 |
| (2) gap difficulty gradient | **是** (跨域 nat/soc/gpu) | **降级** (nat<soc 环 ns, 补充33) |
| (3) budget breadth-not-depth | 否 (GPU 域内, L4 0/21 + gap_rate ANOVA) | 不受影响 (ANOVA 反而更强, 补充34) |
| (4) checkpoint trades cov for metacog | **是** (跨臂 A/B gap rate) | **稳健** (3/3 清洗后仍成立) |

唯一被偏倚打中的是 finding (2), 已降级 (不删除, ordering + gpu 端显著仍成立)。
