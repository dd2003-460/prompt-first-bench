# RALPH 状态机实施计划

> origin: ai
> human intent: 先让 Prompt 动作可稳定复现，再逐层接入状态、日志、DAG 和 Hook。
> status: implementation

## 目标

分四层验证 RALPH：

```text
Prompt 动作复现 → loop-state.json 状态转换 → Hook 工具控制 → Claude Code 并行实验
```

本计划保留 `loop/1-loop/00-综述.md`、现有 `R1-D*` 详细模板和 `loop/1-loop/templates/`。不修改 `AGENTS.md`，不删除旧探索过程。

## 当前实现顺序

1. 最小 `python-statemachine` 节点机：固定顺序节点 `01`～`06`、探索任务接续、阻塞跳过和显式完成兼容。
2. 结构化 Prompt 动作协议：`advance`、`rollback`、`blocked_human`、`skip_blocked`、`candidate`、`explore`、`dispatch`、`join`、`repair_prompt`。
3. 固定 fixture 重放，验证同一状态和同一输出得到同一状态分支。
4. `loop-state.json` 持久化适配层。
5. Markdown 事件日志、DAG、候选任务、PreToolUse/Stop Hook 和真实 Claude 实验。

## Prompt 动作协议

Agent 必须输出可解析的结构化结果：

```json
{
  "action": "advance",
  "status": "passed",
  "stage_id": "02",
  "revision": "r1",
  "next_stage": "03",
  "rollback_to": null,
  "evidence": [],
  "artifact_refs": [],
  "message": ""
}
```

自然语言不要求逐字一致；状态机只接受经过协议验证的动作。

## 状态与编号

- 项目唯一运行状态：`<project-root>/loop-state.json`。
- 普通 Prompt 阶段只使用 `01`、`02`、`03` 等顺序编号。
- `r1`、`r2`、`r3` 表示同一阶段重新进入，不限制计划修订次数。
- `T1.1`、`T1.2` 表示任务图节点；`J1` 表示 Join 节点。
- 人类阻塞任务标记 `blocked_human` 后跳过，不阻塞其他任务。
- 探索是额外控制阶段：先扫描当前项目 `tasks/TASKS.md` 和 ready 队列，有可执行任务时优先接取已有任务并从 01 重新开始。
- 没有可执行任务时，探索输出 `preference_brief` 和带有 `candidate` 标记的候选任务；候选不得被静默执行，只有明确批准后才能作为新任务进入 01。
- `ralph task-next <project>` 是只读扫描命令；结构化探索动作通过校验后才会 claim 任务板，并写入 `task_intake`、`task_intake_history` 和事件日志。

## 后续层

### 事件日志

使用 `loop-events.md`。每个事件包含严格的 `RALPH_EVENT` JSON 区块、Agent 输出摘录、验证结果和 artifact 引用。隐藏思维过程不记录。

### DAG 与并行

同一并行层级必须正交、输出不冲突、可独立验证；不同层级必须声明输入、输出、前置条件、后置条件和 Join 规则。

### Hook

PreToolUse 依次判断角色权限、当前阶段策略、具体工具和路径；Stop Hook 读取 `last_assistant_message`，自动解析并 apply 合法的 `RALPH_STAGE_RESULT`，非法结果返回修复 Prompt。受控会话只允许一个 Stop 循环拥有者。

## 实验记录

每次实验记录 Prompt 版本、状态文件、原始 Agent 输出、期望动作、实际动作、状态差异和失败原因。真实项目接入前必须通过 fixture 重放、非法动作保护、状态恢复和 Shadow Hook 实验。

## 决策变更

| 日期 | 决策 | 原因 |
|---|---|---|
| 2026-07-15 | 先实现最小状态机节点和 Prompt fixture，不先铺完整 Hook/DAG | 优先验证 Agent 是否能稳定复现动作 |
| 2026-07-15 | `ralph run` 对已完成项目开启新运行时从 `01` 重置，并保留 `run_history` 摘要 | 旧项目可能是状态机接入前的跳步产物，继续把输入交给终态会造成 Hook 空转 |
| 2026-07-15 | Prompt 的 `next_stage` 必须来自节点 `on_success`，并禁止只回复 `READY` | 真实本地 Claude 实验暴露了硬编码 `03` 和非结构化终止输出 |
| 2026-07-15 | 不按字面无限拆词；按决策语义拆到“确认/追问/假设/研究”叶节点 | 既要求主动发现隐藏属性，又避免 Prompt 陷入无穷语言分析 |
| 2026-07-15 | 01/02/04 强制派发边界化审计子代理；03 只允许批准任务卡派发 | 防止 Commander 跳过澄清/DAG 直接启动 deep-research |
| 2026-07-15 | `deep-research` 只作为广覆盖候选事实发现，04 引入 claim ledger 核验 | 深搜覆盖面有价值，但其自然语言报告不能自动成为事实或最终推荐 |
| 2026-07-15 | Hook 授权使用阶段、工具、任务卡 ID、生命周期和字段契约，不用 Agent 名称或语义关键词猜测 | 关键词匹配无法可靠判断任务边界或语义正确性 |
| 2026-07-15 | 每个 01～06 阶段均须有有界上下文的独立门禁；03 在全部 DAG 节点完成后再生成 Join 门禁 | 避免主 Agent 自我确认，同时避免“完全无输入”导致无法判断输入输出关系 |
| 2026-07-15 | 每阶段生成固定 `submission-template.json`，通过时必须填写 `payload.stage_review` | 让结构化协议成为可复制填写的接口，而不是要求模型从自然语言记住字段 |
| 2026-07-15 | 任务卡只在 `SubagentStop` 收到带 `<RALPH_GATE_REVIEW>` 的合法回执后完成 | foreground Agent 的自然语言结果不能证明独立门禁通过，曾造成错误 completed |
| 2026-07-15 | 为 `blocked_human` 提供完整专用模板，最终 Prompt 不再展示精简 JSON | 本地模型会优先复制最后的短模板，导致漏掉 01 所需的 `payload.questions` |
| 2026-07-15 | `recover-card` 只能恢复没有有效 gate receipt 的错误终态 | 中断或旧 Hook 缺陷不能静默满足阶段 Guard，同时保留旧 agent ID 作为证据 |
| 2026-07-15 | 事件重放恢复会话输入和任务卡生命周期 | 仅重放阶段动作不能在中断后恢复完整当前上下文 |
| 2026-07-15 | 聚合脚本即使本身无可执行位也由 `ralph-sync.sh` 通过 Bash 调用 | `-x` 检查会静默跳过 ACTIVE 面板更新，破坏中断后的状态可见性 |

