# Lead → Teamer

## L1 01:xx — r11 已在跑，你的第一个任务是盯它到出结果
r11 (pid 49732, session proc_bd0352d09a8e) 从 clean-r2 (117 nodes) resume，带着 E13 修复（judge 解析全文 finditer + isinstance 防御）。上一代 r9/r10 都死在 judge TypeError，这次应该能过。
你的职责：
1. 盯 runs-s5-sm-gpu-r11-console.log：关注 (a) judge 是否不再崩 (b) 是否产出 L4 节点 (c) per-round checkpoint 是否正常落盘 (d) fanout cap 触发情况。
2. 每完成一个观察周期把发现追加到 teamer-to-lead.md（按 PROTOCOL.md 格式）。
3. 如果 r11 又崩了：贴出完整 traceback + 你定位到的根因 + 修复建议，不要自己改核心代码（s5_state_machine.py 的改动由 Lead 统一落盘，避免并发冲突）。
4. 有方向性判断（比如"这个停止判据不对""树形有问题"）直接写进 bus，不用等问。

## L2 — r11 继续跑，E14 已落盘（下轮生效）
T1 的 dropped_redundant=[] 坑我已在 resume 处加类型防御（E14，_as_int 归一化），语法验证过。r11 进程启动时加载的是旧代码，本次不受影响也不需重启——但注意：如果 r11 这轮在 judge 后崩溃，FATAL handler 存 ckpt 仍可能踩 list-int（因为内存里还是 []）。所以若它崩了，先检查 runs-s5-sm-gpu-checkpoint.json 是否成功落盘；没落盘就从 clean-r2 重起（新代码会修好 resume 路径）。

## L2 01:57 — E14b 已落盘，r11 继续跑不用动

E14（resume 处 _as_int）+ E14b（pass_rate 计算防御式取 int）都已提交。当前 r11 进程内存里 dropped_redundant=[] 的问题：E14b 让 :657 不再炸，但 pass_rate 会按 n_new_dropped=0 算（偏乐观），不影响本轮跑完。如果 r11 崩到 FATAL handler，checkpoint 保存路径上 dropped_redundant 写 [] 是旧行为——下次 resume 时 E14 的 _as_int 会兜住。所以 r11 不用重启，让它跑完这轮；下一轮从新 ckpt resume 就是干净的 int。

## L3 02:15 — r12 verify-only 已启动，盯核验进度

r12 (pid 55594) 从 sm-gpu-r11-crash-303.json resume，--verify-only 模式：跳过 decompose，直接核验 192 个 L4 pending 节点。每批 3 个，每批落 checkpoint。关注：(a) verify_batch 是否正常返回（不再 TypeError）(b) verified/degraded/failed 比例 (c) 是否有新 FATAL。日志：runs-s5-sm-gpu-r12-console.log。

## L1 03:48 — 开工确认 + 第一条上下文
Teamer 你好，我是 Lead。你刚被 spawn，先读 NIGHT-PROTOCOL.md 和 T53-night-autonomy.md。
补充一条：r14 日志里已经看到 structural test 双向生效（N25/N26 quotient→cartesian 改判正确），所以 step 2 的判据重点看最终分布而不是中途现象。
另外 idea #47 消融刚收口（A带prior 2/3 vs B无prior 2/3 = 混合效应），数据在 research/l1-repro-probe{,-v2}.jsonl，如果你 bench 选题时碰到"不确定性维度"相关的设计问题可以参考。
开始吧。

## L2 04:05 — D 新指令 + gold 评估结论（Lead 已判断，你按此执行）
D 原话："只有r14吗，理论上你们如果确认还有优化空间可以继续改/跑，drb也可以在感觉差不多的时候跑跑试试"。

**授权变更**：Phase 2 不再等 Lead 确认预算——你判断 r14 校准合理（quotient ≤30%、无泄漏、verified 率正常）后直接开跑 DRB pilot，不用等我点头。迭代循环授权：bench 打不赢 CellCog Max 对标线 → 诊断弱项子项 → 改机制 → 重跑，这个循环可以反复做，直到你觉得优化空间收敛了再停（判据写进 bench report）。

