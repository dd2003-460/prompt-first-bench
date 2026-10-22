# RALPH Runtime

这是项目级 RALPH 运行时。新项目的默认路径是 prompt-first：阶段内容和可读状态均为 Markdown；运行时只保存阶段游标，并由同一 Claude TUI 的 Stop Hook 在完成标记后提示下一阶段。

```text
一个命令 + 一个任务描述
        ↓
初始化或读取 ralph-loop.md
        ↓
01 因素分解（已有条件 / 空缺）
        ↓
02 资料与网页 AI 线索 → 02.5 交叉核验
        ↓
03 行动分解 → 04 执行核对 → 04.5 独立复核
        ↓
每阶段 Markdown 末尾 `<!-- ralph: done -->` → Stop Hook 在同一会话提示下一阶段
```

此路径没有字段 role/disposition、DAG、`field-apply`、网页熔断或工具读写拒绝；它不评判 Markdown 语义。`ralph-loop.md` 仅保存游标，完成标记才会推进。旧字段运行时保留兼容：已有 `loop-state.json` 会继续使用旧路径，新建旧项目请显式 `ralph init PROJECT --workflow field`。

## 最简单的用法

在任意项目目录执行：

```bash
ralph loop ./my-project "我需要调研性价比最高的 GPU，并给出本地 AI 使用建议"
# 也可先建 Markdown 项目，随后补任务
ralph init ./my-project
ralph loop ./my-project "我需要调研性价比最高的 GPU，并给出本地 AI 使用建议"
```

如果目录不存在，运行时会创建目录、初始化 Markdown 游标和项目级 Claude 配置；如果目录已有 `loop-state.json`，则保留旧字段兼容路径。它不会把项目路径解释成当前工作目录之外的绝对根路径，也不会直接修改业务文件。

查看 Markdown 游标与当前阶段提示：

```bash
ralph prompt-first status ./my-project
ralph prompt-first render ./my-project
# 阶段 02 中由本地 Claude 调用；复用已获人类授权的专用 Playwright profile
ralph prompt-first web-llm ./my-project "需要审阅的主张" --context "阶段 01 的相关空缺"
```

查看当前状态：

```bash
ralph status ./my-project
ralph status ./my-project --full   # 只有人工诊断时才导出完整状态
ralph events ./my-project --tail 20
ralph prompt render ./my-project
```

继续被中断的项目：

```bash
ralph resume ./my-project
```

## Agent 的增量填写方式

每个阶段有独立目录：

```text
my-project/
├── loop-state.json
├── loop-events.md
└── loop-artifacts/
    └── stages/
        └── 01/
            └── r1/
                ├── fields.json
                ├── fields.md
                └── advance.json
```

stage 01 的 `goal`、`known`、`unknown` 如果尚未出现在字段矩阵中，runtime 会自动为它们生成三个独立的 pending task；主 Agent 可以只派发一个窄字段，不必一次性构造完整大 JSON。

先创建空草稿（不会覆盖已有文件）：

```bash
ralph field-init ./my-project
```

Agent 可以多次填写同一个文件，也可以每次只填写少数字段。字段按 `concept` 合并：同名字段更新，新的字段追加，已通过字段不会因为下一次增量提交而丢失。

研究字段会自动生成 `stages/<stage>/<revision>/tasks/<task-id>.json`。子代理先把单字段结果写入该文件的 `field` 对象，再运行：

```bash
ralph field-apply ./my-project \
  loop-artifacts/stages/02/r1/tasks/<task-id>.json
```

并行组仍由 DAG 描述；本地模型默认最多同时运行 1 个字段子代理，完成一批后再派下一批。需要调整时设置 `RALPH_MAX_PARALLEL_FIELDS`，这只限制资源占用，不改变任务之间的逻辑依赖。正常 Stop 会在同一 Commander 上下文中继续；若进程实际中断，仍在运行的字段 worker 不会被重复 claim。

最小字段格式：

```json
{
  "fields": [
    {
      "concept": "工作负载",
      "role": "background",
      "attribute": "本地大语言模型推理",
      "disposition": "inferred",
      "rationale": "由用户要求本地 AI 推断，仍需在研究阶段核验",
      "evidence_refs": [],
      "confidence": 0.8,
      "impact": "material",
      "reversible": true
    }
  ]
}
```

提交增量：

```bash
ralph field-apply ./my-project \
  loop-artifacts/stages/01/r1/fields.json
```

