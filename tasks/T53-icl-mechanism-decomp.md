# ICL 机制调研 decomp（2026-11-13）

> origin: human 指令 + ai 分解 · D 原话："prompt导致的不同输出不是非常trivial的结论吗，关键是有什么可解释的，定向的，general的可操控结果，例如icl多大程度上相当于training，具体对应什么，train的梯度等等能否搬到icl"

## 问题重述（去掉 trivial 层）

"prompt 变了输出就变"是废话。真正的问题：**ICL 在机制上对应 training 的哪个对象？这个对应关系里哪些量是可测、可控、可迁移的？**

## 分解树（正交子项）

### A. ICL ↔ training 的对应物是什么（理论侧）
- A1. "隐式优化器"家族：transformer 前向传播被证明实现 GD/预条件 GD/函数 GD——即 context 里的演示数据被 forward pass "在线消化"，等价于若干步梯度更新
  - [已核验] von Oswald et al., "Transformers learn in-context by gradient descent", arXiv:2212.07677 (2022)
  - [已核验] Ahn et al., "Transformers learn to implement preconditioned gradient descent for in-context learning", arXiv:2306.00297 (2023)
  - [已核验] Cheng/Chen/Sra, "Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context", arXiv:2312.06528 (2023)
  - [已核验] Mishra/Patel/Tewari, "Continuum Transformers Perform In-Context Learning by Operator Gradient Descent", arXiv:2505.17838 (2025)
- A2. 反方：并非所有 ICL 都是 fine-tuning 式学习；线性回归任务下 transformer 学的是闭式解（(X^TX)^{-1}X^Ty）而非迭代 GD
  - [待核验] "All In-Context Learning Is Not Fine-Tuning"（凭记忆，ID 未查到，需 ego-browser 确认作者/年份/venue）
  - [已核验] Hagiwara 两篇：linear self-attention 实现 closed-form linear regression solver, arXiv:2607.15819 (2026-07) + masked 版 arXiv:2611.02817 (2026-11)
- A3. 表示侧：task vector——ICL 任务被编码为表征空间中的向量；encoder-decoder 视角下 task encoding quality 预测 ICL 性能
  - [已核验] Han/Song/Gore, "Emergence and Effectiveness of Task Vectors in In-Context Learning: An Encoder Decoder Perspective", arXiv:2412.12276 (2024)
  - [已核验] Olsson et al., "In-context Learning and Induction Heads", arXiv:2209.11895 (Anthropic 2022)——induction head 出现点与 ICL 能力突增同步
- A4. 对抗视角：ICL 可被 prompt 劫持（hijacking attack），说明 task 是被"推断"出来的而非硬连线
  - [已核验] Anwar/von Oswald/Kirsch, "Understanding In-Context Learning of Linear Models in Transformers Through an Adversarial Lens", arXiv:2411.05189 (2024)

### B. train 的东西能否搬到 ICL（迁移侧）
- B1. **能搬**：task vector 算术（fine-tune 前后权重差 = 方向向量，可加到 base 模型上做 steering）→ 这是 "train 的产物直接注入 ICL 行为" 的最直接通道 [凭记忆，未本轮核验，conf 0.6]
- B2. **能搬**：LoRA/PEFT 低秩增量 ≈ 对 task vector 空间的显式参数化；ICL 与 PEFT 在同一低维子空间内的可比性 [待核验]
- B3. **不能直接搬**：训练梯度本身——ICL 没有显式梯度通路，"等效梯度"只存在于理论构造里（A1 的 weight construction 是存在性证明，不是模型内部真的在算那个数）。所以"把 train 的梯度搬到 icl"字面意义不成立，成立的是"把 train 学到的**解/方向**搬过去"
- B4. test-time training 作为桥梁：PERK (arXiv:2507.06415, 2025) 用嵌套优化环在 test time 做真实梯度更新来编码长 context——等于承认"纯 ICL 不够时，真的跑几步 GD 是有效升级"

### C. 可解释 + 定向 + general 的可操控结果（落地侧）
- C1. **删句测试的理论版本**：I(prompt; output) 的近似——context 中每个 demo 对最终输出的边际贡献可用 leave-one-out 测，对应 taste-sop #1
- C2. **demo 数量-性能曲线**：ICL 的 sample complexity 与 few-shot 数量的标度关系 → 决定"给几个例子够"（我们 bench 的 k-shot 设计直接用）[标度律细节待核验]
- C3. **格式/位置敏感性**：MCQ option position bias（token bias 导致偏好特定选项 ID）→ prompt 工程里"措辞不改语义但改 token 分布"会系统性偏输出 [已核验] Zheng et al., arXiv:2309.03882 (2023)；instruction sensitivity 使 embedding 评测分数不可复现 [已核验] arXiv:2605.22544 (2026)
- C4. **prompt 压缩**：PCToolkit 等——压缩 prompt 保信息，功能等价选更短（taste-sop #4 压缩律的直接应用）[已核验] arXiv:2403.17411 (2024)
- C5. **grokking/延迟泛化**：ICL 的残差结构——先过拟合 context 再泛化，时间序列上的"先正后负"残差 [凭记忆，未本轮核验]

### D. 对我们系统的直接用途
- D1. T53b hook 臂的解释框架：hook 改变的是 context 分布 → 改变隐式优化器的"初始条件/损失景观"，Δ+0.025 落在噪声内说明该改动对隐式目标无杠杆（taste-sop #3）
- D2. S5 状态机的 prompt 修改流程：每次改 prompt = 改隐式 GD 的损失函数 → 必须走删句测试 + 杠杆测试，否则就是 Goodhart 刷代理
- D3. 非平稳性（F 模块 gap）的新表述：prompt 一改，隐式优化器解的任务变了，历史评估全部失效——这就是 variation budget 问题的机制版解释

## 缺口汇总
1. [待核验] "All In-Context Learning Is Not Fine-Tuning" 精确出处（凭记忆 conf 0.7，标题党嫌疑，可能实际主张更弱）
2. [待核验] task vector arithmetic 的代表文献（Ilharco et al. task arithmetic? 凭记忆 conf 0.6）
3. [待核验] ICL sample complexity 标度律的具体形式
4. A1 各文的适用边界：都假设线性/浅层/合成任务，对 LLM 规模的自然语言任务只是"证据"不是"定理"——引用时必须带这个限定
5. grokking 与 ICL 的关联强度 [待核验]

## 下一步
A/B/C 三块事实密度够写讨论稿了，但 1-3 三个 [待核验] 项按规矩要 ego-browser/arena 交叉验证后才能进行动前提。建议外包 arena 做一轮核验（任务书按 stage-gate 03-dispatch 模板），同时 D1-D3 可以先落进 taste-sop 的"应用场景"节——它们不依赖待核验项。
