# autoresearch 非训练分支调研 → pfb idea 映射（2026-11-24）

> origin: ai · 触发：D 纠正「找 autoresearch 是做 pfb 相关 idea 的，难道只有训练的 research 吗」
> 来源：5 篇 arXiv abs 页本轮实查（来源①）+ 本地 harness-evolution-survey-20261120.md（来源②，DGM 部分）
> 结论先行：autoresearch 有两个分支，我之前只找了训练分支（karpathy 固定时间训练循环，MLX 移植）。
> 非训练分支 = 自主科研 agent（idea→实验→论文→评审），这才是 pfb idea 的坐标系。

## 两分支区分

| 分支 | 代表 | 循环单元 | 与 pfb 关系 |
|---|---|---|---|
| 训练循环型 | karpathy autoresearch（本地 autoresearch-mlx/） | 改 train.py→固定 5min 训练→val_bpb→keep/revert | 无关（改权重，D 明确 prompt+hook 不改权重路线） |
| 科研 agent 型 | AI Scientist v1/v2、Agent Laboratory、Co-Scientist、DGM | idea→实验→分析→成文→评审→迭代 | **pfb 的坐标系** |

## 非训练分支系统清单（本轮实查 abs 页）

| 系统 | arXiv | 机制 | 与 pfb 的关系/我们的增量 |
|---|---|---|---|
| AI Scientist v1 | 2408.06292 (Sakana 2024) | idea 生成→写码→跑实验→写论文→自动评审，<$15/篇 | 评审是 LLM 打分；我们 rubric-v3 双层（outcome+process 分离）+ gold 树按意外性加权，比它的 LLM reviewer 有结构 |
| AI Scientist v2 | 2504.08066 (Sakana 2025) | 去掉人工代码模板，agentic tree search + 实验管理 agent，首篇 AI 生成 workshop 论文过评审 | **树搜索做实验管理**——与 T53 状态机分解树同构但用途不同（它搜实验路径，我们搜问题分解）。可引用对照 |
| Agent Laboratory | 2501.04227 (AMD/JHU 2025) | 人给 idea→文献调研→实验→报告三阶段，人每阶段可反馈；o1-preview 最佳，成本降 84% | 半自主（人给 idea）。我们 Q9-agi 是全自动 + 预算控制，它没做预算轴 |
| Co-Scientist | 2502.18864 (Google, Nature 2026) | 多 agent 生成/批判/精炼假设，tournament 进化，test-time compute 扩展，湿实验验证 | 假设生成+进化锦标赛最接近"研究闭环"；但依赖 Gemini 级模型 + 生物湿实验，无预算约束维度 |
| DGM | 2505.22954 (UBC 2025) | agent 改自己代码，archive+变异+benchmark 验证（来源②，本地已调研） | 自我改进机制；本地调研结论=太重，机制可小规模借鉴 |
| MLE-bench | 2410.07095 (OpenAI 2024) | 75 个 Kaggle 竞赛评 ML agent，medal-based 绝对标尺 | 评测设计参考（绝对标尺 vs relative）；非科研 agent 本身 |

## 与 pfb 已有工作的对齐（不重复造）

- **"知道自己不知道"机制**：pfb 已有三道外部闸（数字溯源/矛盾对质/熵排序）+ defensive-language 分级（r1 复盘，11-03）。上面 6 家**都没有**"模型显式标缺口→触发调研"的闭环——AI Scientist 系靠 LLM reviewer 事后打分，Co-Scientist 靠 tournament 淘汰，都是外部选择压力，不是模型自知。这是 pfb 的空白点，保持。
- **预算控制**：Q9-agi 题面（预算大→完整覆盖 gold，预算小→压缩细节）在 6 家中无对应——Agent Laboratory 有人反馈但无预算轴，Co-Scientist 有 test-time compute 扩展但无"单位预算闭环成功率"排序键。Q9 的预算轴仍是独有。
- **树结构用途差异**：AI Scientist v2 的 tree search 搜的是实验执行路径；T53 的分解树搜的是问题正交分解。引用 v2 时需明确区分，避免审稿人混淆。
- **评审机制**：rubric-v3 双层分离 + 意外性加权（w∝1/P(拆分|父节点)）vs 各家 LLM reviewer 单分。deepresearch-bench 调研任务书（10-29）已覆盖各家 scoring 扒取，此处不重复。

