# 02 信息调研：公开证据

观察日期：2026-10-22 UTC（系统日期）。预算：5个实质来源（上限10）。网页 LLM：`ralph` 与 `ego-browser` 均未安装（`command -v` 无输出），故规定的 `ralph prompt-first web-llm` 无法运行；记录通道限制后继续公开来源检索。Arena 多模型对战不可由当前会话工具发起，留待 cross-check 限制。

## 研究发现（证据线索，非最终因果结论）

1. **Meta-Task Planning for Language Agents**，arXiv:2405.16510（2024）。摘要报告 TravelPlanner 平均约40% success，对比 SOTA baseline 2.92%；API-Bank 较 LLM(api)-4 + ReAct 高约14%。来源：https://arxiv.org/abs/2405.16510 。这是特定多智能体分层任务规划系统与基线的系统级对比，不能隔离“prompt-first 01–04.5”或正交/完备、门禁等组件；任务/实现差异可能混杂。数值以摘要为准，未独立复算。
2. **Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks**，arXiv:2503.09572（2025）。报告 WebArena-Lite 57.58%、WebVoyager 81.36%（其表格还列出不同方法/模型结果，如 QWQ-32B 81.36、Llama-3.1-8b 58.08）。来源：https://arxiv.org/abs/2503.09572 。专门训练的 planner、合成数据和执行机制共同变化，不能归因于纯提示拆解；对照可比性需全文确认。
3. **An Approach for Systematic Decomposition of Complex LLM Tasks (ACONIC)**，arXiv:2510.07772（2025）。摘要/检索页报告 SATBench Claude 49.3→58.1%，LLaMA 21.5→36.5%；来源：https://arxiv.org/abs/2510.07772 。与任务复杂度度量相结合的特定分解方法提供正向线索，但不是 prompt-first 全流程；摘要数字及统计不确定性未经本文逐表复核。
4. **Agentic LLM Planning via Step-Wise PDDL Simulation: An Empirical Characterisation**，arXiv:2603.06064（2026）。检索页结果报告 agentic 方法在一组比较中 success 20%，direct 方法 50%；来源：https://arxiv.org/abs/2603.06064 。构成反例线索：规划/代理化不保证提升，且须核正文了解任务配置与样本，当前未核实细节。
5. **Plan-and-Execute Agents**（LangChain 官方说明，GitHub/LangGraph 生态），https://www.langchain.com/blog/planning-agents 。描述 planner 生成多步计划、executor 执行、replanner 根据结果修订。说明框架机制可实现，不提供同条件随机对照效果。
6. **Microsoft AutoGen** 官方文档“Task Decomposition”，https://microsoft.github.io/autogen/0.2/docs/topics/task_decomposition/ 及 repo https://github.com/microsoft/autogen 。文档给出二 agent/group chat 等分解实现；GitHub 当前标注项目 archived/no longer maintained（该状态不影响其作为历史机制证据）。不属于分解质量的因果评估。

## 来源与限制
- 公开搜索得到摘要/官方页面线索；部分 arXiv 页面未经直接全文抓取/逐表核验。以上统计标为“检索摘要报告”，不当作高确定性证据。
- 系统级代理/规划对比的 treatment 不一致：可能同时加入额外模型调用、训练、执行工具、反馈回路；成功率定义与基准不同，不能横向汇总或转成 prompt-first 效应量。
- 未发现公开证据直接测试 1-loop 全套，或正交完备、交叉验证、落盘门禁、反方复核分别带来的边际效果；也未发现可支持强/中/弱模型收益交互的匹配消融。
- 阶段 02 暂定结论：方向性证据混合且间接；转入 02.5 独立性/反例核验。

搜索来源为 web_search，搜索词含：`LLM agents task decomposition direct baseline success rate empirical`、`GitHub LangGraph plan and execute`、`AutoGen task decomposition`。