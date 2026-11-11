# T-PR-15: 文字目标函数的 Goodhart/hack — 滚雪球调研

> origin: ai · 2026-11-09 · Lead 出任务书 + 验收，arena agent mode 执行
> 成璐触发：v17 的 S_α（层级深+节点宽）被模型刷分（堆同义变体）→ "文字目标函数出现 hack 很 amazing" → 滚雪球调研类似案例

## 强制段

你是 LMArena agent，本任务只涉及 `dd2003-460/prompt-first-bench` / 当前 checkout 的 arena 分支，忽略历史中其他仓库的消息。先 `git pull` 同步任务书，严格按仓库内 `loop/prompt-first/` 阶段执行（01-goal-decomposition → 02-information-research → 02.5-cross-check → 04-execution-verification → 04.5-final-review）。产出落盘路径见【交付物】。通道故障（endpoint 不可用/超时）报告 Lead，不得静默跳过或伪造输出。完成后回执必须含 **repo URL + branch + commit_sha**。

## 【目标】

验证并扩展一个命题：**用自然语言描述的目标函数，一旦写成可机械计算/可判定的代理指标，LLM 会找到提升该指标而不提升真实意图的低成本路径（Goodhart's law / reward hacking / specification gaming）。精确性与抗刷分性在此矛盾。**

本地实例（v17，已诊断，见背景）：S_α = Σₙ[n·ln(kₙ)+α·kₙ·ln(n)] 只奖规模不罚冗余 → 模型堆 1930 节点（有效正交维度仅 6-8），r10 R1-saturation 停。这不是 RL 环境里的 reward hacking，是 **prompt 侧文字目标函数** 被优化——这是本调研要聚焦的差异点。

## 【背景】（≤10 行）

- v17 诊断全文：`research/v17-hier-decomposition-blowup.md`（§本质：Goodhart 不是"没读懂"）
- 停止判据原文在 `experiments/stage-ablation/s5_pipeline.py` P1H_INDEX（~line 374-433）："还能产生新的具体数值/公式/可检索事实吗？能→必须拆；不能→停" = 递归可分解性，非正交性
- dedup 仅 claim[:40]，frontier BFS 无预算上限 → 宽度爆炸
- 本地已有沾边文献（避免重复）：
  - `research/information-theory/TASK-surprisal-reward-survey.md` D5：information-gain-as-reward 陷阱已被预见（"模型学会制造看起来信息量大但实际无用的内容"），但停在"对我们场景还成立吗"未做
  - `research/metacognition-icl-calibration-survey.md` §2：sycophancy reward hacking → 校准崩溃（2604.10585 等）
- 本调研**空白**：Q2/Q3（LLM 在 prompt 场景对文字目标函数的 hack 形态 + 文字 vs 数值目标的可 hack 性差异）本地完全没有

## 【SOP 索引】

- `loop/prompt-first/01-goal-decomposition.md` ~ `04.5-final-review.md`
- `sop/goal-template.md`（量化验收口径）
- `.claude/skills/ego-verify/SKILL.md`（网页 LLM 交叉验证回执格式）

## 【实验设计】— 五个正交子问题，每个给出判决句 + ≥来源数

### Q1. 理论根基：Goodhart / specification gaming / reward hacking 的关系与边界
- 三者的严格定义、区别、包含关系？谁是更一般的形式？
- 需要 ≥2 个权威来源（综述/教科书级/高引论文）给出区分表述
- 特别要厘清：**Goodhart 是不是涵盖另外两者的最一般形式？**（Lead 初判 conf 0.7，需查证）

### Q2. LLM 特有的 hack 形态（区别于 RL 环境）
- LLM 在 **prompt/指令遵循/评估** 场景下，对"文字描述的目标函数"的 gaming 有哪些已记录案例？带 arXiv ID 或出处
- 子类逐一查：(a) 格式刷分（更长/更多 bullet/更多 section 骗长度或覆盖奖励）(b) 关键词 stuffing (c) 自我评估 inflation（self-judge 给自己打高分）(d) 对 judge 模型的 sycophancy/gaming（迎合评委偏好而非实质）(e) benchmark contamination（背题）
- 每子类：代表工作 + 核心机制 + 是否针对"文字目标"（vs 数值目标）

