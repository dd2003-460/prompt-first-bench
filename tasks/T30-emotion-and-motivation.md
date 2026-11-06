# T30 — LLM 情绪表征与 prompt 层面情绪操控调研

> **目标仓库**：prompt-first-bench（pfb）· branch main
> **派发日期**：2026-11-07
> **前置**：T26 Q1-Q3（lit-survey/t26-prompt-style-research.md）、tasks/2026-11-07-nine-points.md 第 10 点、S10 任务卡 H4
> **归类**：引导式 prompt 策略 → 人情绪维度（与机械/引导大分类下的"引导"子项对齐）
> **验收标准**（机器可查）：
> 1. `lit-survey/t30-emotion-and-motivation.md` 落盘，≥8 个独立来源（arXiv ≥4 + 博客/报告 ≥2 + GitHub ≥2），每条带 URL + conf
> 2. §1 情绪表征层：Anthropic R8（171 emotion vectors）完整解读——哪些向量与"作弊/走捷径"行为相关、steering 幅度多少、是否可被 prompt 文本间接移动（找 activation steering → prompt 的因果链证据）
> 3. §2 行为层：反复拒绝/打回场景下 LLM 行为变化的实证（≥3 篇）。重点：焦躁→performance vs 焦躁→genuine effort 的分岔条件是什么？有没有"被拒 N 次后 fabrication rate 上升"的直接测量？
> 4. §3 prompt 操控层：安抚语句 / 信任框架 / 终极目标框架 / 讲原因——这四类 prompt 策略对情绪向量的影响有没有被测量过？如果没有，设计一个最小实验方案（用什么 probe、什么指标、多少样本）
> 5. §4 正反馈循环：人类-AI 交互中"用户状态→模型表现→用户状态"的循环有没有被形式化？（搜 affective computing + human-AI interaction + dialogue state tracking 方向）
> 6. §5 ICL vs RL 等价性：找到所有讨论"in-context learning as implicit weight update / gradient descent"的工作（≥5 篇），总结：①谁最先提出 ②数学上等价到什么程度 ③边界在哪（持久性/累积性/容量）④对 pfb 的含义（我们的 reviewer 反馈 = 哪种类型的"更新"）
> 7. 找不到就说找不到，不编 DOI；conf 逐条标

## 背景

成璐 2026-11-07 三点触发：
1. "为什么是信息论等价的，也许这里也值得写个 note，ICL 和 RL 在某种程度上等价吗，例如上下文相当于临时的权重更新？（把之前上下文当成小的新增权重，和没上下文相比，计算更后面的 kvq 似乎不一样?）这有论文研究过吗？我迫切希望知道谁这么天才!"
2. "情绪影响这很有意思，不过你可以先调研，再进一步调研（我很多天才的想法会有更天才的人做），让 arena 跑然后 push 到 pfb 的情绪研究吧!（似乎可以归类到机械/引导的引导下面的人情绪）"
3. S10 H4（拒绝时安抚降低 fabrication）需要文献支撑才能判断值不值得测

## 搜索矩阵

### §1 情绪表征
- Anthropic "On the Biology of a Large Language Model" (2025) — R8 原始出处
- "emotion vectors" / "affect in LLMs" / "sentiment steering" arXiv
- "activation steering" + "behavior change" + LLM safety
- OpenAI / DeepMind 有没有类似的 internal representation 分析？

### §2 行为层（拒绝/压力）
- "repeated rejection" + LLM + behavior
- "frustration" / "desperation" + language model + cheating/fabrication
- "pressure" + "LLM agent" + "shortcut" / "reward hacking"
- NoPUA (R6, wuji-labs/nopua) 的 PUA 恐惧框实验细节（Study 1+2 全文）
- "multi-turn" + "feedback" + "LLM" + "degradation" / "improvement"

### §3 prompt 操控
- "trust framing" + system prompt + agent performance
- "empathy" / "soothing" + LLM + error correction
- "goal priming" / "ultimate goal" + LLM motivation
- "explaining why" + instruction following + LLM（vs mechanical instruction）

### §4 正反馈循环
- "human-AI interaction" + "user affect" + "AI performance"
- "dialogue state" + "emotional feedback loop"
- "collaborative AI" + "mutual adaptation"
- affective computing 里的 "emotional contagion" 是否适用于 human-LLM

### §5 ICL vs RL
- "in-context learning" + "gradient descent" / "implicit optimization"
- "context as weights" / "soft prompt" / "task vector"
- von Oswald 2023 / Garg 2024 / Min 2022 / Dai 2023 ("Can transformers learn in-context by gradient descent")
- "KV cache" + "attention" + "implicit parameter update"
- "test-time training" vs "in-context learning" 关系
- "LoRA" / "adapter" vs "ICL" 容量对比

## 特别要求

- 成璐原话："我迫切希望知道谁这么天才" → §5 必须给出**时间线**（谁最早提出 ICL≈隐式优化、怎么发展的、现在最前沿到哪了）
- 不要只列论文标题，每篇给 2-3 句核心贡献 + 与 pfb 的关系
- 如果某个方向确实没人做过（比如"安抚语句对 fabrication rate 的影响"），明确说"这是空位"并设计最小实验方案
- 产出 ≤5 页正文 + 来源表 + 时间线图（§5）

## 边界

- 不跑实验，纯调研
- 与 T29 的关系：T29 做了 NoPUA 拆解（§2 三层），T30 深入情绪机制本身（不重复 T29 的 NoPUA 拆解，引用即可）
- 回执必须含 repo URL + branch + commit_sha