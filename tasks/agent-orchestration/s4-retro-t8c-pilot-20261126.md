# S4 复盘：T8c 重锚定试点（监督者-执行者架构首跑全链）

# origin: ai (2026-11-26, Lead 判断产出)
# 范围：ReAnchor-A → smoke 重跑（n=3/臂）→ 判决 → ReAnchor-B 收口，2026-11-26 23:26-23:58
# 定位：agent-orchestration goal S4 验收材料（架构可靠性结论 + SOP 写回清单）

## 试点链路（实际发生）

| 时刻 | 事件 | 谁 | 结果 |
|------|------|-----|------|
| 23:26 | smoke 重跑起跑（97852） | 执行者 | A 臂 3/3 完成 |
| 23:33 | 97852 死于 WROTE arm_a 后（无 traceback） | — | 死因未定位 |
| 23:33 | 核磁盘 → 只重跑 B 臂（1383，保留 A 臂数据） | 执行者 | 协议合规（任务卡 §3.3 接力规则） |
| 23:47 | B 臂 3/3 完成（`WROTE arm_b + finished`） | 1383 | 无 traceback |
| 23:52 | eval + 判决 + 报告 + 收口 | 执行者 | 停止不扩样（s_A=0/3, s_B=1/2） |
| 23:5x | 独立 eval 复算 + 仪器核验（winner=V100 非旧锚） | Lead | 与执行者判决一致 |
| 23:5x | ReAnchor-B 验收（正文逐字节一致 sha256 复算） | Lead | PASS |

## 暴露问题 + 处置状态

1. **F1 PID 登记不互通**（stop_hook 等待分支只读 goal state，执行者 PID 只记 receipt → 便签轰炸 30-60s/次）
   → ✅ 已修：即时写 goal state + 协议硬边界加"PID 同时写 goal state"（commit 5befa63f9）
2. **短 ID 命名 bug**（任务名含 `/` → receipt 文件名不可创建，执行者被迫子目录镜像 workaround）
   → ✅ 已修：协议加命名规则（禁 `/`，违规报 T-失配 由监督者修表）；smoke 行任务名待下轮改
3. **monitor 闸门盲区**（进程退出不改变队列输出 → 执行者醒不来，要等 45min STALE 翻转；本轮靠 Lead 手动跑 eval 兜底）
   → ⏳ 已立项（decomposition 任务表，载体 sub-27b）：queue_monitor 增加 receipt PID 探活，进程死 → 输出 DEAD:<id> 使闸门开
4. **执行者死亡接力**（97852 死因未定位，同死法 2 次=换路规则未触发——只死 1 次）
   → ✅ 协议按设计工作；死因未定位本身记为遗留（无 traceback 的进程死亡，疑 Hermes 跟踪进程组回收，F3 已写进协议：用 setsid 等价脱离）
5. **判决一致性**（执行者判决 vs Lead 独立复算）
   → ✅ 两层验证有效：数字一致 + 仪器核验（judge winner 锚 V100）独立确认非伪影

## 架构可靠性结论（S4 验收项）

- **可防御**：执行者协议在 3 个真实故障场景（进程死亡/命名违规/IDLE 空转）下均按设计路由，无一次需要 Lead 改协议救场；判决两层一致。
- **真实缺口**：monitor 闸门的事件盲区（#3）——长任务完成时刻不产生队列状态变化，执行者感知延迟 = STALE 阈值（45min）。本轮靠 Lead 手动兜底，规模化后不可接受。修复前，长任务接力依赖 Lead 挂进程监听（已验证可行但非架构内）。
- **成本面**：monitor 闸门生效后空拍成本≈0（23:43 拍次被抑制，executions 无记录）；真实唤醒 3 次耗时 19s/695s/1 次重复循环死亡。

## SOP 写回清单