| 2026-07-16 | 06 后固定进入探索尾节点，优先扫描并接取项目 `tasks/TASKS.md` 中的 ready/pending 任务 | 让完成一个任务后可以自动接续已有任务；没有 ready 任务时才输出偏好简报和 candidate，避免流程终止或静默创造任务 |
| 2026-07-16 | oMLX 运行时错误不再进入普通字段修复循环；Stop Hook 记录 `runtime_interrupted` 并允许安全停止 | 实际日志显示 71,805-token prefill 触发 memory guard；完整恢复 Prompt 会增加原会话上下文，必须从持久化状态开短上下文恢复 |
| 2026-07-16 | 保留 oMLX tiered/SSD cache，不把 `aggressive` 作为默认修复 | 日志确认 32 个缓存 block、65,536 tokens 已成功恢复；失败点是活跃请求的 prefill 峰值和 `No idle model evicted`，不是 SSD cache 被关闭 |
| 2026-07-16 | RALPH 受控会话记录 `PreCompact`/`PostCompact`，并把当前设备的默认主动压缩目标下调到约 32k | 自定义模型可能按默认 200k 窗口计算；最新日志显示 41,472-token prefill 已超过 balanced 安全上限，64k 作为默认目标偏晚；压缩 Hook 只观察，不阻止恢复路径 |
| 2026-07-16 | 01 阶段增加“需求分流闸门”和 `inferred` disposition；只有四条件同时满足才向人类提问 | 旧提示虽然允许假设，但没有阻止模型把未单独命名的字段都变成选择题；GPU/硬件、云服务角色和模型档位应优先从输入、环境、研究或场景推导 |
| 2026-07-16 | `dispatched` 明确为内部等待状态；禁止重复派发、用 Agent/Write 生成运行时契约，并禁止 Commander 全量读取 `loop-events.md` | 真实运行中重复派发被正确拒绝后，模型尝试绕过 Write 并反复读取事件日志；这会造成工具循环和上下文/KV cache 膨胀 |
| 2026-07-16 | `recover-card` 默认不触碰 `dispatched`；只有确认旧进程退出且没有 `SubagentStop`/有效 gate receipt 时，才允许显式 `--force-dispatched` 恢复为 `pending` | 防止把仍在运行的子代理误判为 stale，同时为旧会话残留 agent_id 提供可审计的恢复路径 |
| 2026-07-16 | 新 `ralph resume` 在状态快照已列出 pending 卡时，下一次工具调用直接派发指定 Agent；不再同时要求先 Read 状态文件 | 实验显示“先 Read”与“立即 Agent”会形成提示冲突，模型会回到读取/规划循环 |
| 2026-07-16 | 用“我需要跑本地 AI，帮我调研性价比最高的 GPU”作为最小完整分解基准；同时验收语义覆盖、结构化协议和独立审计生命周期 | 简单输入仍应展开背景、目标、约束、比较维度、交付物和不确定性；不能用自然语言看起来完整替代可验证 task_spec |
| 2026-07-16 | 真实实验的第一动作闸门改为 pending auditor 时必须先派发指定 Agent | 第一次实验先调用 `deep-research`/AskUserQuestion，未形成结构化 task_spec；反馈后第二次实验成功派发 auditor，并由独立审计返回 `rollback`，证明空结构不会被误判为通过 |
| 2026-07-16 | 阶段 01 的 auditor 返回 rollback 后增加受控 `clarify` 动作；它只写回完整 task_spec、递增阶段 revision 并重新生成 auditor，不直接进入 02 | 真实 GPU 项目停在 `01-r1` 的根因是 rollback 之后没有合法的结构化写回路径，Commander 于是尝试 Write、AskUserQuestion 和重复读日志 |
| 2026-07-16 | 任务卡生命周期改为终态单向；迟到的 PostToolUse 不得把 `completed`/ `failed` 改回 `dispatched` | 真实事件中 gate 已收到合法 rollback 回执，随后 PostToolUse 又写入 dispatched，造成状态与事件矛盾和等待死锁 |
| 2026-07-16 | 新增 `ralph loop` 外层监督器；每轮 Claude 退出后从持久化状态开新上下文，并自动回收本轮残留 dispatched 卡 | Stop Hook 能保护当前进程，但无法复活 API reset、memory guard、终端关闭或无响应后已经退出的 Claude；持续性必须由外层进程承担 |
| 2026-07-16 | 同一 Claude 上下文连续 3 次阶段协议失败后释放上下文；重复 Stop Hook 也计入失败预算 | 仅看文件活动会把“持续写 rejection 事件”的格式循环误判为进展，必须交给外层监督器换新上下文 |
| 2026-07-16 | 当前阶段有必派 pending 卡时，Commander 的第一工作工具只能是指定 Agent；允许 `ralph ...` 控制命令作为诊断例外 | 实验中 Prompt 已要求立即派发，但 Hook 仍允许先 Read，导致模型重新规划和读取循环 |
| 2026-07-16 | dispatched 子代理遇到重复 Stop Hook 时保留卡状态，不解析 Commander 的旧结果；阶段输出按 `loop-artifacts/stages/<stage>/<revision>/` 归档，并提供 `ralph validate --result [--apply]` | 把进程存活、子代理生命周期、阶段结果校验和状态写回分开，避免旧消息触发假修复，同时为文件化提交提供机械校验入口 |
## 实施记录