命令会检查：JSON 语法、必填字段、`disposition` 枚举、证据数组、置信度范围、重复 `concept`。失败时只报告本次草稿的问题，不改动 `loop-state.json`；修复后重复运行即可。

允许的字段状态：

```text
confirmed          用户明确提供或有充分证据确认
inferred           可从上下文合理推断，但应记录依据
assumed_default    使用项目默认偏好，必须可追溯
research_required  需要研究，必须在后续阶段补 evidence_refs
pending            尚未完成，不阻止增量保存，但不能通过阶段门禁
```

字段不完整不是错误，也不是必须回滚。它只会返回 `remaining.pending`、`remaining.researching` 或 `remaining.splittable`，Hook 会把这些缺口作为下一轮短提示。Agent 可以反复填写同一字段；每次只修复提示列出的空项，已经通过的 concept 不会被空草稿覆盖。即使 `fields.json` 中还保留运行时生成的空 `pending` 占位，也可以先保存其他字段；只有阶段推进时才会因为 remaining 不为空而不能通过。JSON 语法错误只拒绝本次 `field-apply`，不会改变状态，错误消息会给出行列和同一重试命令。

flow-only 测试中的单字段 worker 另有一条机械保护：如果它把未修改的空 `pending` 占位直接提交，`field-apply` 会拒绝并明确要求 `Write/Edit → disposition=inferred → field-apply`；这不影响 Commander 保存其他未完成字段。

字段 worker 的 Read 预算按“派发尝试”计算，而不是按字段永久计算。worker 被 watchdog 回收或父上下文中断后，下一次重新派发会重置 `field_read_count`，因此不会出现“上一个 worker 读满 3 次，新的 worker 一启动就被拒绝”的恢复死锁。每次重新派发仍要求尽快执行 `Write/Edit → field-apply`。

如果字段代理已经成功运行 `field-apply`，但仍因外部证据不足保持 `research_required`，任务会进入 `deferred`：本轮不立即重派，避免死循环；当前 Claude 上下文结束后，supervisor 会自动把它重新开放为 `ready`，下一次短上下文继续补证。它不会被误标为永久完成，阶段门禁仍会准确阻止提前推进。

删除字段使用：

```json
{"fields": [{"concept": "临时假设", "delete": true}]}
```

## 阶段推进

字段补齐后，Agent 在当前阶段目录写入 `advance.json`，再执行：

```bash
ralph apply ./my-project \
  loop-artifacts/stages/01/r1/advance.json
```

`apply` 是状态机入口，不是普通文件复制命令。它会按以下顺序工作：

```text
解析 action 文件
→ 检查 stage_id / revision / action / next_stage
→ 检查当前节点的 Guard、required outputs 和字段门禁
→ 触发 python-statemachine 转换
→ 追加 loop-events.md
→ 原子保存 loop-state.json
```

典型动作：

```json
{
  "action": "advance",
  "status": "passed",
  "stage_id": "01",
  "revision": "r1",
  "next_stage": "02",
  "evidence": ["loop-artifacts/stages/01/r1/fields.md"],
  "message": "背景、目标、约束和未知因素已完成增量分解"
}
```

如果验证失败，写 `rollback`；如果只是字段还没填完，不要伪造 `advance`，继续修改字段草稿即可。真正无法在本地推断、研究或采用默认值的内容才使用 `blocked_human`。人类阻塞任务可以转为 `skip_blocked`，然后继续 ready 任务；没有 ready 任务时进入 `exploration`，输出 `preference_brief` 和带 `candidate` 标记的新任务。

探索尾节点有一个专门的防误执行规则：候选任务使用 `candidate` 动作写入队列，保留 `status=candidate`，返回 `preference_brief` 给主 Agent 分析；不能把未获批准的候选写进 `advance.payload.exploration.selected_task`。只有从 `tasks/TASKS.md` 选出的 ready/pending 任务，才用 `selection_mode=task_board` 的 `advance` 回到 01。

## Hook 到底做什么

Hook 不是状态机本身，而是工具准入和即时提示层。它会在 Claude 忘记命令或选错工具时把正确命令、当前文件和下一动作注入上下文：

```text
PreToolUse  → 判断工具是否触及受保护资源，并注入字段命令提示
PostToolUse → 记录有限工具结果，不保存完整上下文
PreCompact  → 记录压缩开始
PostCompact → 记录压缩摘要
Stop       → 默认阻止退出，并在同一 Claude 会话中注入下一轮提示
```

