# B1: AI/ML 域内泛化 — 新题选题 + Gold Tree 构建

> origin: ai · 2026-11-07 · PFB-APPLY B 面子任务
> 状态：任务卡就绪，待 S10 打分完成后派发 arena

## 背景

D-face 跨域 FAIL 已定性为 27b 模型天花板（三轮实验确认）。范围限定决策已落地：pfb 适用域 = AI/ML。B 面（真实泛化）改为在 AI/ML 域内验证——不同子领域之间 pfb 是否仍然有效。

现有 5 题覆盖：GPU 硬件规格、模型选型、推理基础设施、数据处理架构、科研方法论。需要加 3 道新题，覆盖不同子领域且与现有 5 题正交。

## 候选新题（选 3）

| # | 子领域 | 题面方向 | 与现有题的正交性 |
|---|--------|---------|----------------|
| Q8 | LLM 评估方法 | "设计一个 LLM benchmark 评估代码生成能力，需要考虑哪些维度？如何防止数据泄漏？" | 与 Q5(科研方法论) 部分重叠但聚焦 LLM-specific 评估；gold 可参考 HumanEval/MBPP/Codeforces 设计文献 |
| Q9 | 多模态架构 | "Vision-Language Model (CLIP/SAM/GPT-4V) 的架构差异和适用场景对比" | 全新子领域，现有 5 题无覆盖 |
| Q10 | RLHF/对齐 | "RLHF pipeline 的关键步骤、超参选择和对齐税(alignment tax)的量化" | 全新子领域，涉及训练流程而非推理/部署 |

**推荐：Q8 + Q9 + Q10 全选**——三个子领域互不重叠，且都与现有 Q1-Q5 正交。

## 每道题需要产出

1. **题面文件**：`bench/questions/Q{N}-*.txt`（问题描述 + 约束条件）
2. **Gold tree**：`bench/rubric-v3/ablation/gold-Q{N}.md`（节点树 + 叶子值 + 来源标注）
   - 标准：对标 gold-Q6.md / gold-Q7.md 的格式（节点编号 N-X.Y、深度 ≤4、叶子带具体数值/引用）
   - 独立调研：不得引用 Q1-Q5 的 gold 内容
3. **QUESTIONS 注册**：`ablation_harness.py` → QUESTIONS dict 新增条目
4. **搜索 query**：每题一条 arXiv 检索 query（用于 research_hook）

## 验收标准

- [ ] 3 道新题题面落盘
- [ ] 3 份 gold tree 落盘（每份 ≥30 节点、≥10 叶子、深度 ≤4）
- [ ] QUESTIONS 注册完成，harness 能识别 Q8/Q9/Q10
- [ ] 独立调研声明（未引用 Q1-Q5 gold）
- [ ] commit + push 到 arena 分支

## 派发方式

arena agent mode（有 web 检索能力），任务书 = 本文件 + 格式参考（gold-Q6.md 前 50 行）+ 验收标准。