# 实验台账（全局视角的唯一落盘 · 2026-11-26 D 需求建立）

> **为什么有这个文件**：D 2026-11-26："需要一个能有全局视角的实验员条理清晰安排实验去消融（前人做不到的进展）"。
> 全局视角不能放在任何 agent 的上下文里（27b sub 7死6 实证：上下文一死视角就没了）。本文件 = 实验员的全局视角本体，任何 agent 读它即知全盘，它不随任何上下文死亡。

## 规则（闸门，跑实验前逐条过）

1. **预注册闸门**：每个实验开跑前，本表对应行的"预注册判据"列必须已填且 commit（跑完只读，事后修订另开行标 post-hoc）。无预注册的实验不许跑——防事后凑故事，也是 novelty claim 的防御点。
2. **一行一实验**：一个消融问题 = 一行。假设必须是可证伪的一句话（"X 导致 Y"），不是"看看 X"。
3. **novelty 定位必填**：每行"前人 diff"列写：前人做到哪（引用 competitor-survey.md 或文献）+ 我们多走的这一步是什么。写不出 = 不是进展，是重复，不进队列。
4. **状态机**：planned → preregistered → running → done / invalid。invalid 不删除，保留 + 作废原因（负结果也是资产：它排除了什么错误解释）。
5. **机械判据优先**：判据尽量落到可复算的数字（judge 脚本/oracle），模型判断只作 secondary。
6. **排序权在 arena**：下一步跑哪个臂（信息增益最大优先）由 arena 读本文件后排，Lead 验收排序理由，sub 只执行排好的单个臂。

## 每组实验的落盘规范（D 2026-11-26 要求："每一组实验对照/实验组数据和judge清晰"）

> 台账管"有哪些实验、下一步跑什么"（管理视角）；本节管"每组实验内部数据是否清晰"（实验视角）。D 的要求落在本节。

**最小单元 = 一个目录 `exp-results/<exp-id>/`，四件套齐备才算"清晰"：**

| 件 | 文件 | 内容 | 闸门 |
|---|---|---|---|
| 预注册 | `spec.md` | 假设（可证伪一句话）/ 对照臂与实验臂定义 / judge 判据+版本 / 样本量 | 跑前 commit，commit 时间戳必须早于 arms 数据 |
| 数据 | `arms/<arm-name>/` | 每臂：原始输出（raw，不裁剪）+ 提取数据 | 对照臂和实验臂各一目录，命名一致可比 |
| judge | `judge/eval.json` | judge 脚本版本 + 判据引用 + 每臂逐样本分数 + 汇总 | 必须由脚本生成可复算（手填=不合格） |
| 结论 | `report.md` | 一行：对照 vs 实验 Δ + 判据 + 数字 + 是否过预注册线 | 数字必须与 eval.json 一致（lint 比对） |

**"清晰"的可检验定义**：任何人读 `report.md` 一行 + 打开 `eval.json` 能复算出每个分数，不用再翻散文找数字。lint 三条：① 四件套文件存在 ② spec commit 时间 < arms 数据 mtime（预注册先行）③ report 数字 == eval.json 数字（机械比对）。

**存量处置**：现有实验（T8b/T8c smoke、stage-ablation）大多散文件不合规 → 盘点 completeness 字段查现状，不合规的排队重组（脚本搬目录 S1 + report 一行 S2）。**新实验（T8c 正式批起）直接按本规范跑**，不合规的 run 不收进台账。

## 表

| ID | 消融问题（可证伪假设） | 臂 | 预注册判据 | 状态 | 结果（数字） | 前人 diff | 证据 |
|---|---|---|---|---|---|---|---|
| _（待盘点 sub 回填：experiment-inventory-20261126.json → 本表）_ | | | | | | | |

## 队列（arena 排序区）

- 待排：（盘点回填后由 arena 出排序 + 理由）

## 指针

- 竞品/前人基线：`pfb/experiments/stage-ablation/competitor-survey.md`
- 阶段消融设计：`pfb-thinkmech/experiments/stage-ablation/DESIGN.md`
- 机制准入（新检测器/触发器才准进队列）：`tasks/think-trigger/decomposition.md` 机制准入门节
- 盘点原料：`exp-results/experiment-inventory-20261126.json`
