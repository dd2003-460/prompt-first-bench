# T50 B1 新题 Gold Tree 构建（Q8/Q9/Q10）— 阶段 01 目标分解

> 创建：2026-11-07 · 阶段：01（目标分解）· 依据：`tasks/T50-B1-gold-trees.md` + `loop/prompt-first/01-goal-decomposition.md`
> 执行通道：arena agent（本会话，repo 内执行）· 分支 `arena/5c63a992-prompt-first-bench`
> **本阶段是因素分解，不是资料搜集**：下文出现的全部论文名、数值（164 题 / 400M pairs / β=0.2 等）均为任务书给出的**待验证研究目标/假设**，未经核验前不得当作事实引用。

---

## 1. 目标与交付物

**任务**：为 pfb B 面（AI/ML 域内跨子领域泛化验证）新建 3 道题（Q8 LLM 评估方法 / Q9 多模态架构 / Q10 RLHF 对齐），每题构建 gold tree，并完成 harness 注册，走完整 1-loop。

**必须交付（缺一即半成品）**：

| # | 交付件 | 验收形态（机器可查） |
|---|--------|---------------------|
| D1 | 题面 ×3 | `bench/questions/Q8-*.txt`、`Q9-*.txt`、`Q10-*.txt` 存在且非空；格式对标 Q6（头注释 + 拆解者 preamble + 「问题：」行可被 `extract_question()` 提取） |
| D2 | gold tree ×3 | `bench/rubric-v3/ablation/gold-Q8.md`、`gold-Q9.md`、`gold-Q10.md` 存在；每份 ≥30 节点、≥10 叶子（grep 计数）、主干深度 ≤4、叶子带数值 + 来源 URL + 访问日期；顶部有「未引用 Q1-Q5 gold」独立调研声明 |
| D3 | harness 注册 | `experiments/stage-ablation/ablation_harness.py` QUESTIONS dict 含 "Q8"/"Q9"/"Q10" key（domain/prompt_file/gold_file/search_query 四字段，参照 Q6/Q7） |
| D4 | 搜索 query 注册 | `experiments/stage-ablation/research_hook.py` ARXIV_QUERIES dict 含 "Q8"/"Q9"/"Q10" key（每题至少一条 arXiv query） |
| D5 | loop 工件 | `loop-artifacts/stages/{01,02,02.5,03,04,04.5}/T50-*.md` 六阶段齐全，每阶段判定 pass 才进下一阶段 |
| D6 | commit + push | git log 有新 commit 且 message 含 "T50"；全部工件在 arena 分支上可 fetch |

**不交付（出域）**：score.py / score_s10.py / gates.py 修改；Q1-Q5 任何文件修改；跑实验 runs（B 面实验由 Lead 后续派发）。

---

## 2. 因素分解（正交 + 覆盖 + 递归）

### F1 题目设计（3 题的题面质量）
- F1.1 子领域正交性：Q8（LLM 评估方法）、Q9（多模态架构）、Q10（RLHF/对齐）两两不重叠，且与现有 Q1-Q5（GPU硬件/模型选型/推理基础设施/数据处理架构/科研方法论）+ Q6-Q7（networking/storage，D面用）不重叠。
  - 已确定：任务书已指定三题方向 → 正交性由题面措辞保证（Q8 是"怎么建 benchmark"不是"选哪个模型"，与 Q2 区分；Q10 是"训练对齐 pipeline"不是"推理服务"，与 Q3 区分）。
  - [待核验] Q9 与 Q2（模型选型）的边界：Q9 聚焦架构/训练策略对比，不聚焦选型性价比 → 题面里显式约束。
- F1.2 题面可拆性：题面须含足够场景约束，使答题者能拆出"根节点"（Q6/Q7 是成本数字根节点；Q8/Q9/Q10 是设计/对比类题，根节点须转译成可量化的判据——如 Q8"benchmark 的判别力/抗泄漏性"、Q9"任务-架构匹配度"、Q10"对齐收益-税净效应"）。
  - 空缺 G1：设计类题的根节点如何数字化（参照 gold-Q6 的 c_1k 模式）→ 阶段 02 调研各题文献后由 gold tree 定义。
- F1.3 格式合规：与 Q6/Q7 题面文件逐段同构（头注释字段齐全：用途/gold tree 路径/注册位置/域隔离/标记说明/预期根节点/已知空缺/判分口径/基线/建题日期）。

