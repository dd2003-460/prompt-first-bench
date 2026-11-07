# 立场/角色 prompt 的激活方向与重叠度 — 调研（2026-11-07）

origin: ai | 触发：成璐"不同立场等对同模型激活方向和重叠程度有研究吗，也许这就是多 role 辩论的意义"
方法：arXiv API 直查 6 组 ~46 条命中（本轮工具输出，来源①）。未读 PDF 全文，具体数字标 [待核验]。

## 一句话结论

**有研究，而且直接支持你的猜想——但比"正交"更微妙：persona 在表征空间里是线性可分解的方向，不同 persona 之间部分相关、部分独立，且 persona 维度和 reasoning 维度基本解耦。** 这意味着多 role 辩论确实能在同一个模型内制造出真实的表征差异（不是纯文本层面的角色扮演），但增益大小取决于你选的 role 之间的夹角——选错了（两个高度相关的 persona）就退化回 Martingale Curse 的自我对话。

## §1 核心论文（按相关性排序）

### 1.1 "As X, Do Y: How Persona and Task Combine in Instruction-Tuned LLMs"（2605.23147, 2026-05）★ 最直接
role prompt 在 residual stream 的**一个特定位置**（prompt-to-answer transition = 最后一个 prompt token + 前两个生成 token，早/中层带）呈现**干净的线性分解**：总激活 ≈ persona 分量 + task 分量。这是"persona 是独立方向"的最强证据——不是弥散在整个表征里，而是有明确的几何结构。
→ **含义**：测两个 role 的重叠度，只需要在这个位置取残差向量算夹角，不需要全层扫描。实验成本极低。

### 1.2 "Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs"（2611.06848, 2026-11-04）★ 最新
采用不同视角会**重组**表征——直接推翻了 linear probe / SAE 的"特征跨上下文稳定"假设。同一模型在不同 persona 下，feature 的表示方式会变。
→ **含义**：persona 不只是沿某个方向平移，还会改变局部表征几何。这对多 role 辩论是双刃剑：重组 = 真正的视角差异（好），但也意味着用固定探针去检测"哪个 role 在说什么"不可靠（坏）。

### 1.3 "FOCUS: Decoupling Expert Personas in LLMs"（2608.05611, 2026-08）
专家 persona 激活能提升领域任务准确率，但现有 persona 控制有 **cross-domain coupling**——激活"物理专家"时会连带激活其他领域的残留。
→ **含义**：role 之间不是完全独立的，存在耦合项。选 role 时要挑耦合低的组合（如"较真的逻辑审查者" vs "怀疑论的数据审查者"可能耦合低，"物理专家" vs "数学专家"可能耦合高）。

### 1.4 "The Geometry of Persona: Disentangling Personality from Reasoning"（2512.07092, 2025-12）
personality 维度和 reasoning 维度在表征空间里**可解耦**。
→ **关键推论**：给模型注入"怀疑论人格"不会破坏它的推理能力——persona 和 reasoning 走的是不同的子空间。这直接回答了"加 role 会不会把模型搞笨"：**理论上不会，因为不占同一个维度**。

### 1.5 "PersonaManifold"（2609.34571, 2026-09）
persona 表征空间是**弯曲流形**，不是欧几里得线性空间——欧式操作（加减 persona 向量）在某些区域失效。
→ **含义**：两个 role 向量的"重叠度"不能用简单的余弦相似度一概而论；在大角度组合时，中点可能不在流形上（即"两种立场的平均"不是一个真实存在的立场）。

### 1.6 "PERSONA: Compositional Inference-Time Personality Control via Activation Vector Algebra"（2602.15669, 2026-02）
persona 向量可以做代数组合（加/混合），且组合效果可预测。
→ **含义**：可以合成"半较真半怀疑"的中间 role，做 dose-response 曲线——和我们 T0/T1/T2 措辞梯度实验同构，只是作用点在激活层而非 prompt 层。

### 1.7 "Your Language Model Secretly Contains Personality Subnetworks"（2602.07164, 2026-02）
模型内部存在**专门的人格子网络**，切换 persona 时这些子网络被选择性激活。
→ **含义**：persona 切换不是全局扰动，而是局部子网络的开关——进一步支持"role 制造真实独立性"的机制解释。

### 1.8 "Creative Collision: Directorial Persona Steering and Competition in LLMs"（2606.16240, 2026-06）
同时注入**两个** persona 方向时的竞争动态——两个方向不完全兼容时会互相干扰。
→ **含义**：多 role 辩论如果让同一模型在同一时间扮演两个 role（而不是串行调用），会出现方向干涉；串行调用（role A 说完 → 清空 → role B 说）则避免这个问题。

## §2 对你猜想的判断

"多 role 辩论的意义 = 不同立场激活不同方向" —— **机制层面成立，但有两个修正**：

1. **不是任意 role 都行**：role 间夹角决定独立性。高相关 role（"严谨工程师" vs "仔细工程师"）≈ 自我对话，零增量；低相关 role（"找逻辑漏洞的" vs "质疑数据口径的" vs "领域协议审查者"）才有真增量。选 role 的标准应该是**预期激活方向的低耦合**（参考 FOCUS 的 cross-domain coupling 概念）。

2. **persona ≠ reasoning 维度**（2512.07092）：所以"加 role 不伤推理"是有依据的，但反过来也意味着——**role 本身不产生新信息，它只改变注意力分配**。多 role 辩论的增量来自"不同 role 关注不同的东西"，不是"不同 role 知道不同的东西"。这和 E3 的结论一致：增量在调查阶段（注意力导向哪里），不在事后修正。

## §3 可做的廉价实验（本地 27b，~半天）

利用 2605.23147 指出的测量位置（prompt-to-answer transition 的残差向量）：
1. 取 3 个候选质询 role 的 prompt（较真/怀疑论/领域专家）+ 1 个中性 baseline
2. 同一问题、同一上下文，分别跑 4 次，取该位置的 hidden state
3. 算 4×4 余弦相似度矩阵
4. 若 role 两两 cos < 0.7（[阈值凭经验设，待调]）→ 独立性足够，S8-cascade-discuss 的三角色设计成立；若 cos > 0.9 → 换 role 组合或退回单质询者

这个实验可以直接当 S8 臂的前置验证，不用等全流程跑完才知道 role 设计是否有效。

## §4 缺口

- [待核验] 2605.23147 的"干净线性分解"是在哪些模型上验证的（摘要未提模型名）
- [待核验] 2611.06848 的"重组"效应量有多大（是整体重排还是局部微调）
- 没有文献直接测过"多 role 辩论场景下 role 间的实际重叠度随讨论轮次的变化"——§3 的实验如果做了，这部分就是空白里的第一个数据点