- 已实现 `scripts/ralph_runtime/` 最小 Python 运行时。
- 已使用 `python-statemachine` 3.2.0 实现固定节点机和合法转换。
- 已实现结构化 Prompt 动作协议、Prompt 哈希、修复 Prompt 和 fixture 重放。
- 已实现 `loop-state.json` 初始化、迁移、原子写入和动作应用。
- 已实现 `loop-events.md` 事件追加、Agent 输出摘录、完整输出 artifact 和事件重放。
- 已增加一条命令启动入口：`ralph run "任务描述"` 自动从 workspace 匹配或创建项目；`ralph run <project> "任务描述"` 保留显式路径模式。
- 已支持旧版 `.claude/ralph-loop.local.md` 迁移到项目 `loop-state.json`，并让启动命令加载 `user,project,local`，保留用户本地模型配置。
- 已实现 DAG 环检测、依赖检查、并行组正交键和写入冲突检查。
- 已实现 Hook Shadow/Enforce 纯函数和项目级 settings 安装。
- 已实现 Stop Hook 自动 apply、字段/状态失败修复提示和重复输出幂等保护。
- 已实现已完成项目的新运行重开：旧完成运行摘要写入 `run_history`，新运行从阶段 `01` 开始；`ralph start` 仍保持原阶段。
- 已修正 Prompt 的动态 `next_stage`，并增加 `--effort` 选项以控制本地 Claude 的推理开销。
- 已完成独立虚拟环境部署和 42 个本地测试。
- 已完成真实本地 Claude 终端实验：PTY 交互可用，非法 `READY` 被记录并触发修复提示；随后合法 `advance(01→02)` 被 Stop Hook 自动应用，`loop-state.json` 更新为阶段 `02`，事件日志和 artifact 均生成。
- 已实现 `contracts.py`：阶段契约、规范 `task_spec`、项目内 task card 文档和指定 Agent prompt 标记。
- 已实现 01 的语义属性矩阵与一次性问题包字段校验；一个属性达到确认、追问、假设或可验证研究任务时停止继续拆分。
- 已实现 02 的 DAG/任务卡字段校验；通过后自动为 ready 节点生成 03 任务卡。
- 已实现 04 的 claim ledger 字段校验：关键事实必须带来源、来源类型、复核者和核验状态。
- 已实现 PreToolUse 拒绝裸 Agent、PostToolUse/SubagentStop 更新子代理卡生命周期、UserPromptSubmit 将人类补充写回规范任务输入。
- 新受控会话默认使用 `enforce`；可显式使用 `--mode shadow` 做诊断。
- 已新增阶段契约回归测试；运行时测试总数为 49。
- 已将阶段门禁扩展到 `01`～`06`：审计代理只获得 `stage-input-package.json`、阶段契约与提交模板；主对话与隐藏推理不进入其上下文。
- 已新增 `submission-template.json`，并要求每个 advance 填写独立 `stage_review`；03 的全部 DAG 节点完成后会自动生成 `execution-join-auditor`。
- 已将运行时回归测试扩展至 52 项。
- 已接入 `SubagentStart`：批准任务卡在子代理启动时绑定 `agent_id` 并注入边界；已绑定 worker 的工具调用按任务卡白名单和可读文件再次拦截。
- 已改为只有 `SubagentStop` 的合法 `<RALPH_GATE_REVIEW>` 回执才能完成阶段门禁；无标记、缺字段或不合格回执保持 `dispatched` 并返回修复提示。
- 已新增 `ralph recover-card <project> <card-id> --reason ...`，用于恢复没有有效门禁回执却被错误标为 `completed`/`failed` 的卡；已在金融项目的旧错误终态上实际使用。
- 已将完整 `submission-template.json` 与 `blocked_human` 专用 JSON 模板同时放入最终 Prompt，防止模型只复制省略 `payload` 的短结构。
- 已扩展事件重放：会话任务、人类补充、任务卡派发、绑定、完成、失败和恢复都会重建；已用金融项目真实日志对比当前阶段、任务输入、卡状态、旧 agent ID 与恢复次数，结果一致。
- 已修复 `ralph-sync.sh` 对非可执行 `aggregate-active.sh` 的错误 `-x` 判断；ACTIVE 面板现已显示金融、人格提取和 LaTex 项目。
- 已完成金融项目真实 Claude Code Hook 试验：旧子代理未返回门禁 JSON，控制器发现并安全回退；后续 9B 与 3B 本地模型在 Claude Code 工具上下文中长时间未开始新的工具调用，因此主动中断，不把无响应误当作阶段完成。三个项目均保持 `01-r1`、门禁卡 `pending`。
- 当前运行时回归测试共 63 项，全部通过；Python 模块编译、任务板扫描和探索接续 Smoke Test 均通过。
- 已加入 Markdown 任务板接续：金融任务 F1-F5、LaTeX 任务 L1-L4；`ralph task-next .` 只读选择最高优先级且依赖满足的任务，结构化探索通过后才 claim。
- 已将 Stop Hook 的正常继续和协议修复改为有界短恢复 Prompt；完整阶段 Prompt 不再在 Stop 响应中重复注入。
- 已识别 API/连接/超时/oMLX prefill memory guard/OOM，事件只保存有限错误摘要；状态不推进、不回滚，允许会话安全退出。
- 已新增 `ralph resume <project>`：不使用 Claude `--continue`，从 `loop-state.json` 开启新上下文，避免重复提交超大 transcript。
- 已加入运行时中断、短恢复 Prompt 和 Stop Hook 回归测试；当前运行时回归测试共 77 项，全部通过；模块编译和 CLI `resume` 帮助检查通过。
- 已为 `ralph run`、`ralph start --launch` 和 `ralph resume` 注入项目级自动压缩预算：当前默认 `40000 × 80% ≈ 32000` token，可通过 CLI 或 `RALPH_*` 环境变量调整，不修改全局 Claude 配置；有足够内存时可显式调回约 64k。
- 已安装项目级 `PreCompact`/`PostCompact` Hook；它们把压缩开始、完成、触发类型和有限摘要写入 `loop-events.md`，并保持压缩永不被 RALPH 阻塞。
- 已更新 01 阶段 Prompt、requirements-auditor 任务卡和协议：支持 `inferred`，并要求按证据优先级、影响程度和场景覆盖能力筛选问题，避免把可推断信息重复问给人类。
- 已加入有界事件诊断：`ralph events <project> --tail N` 只返回有限摘要；Commander 全量 Read `loop-events.md` 会被 enforce Hook 拒绝；PostToolUse 工具响应在写入日志前截断。
- 已把任务卡生命周期和运行时物化边界写入阶段 Prompt、项目模板和阶段契约：`dispatched` 只能等待 `SubagentStop`，不能伪装成 `blocked_human` 或通过 Agent 绕过 Write 限制。
- 已实现 stale `dispatched` 卡的显式 `--force-dispatched` 恢复保护；真实 GPU 项目已确认旧进程退出、无有效 gate receipt 后恢复为 `pending`，并用新上下文成功重新派发 auditor。
- 已将新上下文的 pending-card 首动作、Commander Bash 拒绝提示和只读 Worker gate 输出做成明确反馈；真实本地实验已验证 `pending → Agent allow → dispatched`、Stop 等待和 Worker 工具边界。
- 已修复 Stop Hook 的终态分支：`blocked_human` 自动 apply 后允许当前会话结束，不再返回 `decision=block` 触发无意义的 ToolSearch/事件读取循环；新增回归测试覆盖该行为。
- GPU 项目真实实验已完成 `requirements-auditor` 门禁：合法 `blocked_human` 结果被 Stop Hook 自动写入 `loop-state.json`，问题包进入 `queue.blocked_human`；实验暴露了旧逻辑的 `stop_intercepted_after_apply`/后续工具尝试，现已改为 `stop_allowed_after_apply`，并由回归测试锁定。
- 已根据真实错误增加统一 `RALPH_FEEDBACK[错误码]`：覆盖事件日志循环、重复派发、任务卡生命周期、Commander 越权写入、AskUserQuestion、Worker 范围、门禁回执、阶段协议、Stop 无动作和 oMLX/连接中断；每条反馈都包含检测、修正、唯一下一步和禁止事项。
- 协议修复提示现在保留原输出中可识别的 action；有 pending/dispatched 卡时优先反馈派发/等待，不再展示会诱导模型提前推进的 `blocked_human` 或 `advance` 模板。
- 当前运行时回归测试共 90 项，全部通过；Python 模块编译和 `git diff --check` 均通过。
- 新增简单任务分解 benchmark：用“我需要跑本地 AI，帮我调研性价比最高的 GPU”检查七个语义角色、attribute_matrix 叶节点、隐藏属性、处置方式、场景、成功标准和问题闸门；真实项目模式还必须核对 `requirements-auditor` 的 completed 独立门禁生命周期。
- `ralph benchmark-decomposition` 只读评估项目状态或保存的 action/task-spec JSON；它与状态机分工明确，协议负责字段合法性，benchmark 负责语义完整性，Hook/门禁负责实际派发是否发生。
- 简单任务基准的固定 fixture 已通过（score=1.0），运行时回归测试 90 项全部通过。
- 已实现 stage-01 rollback→clarify→新 revision auditor 链路；clarify 会把 task_spec 标记为 `structured_pending_audit`，不会绕过独立门禁。
- 已实现终态任务卡单向保护、gate receipt 驱动的 stale-card reconciliation、`subagent_card_reconciled` 事件以及监督循环的启动/结束事件。
- 已实现 `ralph loop`：新项目输入一次任务即可自动创建/匹配项目；旧会话退出后使用新 Claude 上下文继续，默认自动跳过 `blocked_human`，`--wait-human` 可改为等待。
- `ralph loop` 默认启用 1800 秒无事件/状态活动看门狗；超时只终止卡住的 Claude 上下文，不删除状态，并在下一轮使用新上下文恢复。
- 本轮新增回归覆盖 clarify 状态转换、迟到 Hook 不回退、有效 gate receipt 回收和 supervisor cycle；运行时测试共 95 项，全部通过。
- 已增加同上下文协议修复预算、pending 卡首动作强制、重复 Stop 等待保护，以及阶段范围结果工件和 `ralph validate <project> --result <artifact> [--apply]`；新增回归后测试继续全部通过。

### 2026-07-25 增量字段协议与真实会话修正

- 当前活动协议改为 field-centric；旧 task card/auditor 不再进入 Prompt、Hook 决策或活动生命周期。历史卡片代码和文件仅为迁移/审计兼容，不得重新激活旧流程。
- `field-init`、`field-apply`、`apply`、`ralph resume` 等命令现在由 PreToolUse/Stop Hook 按当前阶段持续提示；Agent 不需要记忆命令。普通空字段、部分填写和 JSON 语法错误都采用增量修复，不回滚整个阶段。
- `research_required` 每个 concept 生成一个 `field_task`；Agent prompt 必须带 `RALPH_FIELD_TASK=<task.json>`。PreToolUse 标记 `dispatching`，PostToolUse/SubagentStart 绑定 Agent，SubagentStop 完成或恢复 `ready`。
- 有活动字段 Agent 时，`enforce` Stop Hook 才阻止父 Commander 结束；`hybrid` 只记录软提示并交给 supervisor 恢复，避免本地模型陷入 StopHook/Read 循环。若父上下文因 API/OOM 真的死亡，下一轮 supervisor 才会把残留任务恢复为 `ready`。
- 修复了本地模型把 `.json` 任务文件误写成 `.js` 的错误：Hook 给出 canonical JSON 路径和唯一下一步，不创建副本。
- `role: task_graph` 字段现在由 `field-apply` 调用 `validate_plan(strict=True)` 校验；校验失败不写状态。通过后为每个 DAG node 生成 `graph_task` 文件，保留依赖、并行组、正交键、输入/输出、前后置条件和写入范围。
- 并发字段合并使用项目级锁；默认最多 2 个本地字段 Agent，只是资源限制，不改变 DAG 的逻辑并行关系。
- 删除全局 `~/.claude/settings.json` 中历史 `claude-code-monitor` 的全套 Hook，受控 RALPH 项目只保留项目级 RALPH Hook，避免重复 Stop/PreToolUse 控制器。
- 当前新增/修改代码通过 `test_field_workflow.py` 的 15 项针对性测试和 Python compileall；历史 card-centric 测试不再作为当前 field workflow 的验收标准。

