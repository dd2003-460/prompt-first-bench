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
