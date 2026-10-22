# RALPH Loop 使用手册（面向成璐）

> 这份文档只讲"怎么用"，不重复 runtime 内部实现。
> 想看状态机 / Prompt / DAG / Hook 的关系，读 `ralph_runtime/README.md`；
> 想看字段门禁设计，读 `ralph-dynamic-fields-design.md`；
> 想看错误码对照，读 `ralph-feedback-prompts.md`。

---

## 0. 一句话定位

- **RALPH 负责**：校验 Agent 返回、判断阶段转换是否合法、保存状态、记录事件、用 Hook 控制工具调用能不能发生。
- **Claude 负责**：理解任务、执行工作、提交结构化结果（`RALPH_STAGE_RESULT` JSON）。
- **新研究方向 = 新项目**：每个 `D1-*` 一个独立项目，自带 `loop-state.json` / `loop-events.md` / `tasks/`。
- **本地 35B 字段中心闭环**：正常跑用 `ralph loop`（进程退出后自动开新上下文继续）。

Workspace 根：`/Users/a1-6/Desktop/workspace`
Runtime 入口命令：`ralph`（已装在全局 venv，改 `loop/ralph_runtime/` 后即时生效）。

---

## 1. 如何启动一个新项目（用这个 runtime）

### 1.1 最短启动（自动匹配 / 创建）
```bash
cd /Users/a1-6/Desktop/workspace
ralph run "我需要跑本地 AI，帮我调研性价比最高的 GPU"
```
这条命令会自动完成：
1. 在 `workspace/projects/` 下扫描带 `loop-state.json` / `tasks/` / `loop/INDEX.md` 的项目；
2. 关键词匹配足够明确时**复用**旧项目，否则创建一个确定性的 `D1-*` 项目目录；
3. 缺失时创建 `loop-state.json`、`loop-events.md`、`CLAUDE.md`、`.claude/agents` 软链、`settings.ralph.json`（enforce 模式 Hook）；
4. 把任务写进状态，并作为交互式 Claude Code 会话的第一条输入。

### 1.2 显式指定项目路径
```bash
ralph run /path/to/project "任务描述"
```
- 项目已存在 → 复用 `loop-state.json`，**不会**把阶段重置到 01（只更新任务描述）。
- 项目状态已是 `completed` → `ralph run` 视为一次明确的新运行，保留旧摘要到 `run_history` 并从 01 重开。

### 1.3 持续无人值守（推荐的正常用法）
```bash
ralph loop "任务描述"                 # 自动匹配/创建，每轮新上下文持续推进
ralph loop /path/to/project           # 显式继续已有项目
ralph loop "测试任务分解" --max-cycles 3 --effort low   # 只跑有限轮做实验
```
- 每轮：读 `loop-state.json` → 回收上轮遗留的 `dispatched` 卡 → 用新 Claude 上下文提交阶段 Prompt → 退出后等 grace period → 有门禁回执就完成卡、无回执就退回 `pending` → 下一轮。
- 默认遇到 `blocked_human` 会按任务策略**跳过并进入后续可执行节点**；需要真等人时用 `--wait-human`。
- 默认 `--idle-timeout 1800`：连续 30 分钟 `loop-state.json` / `loop-events.md` 无变化才终止当前上下文（状态保留，进下一轮）。设备慢可调到 3600，完全关闭用 `--idle-timeout 0`。

### 1.4 放进 tmux（关终端也继续跑）
`ralph loop` 是前台进程，关终端会被杀。用 tmux 包一层：
```bash
tmux new -s ralph-<项目短名> -d 'ralph loop /path/to/project'
tmux ls                      # 看有哪些会话
tmux attach -t ralph-<短名>  # 进入查看（Ctrl-b d  detach，不中断）
```
会话命名约定：`ralph-<短名>`（例如 `ralph-mon`、`ralph-motivation`）。runtime 本身不强制 tmux，这只是运行方式。

### 1.5 继续 / 恢复（不重置）
```bash
ralph start /path/to/project            # 只启动项目，不注入新任务描述
ralph resume /path/to/project           # 丢弃旧 transcript，用短上下文从 loop-state.json 恢复
```
> 本地模型因上下文/内存保护停止时，**不要**用 Claude Code 的 `--continue`（会重新 prefill 巨大旧对话）。用 `ralph resume`。