### 2026-07-25 Hook 命令提示与上下文退出恢复

- 当前活动状态不再创建或恢复 `subagent_cards`；旧卡片只作为历史迁移/审计代码，不进入字段运行路径，也不再生成旧任务卡目录。
- PreToolUse 对 Commander 的每种工具调用都注入统一命令提示：`field-init`、增量 `field-apply`、`render`、有限 `events` 和 `apply`，并明确禁止直接修改 `loop-state.json`。
- PostToolUse 发现 Bash/Write/Edit 失败时，直接返回短修复提示：只修复错误列出的 JSON/字段，保留已通过字段，再重试同一个 `field-apply`。
- 字段草稿允许多轮填写；同一 `concept` 增量合并，已通过字段不会被空草稿覆盖。字段任务文件是 Agent 的唯一工作面，状态文件只能由 runtime 原子更新。
- Stop Hook 继续保护活动字段 Agent；若 Claude 因 Stop Hook 次数上限、API/OOM 退出而没有 `SubagentStop`，外层 supervisor 在每个 cycle 结束后把残留 `dispatching/dispatched` 字段恢复为 `ready`，下一轮短上下文继续。
- 本轮验证：活动字段工作流测试 `24 passed`，Python 模块编译通过；历史卡片测试不再作为当前验收入口。

### 2026-07-25 真实并行会话修正（第二批）

- 外部搜索失败熔断现在识别 HTTP 错误、403、无响应、`searchCount=0`、空结果以及只返回 `<tool_call>`/占位文本的伪成功包；连续两次后禁止继续 WebSearch/WebFetch，要求字段 Agent 将 `research_required`、空 `evidence_refs` 和待补原因增量写回并运行 `field-apply`。
- 字段任务的生命周期元数据以 `loop-state.json` 为准；任务文件只保存可编辑的 `field` 草稿，物化过程不会再用旧 `ready` 覆盖当前 `dispatched`。
- 并行字段派发增加项目级文件锁和按任务 ID 的原子预约，避免两个并发 PreToolUse 写回旧快照导致丢失预约。
- SubagentStart 保存并使用 Agent 名称/`agent_type` 做身份绑定；启动顺序相反时仍绑定到正确 concept，不再按到达顺序误配字段。
- 真实会话已验证两个并行字段分别绑定到“最大模型规模”和“token 生成速度”；定向回归测试现为 `29 passed`，compileall 通过。
- 连续失败熔断在成功的网页响应后会归零；当前定向回归测试现为 `30 passed`，compileall 通过。

### 2026-07-25 增量提示和重复工具动作收敛（第三批）

- Commander 的 Hook 提示现在只展示当前批次的 ready 字段（默认最多 2 个）和正在运行字段，不再把全部动态任务文件塞进主上下文；下一批由下一轮状态重新渲染。字段数量仍由当前 `attribute_matrix` 动态决定，不写死为六个。
- Commander 和 Worker 的每次 PreToolUse 都会注入当前可用命令：`status`、有限 `events`、`field-init`、增量 `field-apply`、`validate`、`render`、`apply` 和 `resume`。Worker 提示只指向自己的 task JSON，避免把状态文件当作可编辑草稿。
- `field-apply` 继续作为唯一增量写入口：JSON 语法错误、字段缺失、DAG 错误只拒绝本次提交并返回修复项；已通过 concept 不会被空草稿覆盖，成功提交会留下 apply receipt，允许字段 Agent 在不完整时释放并让下一批继续。
- `FIELD_DISPATCH_FIRST` 在 hybrid 模式第一次是软提醒；同一 supervisor cycle 内重复两次后升级为 `FIELD_DISPATCH_FIRST_ESCALATED` 硬拒绝，防止本地模型反复 Read/规划而不派字段 Agent。状态保护、危险副作用、越界路径和活动人类阻塞始终硬拒绝。
- 默认单字段网页工具最多尝试 3 次；连续 2 次失败进入字段级熔断，成功结果会清零计数。失败不伪造证据，只要求字段 Agent 把待补原因增量写回并运行 `field-apply`。
- 本批修改后的新字段工作流测试仍全部通过（`test_field_workflow.py`），模块编译通过；历史 card-centric 测试与旧卡片文件不属于当前活动协议。
- 字段流程外的 Commander 协调工具（例如 `SendMessage`）在 hybrid 中按 `TOOL_STAGE_SCOPE_FIELD` 硬拒绝；当前增量字段回归测试为 `33 passed`，避免“已派发后再发错误消息接口”造成假性停滞。
- `SubagentStart` 的候选选择和 agent identity 写入现在在同一项目锁内完成；并发到达时不会再把两个字段代理绑定到同一 concept。`PostToolUse:Agent` 只保留 parent/child 别名，不抢占正式 primary binding。
- 不完整但已经 `field-apply` 的字段不再标记为终态 `completed`，而是进入 `deferred`；当前上下文结束后由 supervisor 自动恢复为 `ready`，保证外部证据暂时不可用时既不立即循环，也不丢失后续重试机会。
- 修复了 Claude Code 并行 `SubagentStart` 身份与实际子代理 prompt 可能交换的问题：worker 第一次访问的 task JSON 路径是最终身份事实，Hook 会原子重绑 `agent_id` 到该字段；相对路径始终先按项目根解析，避免跨项目 cwd 触发 Hook 崩溃。
- Commander 直接读取当前字段 task JSON 现在会被 Hook 拒绝并提示派发 Agent；如果模型收到派发反馈后仍无活动字段 Agent，supervisor 默认 90 秒触发专项恢复，保存状态并启动新上下文。可用 `RALPH_FIELD_DISPATCH_STALL_SECONDS` 调整或设为 `0` 禁用。
- 当前 field-centric 定向回归测试为 `35 passed`（新增任务路径身份修复、Commander 任务文件读取门禁与增量提示回归），模块编译通过；历史 card-centric 测试保留为迁移审计样例，不作为当前活动协议验收入口。
- 现场恢复实验已验证：模型连续两轮“先读任务文件/不派 Agent”时，Hook 拒绝越权读取，专项 supervisor 看门狗触发新上下文；第三轮按提示启动两个字段 Agent，两个 task JSON 首次读取路径与字段身份一致，当前状态均为 `dispatched`。
- 外部搜索失败后的字段 Agent 也增加独立恢复边界：达到字段熔断且长期没有 `field-apply` 时，supervisor 保存任务文件并在新上下文重开，不把网络/本地模型无响应误判为阶段完成。
### 2026-07-25：字段子代理无提交进度时的恢复

现场实验发现：两个字段 Agent 能正确读取各自任务文件，但本地 Claude 在网页工具前长时间思考时，主 Claude 的 Stop Hook 会一直等待 `SubagentStop`。原先的 supervisor 只在网页失败熔断后恢复，因此这种“没有失败事件、也没有 field-apply”的情况仍可能空转。

现在 `RALPH_FIELD_AGENT_STALL_SECONDS` 同时检查：字段仍为 `dispatching/dispatched`、`apply_count` 没有增加、任务的 `updated_at` 超过窗口，或网页失败熔断已达到阈值。恢复只终止当前 Claude 上下文，保留字段任务和草稿；下一 supervisor cycle 通过 `reopen_stale_field_tasks` 重开为 `ready`，再由新上下文继续派发。默认窗口为 300 秒，现场可用环境变量缩短测试或放大以容纳弱设备的长思考。

