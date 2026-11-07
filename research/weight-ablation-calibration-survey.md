# 权重消融 / 校准干预 — 前沿调研 + 本地可行性（2026-11-07）

origin: ai | 触发：成璐问"能通过内部消融向量/权重更改去校准吗？有什么问题？拒绝行为消融会退化吗？能在我们模型上实现吗？"
方法：arXiv API 直查（本轮工具输出，来源①）+ 本地模型文件检查（来源①）。未做网页 LLM 交叉验证。

## 结论速览

1. **能，但"改权重"和"推理时改激活"是两条不同的路**。前者永久、不可逆、有副作用风险；后者每次前向加一个方向向量，随时可关。学界主流推荐后者（representation engineering），因为便宜且可回滚。
2. **拒绝行为消融确实会退化**——这不是传闻，多篇直接证据（§2）。机制：refusal 不是单一干净的方向，ablate 掉它连带伤到相邻的行为维度（helpfulness、指令遵循）。2026-01 的新工作专门在修这个"附带损伤"问题。
3. **对我们最相关的发现**：post-training（RLHF/DPO）同时造成 accuracy 下降和 calibration 崩溃（overconfidence），而 model merging 可以沿 Pareto 前沿找回一部分校准（2510.17426）——"alignment-calibration trade-off"是被命名的正式概念。
4. **我们本地模型上完全可实现**：磁盘上已有现成的 abliterated 模型（Youssofal/Qwen3.6-35B-A3B-Abliterated-Heretic-MLX-6bit），说明这条路我们其实走过一次。当前 27b 服务底座（8787 → qwen3.8-27b）是 **5-bit affine 量化**（group_size=64, hidden_size=5120），直接动量化权重数值上可行但精度风险高；更稳的路径是 LoRA 适配器或推理时 activation steering（不需要反量化）。

## §1 两条技术路线

### A. 推理时 activation steering（不改权重）
| arXiv | 要点 |
|---|---|
| 2505.11615 | 对齐 behavioral 和 neural representations 来 steer 风险偏好——steering vector 构造方法论 |
| 2502.19721 | 无监督提取 concept vectors 控制 bias |
| 2410.01174 | inference-time category-wise safety steering |
| 2606.22686 | "The Geometry of Refusal"：safety compliance 是线性可操纵 feature 还是深层语义决策——用对照实验定位 |
| 2602.09870 (Steer2Edit) | **桥接工作**：从 activation steering 走向 component-level editing——把推理时发现的稳定方向固化进权重，得到持久化编辑。这正是"先探针后消融"的完整链路 |
| 2601.03300 (TRYLOCK) | 分层防御：weight editing + representation engineering 组合，单点防御不够 |

### B. 永久权重编辑 / 消融
| arXiv | 要点 |
|---|---|
| 2410.03415 | **单向量消融缓解 false refusal**：surgical、cheap、flexible——只 ablate 一个方向，专门治"不该拒的拒了" |
| 2410.10871 | refusal-vector ablation 用在 Llama 3.1 70B agent 上——规模化可行性先例 |
| 2601.08489 | **Surgical Refusal Ablation**：raw refusal vector 直接 ablate 会有 collateral damage + distribution drift，需要 concept-guided spectral cleaning 先把安全维度和智能维度解耦 |
| 2412.10257 (TARS) | targeted angular reversal 做知识删除——比直接置零温和 |
| 2503.22048 (ThinkEdit) | 可解释 weight editing 治 reasoning 模型的"思考过短"问题——**非安全方向的 weight editing 先例**，证明编辑不只有安全用途 |
| 2602.22554 | sparse weight editing 做多语言安全对齐 |

## §2 拒绝消融退化的证据链（直接回答"会退化吗"）

- 2601.08489（2026-01）：明确说 raw refusal vector ablation "often causes collateral damage and distribution drift"——退化是默认结果，不是意外。修法是先做 concept-guided 分解再选择性清理。
- 2608.25390（2026-08）：refusal training 的几何结构会被多样化 refusal prefix 改变（stable rank 上升），使得单向量 ablation 攻击变弱——反过来也说明 refusal 表征是低维但不单方向的，一刀切必然伤及无辜。
- 2509.09708：解剖 Gemma-2-2B-IT 和 LLaMA-3.1-8B-IT 的 refusal 内部成因——refusal 由多个组件协同产生，不是单点开关。
- 2406.14563：model merging 里"one bad model spoils the bunch"——合并操作本身也会破坏 alignment，说明权重空间的编辑对行为影响是非局部的。

**一句话**：退化是真的，但 2026 年的新方法是"先解耦再动刀"，不是硬 ablate。

## §3 校准专用（我们的目标不是去 refusal，是校准置信度）

