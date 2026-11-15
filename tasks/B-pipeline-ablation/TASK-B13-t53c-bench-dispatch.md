# T53-C — deepresearch 泛化 bench（arena 执行）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 目标

用 `experiments/stage-ablation/s5_state_machine.py`（Lead 已写好）跑 5 道 deepresearch 题，记录节点数/轮数/核验率/返工次数/judge 分。对照 3 个基线。

## 题目（5 道，多跳+事实混合）

1. "2024 年 NVIDIA H200 GPU 的 TDP 是多少瓦？比 H100 SXM 高多少百分比？"
2. "Transformer 原始论文中 multi-head attention 的 head 数是多少？GPT-3 用了多少？差几倍？"
3. "HotpotQA 数据集有多少条标注？其中 compositional 类型占多少比例？"
4. "LLaMA 2 70B 的参数量是多少？训练用了多少 token？"
5. "DeepSeek-V3 的 MoE 总参数和激活参数分别是多少？ratio 是多少？"

## 基线

- B1: v17 无限预算 (`s5_hierarchy.py`)
- B2: 朴素 CoT（无分解，直接 call_llm 答题）
- B3: 固定 3 层分解（max_depth=3, 无目标函数停止）

## 输出

每题一个 JSON: `{qid, method, n_nodes, n_rounds, verify_rate, rework_count, judge_score, leak_hits}`
汇总到 `experiments/stage-ablation/runs/t53-bench/summary.json`

## Judge

用 B-face (localhost:1234, qwen2.5-7b) 对最终答案打分 0-1（rubric: 数字正确 0.5 + 单位/对比正确 0.5）。

## 失败降级

状态机跑不通 → 报告具体报错 + 哪一步挂了，不要自己改代码。
Judge 不可用 → 标 judge_score=null，人工后补。