### 2026-07-25：required output 门禁与 DAG 节点增量提交

字段 gate 现在同时检查当前节点的 `required_outputs`，不会因为 attribute matrix 的叶字段都已填写就跳过 `research_findings`、`cross_validation`、`task_graph` 或 `coverage_proof`。缺口以软提示返回，仍可多轮增量填写；状态推进命令只有在缺口清零后才通过。

执行 DAG 增加 `ralph graph-apply PROJECT NODE_FILE`：子代理只修改自己的 `graph_task` JSON，runtime 校验 JSON、节点存在、依赖已完成以及 output/evidence 非空，随后原子更新 `plan.completed`，重新计算 ready/blocked/Join。并行节点可以独立提交，Join 只有所有依赖完成后开放；禁止直接改 `plan` 或 `loop-state.json`。

本轮字段工作流定向测试为 `40 passed`，compileall 和 `git diff --check` 通过。

当前活动验收入口为 `test_field_workflow.py`、`test_dag.py` 和 `test_decomposition_benchmark.py`；合计 `51 passed`。完整测试目录中仍有历史 card-centric 用例，它们主动访问旧 `subagent_cards`、旧 02→03 节点顺序和旧 prompt 文本，因此会失败；这属于旧协议测试未迁移，不是当前运行时重新启用旧卡片。它们保留作迁移审计证据，不作为 field-centric 发布门禁。

现场 GPU 项目还暴露了一个独立限制：本地 Claude 的网页工具在多个字段上未产生可用结果，runtime 已按设计保留 `research_required`、不伪造 evidence，并通过字段 watchdog 重开上下文。这个现场实验不能证明真实网页研究已完成；它证明的是“不响应也不会永久卡死或误推进”。

### 2026-07-25：Hook 命令提示、增量提交和自动 worker 修正

- PreToolUse 现在对 Commander/Worker 持续提示 `field-init`、`field-apply`、`graph-apply`、`validate`、`render`、`status`、有限 `events`、`apply` 和 `resume`；提示明确说明同一文件可多轮填写、只修复错误列出的字段、保留已有通过字段。
- `field-apply` 是唯一字段增量写入口，`graph-apply` 是唯一 DAG 节点完成入口，`apply` 是唯一阶段状态转换入口；语法错误、缺字段和依赖错误只拒绝本次提交，不回滚已保存内容。
- 活动运行时不再回退到旧 task-card/auditor 协议；无字段绑定的 SubagentStart/Stop 只记事件，不会凭自然语言完成旧卡。历史卡片文件和迁移代码不属于活动状态。
- hybrid StopHook 对残留 `dispatching/dispatched` 字段只做软提示并交给 supervisor 恢复；只有 `enforce` 才硬阻塞。这样本地模型不会因为没有 SubagentStop 而陷入 StopHook/Read 循环。
- 新增可选 `RALPH_AUTO_FIELD_WORKERS=1`：Commander 不派 Agent 时，supervisor 可直接启动有界的独立字段 worker。worker 使用 `RALPH_AGENT_ID`、相同 Hook 和任务文件，启动失败自动释放预约；字段无进度时允许父 Commander 换短上下文，但不会重复 claim 活动 worker。
- 定向字段/DAG/benchmark 验收共 52 项通过；模块编译通过。完整旧 card-centric 测试不再是当前发布门禁。

### 2026-07-25：自动 worker 独立超时与有限工具预算

- 自动字段 worker 增加独立生命周期超时（`RALPH_AUTO_FIELD_WORKER_TIMEOUT`，默认 1800 秒）；超时会终止 worker、清除 agent 绑定、恢复 `ready` 并记录事件，不会留下永久 `dispatched` 槽位。
- 自动 worker 提示明确要求：读取自己的字段后立即增量填写，网页最多尝试两次；没有有效结果时提交 `research_required + evidence_refs=[] + rationale`，不得只返回自然语言。
- 现场新会话已确认新提示和动态 task identity 注入成功；当前两个字段 worker 正在运行，尚未产生 `field-apply`，因此研究阶段仍未被误判为完成。

### 2026-07-25：worker 超时回收移入监督心跳

- 现场事件显示：网页工具返回只含 `<tool_call>` 的伪失败包后，字段 worker 可能继续占用本地模型上下文；旧实现只在 Commander 轮次边界回收，存在等待边界过长的问题。
- `_run_claude_supervised` 现在每个监督心跳调用 `_reap_auto_field_workers`。worker 超过 `RALPH_AUTO_FIELD_WORKER_TIMEOUT` 后立即终止、清除绑定、恢复 `ready` 并保留草稿；Commander 可继续由新上下文处理，不会永久卡在 `dispatched`。
- 现场确认：worker 超时事件已写入 `loop-events.md`，字段没有伪造 evidence，状态仍为 `research_required/ready`，说明恢复路径生效但网页研究本身尚未完成。
- 定向字段/DAG/benchmark 验收仍为 52 项通过；compileall 和 `git diff --check` 通过。
- 又清理了活动路径中的旧卡片残留：field-centric `ralph loop` 启动和轮次结束不再调用 legacy card reconciliation；Hook 也不再从旧 `subagent_cards` 绑定 Commander/Worker。旧实现只留在迁移/审计函数中，不会影响当前队列。

### 2026-07-25：deferred 字段公平调度

- 真实 GPU 会话暴露了队列饥饿：一个网页证据暂不可用的字段进入 `deferred` 后，下一 supervisor 曾一次性重开所有 deferred，自动 worker 可能反复抢回同一字段。
- 现在只要还有 `ready/pending` 字段，deferred 不重开；ready 队列耗尽后才重开最旧的一个 deferred。这样不会跳过未完成字段，也不会让单个外部失败字段阻塞其他正交因素。
- 定向 field/DAG/benchmark 验收现为 53 项通过；compileall 和 `git diff --check` 通过。

### 2026-07-25：stage-01 自动字段与拒绝反馈验收

- 为 stage 01 缺失的 `goal/known/unknown` required outputs 自动物化独立 pending field task；不依赖 Commander 一次性写大 JSON。
- 真实隔离 smoke 会话验证了：重复 Bash 越权会触发 idle watchdog 换上下文；自动 worker 能进入单字段任务；运行时占位字段不会被 `field-apply` 当作真实进度，超时后回到 `ready` 并记录 `auto_field_draft_apply_failed_on_timeout`。
- 真实 smoke 还验证了新项目首次启动的 Claude 目录信任确认是外部前置交互，不是 RALPH 状态机阻塞；确认后才进入 Claude 会话。
- 自动字段 worker 默认使用 `low effort`（可由 `RALPH_AUTO_FIELD_EFFORT` 覆盖），任务元数据显式包含 `role/attribute`，减少字段为空导致的误操作。
- 定向 field/DAG/benchmark 验收现为 55 项通过；compileall 和 `git diff --check` 通过。

### 2026-07-25：移除不可达旧策略并收紧诊断输出

