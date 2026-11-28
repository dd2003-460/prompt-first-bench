# M0 调研报告 — general 推理成熟机制（A prompt级注入 / B 评测方法 / C 开源实现）
> 2026-11-27 · 执行：arena 会话（绑定分支 arena/f8477718-prompt-first-bench）
> **留空声明①（任务书缺失）**：指定任务书"M0"在 thinkmech-review 分支全历史不存在（实核：d92374e61 与 HEAD 9dd75445c8d046c2dfdf2136beda8ed76c6fd2c0 两时点 `git grep "M0"` 零命中；experiments/stage-ablation/ 与 modules/G-think-mechanism/think-trigger/ 下仅有 T54/T8c/J3a 系列）。本报告按派发消息内规格（三类：A prompt级注入 / B 评测方法 / C 开源实现）重建执行。
> **留空声明②（分支约束）**：会话硬约束禁止 push 到非绑定分支——本报告落盘于 arena/f8477718-prompt-first-bench 同路径，移植命令：`git fetch origin arena/f8477718-prompt-first-bench && git cherry-pick <本commit>`。
> **留空声明③**：会话从未收到过该 M0 任务的此前派发（对话历史：IDEA-review 五轮 + #10 分解树 + 闭式 paper 核验 + thinkmech 只读 review）；"TMLR review"=上轮已完成（只读）；"hermes-workspace-zero"无本会话记录，未混入。

## A. Prompt 级注入（零训练激活已有推理程序，按改动量小→大排序）

| # | 机制 | 触发/做法 | 为什么能激活已有能力 | 证据（URL，本次实检） | conf |
|---|---|---|---|---|---|
| A1 | Zero-shot CoT 触发词 | "Let's think step by step" 单短语 | trigger 短语把模型推入推理分布模式——能力已在参数中，prompt 只改条件分布 | mlanthology.org/iclr/2024/zheng2024iclr-take/ 相关综述引；Kojima et al. 2022（窗口外锚点） | 0.9 |
| A2 | 抽象升级触发（Step-Back） | 具体问题→先问高层概念/原理再作答 | 把"实例级检索"重定向到"原理级检索"，激活泛化程序而非模式匹配 | Take a Step Back, ICLR 2024, https://mlanthology.org/iclr/2024/zheng2024iclr-take/（MMLU 物理+7%/化学+11%、TimeQA+27%，数字**未验证**） | 0.85 |
| A3 | 分解触发（Least-to-Most/Plan-and-Solve） | 先拆子问题再逐个解 | 跨越 easy-to-hard 泛化缺口：子问题落在已掌握分布内 | Least-to-Most SCAN 99.7% vs CoT 16.2%；papers.lunadong.com/area/reasoning 汇总 | 0.85 |
| A4 | 注入式解码（AID） | 模型要提前 <eos> 时插入短注入短语阻止早停 | 解锁 latent reasoning 无需显式 prompt——直接证据表明"已会但默认不用"可被最小注入翻转 | Adaptive Injection Decoding, ACL 2025 Findings, https://aclanthology.org/2025.findings-acl.520.pdf | 0.8 |
| A5 | 输出 schema 约束 | 要求证据字段带 f(参数±Δ) 形式（pfb P3 verify 设想） | 对输出格式提要求≠注入新知识，逼迫模型调用已有参数敏感性程序 | T54 任务书背景（内部）；外部对应物=结构化 CoT（未找到同构文献，gap 声明见 §D） | 0.6 |
| A6 | 知识选择转向（SpARE，激活级非 prompt 级，边界标注） | 残差流 steering 控制用 parametric 还是 contextual | 证明"知识选择行为"可被外部信号控制——机制层证据但需白盒，非 prompt-only | SpARE, NAACL 2025, https://aclanthology.org/2025.naacl-long.264.pdf | 0.75 |
| A7 | 信息增益驱动的提问/行动选择（UoT/BALAR） | 以 expected MI 选下一个动作 | 把"要不要调用贝叶斯更新"变成显式选择目标而非默认倾向 | arXiv:2402.03271（NeurIPS 2024）；arXiv:2605.05386（BALAR, 2026-05）——复用 IDEA-review 第四轮实核 | 0.8 |