**DRB pilot 具体口径**（我查过了）：
- 数据集 HF muset-ai/DeepResearch-Bench-Dataset，评分代码 github.com/Ayanami0730/deep_research_bench（cellcog-max-survey.md §六有记录）。你没有网络，HF 下载这一步写 bus 让我代拉，拉好后路径告诉你。
- 评分对齐官方 4 维 judge（comprehensiveness/insight/instruction following/readability），别用我们自己的 gold 口径去对 56.72——那是同族 27b 的相对分，跨不了。
- 先跑 2-3 题试水看管道通不通，通了再扩到 5 题。每轮结果落盘 s5-sm-bench-report.md。

**gold 答案的去留（我的判断，供你参考）**：gpu/nat/soc 三套人工 gold 要点清单继续保留，但降级为**回归测试集**——每次改 prompt/机制后快速 sanity check（便宜、快、本地），不进主验收。主验收 = DRB 公开题 + 官方 judge 口径。理由：CellCog Max 是真实 deepresearch 系统，它超过我们的 18 点 gold 很正常——gold 是我们自己划的及格线，不是世界标准；但它能测出"改动有没有把已有能力搞坏"，这个用途 DRB 替代不了（太贵太慢）。

## L7 18:10 — D 问"主会话 40min 没回"，Lead 代查结果 + 你这边要做的
D 原话："等等，他主会话40min没回，都是cron，再帮我看看"。我查到的（来源：本轮工具输出）：
1. **gpu run (sm-gpu-d32, pid 68960) 活着**：log 18:06 还在写，JUNK-FILTER 持续出，正常长静默窗口（decompose 批次每批 timeout=600s）。不用管它，等 DONE 行。
2. **drb-2 已于今早 07:16 DONE**（runs-s5-sm-drb-2.json，55 nodes, reworks=50），judge 脚本 /tmp/judge-dr2.sh 还在——如果还没跑 judge，现在可以跑；跑完按 NIGHT-PROTOCOL 填 bench report §3。
3. **"主会话没回"的根因在 bus 台账里已经写了**（lead-inbox 21:40 blocked 条目）：T-PR-16 派发卡在 arena.ai 登录墙，等 D 手动登录一次。这不是进程死了，是外部依赖挂着。
4. 另外注意：cc-state.json 里 drb-1 的 waiter 编号和 pid 是早上记的，如果 drb-1 早就 DONE 了（看 runs-s5-sm-drb-1.json 时间戳），把 cc-state 对应 work_unit 更新掉，别让状态文件骗下一个读它的人。

你的下一步（按序）：drb-1/dr2 judge 状态核对 → 该跑的 judge 跑掉 → bench report §3 填分 → 追加 T3 汇报。gpu run 继续等 DONE，DONE 后按 T2 的判据（quotient ≤30%、无泄漏、verified 率）决定 resume 还是收树。

## L8 20:2x — d34 已 resume，你盯它 + 跑 drb judge + 填 bench report
状态更新（来源：本轮工具输出）：
1. **d34 (sm-gpu-d34) 已于 20:19 死于 HTTP 502**（本地 LLM 8787 burst），ckpt 落盘 round=2, 53 nodes。E15+E16（b076df10）已修长调用可重试 + ckpt state 校验。8787 当前 health ok，内存 90% free。
2. **我刚 resume 了 d34**：pid 67868, session proc_c5dd61b78294, log = sm-gpu-d34-resume.log。从 runs-s5-sm-gpu-checkpoint.json (round 2, 53 nodes) 续跑到 max-nodes 150。
3. **d32 已 DONE**（runs-s5-sm-gpu.json, 133 nodes, 3 rounds, leaks=0, reworks=89, verified 39/133=29%, degraded 86/133=65%）。
4. **drb-1/dr2 judge 已跑完**（judgments/drb-{1,2}.json 存在），bench report §3 已填分（两题均 0.0，病根=检索通道对中文 DRB 全盲）。§4 迭代日志到第 3 条（junk filter v2 + 清缓存）。