- 删除 `stage_policy.py` 中永远不可达的旧 task-card/auditor 分支；字段中心策略成为唯一工具决策路径，避免残留卡片文件重新影响 Hook 提示。
- 删除 `SubagentStop` 中永远不可达的旧卡片完成/门禁回执分支；无字段绑定的生命周期事件只记录，不改变状态。
- `ralph status` 默认改为有限摘要，只显示阶段、字段/DAG 计数和当前 artifact；完整状态必须显式使用 `ralph status <project> --full`，防止状态诊断再次撑大模型上下文。
- 状态加载增加 artifact 与最近结构化结果的富集合并：阶段 artifact 只剩种子字段时，不会覆盖 `last_result` 中更完整的分解；新增回归测试验证这一恢复路径。
- 当前定向验收为 `58 passed`（field workflow、DAG、分解 benchmark、status/supervisor 兼容测试），compileall 和 `git diff --check` 通过。
- 真实会话进一步发现：字段已恢复为 `ready` 时，旧 Claude worker 进程可能仍存活。supervisor 现在按持久化生命周期回收这类 orphan worker，并记录 `auto_field_worker_orphan_reaped`，避免资源泄漏和重复派发假象；新增测试已通过。
- 为满足“一条命令持续运行”，自动字段 worker 改为默认启用；它仍受 `RALPH_MAX_PARALLEL_FIELDS`、字段级工具预算和 `RALPH_AUTO_FIELD_WORKER_TIMEOUT=1800` 约束。纯 Commander 实验可显式设置 `RALPH_AUTO_FIELD_WORKERS=0`。

### 2026-07-25：缺少字段标记时的混合模式自绑定

- 真实会话发现，本地 Claude 有时会把 Agent 描述传给工具，却丢失 prompt 第一行的 `RALPH_FIELD_TASK`。若一律硬拒绝，字段队列本身没有问题，主 Agent 却可能因格式遗漏停在原地。
- hybrid 模式现在从当前 `ready/pending` 队列自动绑定一个字段并继续；仍然一 Agent 一字段，子代理仍必须写自己的任务 JSON 并运行 `ralph field-apply`。enforce 模式继续要求显式 `RALPH_FIELD_TASK`，用于严格验收。
- 新增回归测试确认自动绑定不会扩大任务范围；本轮定向验收为 60 项通过。该修复解决的是派发格式鲁棒性，不代表外部网页工具一定可用。

### 2026-07-25：低内存设备避免首轮双 Claude 并发

- 现场观察到自动字段 worker 与 Commander 在首轮同时启动，会让本地 MLX 同时保留两个上下文；这会把模型/ KV cache 的资源问题误表现成状态机停滞。
- 现在首轮只启动 Commander；只有 Commander 上下文结束且 ready 字段仍未派发时，下一轮才启动有界自动 worker。字段队列、Hook 和 `field-apply` 规则不变。
- 新增回归测试验证首轮不调用 fallback、第二轮才允许调用；本轮 field/DAG/benchmark/node/supervisor 定向测试为 62 项通过。

### 2026-07-25：监督器重启时回收嵌套 Claude

- 真实 watchdog 实验发现：父 Commander 被 idle recovery 终止后，旧 nested Claude 仍存活，造成字段长期保持 `dispatched` 的幽灵任务。
- `_run_claude_supervised` 现在为每个 Commander 建立独立进程组；watchdog 先终止整个进程组，再进入下一轮。重启现场已确认旧 nested Claude 消失，字段从 `dispatched` 恢复为 `ready`，新上下文重新获得完整队列。

### 2026-07-25：首次无动作也进入派发看门狗

- 现场还发现，Commander 可能在收到阶段提示后长时间思考，却没有产生任何工具反馈；旧逻辑只有在先犯一次派发错误后才启动 90 秒 watchdog。
- 现在只要当前 supervisor cycle 有 ready/pending 字段且没有 active 字段 Agent，就开始计时；超时后由进程组恢复和 fallback worker 接管。已有子代理或正在进行的窄研究不会被这个看门狗打断。

### 2026-07-25：自动 worker 心跳回收与完整链路现场验收

- 真实 GPU 项目现场确认了 `supervisor_field_dispatch_stall_recovery`、`field_tasks_reopened_after_cycle`、`auto_field_worker_started` 和 `auto_field_worker_stall_reaped`：本地网页工具失败或模型停在 Read 后，字段不会永久保持 `dispatched`。
- 修复自动 worker 与父 Commander 生命周期脱节的问题：fallback worker 现在使用独立进程组；其自身字段心跳超过 `RALPH_FIELD_AGENT_STALL_SECONDS` 时会被回收、保留草稿并释放为 `ready`。旧版继承监督器进程组的 worker 只终止自身 PID，避免误杀 shell/监督器。
- Commander 的 `COMMANDER_BASH_SCOPE_FIELD` 反馈在存在 ready/pending 字段时明确要求“下一次工具调用必须是带 `RALPH_FIELD_TASK` 的 Agent”，减少被拒后重复 Bash。
- 在 field-centric 项目现场以受控 `field-apply` / `apply` / `graph-apply` 走通了 01 → 02 → 02.5 → 03 → 04 → 04.5 → exploration：02 动态生成 3 个独立研究字段；03 的 T1.1/T1.2 并行完成后才开放 J1；Join 完成后进入验证和探索；探索候选进入 queue，未被静默执行。
- 现场真实 Agent 的限制也被保留为事实：本地模型在两个 stage-01 字段 worker 中只读取任务文件，未完成 field-apply；该项被标为可逆 `assumed_default`，并产生下一轮 `candidate`，没有被伪造为成功。
- 旧 exploration 测试已迁移为当前 candidate 入队语义，不再依赖旧 `subagent_cards`。当前 field/DAG/benchmark/节点/候选/监督器定向验收为 65 项通过，compileall 和 `git diff --check` 通过。
- 对一个新建最小项目做了第二次真实 Agent 复测：将 pending worker 提示压缩为明确的 Read → 修改自己的 task JSON → `field-apply` 三步后，worker 仍只执行 Read，90 秒无增量回执后被回收。结论是当前本地 Claude/oMLX 会话执行工具链仍不稳定；这是 Agent/运行环境问题，不是 `field-apply` 或状态门禁问题。该复测项目保留为失败样本，状态为 01/r1、3 个字段 ready。

### 2026-07-25：旧策略断言迁移与挂起复测收尾

- 长窗口复测继续观察约 5 分钟后，字段 worker CPU 接近空闲，仍只有 Read、没有 `field-apply`；确认“继续等待”不会增加证据。手动停止测试 supervisor 后通过 runtime 的 stale-field 恢复函数将该样例重新置为 3 个 `ready` 字段，避免留下幽灵 `dispatched` 状态。
- 将仍要求 `RALPH_TASK_CARD`、auditor 和旧派发顺序的 `stage_policy` 测试迁移为字段协议断言：普通文件可增量编辑，`loop-state.json` 仍硬保护；ready research field 必须提示 `RALPH_FIELD_TASK`；错误命令必须改用 `field-apply` / `graph-apply` / `apply`。
- 清理 Hook 可见的旧任务卡措辞：完整事件日志只允许有限 `ralph events --tail`，阶段文档读取提示改为当前字段 Agent，修复提示不再把中途自然语言称为旧协议错误。
- 当前字段/DAG/benchmark/node/candidate/stage-policy 定向验收为 `66 passed`；compileall 和 `git diff --check` 通过。完整历史 card-centric 测试仍保留用于迁移审计，不属于活动 field-centric 发布门禁。

### 2026-07-25：长思考窗口、Read 无进展门禁与恢复任务保护

