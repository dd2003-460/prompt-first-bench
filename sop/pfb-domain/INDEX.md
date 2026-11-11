# PFB 领域 SOP 索引

> origin: ai · 2026-11-07 · 成璐指令："pfb这些规则可以做成领域sop"
> 本文件夹是 pfb（prompt-first-bench）实验的完整操作规程。每份文件开头解释"为什么这样做"，再给具体步骤。新 agent 接手时从这里开始读。

## 文件清单

| 文件 | 内容 | 什么时候用 |
|------|------|-----------|
| `INDEX.md` | 本文件 | 入口 |
| `prompt-design.md` | prompt 臂设计规范：v0-v3 版本线、引导式 vs 机械式、S10 tone finding | 设计新臂 / 修改现有 prompt 时 |
| `judge-calibration.md` | judge 校准流程：异族 judge 要求、κ≥0.6 门禁、battle 通道操作、M1-M6 rubric | 跑评分前 / 数字要对外宣称时 |
| `run-protocol.md` | 实验运行规范：arm×question×rep 矩阵、落盘格式、resume 机制、error handling | 跑新实验 / 补 run 时 |
| `scoring.md` | 评分流程：score.py / score_s10.py 用法、gold tree 对齐、M1-M6 各维度含义、conf cap | 打分 / 出对比表时 |
| `research-hook.md` | research_hook 架构：arXiv API + 直访站点双通道、KNOWN_SITES 维护、snippet 提取、HBM 窗口去重 | 改 research hook / 加新题源站时 |
| `gold-tree.md` | gold tree 构建规范：节点/叶子定义、Jaccard 覆盖率计算、正交性检查、B1 新题模板 | 建 gold / 算覆盖率时 |
| `arena-outsource-pfb.md` | pfb 专属 arena 外包：任务书模板、回执验收、T 编号台账 | 派 arena 做 pfb 相关工作时 |
| `modification-rationale.md` | 机制修改三问（为什么加/正交性/外部依据）+ 退出条件 + 当前生效机制清单 M1-M10 | **任何规则/机制改动前必读** |

## 核心原则（所有 SOP 共享）

**1. 引导式 > 机械式。** S10 实验证明（@4ecb5ee）：同样的纠正内容，人话+讲原因+安抚（total 0.70-0.75）比机械清单（0.426）好 0.32。这不是风格偏好，是模型行为差异——机械反馈让模型停在表面交卷，引导式让模型继续深挖。所以所有面向模型的 prompt（包括 reviewer 反馈、judge 指令）都用目标+原因结构，不用打勾清单。

**2. 先查后拆。** 分解本身不应依赖模型判断。正确顺序：调研父节点 → 发现矛盾 → 按证据分解 → 递归。直接让模型"列出子项"会把它的偏见固化进结构里。

**3. 自判不对外。** 本地 27b 自判（conf cap 0.7）只用于方向判断和快速迭代。任何要写进论文或对外宣称的数字，必须过异族 judge（≥2 家族，κ≥0.6）。

**4. 以事实为准。** 反作弊规则：模型说"我查了 X"不算数，要看输出里有没有实际引用 X 的内容。独立性警觉通过 T29 R1-R7 检查。

**5. 范围限定诚实。** D-face 跨域 FAIL（Q6/Q7 覆盖率 0.44）不是 bug，是模型能力边界的诚实测量。pfb 适用域声明为 AI/ML，跨域结果作为 limitation 讨论，不硬撑。