| 项 | 落点 | 状态 |
|----|------|------|
| PID 双写（receipt + goal state） | executor-protocol.md 硬边界 | ✅ 5befa63f9 |
| 短 ID 禁 `/` | executor-protocol.md 硬边界 | ✅ 本轮 commit |
| monitor PID 探活（DEAD 状态） | queue_monitor.py + 协议路由 | ✅ 9309abbaf（S4-1，Lead 验收 2026-11-27；实战首跑=CapFix-Verify 进程退出后 DEAD 触发→执行者核磁盘三判据接力验收，路由按设计工作） |
| setsid 等价脱离（Hermes 跟踪 ≠ setsid） | executor-protocol.md（F3） | ✅ 执行者已写 |
| 长任务 Lead 挂进程监听（临时，#3 修复前） | 本文件 §缺口 | 临时约定（DEAD 探活上线后此约定降级为兜底） |
| monitor 状态列括号剥离（静默停摆修复） | queue_monitor.py 解析器 | ✅ c36d8c9c9（实战验证 2026-11-27 00:34：B-Rerun 行「就绪（2026-11-27 00:33 立项）」→ READY，修复目标场景命中） |
| 起长任务前查 receipts/ 当锁（#8 跨会话协调） | executor-protocol.md 硬边界 | ✅ 5c419fe55（2026-11-27 00:37 事故后） |

## 补充故障模式（2026-11-27 凌晨，S4-1 交付时观察到）

6. **sub 汇报层复读循环 ≠ 执行失败**（deleg_3e9281bb）
   → 现象：sub 执行层全落盘（commit 9309abbaf 完好、逻辑 5 处在位、worktree 无半成品），
   但写最终汇报行时掉进复读循环被掐 → 系统报 failed。
   → 处置规则：收到 sub failed 先核磁盘（commit 链 + 逻辑在位 + worktree 干净），
   三件全过 = 误报，不重派（重派 = 重复劳动 + 烧 token）。
   → 与既有"信磁盘不信 sub 最后一句话"规则同构，本案例是其在 failed 通知上的应用。
7. **monitor 静默停摆（状态列精确匹配）**
   → 现象：任务行状态写「就绪（2026-11-27 00:07 立项）」（带括号注释），
   queue_monitor 的 `st in ("就绪","执行中")` 精确匹配 → 整行跳过 → 队列假 IDLE，
   任务永不被认领（比 STALE 盲区更隐蔽：STALE 还有 45min 翻转，这个是永久停摆）。
   → 修复：解析器 re.sub 剥括号后缀再判（已修，commit 见下）；
   → 教训：monitor 的信号完整性 = 架构的感知层，解析器对状态列的容错必须
   覆盖"人会在状态列加注释"这个高频行为。
8. **Lead 直接起重复进程（跨会话协调盲区，2026-11-27 00:37）**
   → 现象：CapFix-Verify 已由微信执行者 00:29 完成（回执 DONE），Lead 00:37 未查
   receipts/ 直接起重复进程 25725，跑完 stage 01 后覆盖执行者的 sidecar B1_01/B1_02
   （固定文件名），靠 git 从执行者 commit 67d0582fb 恢复。
   → 根因：monitor 的 WORKING 状态只挡执行者之间互抢，不挡 Lead 直接起进程——
   两个独立会话（QQ Lead + cron 执行者）盯同一张任务表，锁的覆盖面缺了 Lead 这一侧。
   → 处置：executor-protocol 硬边界加「起长任务前查 receipts/ 当锁」（commit 5c419fe55）：
   任何会话起长任务前 `ls receipts/<短ID>.json`，status∈{claimed,working,done} → 不重复起。
   判别信号：sidecar/产物 mtime 早于自己启动时刻 = 别人先跑过，立即停手核回执。
   → 与 #3 同族：都是"感知层覆盖不全"——#3 是执行者对完成事件无感，#8 是 Lead 对
   执行者已认领无感。架构可靠性结论需修订：可防御范围 = 执行者↔执行者互抢；
   Lead↔执行者跨会话协调目前靠 receipts 锁 + 人工纪律，未形成架构内闸门。
