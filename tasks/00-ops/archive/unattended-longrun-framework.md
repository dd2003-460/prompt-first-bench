# Goal: 无人值守长程任务执行框架

> origin: ai · 2026-11-15 · D 指令"我还是希望无人值守"
> 与 pfb-hardening-v2 正交：那个是"修 pipeline 出报告"，这个是"让 agent 能自主跑长程任务"

## §1 五字段

```
【目标】构建 agent 自主执行长程任务的框架：给定总目标后，自动分解→并行派发→验收→推进，
      无需用户中间介入（除非碰到只有人能做的事）。
【阶段】pfb 项目，当前 pfb-hardening-v2 在 phase1-fix-pipeline（1/5），
      本 goal 是基础设施层，不依赖具体 pipeline 修复进度。
【SOP 索引】
  - agents/goal-template.md §3.5（subagent 协议）
  - ~/.hermes/rules/engineering.md（长跑进程判据）
  - ~/.hermes/rules/autonomy.md（自主决策 + 收尾禁令）
  - sop/arena-loop-pipeline.md §3（仓库映射 + 会话台账）
【验收标准】
  1. 给定一个目标（如"跑完 soc 119 节点 verify"），agent 能自动：
     - 分解成 ≤5 个并行子任务
     - 用 delegate_task 派发（每个 subagent 独立上下文）
     - 收齐结果后自动验收（gate 检查）
     - 未达标 → 带反馈重新派发（最多 2 轮）
     - 全过 → 落盘 + commit
  2. 长进程（>5min）用 setsid nohup 起，PID 写进 goal state，
     每 5min 自动探活（kill -0），死了自动重启（最多 3 次）
  3. 用户不介入的情况下，从"给定目标"到"完成 + commit"全程自主
     （只有"手动上传 arXiv / 花钱 / 对外发布"才停下等人）
  4. 故障恢复：进程死了 → 自动重启；subagent 返回垃圾 → 自动重派；
     连续 3 次失败 → 写 HALT 停 + 落盘诊断报告
【失败降级】
  - delegate_task 不可用 → 串行执行（不并行，但能跑完）
  - 长进程反复死（>3 次）→ 写 HALT + 落盘诊断，等人
  - 验收 gate 反复不过（>2 轮）→ 降级为"部分完成"，落盘已完成部分 + 标记缺口
```

## §2 分解树（正交 + 完备 + 递归原子）

```
无人值守框架
├── A. 任务分解器（给定目标 → ≤5 个并行子任务）
│   ├── A1. 输入：goal 描述 + 当前状态（checkpoint/loop-state.json）
│   ├── A2. 输出：子任务列表（每个带：目标/输入/输出/gate 标准）
│   ├── A3. 约束：正交（不重叠）+ 完备（覆盖全部）+ 原子（一步可做完可检查）
│   └── A4. 落盘：tasks/decomposition.md（分解树 + 任务表）
│
├── B. 并行派发器（子任务 → delegate_task）
│   ├── B1. 每个子任务一个 subagent（独立上下文）
│   ├── B2. context 字段：goal-template §1-§5 全文 + 子任务描述 + 相关数据路径
│   ├── B3. 并发上限：3（避免资源竞争）
│   └── B4. 派发后前台持续干活（不结束 turn，防静默黑洞）
│
├── C. 验收器（subagent 返回 → gate 检查）
│   ├── C1. 输入：subagent 返回的 summary + 产出文件路径
│   ├── C2. 检查：产出文件存在？指标达标？（按子任务 gate 标准）
│   ├── C3. 未达标 → 带具体差距反馈重新派发（最多 2 轮）
│   └── C4. 全过 → 落盘 + commit
│
├── D. 长进程管理器（>5min 任务 → setsid nohup）
│   ├── D1. 启动：setsid nohup <cmd> > log 2>&1 &
│   ├── D2. PID 写进 goal state（JSON 文件）
│   ├── D3. 每 5min 探活：kill -0 <pid>
│   ├── D4. 死了 → 自动重启（最多 3 次）
│   └── D5. 连续 3 次死 → 写 HALT + 落盘诊断
│
└── E. 故障恢复器（异常 → 自动处理）
    ├── E1. subagent 返回垃圾 → 自动重派
    ├── E2. 长进程死了 → 自动重启
    ├── E3. 验收 gate 反复不过 → 降级为"部分完成"
    └── E4. 连续 3 次失败 → 写 HALT + 落盘诊断报告
```