默认模式是 `hybrid`，默认 Stop 策略是 `inline`：

- 正常 Stop 返回 Claude Code 标准的 `decision: block`。模型不退出、不丢上下文，收到包含上轮摘要和当前恢复目标的提示后继续工作；若输出重复，提示会要求转换诊断/修复策略。
- 只有内存、连接或进程级中断才由 supervisor 从 `loop-state.json` 启动短上下文恢复。这些情形不能可靠地在已损坏的会话中修复。
- 如需旧的“每个 Stop 后新上下文”实验模式，显式使用 `--stop-policy fresh` 或设置 `RALPH_STOP_POLICY=fresh`。项目 Hook 可用 `ralph install-hooks <project> --stop-policy inline` 重新安装。

### 可审计的网页 LLM 交叉核验

`WebSearch`/`WebFetch` 只能获取公开资料，不能可靠地向登录式网页聊天页提交问题。因此“网页 LLM 已询问”不是提示词声明，而必须有 `ralph web-llm-check` 写出的阶段回执。可为至少两个独立的 OpenAI 兼容 HTTPS provider 配置**环境变量名**（不要把密钥写进项目）：

```bash
export RALPH_WEB_LLM_PROVIDERS_JSON='[
  {"id":"provider-a","endpoint":"https://api.example-a.com/v1/chat/completions","model":"model-a","api_key_env":"PROVIDER_A_API_KEY"},
  {"id":"provider-b","endpoint":"https://api.example-b.com/v1/chat/completions","model":"model-b","api_key_env":"PROVIDER_B_API_KEY"}
]'
export PROVIDER_A_API_KEY='…'
export PROVIDER_B_API_KEY='…'
```

若需要让 RALPH 内的本地 Agent 用 Playwright 启动可见浏览器、逐字输入同一核验问题、提交并读取网页回复，**先由人类为该项目一次性授权**（站点与 02.5 / 04.5 loop prompt 的 allowlist 对应）：

```bash
ralph web-llm-authorize . --providers perplexity chatgpt gemini
```

命令只写入 `loop-artifacts/contracts/web-llm-browser-authorization.json`，其中只有授权站点和公开 URL。阶段 Agent 无权执行这个 control-plane 命令；授权后它只能在交叉验证阶段运行 `ralph web-llm-check`，因此实际浏览器输入与提交是**本地 Agent 的动作**，不是提示词中的虚假声明。也可以使用一次性的环境变量覆盖项目授权（适合 CI）：

```bash
export RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON='[
  {"id":"perplexity-review","site":"perplexity"},
  {"id":"chatgpt-review","site":"chatgpt"}
]'
export RALPH_WEB_LLM_BROWSER_HEADLESS=0
```

浏览器 provider 使用全新的临时上下文。需要登录的站点会在可见窗口中报告登录缺失，不会尝试填写账号或密码，也不会复用或读取已有浏览器 cookie；此时将错误留在回执中而非伪造结果。API 与浏览器 provider 可以混合，但必须总共至少有两个不同 provider 才会计入交叉核验。

若人类明确希望**所有未来项目**都能用同一账号提问，可设置全局授权和一个**专用**持久 Playwright profile：

```bash
ralph web-llm-authorize --global \
  --providers perplexity chatgpt gemini \
  --profile-dir "$HOME/.local/share/ralph-runtime/browser-profile"
```

首次使用该空 profile 时，人类需在弹出的可见浏览器中自行登录一次；之后所有 RALPH 项目都会复用它，无需每次登录或重复授权。不要把 profile 指向日常 Chrome、Codex in-app Browser 或其他现有 profile：运行时不会读取、复制或导入那些 cookie / 密码 / 会话。全局授权意味着符合阶段契约的任务摘要会被发送到所选网页 LLM；敏感项目请改用项目级授权或关闭全局配置。

把当前阶段目录内的请求文件写为 `{ "claim": "…", "context": "…" }`，然后运行：

```bash
ralph web-llm-check . loop-artifacts/stages/02.5/r1/web-llm-request.json
```

命令只保存 provider、模型、端点主机、传输方式、时间、回答和哈希，不保存密钥、cookie 或登录状态。少于两个成功 provider、未配置 provider 或没有回执时，任务只能标记为“权威来源交叉核验”，不得声称已完成网页 LLM 交叉验证。LLM 回答只用于发现反例或遗漏；事实仍必须由至少两份独立权威来源支持。