- 本地 Qwen 现场确认：默认字段派发看门狗过短时，Commander 在真正发出 Agent 前就被 supervisor 终止。`RALPH_FIELD_DISPATCH_STALL_SECONDS` 默认调整为 600 秒，已派发字段无进展窗口 `RALPH_FIELD_AGENT_STALL_SECONDS` 默认调整为 900 秒；两者仍可由实验环境覆盖。
- Worker 的 Hook 现在记录 `field_read_count`。同一字段前 3 次 Read 仍允许并持续注入“下一步必须 Write/Edit → field-apply”的增量提示，第 4 次重复 Read 才硬拒绝并给出 `FIELD_READ_LIMIT`，避免弱模型因过早硬拒绝直接结束子代理，也避免无限读循环。
- 真实现场出现了可验证的 `field_increment_applied`：stage-01 的真实字段 Agent 把 `goal` 写入 task JSON 并通过 `ralph field-apply` 合并，事件记录了 remaining.required_outputs=`known,unknown`。这证明字段文件→校验→原子合并链路实际可用；后续 `known/unknown` 现场仍可能因本地 Agent 停在 Read 而未提交，不能把它们伪造为完成。
- 修复恢复命令的状态保护：对一个仍在运行的项目重复传入稍有不同的任务文字，不再调用会重建 `task_spec` 的 `set_task`，而是保留当前 stage/字段并追加 authoritative input；只有已完成项目才通过 `start_new_task` 创建新 run。这样中断恢复不会抹掉已通过字段。
- 真实实验中发现旧 supervisor 子进程会在父进程结束后独立存活；本轮通过独占 supervisor 锁、独立进程组和 stale/orphan 回收清理了现场遗留进程，所有被中断字段均回到 `ready`，状态文件未损坏。
- 新增/更新增量读门禁、任务描述保护测试；当前字段增量定向测试 5 项通过，模块 compileall 通过。完整历史 card-centric 测试仍不能作为当前协议门禁，原因是它们主动断言已删除的 `subagent_cards`、旧 prompt 和旧节点顺序。

### 2026-07-25：修复 pending 字段被误派 Agent 的活动路径漏洞

- 真实复测发现：虽然 Prompt 已写“只有 `research_required` 才派 Agent”，Hook 的旧分支仍把所有 `ready/pending` 字段放入自动绑定队列；因此 stage-01 的 `known/unknown` 结构字段仍可能被绑定成旧式子代理。
- Hook 现在只从 `research_required` 队列绑定 Agent；没有研究字段时，Commander 的 Agent 调用硬拒绝为 `FIELD_AGENT_NOT_NEEDED`，要求回到 `fields.json → ralph field-apply`。显式标记为 pending 的 Agent 也被拒绝，不再形成未绑定子代理或旧 auditor 回退。
- `_field_dispatch_stall_requested` 同时覆盖 pending 结构字段和 research 字段：若 Commander 长时间没有产生增量状态变化，supervisor 会按可配置窗口启动新上下文；该看门狗不创建 Agent，只恢复 Commander，因此不会复活旧协议。
- 真实会话中已观察到：旧逻辑曾触发 `FIELD_TASK_PATH_CORRECTION` / `COMMANDER_BASH_SCOPE_FIELD` 后仍停在 01；停止并清理后状态保持 `known/unknown=ready`，没有把未完成字段标为成功。新逻辑需在下一次会话中继续验证 Commander 的实际 `field-apply`。
- 真实 smoke 随后实际产生 `supervisor_field_dispatch_stall_recovery`（临时窗口 90 秒），并启动 fresh context；停止后 `known/unknown` 仍为 `ready`，没有幽灵 Agent 或伪完成。
- Hook/策略又补齐了 pending 字段的 Bash 反馈：不再错误提示“下一次必须 Agent”，而是明确 `Write/Edit fields.json → field-apply`；增加 `ralph field-status` 只读别名，降低本地模型调用不存在诊断命令的失败率。
- 本轮定向字段/策略/CLI/DAG/benchmark 测试 `86 passed`，compileall 和 `git diff --check` 通过；完整历史 card-centric 测试仍仅作迁移审计。

### 2026-07-25：增量恢复预算修正与 worker 提示压缩

- 发现一个恢复边界问题：字段 worker 的 `field_read_count` 曾随任务永久保留。旧 worker 读满 3 次后被 watchdog 重开，新 worker 可能一启动就触发 `FIELD_READ_LIMIT`，形成“恢复后仍不能读”的假死。
- `claim_field_task` 和 stale 重开现在按每次新的派发尝试将 `field_read_count`、网页失败/尝试计数清零，并把计数同步回任务 JSON；已通过字段内容和 `apply_count` 不受影响。
- pending 结构字段的自动 worker prompt 压缩为固定三步：读取自己的 task JSON → 只改当前 `field` → 执行 `ralph field-apply`。研究字段仍保留有限外部证据尝试和不可验证时的 `research_required` 降级路径。
- 新增恢复回归测试，验证 stale retry 可以重新读取；定向测试、compileall 需在本次现场复测后再次记录。

现场复测结果：使用临时 `RALPH_FIELD_DISPATCH_STALL_SECONDS=60`、`RALPH_FIELD_AGENT_STALL_SECONDS=90` 和 `RALPH_AUTO_FIELD_WORKER_TIMEOUT=180`，旧的 stage-01 `known/unknown` 字段均能重新派发；两个 worker 随后均因本地模型没有产生 `field-apply` 而被 `auto_field_worker_stall_reaped` 回收，任务回到 `ready`，进程组清理完成。该实验验证了恢复与防幽灵进程，不证明本地模型已经稳定执行三步动作；当前字段仍未推进，保持真实失败状态。定向验收现为 `87 passed`，compileall 与 `git diff --check` 通过。

同一现场还确认低内存设备不应默认并发两个本地字段 worker；实际并行能力保留在 DAG，`RALPH_MAX_PARALLEL_FIELDS` 默认降为 `1`，需要时再显式提高。

### 2026-07-25：fallback worker 与 Commander 串行化

- 进一步发现：即使首轮不并发，fallback worker 启动后旧 supervisor 仍会在同一轮立刻启动新的 Commander；这会再次形成两个本地 Claude 上下文竞争 KV cache。
- 现在 supervisor 在 `auto_field_worker_started` 后等待该 worker 完成或被 watchdog 回收，只有 worker slot 释放后才启动下一轮 Commander。worker 退出但没有 `field-apply` 时，Runtime 立即清除绑定、重置 Read 预算并恢复 `ready`。
- 真实现场验证了事件顺序：`auto_field_worker_stall_reaped` → 下一次 `supervisor_cycle_started`；worker 期间进程表只有一个 Claude 子进程。新增串行监督器回归测试；当前定向测试、compileall 和 diff 检查通过。
- 实时 Commander prompt 现在只保留当前任务、当前字段、命令和阶段方法摘要；完整阶段文档与默认画像不再每轮重复注入。现场生成的普通 prompt 约 3.5k 字符、compact recovery 约 2.6k 字符，减少本地模型首次工具调用前的 prefill 压力。
- 自动 worker 不再使用 `claude --bare`：`--bare` 会跳过 RALPH Hook，导致 worker 读完 task JSON 后得不到 PostToolUse 的增量写入提醒。现在 worker 加载项目级 `settings.ralph.json`，仍只开放 Read/Write/Edit/Bash 和自己的 task prompt；本地 endpoint/model 继续从用户环境复制。下一次真实现场需验证 Hook 是否将停在 Read 的 worker 推动到 `field-apply`。

### 2026-07-25：stage-02 动态字段恢复与 worker 工具边界复测

- 真实 stage-01 已通过绝对路径的 `ralph field-apply`，并自动进入 stage-02；但 stage-02 恢复了 stage-01 的因素矩阵后，旧判断把它误认为“已有研究字段”，导致研究队列为空。现在 materializer 会识别真正的 `research_findings/research_required` 条目；若不存在，就从 stage-01 的 `unknown` 按分隔因素动态生成独立字段任务。
- 真实复测确认 stage-02 已落盘 2 个 `research_required` 字段，Commander 没有派发时由 supervisor 启动有界 auto worker；任务生命周期按 `ready → dispatched → ready` 恢复，没有伪造完成。
- 真实 worker 曾把“外部搜索”错误实现为 Bash/curl；Hook 记录了实际命令并继续拒绝。自动 worker 现在显式开放 `WebSearch/WebFetch`，禁止 Bash/curl/python/grep 搜索，外部工具失败时保留 `research_required + evidence_refs=[] + rationale`。
- worker 只允许执行受控 `ralph field-apply` 的 Bash 命令；命令解析器改为 shlex 单命令解析，兼容绝对路径、引号、`cd`、环境变量和 `command` 前缀，但仍拒绝 shell 链接、重定向和任意文件操作。
- 同一字段第二次 Read 已改为硬反馈 `FIELD_WRITE_AFTER_READ`，hybrid 也会真正 deny；成功 WebSearch 的 PostToolUse 会立即要求 Write/Edit → field-apply，避免模型在搜索后继续循环。
- 现场仍发现本地 Qwen 在外部搜索失败后可能没有写字段；supervisor 已按字段心跳回收 worker，状态保持 `ready`。这证明恢复和安全边界有效，但尚未证明本地模型能稳定完成 stage-02 的证据提交；该限制不能被状态机伪装成成功。
- 本轮定向 field/stage-policy 测试通过，compileall 通过。当前真实项目仍在 stage-02，字段任务为 2 个 `ready`，等待可验证证据或下一轮受控 worker。

