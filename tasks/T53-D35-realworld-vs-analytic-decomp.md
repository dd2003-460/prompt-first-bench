# T53-D35 — 真实世界迭代 vs 解析先验+泛函梯度下降（decomp）

> origin: ai · 2026-11-12 · 成璐指令："基于真实世界的迭代和梯度下降对比纯理论给一个解析先验再让模型做泛函梯度下降哪个好或者可以结合（可能需要你滚雪球了）"

## 问题重述（防曲解）

两种优化 decomp 状态机/目标函数的路线：
- **A 真实世界迭代**：跑 bench → 看指标 → 改 prompt/参数 → 再跑（model-free，环境反馈驱动）
- **B 解析先验 + 泛函梯度下降**：先用理论推导出目标函数结构（哪些项、什么形式），再让模型在这个函数空间里做梯度更新（model-based，先验驱动）

问：哪个好？还是结合？

## 分解树

### S1 同构映射（把问题翻译成已知领域）— 我自己能做
- A ≈ model-free RL / policy gradient（用环境回报直接调策略）
- B ≈ model-based planning / MBPO（先学/先验一个环境模型，在模型里算梯度）
- 关键变量：**环境的 stationary 程度**。RL 理论假设固定环境；我们的"环境"是 LLM 的分解行为，而策略（prompt）本身在改变它的输入分布 → non-stationary。
- 初步判断（凭理论直觉，conf 中）：non-stationarity 是 B 的致命伤——解析先验推导时假设的环境，在第一次 prompt 修改后就变了，先验失效。所以纯 B 不成立，**倾向结合：B 定结构（目标函数有哪些正交项、停止判据的形式），A 定参数（阈值/权重），每 K 轮用新 run 数据重估结构**。
- 缺口：这个判断需要文献支撑才能写进报告（见 S3）。

### S2 我们自己的证据盘点 — 我自己能做
- v17 Goodhart 诊断（research/v17-hier-decomposition-blowup.md）：文本目标函数被 hack 的案例 = "目标函数定义不清时被优化器钻空子"，支持"结构要先验约束"
- S8M 四臂表 + S5 管线消融：已有 ≥2 轮"改 prompt → 指标动/不动"的真实数据，可以直接当 A 路线的样本
- D34 rework 双路径：fix_rate 就是 A 路线的新观测点
- 缺口：目前只有 27b 单模型数据，"结合方案"是否跨模型成立未知 [待核验]

### S3 文献滚雪球（外包 arena）
对标方向（凭记忆列的，全部待 arena 核验存在性+结论）：
1. MBPO (Hansen et al.) — model-based policy optimization，模型误差如何限制性能
2. REINFORCE baseline / 方差缩减 — 离散搜索空间的梯度估计噪声有多大
3. Hyperband / BO vs grid search — 外层超参优化的样本效率
4. Prompt optimization 文献：ProTeGi / OPRO / DSPy — 这些就是"对 prompt 做梯度下降"的已发表工作，**这是最直接的竞品/对标，必须先查清它们怎么处理 non-stationarity 和 Goodhart**
5. 对抗鲁棒优化 / minimax — Goodhart 防御的理论框架
- 缺口：具体论文名/结论/数字全部 [待核验]，arena 回执落 research/web-llm/ 才算数

### S4 可执行的实验设计（S3 回来后我出）
- 最小验证：同一个改动，(a) 纯 A（跑了再调）vs (b) 先验预测该往哪调再验证 —— 比较"达到同等指标所需的 run 次数"
- 验收口径：run 次数 + 最终 pass_rate，judge 族沿用异族 M1-M6
- 缺口：需要 Teamer 配合跑对照（写进 lead-to-teamer）

## 正交性核对
S1（理论定位）/ S2（自有证据）/ S3（外部文献）/ S4（实验设计）两两不重叠：S1 回答"这是什么问题"，S2/S3 回答"已知事实"，S4 回答"怎么证"。✓

## 当前行动
- [x] decomp 落盘（本文件）
- [ ] S3 派 arena（任务书另写，走 arena-outsource SOP）
- [ ] S1 判断写成 1 页分析（等 S3 回来合并）
- [ ] S4 实验设计（等 S3）