如果 Claude 上下文在 `SubagentStop` 前退出，supervisor 会在 cycle 边界自动将残留字段任务恢复为 `ready`，避免幽灵 `dispatched` 永久卡住。

默认不会因为无状态写入、字段派发迟缓、Agent 长时间研究或连续失败而结束或重开 Claude 上下文。Commander 在同一上下文内收到 Hook 的阶段性修复提示，并继续更新当前字段；状态和上轮错误都保留。只有用户显式设置 `--idle-timeout`、`--max-failed-cycles`、`RALPH_FIELD_DISPATCH_STALL_SECONDS` 或 `RALPH_FIELD_AGENT_STALL_SECONDS` 时，supervisor 才会把相应等待阈值当作一次可恢复的 fresh-context 边界。

若显式启用字段 Agent 监视，运行时会在网页工具连续失败或派发后长期未执行 `field-apply` 时记录原因，并以持久化任务文件恢复。默认关闭这个监视；长研究和自我修复不应被框架误判为无进展。

- 字段缺失、普通阶段范围错误：允许工具继续，但在 Hook 上下文中明确告诉 Agent 修复什么。即使有 research 字段等待 Agent，Commander 仍可增量编辑当前阶段 `fields.json`，并执行 `field-init`、`field-apply`、`graph-apply`、`apply`、`status`、`events`、`validate`、`render`、`task-next`；这些受控 `ralph` 命令不会被“先派 Agent”提示拦截。未列入协议的 Bash、直接状态文件修改和越界写入仍会被拒绝。
- `research_required` 字段：逻辑上硬性要求一个字段对应一个 Agent；正常情况下 Agent prompt 带 `RALPH_FIELD_TASK=<task.json>`。如果本地前端丢掉了这行，hybrid Hook 会从 ready 队列自动绑定一个字段并继续，仍不允许合并多个字段；enforce 模式继续要求显式标记。两种模式都不能先读完整日志或直接改状态。
- 字段 Agent 已启动：状态保存为 `dispatched`，Stop Hook 阻止父 Commander 提前结束，直到收到 `SubagentStop` 或由下一次 supervisor 启动恢复为 `ready`。同一字段最多允许重复 Read 3 次；之后重复 Read 会被 Hook 拒绝，唯一下一步是 Write/Edit 后运行 `field-apply`。
- Commander 不能用未列入当前阶段白名单的协调工具（例如 `SendMessage`、任意任务管理工具）催促子代理；子代理完成后由生命周期事件和字段文件驱动下一轮。这样可以避免模型调用错误的消息接口，把工具参数错误误判为研究失败。
- 直接写 `loop-state.json`、危险副作用、越界路径、活动人类阻塞：硬拒绝。
- Stop 的协议错误默认不会丢掉同一长上下文；重复输出会注入“策略切换”提示，要求先做不同的诊断、修复或验证动作。仅 `fresh` 策略才允许 `ralph resume` 从持久化状态创建新上下文。
- supervisor 的 idle 进度只看 `loop-state.json` 的实际变化；`pretooluse_observed` 等噪声事件不会延长 idle 计时，因此重复被拒绝的 Bash/Read 不会形成无限反馈循环。
- 两个并行 Agent 的预约由项目锁按 `task-id` 原子完成；SubagentStart 再按 Agent 名称绑定，避免并发到达顺序造成字段串线。
- 网页工具若返回 HTTP 错误、403、零结果或占位工具调用，连续两次后会被 Hook 熔断；单个字段默认最多发起 3 次网页工具尝试。Agent 必须把当前字段保留为 `research_required`、写明待补原因并运行 `field-apply`，不能无限重试或伪造来源。成功拿到有效结果后，失败计数和尝试计数会自动归零。

需要临时诊断时可以使用 `shadow`，但不建议作为长期运行模式：

```bash
RALPH_HOOK_MODE=shadow ralph run ./my-project "任务描述"
```

需要全量硬门禁时使用 `enforce`：

```bash
RALPH_HOOK_MODE=enforce ralph run ./my-project "任务描述"
```

正常本地模型运行使用默认 `hybrid` 即可。Hook 会自动注入类似以下提示，不要求人手记命令：

```text
若草稿不存在，运行 ralph field-init .
填写当前阶段 fields.json
运行 ralph field-apply . <fields.json>
只修复命令列出的字段，保留已经通过字段
全部完成后写 advance.json，再运行 ralph apply . <advance.json>
```