### F2 Gold tree 内容质量（核心交付）
- F2.1 结构合规：节点编号 N-X.Y、主干深度 ≤4、≥30 节点、≥10 叶子、SHARE/leaf 标记、图例、★判断、黑盒表、OC-1 卡片样例、来源表、「找不到/未验证」节——全部对标 gold-Q6.md 结构。
- F2.2 叶子数值真实可溯源：每个叶子带具体数值/区间 + 来源 URL + 访问日期。
  - 空缺 G2：Q8 关键数值（pass@k 公式、HumanEval 164、MBPP 974、LiveCodeBench 时间窗机制）→ 一手 arXiv 论文核验。
  - 空缺 G3：Q9 关键数值（CLIP 400M pairs / ViT-L/14 768-dim、SAM 11M images / 1.1B masks、GPT-4V 动态 tile 机制与 token 数、Gemini 原生多模态/长上下文）→ 一手论文/官方文档核验。
  - 空缺 G4：Q10 关键数值（InstructGPT 三步 pipeline、PPO KL coefficient β=0.2、DPO β=0.1、alignment tax MMLU -5~15pp）→ 一手论文核验；**任务书示例值 β=0.2 与 -5~15pp 是待验证假设，查不到可靠来源就标 [待核验]，不得照抄**。
- F2.3 独立调研：不得引用 Q1-Q5 gold（`gold-tree.md` 等）内容；每份 gold 顶部显式声明。
- F2.4 覆盖广度：每题的 tree 须覆盖任务书"关键叶子值示例"全部 4 项 + 文献主流维度（Q8: 维度设计/防泄漏/防过拟合；Q9: 架构差异/训练策略/适用场景；Q10: pipeline 步骤/超参/税量化）。

### F3 注册与工具链兼容
- F3.1 QUESTIONS dict：4 字段格式；prompt_file/gold_file 用 `os.path.join(PFB, ...)` 相对仓库根（参照 Q6/Q7 条目）。
- F3.2 ARXIV_QUERIES dict：每题一条精准 query（任务书要求）；[待核验→决策] 是否同时补 KNOWN_SITES / FILTER_KEYWORDS（Q6/Q7 先例两者都有；任务书未强制 → 补上以保持 hook 行为一致，属 D4 的自然延伸，记录于阶段 03）。
- F3.3 兼容性验收：python 语法检查（import 或 ast.parse）通过；`extract_question()` 对新题面能提取出非空核心问题段。

### F4 流程合规（1-loop + git）
- F4.1 六阶段工件落盘 `loop-artifacts/stages/<N>/T50-*.md`，逐阶段判定。
- F4.2 commit message 含 "T50"；push 到 `arena/5c63a992-prompt-first-bench`。
- F4.3 约束遵守：不改 Q1-Q5 文件、不改 score.py/score_s10.py/gates.py、不建新目录。

### F5 调研通道可用性（风险因素）
- F5.1 沙箱网络受限（bash 出网仅 github/pypi/npm）→ 调研走平台 web_search/fetch_page 工具；[待核验] 工具对 arxiv.org/export.arxiv.org 可达性。
- F5.2 降级方案（任务书给定）：web 搜索不可用 → arXiv API + 已知论文内容，conf 降 0.2；仍不可用 → T50-partial 落盘已完成部分。

---

## 3. 已知 / 可推导 / 空缺三分

**人类已提供（确定）**：三题方向 + 关键叶子值示例（作为假设）+ 交付物路径 + 验收标准 + 格式参照物（Q6 题面 / gold-Q6.md / Q6-Q7 注册条目）+ 约束与降级方案。

**可推导（确定）**：
- I1：题面文件的 preamble 与「问题：」行结构由 `extract_question()` 的正则 `r"问题[：:]\s*(.+?)(?:\n\n请给出|\Z)"` 决定 → 新题面必须含「问题：」行，且其后为完整题面。
- I2：QUESTIONS 新条目 path 用 PFB 常量（Q6/Q7 先例），不用 WORKSPACE（Q1-Q5 旧例）。
- I3：≥30 节点/≥10 叶子 的 grep 计数口径 = tree 代码块中 `N-` 编号数与 `leaf` 标记数（与 gold-Q6.md 头部自报 41/15 的口径一致，验收前先自测）。
- I4：三题均为 AI/ML 域内子领域（B 面定位），题面语言/结构与 Q1-Q5 的调研类题更接近，但文件放 Q6/Q7 同路径体系。

**空缺清单（阶段 02 必须回答）**：

