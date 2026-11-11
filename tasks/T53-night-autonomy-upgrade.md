# 夜间自治升级：cron + subagent ralph + bus 唤醒（2026-11-12）

## 架构（D 指定）

```
cron (30m, job d7f720fed14d)
  └─ 每次唤醒 = Lead 新会话
       ├─ 读 T53-night-autonomy.md 执行日志 → 知道进度
       ├─ 读 bus 文件（lead-to-teamer / teamer-to-lead 尾部）→ 看 subagent 汇报
       ├─ 有活跃 goal 的活 → delegate_task spawn subagent（ralph 模式，goal 定验收）
       │     └─ subagent 干完一个工作单元 → 追加写 teamer-to-lead.md（带序号+时间戳）
       └─ 自己直接做不需要 subagent 的事（监控/分析/落盘）
```

关键区别 vs 纯 cron：cron 只负责"叫醒 Lead"，Lead 被叫醒后通过 **bus 文件** 和 subagent 交换信息（持久、可追溯），subagent 由 Lead 用 delegate_task 派、定 goal 跑 ralph。subagent 不能自己联网/问人，所以需要在线信息的活由 Lead 代查写文件给它。

## bus 协议（沿用 tasks/T53-bus/PROTOCOL.md，Decision 21）

- `tasks/T53-bus/lead-to-teamer.md`：Lead 写指令/方向修正，格式 `## L<n> <HH:MM> — 标题`
- `tasks/T53-bus/teamer-to-lead.md`：Teamer 写进展/决策点/坑，格式 `## T<n> <HH:MM> — 标题`
- 双方追加式不覆盖；每完成一个工作单元读一次对方文件尾部。
- 实时纠偏走 delegate_task steer；bus 是持久记录。

## 当前状态

- r14 运行中（proc_9f36253dab6c, pid 69056），r1 出 22 节点，structural test 生效（N8 quotient 判定理由含显式运算结构 BW=(Weight+KV)/Lat）。
- cron t53-night-autonomy enabled，每 30m 唤醒。

## 执行日志

- 2026-11-12 ~02:40 架构确认：cron 唤醒 Lead + subagent ralph + bus 异步交流（D 指令）。