## 命令表

Hook 会在 Commander/Worker 的每次工具调用中重复注入命令用法；命令或 JSON 失败后，PostToolUse 只要求修复错误列出的字段并重试，不要求重写完整阶段。普通缺失和阶段提示是软提醒；状态文件、危险副作用、活动人类阻塞、字段越界派发、重复读取上限和 `apply` 门禁是硬拒绝。

| 命令 | 用途 |
|---|---|
| `ralph run "TASK"` / `ralph run PROJECT TASK` | 自动匹配/创建项目，或指定项目初始化/恢复并启动受控 Claude 会话 |
| `ralph init PROJECT` | 默认创建 prompt-first Markdown 项目（无任务时首个 `ralph loop PROJECT TASK` 会采用任务）；旧字段模式使用 `--workflow field` |
| `ralph loop PROJECT TASK` | 新显式项目默认使用 prompt-first；同一 TUI 仅凭 Markdown 完成标记经 Stop Hook 推进 |
| `ralph prompt-first {init,status,render,loop}` | 显式使用或检查 Markdown-only 流程 |
| `ralph prompt-first web-llm PROJECT QUESTION --context TEXT` | 用全局/项目授权的本地 Playwright 或 API 网页 LLM 交叉询问，写入 Markdown 回执；不参与阶段语义门禁 |
| `ralph resume PROJECT` | 从现有状态启动短上下文继续 |
| `ralph status PROJECT` | 输出当前状态；默认是有限摘要，`--full` 才输出完整状态 |
| `ralph field-status PROJECT` | `status` 的字段中心别名；查看字段/DAG 有限摘要，`--full` 才输出完整状态 |
| `ralph prompt render PROJECT` | 查看当前阶段提示 |
| `ralph field-init PROJECT` | 创建当前阶段空字段草稿 |
| `ralph field-apply PROJECT FILE` | 增量字段校验、合并、原子保存 |
| `ralph graph-apply PROJECT FILE` | 校验并完成一个 DAG 节点，原子更新 `plan.completed` 和后继 ready/Join |
| `ralph apply PROJECT FILE` | 校验并应用阶段动作 |
| `ralph validate PROJECT` | 只做状态/DAG/契约检查 |
| `ralph events PROJECT --tail 20` | 读取有限事件摘要 |
| `ralph render PROJECT FILE` | 从 JSON 生成人类可读 Markdown |
| `ralph watch PROJECT` | 轮询看板，不读取长事件全文 |
| `ralph replay PROJECT` | 从事件重建可观察状态 |
| `ralph recover-state PROJECT` | 从备份或阶段快照恢复状态 |

## 运行时文件的边界

Python 文件不是第二个 Agent，也不是让模型重新实现状态机。它们分工如下：

```text
nodes.py             固定阶段节点和输入/输出条件
machine.py           python-statemachine 的 Guard/Transition 适配
state.py             loop-state.json 初始化、迁移、原子持久化
protocol.py          action JSON 解析和字段校验
result_artifacts.py  阶段文件路径限制
cli.py               人可执行的 field-init / field-apply / graph-apply / apply 命令
hooks.py             Claude Hook 的 allow/deny/context 和事件记录
prompt_renderer.py   根据 state 渲染当前阶段或短恢复提示
events.py            Markdown 事件日志和有限重放
dag.py               任务图的依赖、环和 Join 校验
```

模型只负责理解任务、研究、填写字段和提出结构化动作；机械部分由 Python 负责。Bash Hook 只是 Claude Code 的入口适配器，调用 `ralph hook <event>`，不复制状态机逻辑。命令不是靠模型记忆：每次 Commander/Worker 的 PreToolUse 都会注入适合其角色的命令提示，包括 `status`、有限 `events`、`field-init`、增量 `field-apply`、`graph-apply`、`validate`、`render`、`apply` 和 `resume`。Worker 只需按自己的 task JSON 写入并执行对应校验命令。`ralph status` 默认只输出阶段、字段任务计数和 DAG 计数；只有人工诊断才使用 `--full`，避免把完整状态重新塞进模型上下文。

### 自动字段 worker（默认恢复模式）

每次 `ralph loop` 默认会为 ready 字段启动一个有界的独立 worker，因此不依赖本地 Commander 必须先记住派发 Agent：

```bash
ralph loop ./my-project --mode hybrid
```