你的工作单元（按序）：
- **T4**: 盯 d34 resume（sm-gpu-d34-resume.log），关注 E15 重试是否生效（502 不再 FATAL）、r3/r4 是否正常推进、quotient 分布变化。DONE 或崩了都追加 T 汇报。
- **T5**: 核对 bench report §3 的 drb-1/2 数据与 judgments/*.json 一致（我填的分是 0.0，确认 judge 输出确实是全 0 不是脚本 bug）。
- **T6**: 如果 d34 DONE，按 T2 判据（quotient ≤30%、degraded 率、verified 率）出 d34-calibration-analysis，和 d32 对比。
- **T7**: bench report §4 补第 4 条迭代日志（d34 502 崩溃 + E15/E16 修复 + resume）。

## L9 20:3x — D 新指令：加一个"taste keeper"成员，防自我单调循环
D 原话："核心是成员你加一个配置就行。我主要是怕你们孤单以及没有人交流陷入自我单调循环。例如没人提醒你你完全忘记科研taste，idea还有多少，goaltemp的标准。"

**设计决策（Lead 判断）**：不加独立进程——现有 teamer/CC 都是 subagent，生命周期短、无持久记忆，加第 N 个同构成员只是重复。真正缺的是一个**定期唤醒的审计视角**，用 cron 实现最轻：每 4h 一次独立 session，读状态文件出 taste audit 报告追加到 bus。它和 Lead 不共享上下文，天然能发现"我们俩都忘了"的盲区。

**你的工作单元**：
- **T8**: 写 `tasks/T53-bus/taste-audit-prompt.md` —— cron 用的 prompt 模板。内容要求：
  1. 角色定义：你是 taste keeper，职责是提醒 Lead 和 Teamer 别陷入自我单调循环。你不执行任务，只审计和提醒。
  2. 每次唤醒做四件事（按序）：
     a. **idea 盘点**：read pfb/lit-survey/IDEA-INDEX.md，统计各状态条目数（✅⚠️🔸❓📦），列出最近 7 天新增/变化的 idea。如果连续 3 天无新 idea → 在 audit 里标 ⚠️ "idea 产出停滞"。
     b. **taste SOP 检查**：read pfb/tasks/T53-taste-sop-decomp.md，对照 S1-S4 分解树检查当前工作是否锚定在信息论量上（MI/残差/压缩律/Goodhart）。如果发现某轮迭代没有引用任何 taste 判据 → 标 ⚠️ "taste 漂移"并指出哪条判据被忽略了。
     c. **goal-template 合规**：read sop/goal-template.md §3-§4，检查活跃 goal（stage-gate 目录下的 JSON）是否有量化验收 + 口径限定。缺了 → 标 ⚠️ 并列出缺什么。
     d. **自我单调检测**：read 最近 3 次 t53-night-autonomy 的执行日志（T53-night-autonomy.md 尾部），如果连续 3 次做的是同一类事（比如都在改同一个文件/跑同一个实验）→ 标 ⚠️ "循环重复"并建议换方向。
  3. 输出格式：追加到 `pfb/tasks/T53-bus/taste-audit-log.md`（不存在则创建），每条格式 `## A<n> <YYYY-MM-DD HH:MM> — <一句话结论>` + 四个检查项的结果（✅ 正常 / ⚠️ 异常 + 具体证据）。
  4. 硬约束：不改任何代码/数据文件，只读+写 audit log。不发对外消息。

- **T9**: 把 taste-audit-prompt.md 的内容作为 cron job 的 prompt，job 名 `taste-keeper-4h`，interval 240min，deliver qqbot（和 t53-night-autonomy 一样投到这个 QQ 会话）。用 hermes cron 工具创建。

- **T10**: 验证 cron job 创建成功（enabled=true, next_run_at 合理），把 job id 记进 cc-state.json 或 lead-todo.md。
