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
