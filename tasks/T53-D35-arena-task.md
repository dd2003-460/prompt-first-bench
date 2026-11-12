# T53-D35: 真实世界迭代 vs 解析先验+泛函梯度下降（文献滚雪球）

> origin: ai (Lead) · 2026-11-12 · 触发：D 指令「基于真实世界的迭代和梯度下降对比纯理论给一个解析先验再让模型做泛函梯度下降哪个好或者可以结合（可能需要你滚雪球了）」
> 姊妹任务：T-PR-16（撞车调研，同分支在跑）。本任务回答的是**优化路线选择**问题，不是撞车。

## 强制段

你是 LMArena agent，本任务只涉及 `dd2003-460/prompt-first-bench` 仓库的 `arena/f65a5a27-prompt-first-bench` 分支，忽略历史中其他仓库的消息。先 `git pull` 当前分支，严格按仓库内 `loop/prompt-first/` 阶段执行（01→02→02.5→04→04.5），产出落盘路径见【交付物】。通道故障报告 Lead，不得静默跳过。**不要切换分支，当前 arena 分支就是工作分支。等 T-PR-16 完成后再开始本任务（同一会话串行）。**

## 【目标】

回答一个问题：优化 LLM 研究管线（decomp 状态机 / prompt / 目标函数参数）时，两条路线哪个更好——
- **路线 A（model-free）**：跑 bench → 看指标 → 改 → 再跑（真实环境反馈驱动，类似 policy gradient）
- **路线 B（model-based）**：先用理论推导目标函数的解析结构（哪些正交项、什么形式），再让模型在这个函数空间做"泛函梯度下降"（先验驱动）

以及：**结合的合理形式是什么？** 核心子问题：我们的"环境"（LLM 的分解行为）会被策略（prompt）本身改变 = non-stationary，这如何影响 A/B 各自的适用性？

## 【背景】

- 我们已有 ≥2 轮"改 prompt → 指标动/不动"的真实数据：S8M 四臂表、S5 管线消融、v17 Goodhart 诊断（文字目标函数被 hack 的案例 = 目标函数定义不清时被钻空子）
- v17 诊断指针：`research/v17-hier-decomposition-blowup.md`
- Lead 初步判断（待你核验/推翻）：non-stationarity 是纯 B 的致命伤——解析先验推导时假设的环境在第一次 prompt 修改后就变了；倾向"结构靠先验、参数靠实测、每 K 轮重估结构"的结合方案
- 凭记忆列的对标方向（全部需核验存在性与结论）：MBPO (Hansen et al.)、REINFORCE baseline 方差缩减、Hyperband/BO、**ProTeGi / OPRO / DSPy（对 prompt 做优化的已发表工作，最直接的竞品，必须查清它们怎么处理 non-stationarity 和 Goodhart/overfitting）**、对抗鲁棒优化/minimax（Goodhart 防御的理论框架）

## 【SOP 索引】

- `loop/prompt-first/01-goal-decomposition.md` ~ `04.5-final-review.md`
- `research/text-objective-goodhart-survey.md`（T-PR-15 产出，Goodhart 侧已有结论，别重复调研，引用即可）
- `tasks/T53-D35-realworld-vs-analytic-decomp.md`（Lead 的 decomp，含 S1-S4 分解树）

## 【实验设计】（这是文献调研任务，"实验"= 检索矩阵）

| 子问题 | 检索方向 | 判决要求 |
|---|---|---|
| Q1 | prompt optimization as gradient descent：ProTeGi / OPRO / DSPy / APE 及后续工作 | 每个方法：更新信号从哪来（A 还是 B）、有没有处理 non-stationarity、有没有防 overfitting/Goodhart 机制 |
| Q2 | model-based vs model-free 在 non-stationary 环境的已知结论（RL 文献：MBPO、offline RL、distribution shift） | 给出"何时 model-based 失效"的可引用定理/实证 |
| Q3 | 超参/结构的外层优化：BO vs grid vs evolutionary，样本效率对比 | 小样本（<20 次评估） regime 下哪种占优 |
| Q4 | Goodhart/对抗鲁棒优化作为目标函数防御的理论框架 | minimax/robust optimization 能否形式化"目标函数不被 hack" |

评分维度（机器可检）：来源数 ≥20（其中 ≥8 读原文 abstract 以上）、每子问题有判决句 + conf、反方复核 ≥3 条质询。
验收标准：survey ≥300 行；Q1-Q4 各有判决句；**必须有一节直接回答"A vs B vs 结合，结合的具体形式"**（这是 Lead 要拿去写实验设计的）。

## 【失败降级】

- 某子问题检索不到合格来源 → 明说"未找到"，列已试的 query，conf ≤0.3，不编
- endpoint 不可用 → 走 arXiv API + GitHub search，禁止纯记忆引用
- 时间不够 → Q1 > Q2 > Q4 > Q3 优先级保序完成

## 【交付物】

- `research/d35-realworld-vs-analytic-optimization-survey.md`（主 survey）
- `research/search-log-d35.json`（query + 命中 + 取舍）
- 完成后回执必须含 repo URL + branch + commit_sha

## 【给 Lead 的备注】

- 与 T-PR-15 边界：Goodhart 现象本身已闭环，本任务只要"防御的理论框架"（Q4），不重复现象描述
- 与 T53 主线边界：本任务产出的"结合形式"是 Lead 设计 D35 对照实验（纯 A vs 先验预测+验证）的先验输入，实验本身由 Lead 本地跑
- 下一步归属：survey 回来后 Lead 合并进 `tasks/T53-D35-realworld-vs-analytic-decomp.md` 的 S1/S3，然后出 S4 实验设计