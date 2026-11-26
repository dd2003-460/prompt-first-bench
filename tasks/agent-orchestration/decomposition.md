# origin: ai · 2026-11-26 · D 指令「改变目标：低效的执行不如先想想怎么把完整思考加入机制；需要清晰的 agent 编排和分配系统；你和微信都不用一直干活，而是看一个或更多执行者干活」

# Agent 编排系统（监督者-执行者架构）— 分解

## 目标
两个聊天入口（QQ/微信）= 监督者：只规划、派发、验收、看。
执行者 = 独立持续工作者，带完整思考机制（think-trigger 12 阶段思考检查点集成）。
验收：一个真实任务（T8c 重锚定）经新架构跑通，监督者不碰执行细节，思考机制留痕。

## 与现有 goal 的关系
- 取代「T8c 重锚定→smoke→n=9」为当前焦点（该链条降级为本 goal 的 S3 试点任务）
- think-trigger（research-agi-budget 子项⑥）的思考机制设计并入本 goal「执行者思考机制」子项
- T8c 任务书已落盘（reanchor-taskcard.md 385 行, 36 替换点），恢复成本=一次脚本运行

## 分解树
1. **现状盘点**（部分完成, 2026-11-26 实测）
   - 本地执行者候选：Hermes delegate_task（瞬态 sub, 27b 截断实证：输入>300 行或输出>100 行必死）/ Agent Teams AI（本地 Electron 多 agent 应用, **本轮实测 API 无响应=未运行**）/ arena LMArena（web 通道, 可达性待验）/ RALPH loop-leader 规格（agents/task-manager.md, 12 phase agent 定义, 有指挥协议无运行体）
   - 本地思考机制资产：think-trigger 12 阶段思考检查点 + 反思文案（含 Utility/Index）+ stop_hook（实证：软提醒无效，思考必须由具体矛盾触发）
   - **核心架构缺口：没人聊天时谁在跑（执行者持久性）**
2. **成熟方案调研**（S1 收集 → S2 综合）
   - supervisor-worker 模式：LangGraph supervisor / AutoGen / CrewAI / MetaGPT / Anthropic multi-agent research system / OpenHands
   - 持久 worker：daemon / cron / background task 模式
   - 思考机制注入：checkpoint 怎么进执行者（prompt / hook / stage-gate 门禁）
3. **架构设计**（S2, 判断-Lead）
   - 角色分离：监督者（薄：任务表+载体判定+验收）/ 执行者（厚：思考内置+自检）/ 验收（回执+磁盘核验+数字复算）
   - 分配：任务表 → 载体判定（sub-27b / sub-arena / 脚本-Lead / 判断-Lead）→ 派发通道映射
   - 失败处理：sub 死 → 磁盘核验 → 换路（今日实证规则，制度化进架构）
4. **试点**（S3）：T8c 重锚定走新架构（机械任务、任务书就绪、验收=3 命令+commit）
5. **验收+复盘**（S4）：回执落盘、思考检查点触发记录、写回 SOP

## 任务表（状态 2026-11-26 22:20）
| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 | 状态 |
|---|---|---|---|---|---|---|
| S1 收集: GitHub+arXiv 成熟方案 → JSON | 无 | API | ~200 (JSON) | 1 | 脚本-Lead | done (s1-collection.json) |
| S2 综合: 架构方案（角色/分配/失败/持久性/思考注入） | S1 | S1 JSON + 本地规格 ~400 | ~150 | 1 | 判断-Lead | done (s2-architecture.md) |
| S3 试点: T8c 重锚定走新架构 | S2 | 任务书 385 | 6 文件+回执 | 1 | executor-cron (job 786f0323d6b8, 10m, monitor 门禁) | done (2026-11-26 23:52, 判决=停止不扩样, 报告 t8c-smoke-rerun-report-20261126.md) |
| S4 验收+复盘+SOP 写回 | S3 | 回执+commit 链 | ~50 | 1 | 监督者 | 执行中（复盘 s4-retro-t8c-pilot-20261126.md 落盘; SOP 写回 4/5: monitor PID 探活 done(9309abbaf), 余 monitor 静默停摆修复(状态列括号后缀, 已修待验收)） |
| S4-1 monitor PID 探活: queue_monitor.py 对 WORKING 行读回执 PID, kill -0 死 → 输出 DEAD:<id>（使 monitor 闸门开, 执行者下拍接力）; 协议路由加 DEAD 分支（同 STALE 处理）; 边界: 只改 queue_monitor.py + executor-protocol.md 路由节, 不动 receipt 格式; 验收: ①活 PID 时输出不变（diff 空）②kill 假 PID 后输出含 DEAD ③selftest 无回归 | S4 | queue_monitor.py ~70 + 协议 ~20 | ~40 | 1 | sub-27b | ✅ 完成 2026-11-27（commit 9309abbaf，Lead 验收: DEAD 分支在位/IDLE 不崩/两次输出一致/协议 L15 路由在位。注: sub 最终汇报行掉复读循环被掐=failed 误报，执行层全落盘，信磁盘不信汇报行） |

## 缺口清单
- [待核验] Agent Teams AI 应用：能否启动？开机自启？（本轮实测 localhost:3456 无响应）
- [待核验] arena 可达性（ego-browser 会话状态）
- [待核验] 持久执行者实现形态（常驻进程 / cron / app / 云端 arena）
- [待核验] 思考机制注入点（执行者 prompt？hook？stage-gate 门禁？）
- [待核验] S2 关键架构判断需 ≥2 独立来源交叉（ego-browser 网页 LLM）
