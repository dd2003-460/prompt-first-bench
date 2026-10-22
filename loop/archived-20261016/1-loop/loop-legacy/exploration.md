# 探索：自主发现新方向并落成新项目（尾节点，非终止）

<!-- origin: ai -->

## 输入
- 本项目任务板 `tasks/TASKS.md`：**只放属于本项目的子任务**（仅当某阶段确实拆出了本项目内的子任务时才用）。
- workspace 级项目注册表 `projects/INDEX.md`：全局只引用索引；**新研究方向在此登记为新的 D1-* 项目**。
- 用户目标、项目缺口与已有研究（memory / loop-state）。

## 本阶段要交付什么
探索节点不是终止节点，但它的职责是**发现新研究方向并落成独立新项目**，而不是在当前项目里反复重跑同一套 01→04.5 流水线（那会把上一轮成果用同名文件覆盖掉）。

1. **先扫描本项目任务板**：读 `tasks/TASKS.md`，必要时跑 `ralph task-next .`，看是否有依赖已满足的 ready / pending **子任务**（注意：是"本项目内的子任务"，不是新研究方向）。
2. **有可接取子任务** → 在 `payload.exploration.selected_task` 完整记录 task_id / title / source / source_path / priority / reason，以 `selection_mode=task_board` 重新进入 01。
3. **没有可接取子任务 → 自主发现新研究方向**：围绕用户目标 / 项目缺口 / 已有研究，做一轮轻量调研（WebSearch、读 memory），生成 1~3 个候选方向。
   **关键区分：每个候选方向是一个全新的研究课题 = 一个全新的 D1-* 项目，绝不是当前项目的 `tasks/TASKS.md` 条目，也绝不 loop 回当前项目的 01。**
4. **为每个新方向在 `workspace/projects/` 下建独立新项目**：
   - `ralph init projects/D1-<slug>` 生成骨架（CLAUDE.md / .claude/settings.ralph.json / loop-state.json）。
   - 把该方向作为新项目的 initial task 写入其 `loop-state.json`（goal = 该方向的一句话目标；known/unknown 留空待 01 填）。
   - 在 `projects/INDEX.md` 登记这个新项目（加一行索引），全局只引用索引。
5. **当前项目探索到此结束**：新方向已在独立项目里，不要再 `advance` 回当前项目的 01。返回 `blocked_human`（payload 里列出已建好的新项目路径），由人类 / 部署层去启动新项目的循环。

## 任务板格式（仅本项目子任务）
Markdown 表格，表头需含 `ID/编号` 与 `任务/title/目标` 列，其余列可选：

| ID | 任务(目标) | 状态 | 优先级 | 依赖 | 背景 |
|----|-----------|------|--------|------|------|
| T-next | 一句话目标 | pending | P1 | | 背景与动机 |

`ralph task-next .` 会选「依赖已满足 + 优先级最高」的 ready/pending 任务。

## 检查
- [ ] 已读 `tasks/TASKS.md` 并跑过 `ralph task-next .`。
- [ ] 有 ready 子任务时 selected_task 完整 + selection_mode=task_board。
- [ ] 无子任务、发现新方向时：**已为每个方向建好独立新项目并登记进 `projects/INDEX.md`**，未把它们写成当前项目的 tasks 条目、未 loop 回当前项目 01。

## 分支
- 接取到本项目子任务：返回 `advance`，进入 `01`（selection_mode=task_board）。
- 发现新方向：建好新项目并登记后，返回 `blocked_human`（说明已建哪些新项目路径），不 loop 回 01。

## 结构化结果（接取子任务时）
```json
{
  "action": "advance",
  "status": "passed",
  "stage_id": "exploration",
  "revision": "r1",
  "next_stage": "01",
  "payload": {
    "exploration": {
      "selection_mode": "task_board",
      "selected_task": {
        "task_id": "T-next",
        "title": "…",
        "source": "task_board",
        "source_path": "tasks/TASKS.md",
        "priority": "P1",
        "reason": "…"
      }
    }
  }
}
```