### 1.6 常用运行参数
| 参数 | 作用 |
|---|---|
| `--mode shadow\|enforce` | shadow=只提示不拦截；enforce=真正拒绝非法工具/Stop（默认 enforce） |
| `--effort low\|medium\|high\|xhigh\|max` | 只影响 Claude 推理强度，不改状态机规则 |
| `--model "模型名"` | 仅本次会话使用的模型（不写回全局配置） |
| `--auto-compact-window 40000 --auto-compact-percent 80` | 本地模型内存保护起点（默认即此） |
| `--dangerously-skip-permissions` | 跳过 Claude 交互式权限确认（RALPH Hook 仍强制） |

### 1.7 路径坑
- `ralph run /gpu硬件调研 "..."` 会被当成**系统根目录**下的绝对路径（不可写）。
- 想在当前目录建项目用 `./gpu硬件调研`，或用户目录 `$HOME/gpu硬件调研`。

---

## 2. 如何找出 / 排查问题

排查顺序建议：**先看状态 → 看事件尾部 → 看 log → 看 Hook 拒绝原因**。

### 2.1 状态与事件快照
```bash
ralph status <project>            # 当前阶段、状态、任务卡生命周期
ralph events <project> --tail 20 # 最近事件摘要（类型/阶段/卡生命周期/短错误/输出摘录）
ralph watch <project>             # 实时看板，每 5s 刷新，任意项目可用
```
> ⚠️ **不要直接用 Read 打开 `loop-events.md`**：会被 PreToolUse 拒绝，且浪费上下文。`ralph events --tail 20` 是受控摘要入口。

### 2.2 Hook 拦截（enforce 模式）的常见原因
Hook 拒绝依据是**结构化状态**（当前阶段 + 角色 + 工具 + 目标路径 + 任务卡首行引用），不是关键词。返回形如 `RALPH_FEEDBACK[错误码]`：
- **缺字段 / JSON 不合法**：`RALPH_STAGE_RESULT` 未过 `protocol.py` 校验（如 `advance requires next_stage`）。→ 只返回满足协议的 JSON，别手改状态文件。
- **越权写入**：Commander 不能裸 `Agent`、不能 `Write/Edit` 阶段契约 / `loop-state.json` / 任务卡。→ 派发必须首行 `RALPH_TASK_CARD=loop-artifacts/task-cards/xxx.md`。
- **门禁回执缺失 / 终态无效**：卡被错误标成 `completed/failed` 但无有效 gate receipt。
  ```bash
  ralph recover-card <project> <card-id> --reason "说明为何这次终态无效"
  # 仅当已核实旧进程退出且无 SubagentStop/gate receipt：
  ralph recover-card <project> <card-id> --force-dispatched --reason "..."
  ```

### 2.3 状态损坏 / 想回退
```bash
ralph recover-state <project>            # 从 .bak 或阶段快照恢复（重置到上一阶段）
ralph recover-state <project> --stage 03 # 恢复到指定阶段快照
ralph recover-state <project> --to-backup
```

### 2.4 阶段结果工件校验
```bash
ralph validate <project>                       # 校验当前 plan 的 DAG 结构
ralph validate <project> --result <artifact>   # 机械校验某个阶段提交工件
ralph validate <project> --result <artifact> --apply  # 校验通过才原子应用
```

### 2.5 分解质量（只读，不修改项目）
```bash
ralph benchmark-decomposition <project>   # 检查 01 语义分解 + auditor 是否真完成
```

### 2.6 LaTeX 书稿类项目的典型坑（本次《动机社会》踩过的）
书稿用 `subfiles`：每章是独立 `.tex`，开头 `\documentclass[../main.tex]{subfiles}` + `\begin{document}…\end{document}`，主文件用 `\subfile{...}` 引入。合并冲突或人工编辑时极易引入下面几类坏文件：

1. **子文件丢了 `\begin{document}` / `\end{document}`**
   → `xelatex` 报 `! File ended while scanning use of \documentclass.`
   → 原因：`\subfile` 靠子文件里的 `\begin{document}` 标记正文起点；缺了它，subfiles 把整篇当 preamble，子文件的 `\documentclass` 被当成正文命令反复执行。
   → 修复：恢复子文件头尾的 `\begin{document}` / `\end{document}`（对照兄弟章节结构）。

2. **合并把 `\xrightarrow{...}` 截坏**
   → 变成 `$ightarrow$`（丢了 `\x` 和参数）或 `\xr\rightarrow{...}`（`\xr` 已在 `main.tex` 定义为 `\xrightarrow`，多接了 `\rightarrow`）。
   → 报 `Runaway argument` / `File ended while scanning use of \documentclass`。
   → 修复：改成 `\xrightarrow{\text{...}}`；`\xr\rightarrow` → `\xr`（即 `\xrightarrow`）。

