# RALPH 错误反馈提示设计

## 目的

Hook 拦截错误后，不能只返回“工具不允许”或“格式错误”。本地模型需要立刻知道：

1. 检测到了什么错误。
2. 当前动作为什么不能继续。
3. 唯一的下一步是什么。
4. 哪些看似合理的绕过动作禁止执行。
5. 如果需要结构化输出，必须填写什么接口。

运行时统一使用：

```text
RALPH_FEEDBACK[错误码]
已检测到：……
立即修正：……
唯一下一步：……
禁止：……
输出要求：……
```

反馈提示是短控制指令，不复述完整任务、不复制 `loop-events.md`、不记录隐藏思维过程。

## 真实错误到反馈动作

| 错误码 | 触发位置 | 模型曾经的错误 | 反馈后的唯一动作 |
|---|---|---|---|
| `EVENT_LOG_LOOP` | Commander Read | 反复读取完整 `loop-events.md`，扩大上下文和 KV cache | 停止 Read；最多运行一次 `ralph events . --tail 20`，有 `dispatched` 卡就等待 `SubagentStop` |
| `DUPLICATE_DISPATCH` | PreToolUse/Agent | 已有 `agent_id` 仍重复派发同一卡 | 不再调用 Agent，读取已有回执或等待子代理结束 |
| `DISPATCH_BINDING_WAIT` | PreToolUse/Agent | Agent 已启动但尚未完成生命周期绑定，又再次派发 | 等待 `SubagentStart/SubagentStop`，不手写 `agent_id` |
| `PENDING_CARD_ACTION` | PreToolUse/Bash | 用 Bash、`cat` 或 Write 创建任务卡、契约或状态 | 下一次直接调用指定 Agent，第一行使用准确的 `RALPH_TASK_CARD=...` |
| `PENDING_CARD_DISPATCH` | PreToolUse/Skill/WebSearch/AskUserQuestion 等 | pending 审计卡尚未派发，却先尝试研究或提问 | 下一次工具调用必须是指定 Agent，并在首行写准确的 `RALPH_TASK_CARD=...` |
| `COMMANDER_MUTATION` | PreToolUse/Write/Edit | Commander 试图绕过 Hook 修改受控文件 | 使用批准的 Agent，或直接返回结构化阶段结果 |
| `COMMANDER_BASH_SCOPE` | PreToolUse/Bash | 用 Bash 生成 `<RALPH_STAGE_RESULT>` 或修改状态 | 只执行 `ralph` 控制命令；阶段结果直接放在 Assistant 消息中 |
| `ASK_USER_GATE` | PreToolUse/AskUserQuestion | 把可以推断、研究或场景化的内容直接问人 | 先派当前审计卡；真正不可推断的问题集中写入 `payload.questions` |
| `HUMAN_BLOCK_ACTIVE` | 任意工具 | 已经 `blocked_human` 后仍继续读文件或派任务 | 结束会话，等待人类回答；新输入由 `UserPromptSubmit` 重新打开阶段 |
| `WORKER_GATE_SCOPE` | Worker 工具调用 | 只读审计卡尝试 Bash、写文件或扩大读取范围 | 只读 `document_refs`，直接返回 `<RALPH_GATE_REVIEW>` |
| `GATE_RECEIPT_INVALID` | SubagentStop | 缺少门禁标记、字段不全或值不在 schema 内 | 不新增工具调用；只把已有结论填写成完整门禁 JSON |
| `STAGE_RESULT_INVALID` | Stop Hook | 回复 `READY`、自然语言或缺少 `next_stage/payload` | 保留已识别的 action，只修复字段；有 pending 卡时优先派 Agent，不输出阶段结果 |
| `STOP_WITHOUT_ACTION` | Stop Hook | 没有结构化动作就停止，导致阶段没有推进 | 按短恢复指令执行当前唯一动作，不能重做历史 |
| `RUNTIME_INTERRUPTION` | Stop Hook | 把 API、连接、超时或 oMLX memory guard 当作协议错误反复修复 | 保留状态，安全结束，使用 `ralph resume` 开启短上下文 |

## 三类反馈不能混用

### 任务卡生命周期错误

核心是“不要再派发”：

```text
RALPH_FEEDBACK[DUPLICATE_DISPATCH]
已检测到：任务卡已经 dispatched 并绑定 agent_id。
立即修正：dispatched 是内部等待，不是 blocked_human。
唯一下一步：等待 SubagentStop；必要时只看一次有限事件摘要。
禁止：再次 Agent、Write 任务卡、AskUserQuestion、循环读取 loop-events.md。
```

### 门禁回执错误

核心是“不要再调研”：

```text
RALPH_FEEDBACK[GATE_RECEIPT_INVALID]
已检测到：独立门禁回执缺少 <RALPH_GATE_REVIEW> 或 schema 字段。
立即修正：只改写已有审计结论。
唯一下一步：返回一次 <RALPH_GATE_REVIEW> + 完整 JSON。
禁止：Bash、Write、Edit、外部搜索、重新派发。
```

### 阶段动作错误

核心是“保留真实 action，只修字段”：

```text
RALPH_FEEDBACK[STAGE_RESULT_INVALID]
已检测到：RALPH_STAGE_RESULT 缺少 next_stage。
立即修正：保留原来的 advance，不把它改成 blocked_human。
唯一下一步：直接返回一份完整阶段提交 JSON。
禁止：READY、自然语言、cat、echo、ralph apply。
```

如果原输出包含 `action=advance`，且错误只是字段/格式缺失，运行时会展示 `advance` 模板；如果错误指出门禁冲突或状态转换非法，则明确要求重新选择合法分支，不保留 `advance`。如果存在 pending/dispatched 任务卡，则优先反馈任务卡动作，不展示会诱导模型提前推进的阶段模板。

## 反馈层级

```text
PreToolUse
  → 拦截非法工具，并在 permissionDecisionReason 返回错误码和唯一下一步

SubagentStop
  → 校验门禁 JSON；失败时 block 当前子代理，只允许返回修复后的门禁回执

Stop
  → 自动 apply 合法阶段动作；非法协议给短修复提示；runtime 错误允许安全停止

UserPromptSubmit
  → 人类补充写回 canonical task_spec，并解除 blocked_human
```

## 设计边界

- 机械错误用字段、状态、路径和生命周期判断，不靠 Agent 名称或自然语言关键词猜测。
- 每次反馈只包含有限上下文；历史日志只能通过 `ralph events --tail` 查看。
- 反馈不能替代独立门禁；它只告诉模型如何修正当前错误。
- `blocked_human` 只用于真正需要人类授权或不可推断且会改变关键分支的问题。
- `candidate` 只能进入候选队列，不能因为反馈修复而被静默执行。