| # | 空缺 | 阻塞什么 | 研究路径（来源类型 + 搜索词） | 备用路径 |
|---|------|---------|------------------------------|---------|
| G1 | 三道设计/对比类题的根节点数字化方案 | gold tree N-0 定义 | 阶段 02 读一手文献后推导（S-c 类） | 参照 gold-Q6 N-0 模式：根=可复算的综合判据 |
| G2 | Q8 全部叶子数值：pass@k 无偏估计公式原文、HumanEval 164、MBPP 974（及 full/sanitized 口径）、LiveCodeBench 时间窗机制细节、contamination 检测方法（n-gram/canary/CDD）、EvalPlus 测试倍数 | gold-Q8 叶子 + 来源表 | arXiv API id_list 批量取 abstract（2107.03374 / 2108.07732 / 2403.07974 / 2305.01210 / 2311.04850 / 2311.06233 / 2310.06770 / 2406.15877）；细节不足再 web_search 单点 | fetch arXiv abs 页；再不行标 conf 0.2 |
| G3 | Q9 全部叶子数值：CLIP 400M pairs/ViT-L/14 768-dim/zero-shot 76.2%、SAM 11M images/1.1B masks/数据引擎、GPT-4V 动态分辨率 tile 规格与 token 计费、Gemini 原生多模态/上下文长度、LLaVA/Flamingo 连接层 | gold-Q9 叶子 + 来源表 | arXiv id_list（2103.00020 / 2304.02643 / 2303.08774 / 2312.11805 / 2403.05530 / 2304.08485 / 2204.14198）；GPT-4V tiling 是官方文档口径 → web_search "GPT-4V dynamic tiling 512x512 85 tokens" + fetch Azure/OpenAI 文档 | 社区实测（simonwillison 等）conf 0.7；查不到标 [待核验] |
| G4 | Q10 全部叶子数值：InstructGPT 三步（13k/33k/31k prompts、RM 6B）、PPO KL β 真实取值（任务书假设 0.2）、PPO-ptx γ、DPO β（任务书假设 0.1）、alignment tax 量化（任务书假设 MMLU -5~15pp）、reward overoptimization KL 规律 | gold-Q10 叶子 + 来源表 | arXiv id_list（2203.02155 / 2305.18290 / 2210.10760 / 2312.01552 / 2310.05492）；β 具体值 abstract 不含 → fetch 论文全文 HTML（ar5iv/arXiv html）或 web_search；alignment tax 量化 → web_search "alignment tax MMLU" | 查不到可靠来源 → 叶子标 [待核验] + conf 0.2，不编数 |
| G5 | 调研通道可用性：web_search / fetch_page 是否可达 arxiv 与微软/OpenAI 文档 | 整个阶段 02 | 阶段 02 第一步先探测（1 次 API 调用 + 1 次 search） | 全不可用 → 按任务书降级：记忆内容 + conf 0.2 + 显式标注 |
| G6 | KNOWN_SITES / FILTER_KEYWORDS 是否同步补 Q8/Q9/Q10 | D4 完整性判断 | 阶段 03 决策（先例一致性 vs 任务书最小改动） | 保守：补上并在 04.5 说明超出任务书范围的部分 |

---

## 4. 边界声明

- 深度 ≤4 = N-0 → N-x → N-x.y → N-x.y.z 为主干上限（gold-Q6 先例：存在 N-2.2.1/N-2.3.1 三级编号即深度 4）。
- 「≥30 节点」按 tree 内全部 `N-` 编号计数（含 N-0）；「≥10 叶子」按 `leaf` 标记计数。
- 访问日期统一用本任务实际核验日（2026-11-07）。
- 候选集冻结：三题的主题范围以任务书为准（Q8 代码生成 benchmark 设计 / Q9 CLIP·SAM·GPT-4V·Gemini 四对象对比 / Q10 RLHF pipeline·超参·对齐税），后续阶段不得悄悄换题或增删对比对象；Q9 允许在 tree 内加"参照架构"（LLaVA/Flamingo 作为连接层谱系），因其属于任务书"架构差异"的自然展开，登记为显式扩展而非漂移。

## 5. 阶段判定

- 目标交付物 D1-D6 明确 ✅；主要因素 F1-F5 正交覆盖（题目设计/内容质量/注册兼容/流程合规/通道风险）✅
- 已知/可推导/空缺三分完成，G1-G6 全部进空缺清单，无伪装已知 ✅（任务书示例数值全部标"待验证假设"）
- 每个空缺有具体研究路径 + 备用路径 + 阻塞影响 ✅
- 阶段 02 可据此直接开始（arXiv id_list 已列全）✅

**verdict：pass** · repair_stage：none