## §3 缺口标注

| 子项 | 缺什么 | 怎么补 |
|------|--------|--------|
| A. 任务分解器 | 没有自动分解逻辑，目前是我手动判断 | 写一个 `task_decomposer.py`：输入 goal 描述，输出子任务列表（用 LLM） |
| B. 并行派发器 | delegate_task 已可用，但 context 字段需要标准化 | 写一个 `dispatch_template.py`：自动生成 context 字段 |
| C. 验收器 | 没有自动 gate 检查，目前是我手动验收 | 写一个 `gate_checker.py`：输入产出文件 + gate 标准，输出 pass/fail |
| D. 长进程管理器 | 没有自动探活/重启，目前是我手动 kill -0 | 写一个 `process_monitor.py`：cron 每 5min 跑一次 |
| E. 故障恢复器 | 没有自动故障处理，目前是我手动判断 | 写一个 `fault_handler.py`：输入异常类型，输出恢复动作 |

## §4 任务表（派发只执行表内条目）

| # | 任务 | 输入 | 输出 | gate 标准 | 优先级 |
|---|------|------|------|-----------|--------|
| T1 | 写 task_decomposer.py | goal 描述 + checkpoint | 子任务列表（JSON） | 正交 + 完备 + 原子 | P1 |
| T2 | 写 dispatch_template.py | 子任务列表 | delegate_task 调用参数 | context 字段含 goal-template §1-§5 | P1 |
| T3 | 写 gate_checker.py | 产出文件 + gate 标准 | pass/fail + 差距描述 | 能自动判断 pass/fail | P1 |
| T4 | 写 process_monitor.py | PID + 日志路径 | 探活结果 + 重启动作 | 每 5min 自动探活，死了自动重启 | P2 |
| T5 | 写 fault_handler.py | 异常类型 + 历史 | 恢复动作 + 诊断报告 | 连续 3 次失败 → 写 HALT | P2 |
| T6 | 集成测试：跑一个完整目标 | "跑完 soc 119 节点 verify" | 完成 + commit | 全程自主，无人介入 | P1 |

## §5 产投比排序

1. **T6（集成测试）**：最高价值——验证整个框架能跑通，不跑通其他都是空谈
2. **T1-T3（分解/派发/验收）**：核心链路，没有这三个框架不成立
3. **T4-T5（长进程/故障恢复）**：增强鲁棒性，但核心链路跑通后才有意义

**建议执行顺序**：T1 → T2 → T3 → T6（先跑通核心链路）→ T4 → T5（再增强鲁棒性）

## §6 对标

- **竞品**：AutoGen（Microsoft）、CrewAI、LangGraph——都是多 agent 框架，但都依赖外部 API（付费），且没有"无人值守"的自动调度循环
- **我们的优势**：本地 LLM（qwen3.8-27b-mtp，免费）+ 已有基础设施（delegate_task/setsid/cron/stop_hook）
- **差距**：他们没有"验收 gate"和"故障恢复"，我们要有

## §7 风险

1. **LLM 分解质量**：task_decomposer 用 LLM 分解，可能拆得不好 → 降级：人工审核分解结果（但这就不是无人值守了）
2. **subagent 返回垃圾**：delegate_task 可能返回不相关的结果 → 降级：gate_checker 自动重派（最多 2 轮）
3. **长进程反复死**：setsid nohup 也可能被杀（OOM/系统重启）→ 降级：连续 3 次死 → 写 HALT + 诊断
4. **资源竞争**：3 个 subagent 并行 + 长进程，可能 CPU/内存打满 → 降级：并发上限 3，长进程优先级低