3. **冲突 HEAD 侧缺 `}` 导致 `\textbf` 未闭合**
   → 报 `! File ended while scanning use of \textbf.`
   → 修复：补上缺失的 `}`。

**通用定位流程**（以 `main.tex` 为例）：
```bash
cd <项目>/motivation_society
rm -f main.aux main.toc main.out main.log
~/Library/TinyTeX/bin/universal-darwin/xelatex -interaction=nonstopmode -halt-on-error main.tex 2>&1 | grep -E "^!|Runaway|File ended|Output written"
```
- 看最后一个 `!` / `Runaway` 指向哪个子文件；**二分法**注释某个 `\subfile{...}` 看是否通过，定位坏文件。
- 对嫌疑子文件检查：头尾 `\begin/\end{document}` 是否配对；brace `{` `}`、`$` 数学定界符、环境 `\begin/\end` 是否平衡。
- 冲突标记必查：`grep -rn "<<<<<<< HEAD\|>>>>>>> " --include=*.tex .`（有则先解冲突，保留 HEAD 侧且**保留 document 环境**）。

---

## 3. 如何监控正在工作的会话

### 3.1 tmux（最直接）
```bash
tmux ls                          # 列出所有会话（如 ralph-mon）
tmux attach -t ralph-mon         # 进入查看实时输出
# 在 tmux 内：Ctrl-b d  detach（ detachment，会话继续跑）
```
- 想停监督器但保留状态：在 tmux 内 `Ctrl-c`（只停监督器，不删状态/事件）。
- `ralph loop` 的 `--max-cycles 0` 是持续运行；`Ctrl-c` 只停监督器。

### 3.2 ralph 命令行看板（任意项目，不依赖 stdout）
```bash
ralph watch <project>            # 轮询 loop-state.json / 阶段文件 / 事件，默认每 5s 刷新
ralph status <project>           # 一次性状态快照
ralph events <project> --tail 20 # 最近动作 / 门禁 / 错误摘要
```

### 3.3 文件级观察
| 文件 | 看什么 |
|---|---|
| `<project>/loop-state.json` | `status` 字段：`stage_0x` / `blocked_human` / `running` / `completed`；任务卡生命周期 `pending→dispatched→completed/failed` |
| `<project>/loop-events.md` | 完整审计（**别全读**，用 `ralph events`） |
| `ralph.log` | 运行日志，在启动目录下（tmux 里 `Ctrl-b [` 滚动或 `tail -f ralph.log`） |

### 3.4 判断是否空转 / 卡住
- 监督器默认 `--idle-timeout 1800`：连续 30 分钟 `loop-state.json` 和 `loop-events.md` 都**无变化**才终止当前上下文；状态保留后马上进下一轮。
- 怀疑卡住：对比 `ralph events --tail 20` 的时间戳与 `ralph watch` 的刷新；若长期无新事件，去 tmux 里看实时输出或 `tail -f ralph.log`。
- `blocked_human` 不是卡死：监督器会跳过它去做其他可执行工作；只有 `--wait-human` 才真停等人。

---

## 4. 红线（不要做的事）
- Commander **不裸派 Agent**、**不 Write/Edit** `loop-state.json`、阶段契约、任务卡（这些由 runtime 生成/校验，绕过 Hook 会被拒）。
- 派发必须首行 `RALPH_TASK_CARD=loop-artifacts/task-cards/xxx.md`，且卡处于 `pending`/`dispatched` 合法生命周期。
- 阶段推进必须过独立门禁（`requirements-auditor` / `dag-auditor` / `execution-join-auditor` / `evidence-verifier` / `decision-auditor` / `handoff-auditor`），`stage_review` 全 `pass` 且无阻塞发现才 `advance`。
- 不要直接 `--continue` 恢复因内存保护中断的旧 transcript，用 `ralph resume`。
- 项目按领域分层，每 `D1-*` 独立；全局只引用索引，不重复创建。

---

## 5. 常用命令速查
```bash
ralph run "任务描述"                       # 最短启动（自动建/匹配项目）
ralph run /path/to/project "任务描述"      # 显式项目
ralph loop /path/to/project                # 持续无人值守
tmux new -s ralph-x -d 'ralph loop /path/to/project'   # tmux 后台

ralph status <project>                     # 状态快照
ralph events <project> --tail 20           # 事件摘要
ralph watch <project>                      # 实时看板
ralph recover-state <project>              # 状态回退
ralph recover-card <project> <card> --reason "..."   # 恢复无效终态卡
ralph validate <project> [--result <artifact>] [--apply]   # 校验
ralph benchmark-decomposition <project>   # 分解质量（只读）
ralph resume <project>                     # 短上下文恢复
```
