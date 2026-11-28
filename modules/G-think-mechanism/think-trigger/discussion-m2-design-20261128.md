# origin: ai
# M2 讨论卡 — 思考机制注入设计（Lead ↔ cc 讨论用）

## 背景（读这些文件，别凭我转述）
1. 5 模板定义：/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-persona-align/memory/general-thinking-template-20261124.md
2. 第一性原理：/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-persona-align/memory/d-thinking-mechanism-first-principles-20261124.md
3. OOD 判决（已定格）：/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/G-think-mechanism/oood-general-probe/oood-column-status.md
4. 生产 prompt（剥离域味版 S1）：/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1/prompts.py
5. 任务表：/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/G-think-mechanism/think-trigger/decomposition.md（M 节）

## 已知实证（硬约束，设计不能违背）
- T2 实验：27b 能复刻"爬一层"的**形式**（机械分 5.67/6），但**内容** 100% 域偏移——形式注入有效，机制注入无效。
- OOD K4b 判决：域味 prompt = 负资产（S1 剥离版 ≥ S0 域味版），kernel 本身是 general 的。
- 执行环境：本地 qwen3.8-27b（vLLM, 8787），单实例，40 节点/臂，无检索口径。

## 要你回答的设计问题（逐条，带你的推理，别只给结论）
Q1. **注入位置**：5 模板（代价模型/统一覆盖/量化落地/类比审计/判据瓶颈）该注入到 prompts.py 的哪个 prompt 的哪个位置？读 prompts.py 后给具体行号级建议 + 理由。哪些模板适合注入、哪些不该（会干扰现有机制）？
Q2. **形式 vs 内容**：T2 证明形式能注入、内容域偏移。你的机制假说：27b 缺的是什么（知识？检索？推理深度？prompt 锚定不足？）？最便宜的判别探针是什么（一次实验能区分"机制没激活"vs"机制激活了但知识不够"）？
Q3. **实验设计**：V0(S1 现状) / V1(+5 模板) / V2(调研 top 机制，待定) × 3 域(气象/硬件/埋雷) × 2 reps × 40 节点。样本量够吗？判据怎么设才算"机制真的落地"（不是形式模仿）？给出可计算的机械指标定义（机制覆盖率/量化 claim 密度/域偏移率怎么从 transcript 算）。
Q4. **失败预案**：如果 V1 只提升形式分不提升内容分，下一步最该做什么（换注入方式？换模型能力假设？放弃 prompt 级走 hook 级）？

## 输出要求
- 写到 /Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/G-think-mechanism/think-trigger/cc-design-review-20261128.md
- 每个 Q 一节，≤15 行/节，中文，带 conf(0-1)
- 最后加一节"反对 Lead 可能倾向的地方"（你的独立判断，哪怕和我预设相反）
- 不要改任何生产文件，只写这一个输出文件