| arXiv | 要点 |
|---|---|
| 2510.17426 | **最相关**："Navigating the Alignment-Calibration Trade-off via Model Merging"——post-training 的 alignment tax 不只是 accuracy 掉，还有校准严重丢失（overconfident、output diversity 下降）；merging 可以找到 Pareto 优的前沿。含义：如果我们要"去 RL 污染"，merge base-model 和 aligned-model 的权重是一个被研究过的操作 |
| 2603.19278 (HypeLoRA) | LoRA 微调中的校准动力学 + hyper-network 生成校准适配器——**轻量校准干预的标准答案**：训练一个小 adapter 专门修校准，不动主权重 |
| 2512.07375 (LUNE) | LoRA + negative examples 做 unlearning——PEFT 路线做行为修改的模板 |
| 2409.19817 | adaptive temperature scaling——logit 层修复，连权重都不用动，只是后处理 |
| 2605.18879 (ZeroUnlearn) | few-shot unlearning——最小数据量的行为修改 |

## §4 本地可行性检查（来源①：本轮 ls/find/python 工具输出）

### 磁盘现状
- `~/.lmstudio/models/Youssofal/Qwen3.6-35B-A3B-Abliterated-Heretic-MLX-6bit` —— **我们已经有过一个 abliterated 模型**（Heretic 系列 = refusal 向量消融的知名社区项目）。所以"abliteration 这条路"不是理论推演，本地已经跑过。
- 当前 8787 服务的 qwen3.8-27b：`~/.lmstudio/models/lmstudio-community/Qwen3.8-27B-MLX-5bit/`
  - 架构：Qwen3_5ForConditionalGeneration，hidden_size=5120，linear_attention + full_attention 混合（每 4 层一个 full attn）
  - **量化：5-bit affine，group_size=64**（config.json 的 quantization_config 字段，本轮读取）
  - 2180 个 tensor，每个 weight 配 scales（affine 量化参数）
  - 4 个 safetensors 分片

### 三条路径的工程评估

| 路径 | 需要什么 | 本地能做吗 | 风险 |
|---|---|---|---|
| **A. Activation steering（推理时）** | 改 vLLM 前向代码，在指定层残差流上加 α·v | 能做但要动 serving 栈（8787 是 proxy→ninfer，MEMORY.md 标注"别动推理引擎"）；替代方案：换 LM Studio 本地 serve 该模型做实验，不动 8787 | 低。可随时关闭。注意 KV-cache 污染坑（2605.10664） |
| **B. LoRA 校准适配器** | 准备校准数据集（输入 + 期望置信度标签），用 PEFT 训小 adapter，serve 时挂载 | 能做。需要 GPU/CPU 训练时间；LM Studio 支持加载 LoRA。数据从 pfb 现有评分记录就能造（M3/M4 分数就是天然的校准信号） | 低。adapter 可卸载，主权重零改动。**这是性价比最高的路径** |
| **C. 直接编辑量化权重** | 反量化→找方向→编辑→重新量化，或直接在量化空间近似操作 | 技术上可行（safetensors 就在磁盘上，python + safetensors 库可读写），但 5-bit 量化下"精确方向"的概念本身模糊——量化误差可能吃掉编辑效果 | **高**。不可逆（除非留备份）、副作用难预测、重新量化引入额外噪声。不建议作为首选 |

### 关键判断
- 用户问的"内部消融向量"在文献里对应的是 **activation direction**（残差流里的方向），不是权重矩阵本身。正确的操作对象是 hidden states，不是 weights——这直接排除了路径 C 的大部分必要性。
- 路径 B（LoRA）本质上是"用梯度下降自动找到该动的方向并固化"，比手工找向量更稳，而且 pfb 的评分体系天然提供训练信号（哪些输出过度自信、哪些欠自信）。
- 路径 A 适合做快速验证：先确认"某个方向真的控制置信度"，再决定要不要固化成 B。

## 与三层架构的关系

之前定的三层图（harness / 信源置信 / 元认知）现在可以细化第三层的干预手段梯度：
1. prompt/ICL（语言层，已验证有嘴心脱钩边界）
2. probe 读取（内部信号喂路由，不改模型）
3. **activation steering（推理时改激活，半可逆）** ← 本次新增
4. LoRA 适配器（PEFT，可卸载）
5. 权重编辑/消融（永久，最后手段）

越往下越贵、越不可逆、副作用越大。工程原则：**能用上层解决的不用下层**。校准问题大概率在第 2-4 档就有解，第 5 档留给真正必须动刀的情况（比如 refusal 行为本身要改）。

## 缺口 / 待核验

- [待核验] 2510.17426 的 merging 方法在 Qwen 系上的复现报告（原文用的什么底座）
- [待核验] 2601.08489 的 spectral cleaning 是否开源
- [待核验] Heretic abliterated 模型的具体消融方法（哪一层、什么方向、α 多少）——README 没细看，如果要复用其经验需读原仓库
- 未做 ego-browser 网页 LLM 交叉验证；以上 conf 按"刚查到的 arXiv 摘要 + 本地文件实测"= ①类，方法细节引用前需读 PDF