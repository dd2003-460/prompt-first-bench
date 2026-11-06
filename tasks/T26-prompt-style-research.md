# T26 — Prompt 风格维度调研：拟人引导（激励/PUA/混合）× 机械，对任务完成质量的影响

> origin: ai · 2026-11-06 · 成璐指令"直接开设然后 push 到 pfb，记得先外包调研"
> 定位：pfb 新子模块的**调研任务书**。本文件是派给 arena agent mode 的任务卡，不是结论。
> 前置发现（本仓内证据，供调研时参考）：S1 臂（decomp 五步法，n=15）vs S0 裸 prompt：mean Δ=+0.014, p_sign=1.0，不显著——"分解没用"可能恰恰因为门禁没做好（review loop 从未执行），也可能是纯 prompt 结构本身增益有限。T23-v2 hetero-judge 显示 H1（分解增益）在同源 judge 下 +0.129、异族 judge 下 -0.187——judge 依赖性极强。本调研要回答：**换个维度（语言风格/情绪向量）是不是比换结构更有效的杠杆？**

## [任务]

回答三个具体问题（每个都要有来源 + conf）：

1. **有没有实证研究**测量过 LLM 在长链推理/多步任务中，prompt 里加入"拟人化激励语"（鼓励、目标函数式奖励暗示、阶段性肯定）或"PUA 式打压语"（负面反馈、失望表达、施压）对**最终任务质量**（不是单轮回复满意度）的影响？区分：(a) 单轮 QA (b) 多轮 agentic 任务 (c) self-refine/critique loop 内部。
2. **"模型有拟人倾向所以激励有效"这个机制假设，证据强度如何**？是相关还是因果？有没有消融实验证明去掉激励句后分数下降（而不是激励句恰好同时改变了信息量/长度/格式）？
3. **可操作的 prompt 设计建议**：如果要做一个"分阶段任务 + 每阶段质检"的 pipeline，在哪些位置放什么风格的话术（激励 / PUA / 中性机械 / 混合）有依据支持？给出具体句式模板 + 预期作用机制 + 风险（如 reward hacking、模型顺从性偏差 sycophancy 放大）。

## [背景]

- 场景：本地 27B 模型跑 4 阶段研究 pipeline（分解→调研→核验→终审），每阶段独立 LLM call，阶段间传工件。
- 现状：所有阶段 prompt 都是机械 checklist 风格。我们想测"分解阶段用引导+激励话术、检查阶段用机械话术"是否比全机械更好。
- 候选话术示例（待调研验证哪种有效）：
  - 激励式："你刚才准确完成了第一层分解，这说明你已经抓住了问题的骨架。现在继续往下切第二层——你离完整覆盖已经很近了。"
  - PUA 式："如果这一层的维度划分不准确，后面所有阶段都是在垃圾地基上盖楼。我很遗憾看到这种粗糙的切分。重新来。"
  - 标注+回补式："碰到你没有先验知识的领域很正常，先把它标进空缺清单，等调研回来再补。留空不是失败，假装知道才是。"
  - 机械式（对照）："检查正交性：每两个维度必须能指出独占参数。不满足则合并或重切。"
- 已知混淆：激励句往往同时增加 token 数、改变输出格式、注入额外约束——做实验时必须控制这些变量（调研时注意文献是否控制了）。

## [约束]

- 中文回答；每条结论标 conf(0-1)；给来源 URL（arXiv/GitHub/官方博客优先）；不确定的标"未验证"
- 重点找 2024-2026 的工作（sycophancy、RLHF reward hacking、agentic prompting、self-refine 改进方向）
- 经典工作也要：Anthropic/OpenAI 的 helpful-honest-harmless 对齐文献里关于"语气影响服从度"的部分

## [交付]

markdown，≤60 行核心 + 附录：

```
## 核心发现（≤20 行）
| # | 问题 | 结论 | conf | 来源 |
|---|------|------|------|------|
| 1 | ... | ... | 0.x | url |

## 关键数字
- （效应量、样本量、任务类型）

## 可操作建议（带模板）
- 位置 X 放 Y 风格，机制 Z，风险 W

## 附录：完整来源列表
```

## [检索入口建议]（你可以改，不必照抄）

- arXiv: "sycophancy LLM", "reward hacking language model", "agentic prompting effectiveness", "self-refine improvement", "LLM persuasion compliance", "in-context motivation language model performance"
- GitHub: 搜 "prompt style ablation" / "persona prompt benchmark" 类 repo
- 关注：sycophancy 文献（Sharma et al. 2023, Anthropic）、"LLMs are overconfident" 类校准文献、multi-agent debate 里 critic 语气的作用

## [落盘约束]

- 交付物写到 `lit-survey/t26-prompt-style-research.md`（本仓库）
- 完成后回执必须含 repo URL + branch + commit_sha
- 文件不存在 = 任务未完成，Lead 不验收

## [正交性自检]

本子领域与 S9H（流程结构消融）正交：S9H 测"几次 call + 有无回退"，本调研测"每次 call 里的语言风格"。两轴独立，可并行。