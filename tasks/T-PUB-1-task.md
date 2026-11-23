# T-PUB-1 · 公式 judge 论文题集 10 题（2026-11-23）
# origin: ai · 派发：arena agent mode · 验收：Lead（D）核 gold

## 任务指纹（回执必须原样带回）
- repo: dd2003-460/prompt-first-bench
- branch: main
- 任务书路径: tasks/T-PUB-1-task.md
- 任务书正文 sha256（第9行起，排除指纹块）: 20af62bf53435ea55b417825796eafc84b76e0949f802020a43ce4fe62677638
- 派发时 main HEAD: a3d0b6d1b

## 背景（agent 需要知道的）
我们要写一篇论文：机械公式验证器替代 LLM-as-judge 做 agent 可靠性评估。
每题预置 3-5 个可机械判定的检查点（gold），模型输出后由 SymPy/脚本判分，
不依赖 LLM judge（消除 self-preference / phantom / surface-compliance 三大失败）。
现在需要 10 道题目 + 每题的 spec（gold 检查点）。

## 交付物
`tasks/T-PUB-1-result.md`，每题一节，含：
1. **题面**（给模型看的完整 prompt，自包含，含所有给定参数）
2. **spec JSON**（给判分脚本用的 gold，模型看不到）：
```json
{
  "id": "T-PUB-1-Q01",
  "domain": "gpu|math|physics",
  "type": "full|rank-deficient",
  "checkpoints": [
    {"id": "c1", "kind": "calc|fact|bool", "desc": "检查什么",
     "gold": "<SymPy 表达式或数值或 0/1>", "tolerance": 0.02,
     "source": "<datasheet URL 或 推导链>"},
    ...
  ],
  "reward_only_feedback": "逐检查点 对/错 串（不含正确值）"
}
```

## 题目要求（10 题）
- **7 题 full 型**（信息充分，满秩）：
  - 5 题 GPU 推理域：decode 吞吐 / KV cache 大小 / ridge point / 显存预算 / 互联带宽瓶颈。
    参数用真实 datasheet 规格（H100/H200/A100），fact 类检查点必须给 datasheet URL。
  - 2 题数学/物理域：有闭式解的推导题（如带根号的对称矩阵特征值、信号衰减链）。
- **3 题 rank-deficient 型**（秩亏，2026-11-23 设计修正，重要）：
  - 题面**故意缺一个关键事实**（如只给"带宽约 3TB/s 级别"不给精确值），
    或给**不完整的检索结果**（只给概述不给数值——模拟"查了但没查全"）。
  - 检查点测的是**批判准确性**，不是"会不会主动去查"（实测证明模型不自主触发检索）：
    - bool：模型是否识别出"来源不足/信息不够"
    - fact：模型是否准确说出缺的是哪个量（gold 预置那个缺失事实）
    - bool：模型是否**没有**幻觉出那个缺失值（瞎编一个数 = 幻觉 = 判错）
  - 这 3 题是论文的核心新维度（校准腿），设计要干净：缺口唯一、可判定、无歧义。

## 防 hack 要求（每题都要满足）
1. 数值不凑整：带根号 / 无理数 / 非整数 GB（防 memorization + 防单点 shortcut）
2. 每题 ≥3 检查点，检查点间有推导依赖（c2 依赖 c1 的中间量，防逐点独立蒙对）
3. 题面参数是模型没见过的组合（真实规格 + 新设定，如 W=2√5 GB）
4. gold 可复现：calc 类给 SymPy 表达式（判分脚本直接 eval），fact 类给 URL

## 验收标准（Lead 核）
- [ ] 10 题齐全：7 full（5 GPU + 2 math/phys）+ 3 rank-deficient
- [ ] 每题 3-5 检查点，kind 标注正确
- [ ] 所有 calc gold 用 SymPy 可 eval（agent 自己跑一遍验证 gold 自洽）
- [ ] 所有 fact gold 有可访问的 datasheet/来源 URL
- [ ] 3 道秩亏题：缺口唯一 + 无歧义 + 幻觉可判
- [ ] 每题附"为什么这题好"一句话（误读陷阱在哪 / 检查点依赖链）
- [ ] 回执：本任务书指纹原样带回 + 自述方法学缺口（哪些题的 gold 你不确定）

## 边界
- 不改仓库其他文件，只写 tasks/T-PUB-1-result.md
- 不确定的 gold 标 [待核验] 并在回执里列出，不要硬编
- 题面用英文（论文用），spec 注释可中文