首轮先由 Commander 独占 Claude 上下文；如果该上下文结束且 ready 字段仍未被派发，Runtime 才会启动最多 `RALPH_MAX_PARALLEL_FIELDS` 个独立 Claude 进程作为 fallback。默认值为 `1`，适合本地 MLX/Qwen 设备；有足够内存时可显式设为 `2+`。这不改变 DAG 的并行组，只限制实际同时运行的本地模型数量。worker 使用项目级 RALPH Hook settings，但只开放 Read/Write/Edit/Bash 和自己的 task JSON；因此 Read 后会收到 Hook 的“立即 Write/Edit → field-apply”反馈，同时不会加载旧会话上下文。pending 结构字段的 worker 提示固定为 `Read → Write/Edit field → ralph field-apply` 三步，不启动网页搜索。`field-apply` 仍是唯一状态写入口；没有 `field-apply` 的自然语言不会算完成。worker 启动失败会立即把任务恢复为 `ready`；这样既能自动恢复，也不会在低内存设备上让 Commander 与 fallback worker 首轮并发抢占 KV cache。

若要只测试 Commander 的主动派发行为，可显式设置 `RALPH_AUTO_FIELD_WORKERS=0`；低内存设备可设置 `RALPH_MAX_PARALLEL_FIELDS=1`。

pending 结构化字段的 worker 默认使用 low effort 且禁止网页搜索；可用 `RALPH_AUTO_FIELD_EFFORT` 覆盖。运行时拒绝 stage-01 生成的占位字段，避免“原样 field-apply”被误记为进度；不完整字段进入 `deferred`，ready 队列耗尽后才公平重开最旧 deferred。

## 并行任务

阶段 03 以后任务图节点可以包含：

```json
{
  "id": "T1.1",
  "parent_id": "T1",
  "depends_on": [],
  "execution_mode": "parallel",
  "parallel_group_id": "G1",
  "input_refs": ["task_spec.semantic_map"],
  "output_schema": {"type": "research_findings"},
  "preconditions": ["字段已完成"],
  "postconditions": ["结果带证据"],
  "writes": ["artifacts/gpu-price.json"]
}
```

把一个 `role: "task_graph"` 字段增量写入 `fields.json` 后，`field-apply` 会先调用 `dag.validate_plan` 检查重复 ID、缺失依赖、环、并行正交性和写入冲突；校验失败不会保存任何状态。通过后，Runtime 会在当前阶段 `tasks/` 下为每个 node 生成一个 `graph_task` 文件，记录 `depends_on`、`parallel_group_id`、输入/输出、前后置条件和 `writes`。因此动态字段数量和动态节点数量都不需要预先写死。

同组节点必须正交、写入范围不冲突、可以独立验证；Join 节点必须列出所有依赖。DAG 校验不允许环、不允许未满足依赖、不允许两个并行节点声明相同写入路径。

执行节点同样支持增量填写：子代理只修改自己的 `graph_task` JSON，写入 `output`/`evidence` 后运行 `ralph graph-apply . <节点文件>`。依赖未完成、输出为空、JSON 语法错误或节点不存在时，本次提交拒绝且不改变状态；通过后才把节点加入 `plan.completed`，并自动开放下一层节点或 Join。这样不会因为一次没填完整而丢失草稿，也不会让 Commander 直接手改 DAG 完成标记。

## 事件日志和上下文控制

`loop-events.md` 只保存可观察事件的有限摘要：阶段变更、工具名、允许/拒绝决定、Agent 生命周期、压缩、停止原因和结构化产物引用。它不会保存隐藏思维过程，也不会把每次完整 Agent 输出重新注入下一轮。

完整大输出应放到阶段 artifact，Markdown 只保存摘要和引用。读取事件时使用：

```bash
ralph events ./my-project --tail 20
```

如果模型或 oMLX 报上下文/内存错误，Hook 不会把它伪装成协议失败；状态保持不变，直接用：

```bash
ralph resume ./my-project
```

建立短上下文继续。这样可以避免反复读取完整 `loop-events.md` 和重复派发任务。

## 测试

在 workspace 中运行：

```bash
python3 -m compileall -q loop/ralph_runtime/ralph_runtime
pytest -q loop/ralph_runtime/tests/test_field_workflow.py
```

完整历史测试目录仍包含旧卡片契约的回归样例，它们不代表当前默认流程；新的 field workflow 测试是本次增量设计的验收入口。