补充现场结果：成功 WebSearch 的 PostToolUse 现在会直接返回 Write/Edit → `field-apply` 指令；外部搜索失败则不允许转为 Bash/curl。手动结束实验 supervisor 后，使用同一个 runtime 的 stale-field 恢复函数将残留 `dispatched` 恢复为 `ready`，并确认没有存活的项目 supervisor/worker 进程。相关 field/stage-policy/DAG/候选测试、compileall 和本次改动范围 diff 检查均通过；历史项目事件日志的既有尾随空格未修改。

### 2026-07-25：flow-only 增量字段与真实链路复测

- `PromptRenderer` 现在在任务描述包含“不要求实际网页研究”或显式 `flow_only` 时，向 Commander 明确注入 flow-only 规则：仍必须执行“一字段一 Agent → Read → Write/Edit → field-apply”，但不调用网页工具、不伪造来源，使用 `inferred` 进行流程验证。
- `loop-state.json` 的 authoritative inputs 现在会丢弃自动生成的 RALPH 提示、去重并限制长度；现场一次保存把 17 条约 31KB 的重复输入压缩为 1 条，避免事件/提示无限回灌上下文。
- 缺失的 required output 不再只在 stage 01 物化；02.5 的 `cross_validation`、03 的 `task_graph/coverage_proof` 和后续阶段也会生成增量字段任务。真实链路已验证：02 的两个字段、02.5 的 cross_validation、03 的两个 required output 均能通过同一套 Read → Edit → 受控 field-apply。
- worker 的受控 `ralph field-apply` Bash 白名单统一适用于所有字段阶段；此前 02.5 worker 被旧策略误拒的问题已修复。回归测试：`test_field_workflow.py` + `test_stage_policy.py` 定向结果为 66 项通过，compileall 通过。
- 03 不再接受“写了一段 task_graph 描述”作为 DAG 完成。flow-only 下若没有结构化 `task_graph.nodes`，字段会重新开放为 pending；专用 worker 提示要求生成两个正交并行节点 `T1.1/T1.2`（`G1`、不同 `orthogonal_key`、不同 `writes`）和 Join `J1`。
- 真实项目 `/Users/a1-6/Desktop/workspace/projects/D1-ralph-real-chain` 已产生并通过 DAG 校验：`T1.1`、`T1.2` 为 G1 并行 ready，`J1` 依赖两者并被正确标记 blocked；03 因结构化 DAG 已存在才推进到 04。停止现场 supervisor 后，`verification_report` 字段已由 runtime 恢复为 ready，没有留下存活的该项目进程。
- 本次现场仍是 flow-only：`inferred` 只证明流程和字段门禁，不证明 GPU 事实、网页证据或 DAG 节点业务执行结果。真实研究模式仍要求 `research_required + evidence_refs`，不能沿用 flow-only 的自动推进。

### 2026-07-25：命令准入与真正的增量提交修复

- 现场复测确认了一个活动路径漏洞：当存在 `research_required` 字段时，旧 Hook 会把 Commander 的所有非 Agent 工具都挡住，连 `field-init`、`field-apply`、`graph-apply` 和 `apply` 也会被拒绝。这会直接造成“字段可以多次填写，但提交命令永远到不了”的假死。
- 现在受控 `ralph` 命令在字段派发提示之前统一放行；Commander 仍不能直接写 `loop-state.json`，但可以增量写当前阶段 `fields.json`/`advance.json`，再交给 runtime 校验、合并和原子保存。普通 Bash、越界写入和状态文件修改仍硬拒绝。
- `field-apply` 不再拒绝运行时生成的空 `pending` 占位。它只校验本次实际提交的结构；未完成字段通过 `remaining.pending/researching/required_outputs` 返回，阶段门禁仍阻止提前 `apply`。JSON 语法错误只拒绝本次提交并给出行列与同一重试命令，`loop-state.json` 保持不变。
- Hook 的每次工具提示现在明确列出 `field-init`、`field-apply`、`graph-apply`、`apply`、`task-next`、`status`、`events`、`validate`、`render` 和 `resume`；增量修复规则明确为“只修复错误列出的字段，保留已通过字段”。
- 自动 worker 启动后把 PID 写入字段生命周期。新 supervisor 启动时会回收上一 supervisor 遗留的持久化 worker，再恢复字段为 `ready`，避免旧 Claude 进程继续占用 MLX/KV cache 或形成重复派发幽灵。
- 定向 `test_stage_policy.py` + `test_field_workflow.py` 通过；compileall 通过。真实复测中 `preference_brief` 已产生真实 `field_increment_applied`，而 `candidate_tasks` worker 仍出现“Read 后不 Write/field-apply”的模型侧停滞；该失败被保留为可恢复状态，不能伪造为探索完成。
## 2026-07-25：探索尾节点与命令提示最终修复

本轮把“候选任务”和“选中任务”明确分开：

- `candidate` 动作只把候选写入 `state.queue.candidates`，保留 `status=candidate`，同时保存 `preference_brief`；它不会启动 01，也不会静默执行。
- `advance` 的 `payload.exploration.selected_task` 只接受 `selection_mode=task_board` 的 ready/pending 任务；未获批准的 candidate 会被 runtime 拒绝，避免候选误执行。
- 探索阶段仍是尾节点而非终止；没有 ready 任务时返回偏好和候选，下一轮由主 Agent 分析后再分解；有人类阻塞的任务直接跳过。

Hook 与实时 Prompt 现在每次都提示：

```text
field-init → Write/Edit 当前阶段 fields.json → field-apply
graph task JSON → graph-apply
所有字段/节点通过 → advance.json → apply
上下文中断 → resume
```

普通字段缺失是软提示：可以保存空的 `pending` 占位并多轮增量修改；`field-apply` 只合并当前 `concept`，不会覆盖其他已通过字段。JSON 语法错误、字段格式错误、DAG 依赖/环/正交性/写冲突错误都会在本次命令中拒绝且不改变状态，并返回修复位置。只有阶段推进才执行完整门禁。

本轮验证证据：

- 实际 Claude/Qwen 链已走过 `01 → 02 → 02.5 → 03 → 04 → 04.5 → exploration`；其中 02 动态生成字段，03 生成两个正交并行节点 `T1.1/T1.2` 与 Join `J1`。
- 通过真实 `ralph graph-apply` 依次完成 `T1.1`、`T1.2`、`J1`；Join 在两个依赖完成后才变为 completed。
- 探索字段通过增量 `field-apply` 完成；实际提交 `candidate` 动作后，事件日志记录 `candidate_created`，状态仍为 exploration，候选只存在队列。
- 一个旧格式的探索 `advance.json` 因缺少 `payload.exploration` 被拒绝；补齐后又因候选未获批准被拒绝。这两个拒绝均没有改写状态，证明门禁仍有效。
- 字段、Hook、DAG、CLI、节点、候选和分解 benchmark 回归测试全部通过；编译检查通过。

当前结论：旧 task-card/auditor 不再是活动运行协议；历史文件和兼容函数仅保留作迁移/审计，不会从旧卡恢复活动任务或阻止字段流程。当前默认协议是“字段增量 + runtime 命令 + Hook 准入 + 结构化动作”。