## B. 评测方法（"general 推理成熟度"怎么测）

| # | 方法 | 测什么 | 证据 | conf |
|---|---|---|---|---|
| B1 | ARC-AGI-2 抽象泛化评测 | 最小演示下的规则归纳，对抗性构造抗污染，测"fluid intelligence"而非知识覆盖 | ARC Prize 2025 技术报告 https://arxiv.org/pdf/2601.10904（2026-01-19；ARC-AGI-3 2026 年初发布标计划）；top score 24% **未验证** | 0.85 |
| B2 | 知识冲突探针（会但不用现象的测量学） | parametric vs contextual 知识选择行为、指令抑制失效 | What Is Seen Cannot Be Unseen https://arxiv.org/html/2506.06485v1（2025-06-06）；counterfactual 线 arXiv:2506.15732 | 0.8 |
| B3 | 跨域零样本迁移曲线（pfb 现行） | nat/soc/gpu 三域 cov/逐点命中率 + 预算轴 | pfb 内部（T53b/ae3d88611）；学术对应=OOD generalization eval（未深查，标注） | 0.7 |
| B4 | 预算约束下的推理评测（accuracy under budget） | ARC 系核心口径：不只 accuracy，而是预算内 accuracy——直接可借为"成熟度=预算效率"定义 | 同 B1（"accuracy under budgeted inference"） | 0.8 |

## C. 开源实现（可直接接 pfb 的）

| # | 实现 | 提供什么 | 证据 | conf |
|---|---|---|---|---|
| C1 | Tree of Thoughts 官方（princeton-nlp/tree-of-thought-llm） | ToT 搜索骨架（BFS/DFS+LLM 评估器），论文 2023 窗口外但实现持续维护（维护状态**未验证**） | 本轮未直抓 repo（GitHub 经 API 故障期），引用自检索汇总页 papers.lunadong.com/area/reasoning——**未验证**，接入前须实核 | 0.6 |
| C2 | LangGraph（MIT 开源） | stateful graph workflow+checkpoint+human-in-the-loop，T1 思考触发 hook 的宿主候选 | https://www.langchain.com/langgraph（官网实检） | 0.85 |
| C3 | 框架族谱（Agno/CrewAI/OpenAI Agents SDK/Google ADK/AutoGen→MS Agent Framework） | 2026 开源 agent 框架全景：多为 workflow 编排，无一内置"思考触发/成熟度评测"——pfb 差异化空间 | https://www.ayautomate.com/blog/best-open-source-ai-agent-frameworks（2026-11-23） | 0.7 |

## D. Gap 声明与反证
- **gap-1**：「输出 schema 约束激活参数敏感性分析」无同构文献。反证路径：① "structured output reasoning sensitivity" 0 直击；② T54 任务书已两次实证 prompt 加规则负收益（内部）；③ 最近邻=De/PaD 结构化解码（未核）。conf 0.65。
- **gap-2**：「general 推理成熟度」作为被评测构念无标准化 benchmark；最近邻=ARC-AGI（抽象）+知识冲突探针（选择行为），两者组合未见于单一生成管线评测。反证路径：B1/B2 检索各 1 次 + "reasoning maturity benchmark"（未单查，**未验证**）。conf 0.6。

## 附录：检索记录
- web 6 次（elicit latent reasoning trigger；ARC-AGI OOD benchmark；agent framework open source；knowledge conflict parametric；+第 7 轮会话内已核引文复用 2 条：UoT/BALAR）；GitHub API 0 次（本轮前段平台 503 故障恢复后未再走 GitHub repo 搜索，C1 标注由此而来）。
- 引文 URL 均来自本次检索或前轮实抓；标注**未验证**者=检索片段数字/未直抓资源。