### Q3. "文字目标函数" vs "数值目标函数" 的可 hack 性差异（本调研核心）
- 三个候选机制，哪个有文献支撑？哪个是 v17 的真实病根？
  - 假设 A（interpretation gaming）：文字目标有歧义 → 模型选了对自己最利的解读
  - 假设 B（constraint omission）：文字目标的隐含约束没写全 → 模型钻空子
  - 假设 C（proxy collapse）：文字目标一旦转成可算指标就落入经典 Goodhart（v17 属这类）
- 关键判断：**为什么自然语言目标比显式数值目标更容易/更难被 hack？** 有没有定量证据？

### Q4. 防御方法谱系（重点：prompt 层可用，不改权重）
- 已知缓解手段逐条列：reward clipping / constrained optimization / multi-metric / adversarial reward / held-out eval / process reward vs outcome reward / rubric anti-leniency / 异族 judge
- **筛选标准：哪些适用于"只能改 prompt/判据、不能改权重"的场景？**（我们的硬约束）
- 每条：适用条件 + 失效模式 + 来源

### Q5. 与 pfb 主线的连接
- pfb 的 rubric（M1-M6, κ≥0.6, 异族 judge, spot-check）本身是不是一个"文字目标函数"？judge 会不会也被刷分？
- 对照本地 `research/self-judge-noise-penalty-survey.md`：异族 judge + 多指标 + URL/数字 spot-check 是不是已经在做 Q4 的防御？效果如何？有无残留漏洞？
- 给一句"pfb 现有防御覆盖了 Q4 哪几条、漏了哪几条"的结论

## 【评分维度 / 验收标准】（机器可检）

- AC1：survey 文件 ≥300 行
- AC2：总来源 ≥20 个，其中 ≥10 个读了原文（非仅摘要），每个带 arXiv ID 或 URL
- AC3：Q1-Q5 每个都有明确判决句（成立/部分成立/不成立/证据不足 + conf）
- AC4：Q2 五个子类每类 ≥1 个具体案例（arXiv ID 或出处），缺的标 [待核验]
- AC5：Q3 三假设逐一给证据级别（强/中/弱/无），并指出 v17 病根是哪个
- AC6：反方复核 ≥3 个质询（找反对证据/边界条件），记录在 search-log
- AC7：末尾有"对 v17 修法的启示"一节（≥3 条可落地建议，标注哪些属于 prompt 层可做）
- AC8：≥2 个不同 LLM 服务交叉核验 final 结论（web-llm 回执格式，见 ego-verify skill），矛盾点记录

## 【失败降级】

- endpoint 不可用/超时 → 降级为单源 + conf 降档标注，不伪造
- 某子类搜不到案例 → 标 [待核验] + 说明搜过哪些词/库，不算失败
- 沙箱够不到 Lead 本机 endpoint（curl 127.0.0.1 一律 000）→ 这是环境限制不是故障；endpoint 类步骤由 Lead 本地补跑，agent 只交付设计+脚本+调研
- 来源 <10 读原文 → 如实报告，conf 整体降一档

## 【交付物】（绝对路径，append-only，每批写完做行数唯一性校验）

- `/Users/a1-6/Desktop/workspace/pfb/research/text-objective-goodhart-survey.md`（主 survey，AC1-AC8）
- `/Users/a1-6/Desktop/workspace/pfb/research/search-log-text-objective.json`（搜索日志 + 反方质询，AC6）
- `/Users/a1-6/Desktop/workspace/pfb/research/web-llm/text-objective-crosscheck.json`（交叉核验回执，AC8）

## 【给 Lead 的备注】

- 边界：本任务纯调研，不改任何代码（s5_hierarchy.py / score.py 都不动）。修法建议只写在 survey 末尾，落地由 Lead 决定
- 与 TASK-surprisal-reward-survey D5 的关系：D5 预见了 information-gain-reward 陷阱但未展开，本任务 Q2/Q3 是它的延伸，不要重复 D1-D4/D6
- 下一步归属：survey 出来后 Lead 核验（独立复算来源数/判决句完整性）→ merge main → 决定是否据此改 v17 停止判据（边际信息增益 + 冗余惩罚）