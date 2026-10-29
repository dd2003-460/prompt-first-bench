# C3 v3 冻结 diff（R4 全因子 8 组 + sham）

> 预注册冻结文件：所有 run 严格复用本文件的删除/替换操作，不允许临场改写。
> 基线 = loop/prompt-first/ 当前 main（r57）。组件定位以 T7.1 工件实际形态为准（T6 r1 键盘域同构）。

## 组件精确定位

| 组件 | 位置 | 内容边界 | 被删 token 数（估） |
|---|---|---|---|
| **freeze** | `01-goal-decomposition.md` L45 | 「候选集冻结（防漂移）」整条 bullet（从 `- **候选集冻结（防漂移）**` 到该行结尾） | ~112 |
| **evidence** | `02-information-research.md` L54 | 「证据来源完备（防"名不副实"）」整条 bullet（Reviewer 质检标准节内） | ~78 |
| **owner** | `03-action-decomposition.md` L32 | 「owner 类型标注（防粒度混排）」整条编号项（第 5 条，含 Reviewer 判据句） | ~91 |

注：三处均为 prompt 的**规则条款**（指令性文本），不是示例或流程骨架。删除后其余条款保持原序、原文。token 数 = CJK 字符 + 拉丁词元（估，±10%）。

## 8 组配置定义

| 配置 | freeze | evidence | owner | 操作 |
|---|---|---|---|---|
| A-full | ✓ | ✓ | ✓ | 无改动（基线） |
| B-nofreeze | ✗ | ✓ | ✓ | 删 freeze 行 |
| B-noevidence | ✓ | ✗ | ✓ | 删 evidence 行 |
| B-noowner | ✓ | ✓ | ✗ | 删 owner 行 |
| B-2del-fe | ✗ | ✗ | ✓ | 删 freeze + evidence |
| B-2del-fo | ✗ | ✓ | ✗ | 删 freeze + owner |
| B-2del-eo | ✓ | ✗ | ✗ | 删 evidence + owner |
| B-none | ✗ | ✗ | ✗ | 删全部三条 |

## B-sham（阴性对照 · R4 升级版）

token-matched「连贯但任务无关」文本替换 **freeze 位**（选 freeze 因它是 r47 偏离度最大、最可能承载长度效应的组件）：
- 替换文本：等长（±10% token 数，目标 ~112±11）的连贯中文段落，内容为**与任务完全无关的通用办公常识**，保持 markdown bullet 格式与缩进一致。
- 目的：控制"prompt 变短/结构变化"混淆，保留语言自然度。sham 出现超容忍效应 → 先查实现与位置混淆，不进因果判读。
- 替换文本定稿（冻结，run 间不得改）：见下方 §sham-text。

### §sham-text（冻结）
- **会议记录规范（通用说明）**：会议纪要应记录议题背景、各方立场、最终决议、责任人与截止时间；未决事项单列并标注跟进节点。归档按项目维度建目录，文件名含日期与版本号以便检索。跨部门事项抄送相关方，避免信息断层。以上为一般管理实践，与本任务选型目标无直接关联。

## 阳性对照（评分器敏感度 · R5 配套）

在独立校准工件中植入 1 个**已知且会影响结论的未处置矛盾**（取 T7.1 02.5 X 清单中一条真实矛盾，把其处置标记改为"已解释"但保留原始冲突数据），要求裁决器识别退化。识别失败 → 停止 M8 因果判读。

## 运行参数（ninfer :8000）

- model=qwen3.8-27b（reasoning 模型）
- max_tokens ≥ 2048（reasoning_content 会吃掉短预算，r52/r53 实测教训）
- temperature 固定（生成用 0.7 对齐 L1 协议；评分/judge 用 0）
- 每配置每域 ≥2 run；seed 集固定并在 m8-scorecard 登记