## 可提取的 pfb 候选 idea（登记，不展开，遵守 11-23 防发散纪律）

1. **预算轴 × 科研 agent**：给 AI Scientist v2 式树搜索加预算控制（节点预算→覆盖-压缩权衡），对照 Q9-agi。与 #36 终点目标函数 U(T)=C·A·S−λ·cost 同构——λ 标定可直接用 Q9 数据。
2. **模型自知 vs 外部选择压力**：Co-Scientist 的 tournament（外部淘汰）vs 我们的三道闸（模型自知）做对照实验——哪个在 27b 上更省预算。这是"知道自己不知道"主张的直接撞车检查。
3. **tree search 用途区分声明**：写论文 related work 时把 AI Scientist v2 的 tree search 与 T53 分解树显式区分（执行路径搜索 vs 问题分解），防审稿人混淆。

状态：调研落盘，idea 登记待 D 确认优先级（主线可发表里程碑优先，11-23 纪律）。

## 补充（2026-11-24 第二轮）：taste / general 检查

> 触发：D 问"有没有要求检查创新点最好是 general 的"。来源①：Sakana 仓库 generate_ideas.py 原文 + arXiv:2502.14297（AI Scientist 复现批评）+ arXiv:2606.15497（end-to-end automation 综述）。

### 业内

| 系统 | general/taste 机制 | 形式 |
|---|---|---|
| AI Scientist v1 | idea prompt 显式："not overfit the specific training dataset or model, and has **wider significance**" | prompt 软约束（一句话），非门禁 |
| AI Scientist v1 | 自评分 interestingness/novelty/feasibility 1-10 | 自评分，2502.14297 证实"arbitrarily assigned and not used in further processing" |
| AI Scientist v1 | novelty 闸：Semantic Scholar 最多 10 轮，"harsh critic" | 机械流程但本质关键词搜索，2502.14297 复现：把 SGD micro-batching 判成 novel（不可靠） |
| AI Scientist v2 | "**simple and elegant** question/observation/hypothesis" + "publishable at **top ML conferences**" + 资源约束 | prompt 软约束；elegance = taste 代理 |
| v2 反思轮 | reflection prompt 检查 quality/novelty/feasibility + "any other factors you think are important" | 开放式自审，无机械判据 |

结论：业内的 general 检查 = prompt 措辞（软）+ 不可靠的 novelty 闸（半机械）。没有一家把"创新点是否 general"做成机械可判的门禁。

### 我们（rubric-v3）

六个 outcome 维度无显式 generality 维度。最接近 = O3 意外性加权（w∝1/p̃），但它奖励"意外"不奖励"通用"：一个发现可以极意外但域内专属（硬件 quirk），O3 高分却过不了 general 关。

### 缺口与最省补法

缺口：我们连业内的 prompt 软约束都没有。
最省补法：O3 加乘性因子或独立 O7"泛化声明"——judge 对照第二格新建 gold 判"该结论能否迁移到 gold 之外的域"。O3 本来就有"第二格用新建 gold"设计，可复用，不增新基础设施。
状态：待 D 确认是否进 rubric-v3 下一版（主线可发表里程碑优先，11-23 纪律）。

## 补充（2026-11-24 第三轮）：能"跑不同 idea"的 autoresearch 系统谱系 + 本地 gpt-researcher 实测

> 触发：D「还有别的可以跑不同 idea 的 autoresearch 系统吗」。来源①：本地 gpt-researcher v0.16.0 代码实查 + 实测（runner `pfb/tasks/XREF-external-reference/run_gptr_q2.py`）。

### 关键区分：接不接外部 idea

| 类型 | 系统 | 能拿我们的 idea 跑吗 |
|---|---|---|
| **接外部 idea**（deep research 类） | gpt-researcher（本地有 v0.16.0）、STORM（Stanford 开源）、OpenAI/Perplexity deep research、LMArena agent、Claude Code（人在环） | ✅ 给 query 就跑 |
| **自己生成 idea**（AI Scientist 类） | AI Scientist v1/v2、Co-Scientist、DGM | ❌ idea 是它自己生成的，不接外部 |

D 想"拿成熟的跑我们的 idea"→ 只能从**接外部 idea** 那类选。AI Scientist 类验证不了"我们的 idea 跑起来怎么样"。

