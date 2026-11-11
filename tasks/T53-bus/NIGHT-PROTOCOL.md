# T53 夜间双人协作协议 (2026-11-12 D 指令)

D 原话："晚上不需要你回我的话，stop hook 可以开。不过最好是给 subagent 开，你被他汇报吵醒，或者他困惑和不确定就找你。两个人比孤独的一个好不是吗。"

## 分工
- **Teamer（subagent, ralph 模式）**：干执行层活——等 r14 出结果 → 提取 edge 分布对照 r13 → 选 5 道 deepresearch 题跑 bench 对标 CellCog Max 56.72 → 打不赢就诊断弱项修机制。每完成一个工作单元往 teamer-to-lead.md 追加一条记录。
- **Lead（主会话）**：方向判断、steer 纠偏、收结果、idea 推进决策、教授邮件起草。被 bus 新条目或 child 结果唤醒时处理。

## Teamer 何时找 Lead（写进 goal 的硬规则）
1. 困惑/不确定：方案二选一拿不准、发现与任务书矛盾的现象
2. 异常：进程崩了且重试一次仍失败、数据明显反常（如 edge 分布又回到 >80% quotient）
3. 工作单元完成：每个 phase 结束时汇报 + 落盘证据路径
4. 需要外部信息：teamer 无网络，要查的东西写进 bus 由 Lead 代查后写回 lead-to-teamer.md

## 唤醒链
- r14 跑完 → background notify 消息插进 Lead 会话（事件驱动，非轮询）
- Teamer 完成/求助 → child 结果作为新消息回到 Lead 会话
- Lead stop-gate（ralph-never-stop 条件版）：有 bus 未读/r14 未完/任务书有待办 → continue；全清 → 放行停止
- cron 降为 2h 兜底看门狗（主会话死了才用）

## 红线（同 T53-night-autonomy.md）
不外发消息、不改 AGENTS.md、不花钱、泄漏题目=事故、版本可复现（commit SHA + checkpoint 不覆盖）。
