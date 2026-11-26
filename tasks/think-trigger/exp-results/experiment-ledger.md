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