### 本地 gpt-researcher 实测（27b 接入）

- **LLM 层 ✅**：`llm_provider/generic/base.py` 支持 `OPENAI_BASE_URL` 自定义端点，FAST_LLM/SMART_LLM/STRATEGIC_LLM 设成 `openai:qwen3.8-27b-mtp` 后 27b 接上了，`create_chat_completion` 直连成功（来源① 本轮实测）
- **搜索层 ❌**：默认检索器 tavily 要 key；换 duckduckgo（免费无 key）被反爬拦（HTTP/2 "Unsupported protocol version 0x304"），`conduct_research` 拿不到源材料，报告退化成"no source material"
- **结论**：gpt-researcher 在 D 本地网络条件下，免费搜索层不可用（DDG 反爬），商业检索器（bing/brave/tavily/exa）都要 key。**成熟开源 deep-research 系统在 D 硬件/网络下的真实限制 = 搜索层**，不是 LLM 层

### 对"拿成熟系统跑我们的 idea"的修正

最干净的实现 = **LMArena agent**（frontier 模型 + 真搜索 + 接外部 idea），已在跑（Q2 模型选型题，会话 01a209ba，对照 S0-Q2 27b 基线）。gpt-researcher 本地那条线因搜索层挂，价值降级为"证明 27b 接 gpt-researcher 的 LLM 层可行 + 暴露 D 网络下开源 deep-research 的搜索瓶颈"。

**D 的直觉「真正成熟可用的不会公开」分两种**：端到端 AI Scientist 类（对，全是演示级）；deep research 类（不对，gpt-researcher/STORM 都开源可用，但搜索层依赖外部 API/反爬，本地裸跑受限）。

## 补充（2026-11-24 第四轮）：D 纠正「我说的是 autoresearch 不是 deepresearch」+ Agent Laboratory 本地可跑性实测

> 触发：D 指出 LMArena/gpt-researcher 都是 deep research（给问题→搜索→报告），不是 autoresearch（idea→实验→迭代闭环）。来源①：AgentLaboratory 仓库本轮 clone 实查（/tmp/AgentLaboratory）。

### 纠正后的分类

| 类型 | 系统 | 能跑我们的 idea | 本地可跑性 |
|---|---|---|---|
| deep research（接问题） | LMArena agent / gpt-researcher / STORM | ✅ 给题就跑 | LMArena ✅（已跑 Q2/XREF-Q1）；gptr ❌ 搜索层 |
| **autoresearch（接 idea，idea→实验→报告闭环）** | **Agent Laboratory**（MIT，AMD/JHU） | ✅ 人给 idea | ⚠️ 见下 |
| autoresearch（自生成 idea） | AI Scientist v1/v2 / Co-Scientist / DGM | ❌ 不接外部 idea | ❌ 演示级/需 Gemini 级 |

**Agent Laboratory 是唯一"接外部 idea 的成熟开源 autoresearch"**，本地可跑性实测两个硬伤：

1. **import 链重型**：`ai_lab_repo.py → app/agents/tools → torch + tensorflow + spacy + sentence_transformers`，全装不可行（D 硬件）；可 monkeypatch 绕过但属 hack
2. **实验阶段与 idea 类型错配（更根本）**：experimentation 阶段 = mlesolver/AIDE 式"写 ML 代码→跑→reward 修"循环，设计给训练/调模型类 idea；Q1（GPU 吞吐分解）是分析题，且实验要真 GPU（本地只有 CPU）——管线能驱动但实验阶段跑不出真结果

### 结论

"拿成熟 autoresearch 跑我们的 idea"在 D 本地条件下的真实状态：
- **端到端可跑 = 无**（Agent Laboratory 受 GPU + 重型依赖双卡）
- **最接近 = LMArena agent**（XREF-Q1 已派发 11-24）：它是 deep research 而非 autoresearch，但它是唯一"接外部 idea + 真执行 + 本地可达"的参照。claim 表述需限定为"frontier+deep-research 参照"，不写成"autoresearch 对照"。
- **Agent Laboratory + 27b 的干净对照**（同模型不同系统）= 被实验阶段 GPU 依赖卡死，降级为"文献调研+规划阶段可跑"的部分验证（价值有限，不立项）。
