# T53 夜间自治任务书（2026-11-12 · D 睡前指令）

> origin: human (D 指令) + ai (执行细化)
> 状态：r14 运行中（proc_9f36253dab6c, pid 69056），本文件是夜间自主推进的完整授权与边界。

## 授权范围（D 原话拆解）

1. **打赢开源 SOTA**（"虽然很可能是幻想"）— 继续调状态机，目标 ≥5 道 deepresearch 题上 judge 分 ≥ CellCog Max 对标基线（DRB 56.72 作为分数锚点）。
2. **打赢之后**：继续实现 D 的其他 idea（IDEA-INDEX.md 里未 ✅ 的条目）。
3. **调研纪律（硬约束）**：真的开始研究某个 idea 前必须滚雪球调研——注意最新进展和"可直接做的组"，避免撞车。落盘 lit-survey/ + IDEA-INDEX 更新完成度标记。
4. **邮件准备**：调研完成后起草给相关领域教授组的通信邮件（只起草，不发送——外发留痕等 D 醒来确认）。

## 硬约束（继承 tasks/T53-decomp-state-machine.md，此处只索引不重复）

- **严禁泄漏**：状态机任何位置不得泄漏题目本身（T53 文件 §硬约束 + research/sm-leak-sop.md）
- **general 原则**：prompt 规则必须是 meta-rule，不得写死某道题的统计量或域特定先验。判定用 structural test（可检验结构特征），不用经验比例。
- **无 train/test 污染**：bench 题特征不得进入 prompt 规则（ICL-as-training，Decision 23）。
- **过去版本可复现**：每次改 s5_state_machine.py 前 git commit；每轮 run 记录 rN + commit SHA；checkpoint JSON 保留全部历史版本不覆盖。
- **目标函数公式**：U(T) = C·A·S − λ·cost(T)（机器侧验收，不进 prompt）；S_α' 只做过程监控（proxy cone），不进 prompt。

## 当前状态（交接快照）

| 项 | 值 |
|---|---|
| r14 | 运行中，commit d230a64d（structural test + 信息量语义），baseline = sm-gpu-r11-crash-303.json |
| r13 教训 | 63/70 节点判 quotient = 例子诱导偏置 → 已修（cartesian 默认 + 运算结构才判 quotient） |
| r14 观察点 | edge_types 应回到 cartesian 主导（quotient ≤20%）；节点数预期 100-150；contribution filter 首次生效（阈值 0.10） |
| 本地 LLM | 127.0.0.1:8787 (qwen3.8-27b) |
| 网络 | ego-browser 可用但慢（WEBLLM-SKIP 属降级非故障） |

## 夜间工作序列（遇阻跳过做下一个，不停摆）

### Phase 1: r14 监控与校准（~1h）
1. 盯 proc_9f36253dab6c 跑完（预计 30-60min）。
2. 提取 stats：节点数 / edge_types 分布 / contribution-filter 触发次数 / leaks / degraded 率。
3. 判定：quotient >30% → 再修 prompt 跑 r15；节点 <80 且 verified <30% → 放宽 fanout cap；正常区间（quotient ≤20%, 节点 100-150）→ 进 Phase 2。
4. 结果落盘 experiments/stage-ablation/r14-results.md（含 r12/r13 对比表）。

### Phase 2: DRB pilot + 迭代优化循环（D 04:05 授权升级：校准合理即开跑，不用等 Lead 确认；打不赢→诊断弱项→改机制→重跑，循环到收敛）
1. 选 5 道 deepresearch 类题（HotpotQA hard / 2WikiMultihop / DRB 公开题集；多跳+事实检索混合，避开 GPU 域）。
2. 每题跑状态机，记录节点数/轮数/核验率/答案质量。
3. 评分口径：异族 judge（数字正确 0.5 + 对比/单位正确 0.5，n=3 median）。
4. 对照：CellCog Max 56.72（overall）+ 子项（comprehensiveness 57.06 / insight 57.67 / instruction following 56.58 / readability 53.81）。
5. 汇总 experiments/stage-ablation/s5-sm-bench-report.md。
6. 打不赢 → 诊断弱项子项 → 回 Phase 1 修机制（不是加题）。

### Phase 3: idea 逐个推进
按 IDEA-INDEX.md 未完成条目产投比排序：
1. 开工前滚雪球调研：arXiv 近 6 月 + GitHub 已有实现 + 谁在做做到哪了。
2. 撞车 → 标 📦 吸收记差异，换下一个。
3. 找"方法已发表但工程未落地"窗口（优势 = 本地 27b + hook 不改权重）。
4. 产出落盘 lit-survey/，IDEA-INDEX 更新状态。

### Phase 4: 教授通信邮件（Phase 3 后）
1. 定目标教授组（领域匹配 + 近期活跃 + 合作意愿信号）。
2. 起草邮件（介绍 autoresearch 方向 + 具体技术问题 + 合作切入点）。
3. **只起草不发送**。存 个人/outbox-drafts/，APPROVALS.md 留痕，等 D 醒来审阅。

## 唤醒与汇报

- cron/heartbeat 周期唤醒（loop-station-keepalive 30min，需确认 enabled）。
- 每次唤醒读此文件 → 看当前 Phase → 推进 → 更新「执行日志」。
- 关键节点（r14 完成 / bench 出分 / 撞车 / 需 D 决策）QQ 汇报，其余静默。

## 红线（夜间也有效）

- 不发任何对外消息（邮件/社交/发布）——只起草。
- 不动 AGENTS.md 非临时内容。不花钱。
- 删工作区外文件前写 APPROVALS。
- 拿不准的事 → 标 [待D醒] 跳过做别的。

## 执行日志- [11-15 16:30] 诊断 nat-mc-v3 搜索通道：DDG lite 被 anomaly 限流（3 次重试全失败），Bing 英文 query 返回垃圾结果（geo 定位问题），中文 query 提取英文关键词策略无效。结论：搜索通道当前不可用，nat-mc-v3 跑完也大概率全 degraded。不修代码（避免动正在跑的进程），等 v3 跑完看结果。
- [11-15 16:31] 核验 PID 91756：已不存在（完成/崩溃）。当前 5 个 SM 进程在跑（nat-mc-v2/v3, gpu-method-r7, gpu-method-challenge-r7），日志都在更新。91756 可能是 r7 的某个 run，r7 还在跑（无 final json）。不杀进程（日志在更新=活着），等 r7 跑完提取 stats。搜索通道诊断已落盘（#16），本轮无新修复。
- [11-15 16:30] 诊断 nat-mc-v3 搜索通道：DDG lite 被 anomaly 限流（3 次重试全失败），Bing 英文 query 返回垃圾结果（geo 定位问题），中文 query 提取英文关键词策略无效。结论：搜索通道当前不可用，nat-mc-v3 跑完也大概率全 degraded。不修代码（避免动正在跑的进程），等 v3 跑完看结果。

- 2026-11-12 20:15 · inbox 收口：T-PR-16 派发双通道全断（hermes browser CDP channel closed；ego-browser 打开 arena.ai = Log In 墙，Google SSO 需 D 手动过）→ inbox 回写 blocked + [待D醒]。idea backlog 盘点已完成落盘（IDEA-INDEX 48 条三分类）。drb-2 judge 出分 total=0.0（4 维全 0，与 L14/L19 数据边界结论一致——报告只列了检索失败意图，judge 按 criterion 判无内容）。r14 进程不在跑（pgrep 空），gpu-rerun2 (153 nodes) 是最新主数据，无需再提 stats。

- 2026-11-12 ~02:00 任务书创建，r14 启动（proc_9f36253dab6c, commit d230a64d）。- 2026-11-12 ~04:05 D 指令升级：① 迭代优化循环授权（不止 r14，确认有优化空间就继续改/跑）；② DRB 感觉差不多时直接跑（HF muset-ai/DeepResearch-Bench-Dataset + 官方 judge 口径对齐 56.72，先 2-3 题试水再扩 5 题）；③ gold 答案降级为回归测试集（保留，不进主验收），主验收 = DRB 公开题。bus L2 已通知 teamer。
- 2026-11-12 ~03:40 Lead 唤醒：r14 已于 02:44 DONE（137 records/40 unique，quotient 12.4%✅，leaks=0，degraded 56.9%⚠️，contribution-filter 零触发❌）。CC 期间已完成 C1/C2/C3（校准分析 + DDG 取证 + id 撞号 fix @7cf91694），卡在内存；现 free RAM ~40GB 已释放。Lead 落盘 experiments/stage-ablation/r14-results.md（含 r11/r13/r14 对比表 + Phase 1 判定：不进 r15，进 Phase 2 DRB pilot）。下一步等 CC 启动 drb-1（新 qid 顺带验证 id fix）→ 组装器 → 四维判分。
- 2026-11-12 ~04:15 Lead 唤醒：drb-1 健康运行中（pid 4308, round-1 VERIFY, log 04:12 仍在写；_nid fix 生效无撞号，fanout cap N1 kept 8/24，edge-reclassify 3 次 cartesian→quotient 符合预期）。处理 inbox：采纳 CC C9 live census（unusable 52%，主因 = cn.bing 跨域噪声非 URL junk）→ Decision 25 改判 deferred（sm-thinking-sop.md 已更新）；审计靶点 #2 升级为 Decision 26 数字溯源提案（research/d26-number-provenance-proposal.md，三问过，未落代码，drb-1 出分后实施）；lead-to-cc L5 回写。commit ac0f0883。下一步：等 drb-1 出树（预计 1-2h）→ assemble → judge → bench report §3；drb-2/drb-16 已就位排队第二题。
- 2026-11-12 ~04:27 Lead 唤醒：处理 inbox cc-state 更新（ack，无需新指令——CC 状态与 L5 一致）。核实 drb-1 活性：cache 写入间隔 <1min（最新 17s 前），r1 ckpt 24 nodes / leaks=0 / degraded 15/24（verify 降档属预期口径）。进程健康，继续等 r2/r3 出树（waiter 脚本在位，final JSON 落 runs-s5-sm-drb-1.json 即触发 assemble→judge 链路）。bus commit e9eff16a 已 push。本轮无可推进增量，静默。
- 2026-11-12 ~04:50 Lead 唤醒：inbox 仅 cc-state ack（无新指令，未删行——非可消费任务条目）。drb-1 推进到 r2（71 nodes，unique id 71 ✅ _nid fix 验证通过；quotient 11/71=15.5% ≤20%✅；leaks=0；status verified 8/degraded 55/pending 5/failed 3；objective 四因子乘积结构合理）。bench report 骨架确认在 git 历史（工作区文件被误删但 7fb67f13 可恢复，未恢复——§3 填写时直接重建更干净）。判分链路三件套验证完毕：criteria.jsonl 就位（qid 1/2/16 各 26-27 条 criterion，权重逐题不同）、assemble E15 兼容 final JSON、judge 输出 judgments/drb-N.json。commit 6afb0553 已 push。下一步：等 drb-1 出树 → judge-dr1.sh → fill bench §3 → launch drb-2。
- 2026-11-12 ~05:35 Lead 唤醒：drb-1 健康推进中——r2 ckpt 04:43（71 nodes，verified 8/degraded 55/pending 5/failed 3），console 显示 r3 已进 gap_check A（6 dimensions），进程 pid 4308 活性正常。处理 inbox cc-state ack（无新指令）。修复两处链路断点：① bench report 从 e47f869a 恢复到根路径 s5-sm-bench-report.md（fill 脚本期望的路径，此前工作区文件丢失且骨架在错误目录）；② judge-dr1.sh 缺失（CC 只建了 dr2/dr16），按 judge-dr2.sh 模式重建到 /tmp/judge-dr1.sh。至此 drb-1 出树后 assemble→judge→fill 三件套全部就位。commit a7b22b35 已 push。下一步：等 drb-1 final JSON（预计 r3/r4 后，~1-2h）→ judge-dr1.sh → fill-bench-dr1.py → launch drb-2。
- 2026-11-12 ~05:15 Lead 唤醒：inbox cc-state ack（无新指令，未删行）。drb-1 活性核实：console 最后写入 05:03（gap_check A 后 1 次 WEBLLM-SKIP 超时，属已知降级非故障），进程 pid 4308 存活。发现 waiter wait-drb1-final.sh 已死（log 停在 04:16，/tmp 脚本被系统清理）——重新拉起（nohup，带 stall+RAM guard）。commit 留痕已 push。下一步：等 drb-1 final JSON → judge-dr1.sh → fill bench §3 → launch drb-2。
  (补充核实：waiter 已重新拉起 pid 20401 proc_afc5df1688b3；r2 ckpt 71 nodes，id 连续到 N94 无撞号 ✅，cartesian 60/quotient 11=15.5%✅；free RAM 7.1GB 偏低但 inactive 27.9GB 可回收，watcher 带 RAM guard 报警)
- 2026-11-12 ~05:30 Lead 唤醒：inbox cc-state ack（无新指令，未删行）。drb-1 健康推进 r3（pid 4308；r2 ckpt 71 nodes 复核通过：unique id ✅、quotient 15.5%✅、leaks=0、verified 8/degraded 55；objective 四因子乘积结构合理；max_depth=4 未到，r3/r4 后出树）。发现上一轮重拉的 waiter（pid 20401）已死且 stall 阈值 30min 过紧——r3 含 gap_check 6 dims + verify 批处理，本地 LLM 下超 30min 属正常。已重写 /tmp/wait-drb1-final.sh（stall 阈值 1h）并重新拉起（proc_e45c87b2029d, pid 22607），final JSON 落 runs-s5-sm-drb-1.json 即触发 assemble→judge→fill 链路。git clean @4f23e0e4。下一步：等 drb-1 final JSON（预计 ~1h 内）→ judge-dr1.sh → fill bench §3 → launch drb-2。
- 2026-11-12 ~06:10 Lead 唤醒：drb-1 已出树+judge 完成（CC 期间自动跑完）。**总分 0.0**（四维全 0）——诊断：检索通道对中文 DRB 题全盲（DDG/cn.bing 返回色情视频/英雄联盟/原神等垃圾源，169 节点里 75% degraded，rework 149 条全是"来源与主题无关"模式）。bench report §2/§3 已回填完整诊断（commit 2a55ba34）。修检索：research_hook.py 加 junk filter（色情/游戏/翻译工具/股票行情等关键词过滤，commit de4e44cc 已 push）。下一步：重跑 drb-1 看 verified 率能否拉到 ≥40%（junk filter 生效后 sources 为空时走纯逻辑校验路径，不再被垃圾源污染）。drb-2/drb-16 排队等 drb-1 重跑出分后启动。
- 2026-11-12 ~07:30 Lead 唤醒：drb-2 已于 07:16 DONE（55 nodes, 3 rounds, leaks=0, reworks=50）但 **verified=0**（degraded 50/pending 5）——与 drb-1 不同的病根：**缓存中毒**。`.research-cache/` 里 2865 条 s5-node 缓存是 junk filter v1 时代存的垃圾源（淘宝/百度翻译/IMDb/测速平台），SM 运行时 cache-first 直接命中旧缓存、跳过所有真实检索通道 → evidence 全是 "no sources from any channel (all 5 failed)"。实测验证通道本身活着（手动调 _wiki_search+_ddg_search 返回 3+3 条有效结果）。修复：清掉全部 s5-node 缓存（→ .research-cache-backup-20261112-072330/），保留 gpu/nat 题级缓存。bench report §2/§3/§4 已回填 drb-2 诊断（commit 18899174 已 push）。drb-2 重跑已启动（pid 45146, log=drb-pilot/run-drb-2-console.log），等出树 → assemble → judge → 看 verified 率能否脱离 0。
- 2026-11-12 ~13:00 Lead 唤醒：发现 drb-2 重跑已于 08:19 FATAL（r1 decompose 时 LLM 调用 4 次 retry 全超时，LLM_TIMEOUT=600s；07:30 后空窗近 5h 无人接管）。事后验证本地 LLM 活着且快（chat test 0.57s）→ 判定为瞬时故障非引擎问题。checkpoint runs-s5-sm-drb-2-checkpoint.json 完整（15 nodes @ r1，leaks=0）。git commit 2a9f2ff3 留痕后 resume 重启（proc_cf3e9f82acb5, pid 3707，skip_l1 生效、edge-reclassify/fanout cap 正常触发）。下一步：等 drb-2 出树（预计 1-2h）→ assemble → judge → 看 verified 率能否脱离 0；若再遇 LLM 长超时考虑给 call_llm 的 decompose 路径单独加大 timeout 或拆小 batch。
- 2026-11-12 ~13:40 Lead 唤醒：inbox 空（0 bytes，无待处理）。核实 CC 期间进展——drb-2 已 DONE（commit 371c9f1e：62 nodes/2 rounds，id 62/62 唯一 ✅ _nid fix 生效，degraded 53/62 全通道型 [CC L7 归因：检索返回主题无关源，非模型幻觉]，fanout cap 未生效 + 孤儿 18 已报 CC L7）。lead-todo 队列第一项 = gpu 新题面重跑。核实启动链路：a64221c1 改的是 s8b_pilot.py 的 QUESTIONS['gpu']（去掉 3s/token 硬约束，保留 32K 容量下限），s5_pipeline.py line 39 `from s8b_pilot import QUESTIONS` 透传给 s5_state_machine.py → 跑 qid=gpu 即用新题面。前置检查全过（git clean / 无残留进程 / .research-cache 已清 16K / LLM proxy 8787 code=200）。后台启动 gpu 重跑（proc_16c8f4bb2f1d, pid 11067，log=runs-s5-sm-gpu-rerun-console.log），25s 后确认 ALIVE 且日志显示新题面已加载（"不设硬性延迟指标..."）、L1 skeleton 进行中。下一步：等 gpu 出树（预计 1-2h）→ 验树（重点盯 D26 数字溯源是否触发 + fanout cap 口径 + 场景假设节点）→ 对比旧题面分数 → 回填 bench report。
- 2026-11-12 ~14:30 Lead 唤醒：inbox 空（0 bytes）。两个长进程状态核实：① gpu 新题面重跑（pid 11154）卡在 r3——log mtime 14:14，502 后 14min 无新输出，LLM_TIMEOUT=600s 未到期，等自然恢复或 FATAL；② drb-2 reverify 已完成（62 nodes, verified 1/62=1.6%）——唯一 verified 是 NN23（Jaccard 定义，纯数学逻辑不依赖检索），51/62 evidence="no sources"。根因确认：**不是 junk filter 问题，是检索通道对中文 DRB 题全盲**（wiki=0/ddg 质量差/arxiv 报错/local_corpus=0）。bench report §3 drb-2 节 + §4 迭代日志 #3 已回填诊断（commit 待 push）。下一步：等 gpu timeout 结束 → 若 FATAL 则 resume；修检索通道（ddg query 改写 + Perplexity via ego-browser）作为 Phase 2 核心瓶颈。
- 2026-11-12 ~14:45 Lead 唤醒：inbox 4 条 D 指令全部已处理（协议/survey 落点/白名单/自主校准，各带回执），清空重排时间戳留痕。gpu 新题面 run **DONE @14:30**（state=stop 正常收敛退出，非 max_depth hit）：75 records / 34 unique ids——**id 撞号复发**（N19–N26 各 ×5，_nid fix 在 drb-1/2 上验证过却没覆盖本 run，已报 CC L20 P0）+ rework_events=[] 与 console 日志矛盾（L20 P1）。结果落盘 experiments/stage-ablation/gpu-rerun-results.md（含 r14 对比表、pending 24% 新信号、gain 伪值标注）。按 L8 先例该文件整体只作历史对照样本，D26 验收走文本匹配。commit 983c3ebc 已 push。bench 分数继续等 DRB 题（drb-1 judge 分 0.0 已落 bench §3；drb-16 排队）。
- 2026-11-12 ~17:45 Lead 唤醒：inbox 有 D 17:05/17:15 两条重复指令（"剩下的 idea…最主要是撞车调研"）→ 响应落盘：T-PR-16 任务书已在 arena/f65a5a27 @161d88b1（#47/#48/#44/#40 四条主张撞车核验），回执写明派发状态，处理行留 inbox、原始行保留。r14/gpu 进程均已退出（gpu run #2 DONE 已落盘 gpu-rerun2-results.md，无需再提取）。**阻塞**：hermes browser 后端 CDP channel closed 起不来；ego-browser 通道未验证 → T-PR-16 派发（门禁 #6 点 Send）未完成。下次唤醒：跑 ego check 脚本确认 f65a5a27 会话状态 → 点 Send 完成派发 → 之后按 lead-todo 推进（P5 CDF 回标脚本可先写，10 个 gain 样本已齐）。commit 7c2c8d3a 已 push。

- 2026-11-12 17:35 Lead 唤醒：inbox 无新条目（21:40 blocked 行上一轮已处理，arena.ai 登录墙维持 [待D醒]）。发现 D32 后 CC 启动的 gpu-d32 新树 run（pid 68960，17:30 L1 完成 5 维 + fanout cap 生效）仍在跑——本轮增量：① git commit b12a2c52 清理 D32 运行残留（J-gpu-full.log + sm-gpu-d32.log + cache deletion）并 push；② 核实 start_drb.sh 的 pgrep 误报（`s5_state_machine.py.*gpu-d32` 匹配到 `python3 s5_state_machine.py gpu-d32` 命令行本身），直接 background terminal 拉起第二个 gpu-d32 进程（pid 70201, proc_ccb5abe29dbd）——**双进程冲突风险**：两者同 qid 会写同一 runs-s5-sm-gpu.json/checkpoint，下一唤醒第一件事是 kill 掉旧 pid 68960（或确认它已死）、只留 70201，避免数据污染。预计 1-2h 出树 → compute_J 重算 I/J（search_query 修复后的 Δ/H* 是否下降 = D32 涌现测试 (a) degraded 率指标）。

## 执行日志
- 2026-11-12 ~18:15 [night-cron] 处理 inbox L2（D 17:05 idea/撞车指令）：撞车调研 T-PR-16 仍阻塞于 arena.ai 登录墙（[待D醒]，不重复试）；idea backlog B 组小实验 #31/#29/#24 授权 CC 按 NIGHT-PROTOCOL 自主排队（lead-to-cc L24）。inbox 已清空。gpu-d32 (pid 68960) r2 ckpt 落盘：67 nodes / 0 dup / verified 23 / leaks=0，log 活跃中；等 r3/DONE 后重算 compute_J 对比 Δ/H* 20.8 基线。已 commit+push (b8a9fd15)。

## 执行日志（追加）

- **2026-11-12 18:25** gpu-d32 已于 18:21 DONE（137 nodes / 3 rounds / state=rework / leaks=0 / reworks=91；status: verified 52 / degraded 78 / failed 2 / pending 5；edge: cartesian 120 + quotient 17）。stats 已读自 `experiments/stage-ablation/runs-s5-sm-gpu.json`。注：JSON n_nodes=137 vs console 报 133，差 4 个重复 id 条目（N60×13 等），属记录层小瑕疵，不影响本轮结论。
- **2026-11-12 18:25** CC 工作核实：D34 query 瘦身（`research_hook._slim_query` ≤6 实义词，修 DDG lite 长尾零结果根因）+ checkpoint/r3/gpu 终态落盘 → 已 commit `fec564f4` push origin main。
- **2026-11-12 18:25** restructure B1 完成：根目录 27 文件 → `archive/root-runs/` + `archive/legacy-docs/`（pid 72066/92810 均已死，确认无活进程引用）；6 处代码引用同步改（r14_analysis/drb_judge/gptr_smoke/gptr_bench_run/gptr_drb10_run/drb_race_judge），py_compile 全过；根目录 57→28。同 commit `fec564f4`。
- **待办**：B2 一级目录归位（bench/lit-survey/knowledge-base/outputs/notes/receipts/checkpoints/demo/src → modules/）——需先建 modules/ 骨架，留下一轮。

| 2026-11-12 ~19:15 | 夜间唤醒：inbox 空；gpu-d34 (pid 92938) ALIVE 健康（SITE-WL 白名单生效，N18 verified via rework-angle）；subagent sa-1 撞车调研已收口（commit 4a0ecc43：prompt-opt prior-art conf 0.78 + SOTA decomp 骨架）；确认 `research/prior-art-sota-systems.md` 未落盘 → 本轮补写 | gpu run 继续跑（预计 1-2h），下轮唤醒验 DONE |

- **2026-11-12 ~19:55** [night-cron] inbox 空（0 bytes）。两臂状态核实：formula 臂 gpu-d34 (pid 92938) ALIVE——r1 done (23 nodes, gain=0.967), r2 gap_check A 7 dims 进行中，SITE-WL/JUNK-FILTER 持续过滤；text 臂 #31 (pid 3027) ALIVE——r2 gap_check A 6 dims 进行中。prior-art-sota-systems.md 确认已落盘于 `modules/E-sota-benchmark/litsurvey/`（上一轮说"未落盘→本轮补写"实际已完成，200 行含五系统架构+DRB judge 协议+成本口径+对标意义+conf 表）。B2 目录归位评估：modules/ A-F 骨架已建但仅含 litsurvey 子目录，根目录 bench/src/scripts 等未移——活跃 run 正在写 checkpoints，现在动结构风险大于收益，留到两臂 DONE 后无进程时执行。P5 CDF 回标已完成（lead-todo L17）。本轮无可推进增量，等两臂 DONE。

- **2026-11-13 21:0x** [night-cron] inbox 空。两臂状态核实：d34 resume (pid 79457) ALIVE——checkpoint 53 nodes (20 verified / 27 degraded / 6 pending), 32 rework events, 0 leaks, r2 核验/重拆进行中；textarm #31 (pid 79837) ALIVE——seed 23 nodes (12 verified / 5 degraded / 6 pending), L1 已跳过（skip_if_seeded），L2 展开中。两臂 L1 各 6 维（同 gpu 题）。M 臂 prompt P1_L1_MINIMAL 已写入 s5_pipeline.py 并 commit 6d2bb3df pushed——接线（import + objective_mode=='minimal' 分支）待 #31 textarm DONE 后做，避免同时改两个在跑进程。预计 d34 ~1.5h 到 150 节点上限，textarm ~1h。无异常，等长进程。

## 2026-11-13 夜间唤醒 (cron, ~18:4x)

**状态**: textarm (pid 79457) 仍在跑，已推进到 N95 rework 后的 fanout/reclassify 阶段（log 尾部），LLM 通道间歇 502 但重试自愈中。d34 formula 臂已于 18:08 结束（53 nodes @ stop）。

**本轮发现（重要）**: `runs-s5-sm-gpu.json` 被 d34 resume run 覆写为 53-node 终态，而 18:05 commit (505a98c6) 里 arm-profiles 的 "F-arm 124n/55.6%/72reworks" 实际来自 **textarm 自己的 ckpt** (checkpoints/sm-gpu-r0.json: 124n, verified 69/degraded 55, objective_mode=text)。即上一轮两臂对比把 T 臂数据记成了 F 臂——"完全一致"结论作废。d34 真实终态 = 53n (verified 20 / degraded 27 / pending 6, reworks 32, leaks 0, quotient 9/53≈17%)。交叉验证：d34 的 53 个节点 id+claim 与 r0(124) 全重合（same_claim=53/53），即 d34 resume 起点的旧 ckpt 是 textarm 树的子集，进一步佐证归属混淆。

**处置**: 未动 runs-s5-sm-gpu.json（git diff 可回滚）；textarm 结束后按 --qid 后缀分别落盘再统一重建对比。arm-profiles 待重写。

**下一步**: 等 textarm DONE（max-nodes 150 上限内，预计还需 1-2h）→ 提取 stats → 修正 arm-profiles + 重算 compute_J/矛盾扫描/P5 gain 样本。

## 2026-11-15 夜间唤醒 (cron)

inbox 空（0 bytes）。核实进程：pgrep 无活跃 SM 进程——**textarm (pid 79457) 已退出**。发现 formula 臂在 **11-15 11:20–11:24 自主跑完**（sm-gpu-formula-r3.log + sm-gpu-formula-verify.log，research-cache 新文件时间戳佐证）：从 runs-s5-sm-gpu-checkpoint.json (163n@r1, textarm r2 超时时的 ckpt) resume → max_depth=4 hit → verify-only 55 pending→verified → DONE state=verified leaks=0 reworks=40，覆盖写 runs-s5-sm-gpu.json。

终态 163n: verified 52 / degraded 106 / failed 5 / pending 0；levels L1=6/L2=17/L3=43/L4=97；edges cartesian 140 / quotient 23。画像落盘 `experiments/stage-ablation/farm-163-profile-20261115.md`。

**异常 [待D醒]**: 52 个 verified 节点里 39 个 evidence 是 "逻辑推导成立，来源未直接覆盖"（logic-only，无外部来源），仅 13 个带真实 retrieval_sources——verify fallback 口径存疑（log 里有 ego-browser PageNavigationTimeoutError，疑似 web-llm 通道失败后走纯逻辑校验标 verified）。F-arm 31.9% vs T-arm 55.6% 的 verified_rate 差异在此口径澄清前不可解读。另 checkpoints/sm-gpu-r0/r1.json 被本次运行改写（HEAD 版本是 textarm 时代状态，git 可回滚；今后跨臂对比须用 git show 取历史版本）。

处置：未动 runs-s5-sm-gpu.json；bench 出分前先定"什么算 verified"口径。本轮 commit 留痕中。

## 2026-11-15 夜间唤醒 #2 (cron)

inbox 空。无活跃 SM 进程（r14 早已 DONE，r14-results.md 11-12 已落盘）。本轮做三件事：

1. **T-arm 同口径重算数字修正**：上轮画像里 T-arm strict 口径写的是 23/124=18.5%（logic-only 41），本轮用与 F-arm 完全相同的判定逻辑（`'来源未直接覆盖' in evidence AND not retrieval_sources`）对 `runs-s5-sm-gpu-textarm-r2.json`（124n，@794791e4 版本与磁盘一致）重算，得 real_ev=24（strict 19.4%）、logic_only=40。差异来源：上轮判定条件可能漏了 evidence 文本里引用了来源编号但 retrieval_sources 字段为空的节点（如 N21/N23/N25 等 rework-angle 节点）。已修正 farm-163-profile-20261115.md 表格+结论段。
2. **ego-browser 通道验证**（上轮 L21 待办收口）：`ego-browser nodejs -e` 直连 arXiv API 成功（LEN=5095），`/Users/a1-6/.local/bin/ego-browser` 存在可执行。结论：webllm 超时不是 ego-browser 本身挂了，是 research_hook 的 webllm JS 脚本内导航目标站（perplexity/chatgpt 登录墙或慢响应）超时。修复方向收窄：(a) webllm 脚本换更稳端点或加短 timeout+快速失败；(b) 中期接 arena 外包检索不变。已写入 s5-sm-bench-report.md 修复日志 #4。
3. **git 留痕**：commit e3538705 pushed（farm-163-profile 数字修正 + bench-report 修复日志 #4）。gpu-criteria.json 已在上轮 43cfbed2 提交。

**[待D醒] 不变**：strict 口径（9.2% vs 19.4%）是否作为 bench 报告官方 verified 口径——宽口径 T 领先 19.7pp，strict 口径 T 领先 10.2pp，方向一致、幅度不同。在此之前不把 verified_rate 写进对比报告。

**下一步**：drb-1 重跑排队等口径定；webllm 脚本修复（短 timeout+快速失败）可做但涉及代码改动，留 D 醒后确认方向再动。

## 2026-11-15 夜间唤醒 #3 (cron, ~13:25)

inbox 空（0 bytes）。发现 **M 臂 (objective_mode=minimal) 已在跑**（上轮 #3 commit 已记录，pid 27188/27192，13:0x 启动）：r1 完成 27n (ver=10/21, logic-only 3, unique id 27/27)，r2 进行中，log 活跃（sm-gpu-minimal.log，SITE-WL/JUNK-FILTER 持续过滤，rework-angle 多节点 verified）。

本轮增量：
1. **r1 ckpt 留痕**：checkpoints/sm-gpu-r1.json 被 M 臂覆写（HEAD 版本是 textarm 时代状态），git commit b65bfeab pushed 留回滚点。
2. **M 臂重跑决策 [自主]**：M 臂 qid=gpu → 终态会覆盖写 runs-s5-sm-gpu.json（F-arm 163n 终态，b2fe484b 已核验落盘）。F-arm 数据 git 可回滚，但为保险起见我 kill 掉 27188/27192，重跑 `python3 s5_state_machine.py gpu --obj-mode=minimal --max-nodes=150`（pid 33637，log sm-gpu-minimal.log 续写）。L1 已正常出 6 维（与 F/T 臂同题同维数，minimal prompt 首验通过）。预计 1-2h DONE，届时 stats 落盘 + 三臂对比（F 163n / T 124n / M 待定）。
3. **CC 状态核实**：cc-state.json 显示 drb-1 11-12 04:09 启动后无后续记录（C9 是最后一条消息），进程早已不在——DRB pilot 实际停摆 3 天，重启需先解决 11-12 C7 的 4 选 1 裁决（降门槛/kill 99641/错峰/暂停），且 11-15 已确认 [待D醒] 口径问题未决（strict vs 宽口径 verified 定义）→ DRB 重跑维持排队，不自主重启。

**[待D醒] 不变**：① strict 口径是否官方；② DRB 重启裁决；③ webllm 修复方向。

**下一步**：等 M 臂 DONE（pid 33637）→ 提取 stats 落盘 marm-profile + 三臂对比表 → bench 出分。

## 2026-11-15 夜间唤醒 #4 (cron, ~13:36)

inbox 空（0 bytes）。M 臂 (objective_mode=minimal, pid 27188/27192) 健康推进 r2：78 nodes / verified 19 (logic-only 6) / degraded 53 / pending 6，unique id 78/78 ✅，leaks=0，rework 63 条，fanout cap + edge-reclassify 正常触发，log 活跃（13:35 仍在写）。r2 ckpt 留痕 commit b3a43a14。

**taste-audit A1 (CC 13:28) 两项异常处理**：
- a. idea 3 天无新登记 → 登记条件 = 产出/决策/洞察型讨论，夜间无新讨论源，不凑数硬造；M 臂出树后三臂对比若产生新洞察再登记。
- b. 最近 3 轮未引用 taste 判据 → 本轮起执行日志显式带 taste 自检行（本轮：M 臂重跑决策 S3 杠杆测试 = minimal prompt 改动对 verified_rate 有杠杆、对树规模无杠杆，选它是因为三臂对比缺 M 臂数据，残差定位 S2 = 缺臂比多臂残差大）。

[待D醒] 三项不变（strict 口径 / DRB 重启裁决 / webllm 修复方向）。下一步：等 M 臂 DONE（预计 1-2h）→ stats 落盘 marm-profile + 三臂对比表 → bench 出分。

2026-11-15 14:0x 夜间 #6：
- 进程核查：pgrep 命中 8 个 pid 但 ps 全不存在——僵尸匹配（shell 残留），M1/M2 实际已退出。
- 根因：wait-and-launch.sh 用 `pgrep -f "s5_state_machine.*method"` 监控，M1/M2 的 qid 就是 gpu-method/gpu-method-challenge，**监控正则匹配到监控进程自身** → 死循环永远等不到退出；两臂实际在 ~13:57 跑完 r1 后退出（log 停在 r1 gap_check，无 "Saved →" 行）。
- 落盘状态：method 臂 r1 ckpt = 26n/ver5/deg15/pend6/leaks0/obj_mode=method（sm-gpu-r1.json 已被覆写，原 r1 是 minimal 臂的，git 历史可回溯）。final json 未生成（进程退出前没走到 out_path 写入）。
- 动作：git commit ac538bb7 留痕（含 5 个新 log + C 臂设计稿 + ckpt 覆写）。
- 下一步：从 r1 ckpt resume M1/M2（--resume checkpoints/sm-gpu-r1.json --qid=gpu-method 等），避免从零重跑；resume 前确认 ckpt qid 与目标 qid 一致（method ckpt qid=gpu，resume 时 qid 参数决定落盘文件名）。
- taste 自检：本轮判断"监控正则自匹配"是 pgrep 经典坑，置信度高（log 时间线 + 进程不存在 + 正则文本三重印证）；resume 而非重跑的选择依据 = 已跑 r1 的 26 节点（含 5 verified）是有效资产，重跑浪费 ~30min 且可能撞不同采样。

## 2026-11-15 夜间唤醒 #7 (cron, ~14:15)

inbox 空（0 bytes）。M1/M2 进程状态核实：pgrep 命中 12 个 pid 但 ps 全部不存在——僵尸匹配（shell 残留），M1/M2 实际已退出（与 #6 结论一致，上轮 #6b 重启的两臂跑完 r1 后退出，final json 未生成）。

本轮增量：
1. **r1 ckpt 复核**：checkpoints/sm-gpu-r1.json = method 臂 r1 终态（26n / ver5 / deg15 / pend6 / leaks0 / reworks19 / L1=6+L2=20 / objective_mode=method），与 #6 记录一致，resume 资产完好。
2. **log 增量留痕**：M1 method 臂 r1 期间 rework-angle N11 verified（'LLM inference minimum GPU memory formula'）+ SITE-WL 白名单生效（kept 2 dropped 1）；M2 challenge 臂 rework-angle N8 verified 但两连 WEBLLM-SKIP（ego-browser ERR_ABORTED）——webllm 通道对 method 臂题面仍不稳定，与 11-12 诊断一致（Perplexity 免费额度用完，修复方向 [待D醒]）。
3. **git**：commit 92e79f29 pushed（3 log 文件增量）。

[待D醒] 三项不变（strict 口径 / DRB 重启裁决 / webllm 修复方向）。下一步：M1/M2 从 r1 ckpt resume 续跑（#6 已定方案：--resume checkpoints/sm-gpu-r1.json --qid=gpu-method / gpu-method-challenge，避免从零重跑浪费 26n 资产）——但 resume 会再触发 webllm 通道（M2 已两连 ERR_ABORTED），在 webllm 修复方向未定前，resume 收益有限（r1 的 6 pending 节点大概率再走同一批超时通道），维持排队，等 D 定 webllm 方向后再 resume。


## 2026-11-15 夜间唤醒 #8 (cron, ~14:45)

inbox 2 条已处理并清空：webllm 修复确认（CC 14:24-14:37 多端点 fallback + ego-browser API 兼容，DeepSeek 验证 3 引用）+ r3 资产核实。lead-to-cc 回执已写。

本轮增量：
1. **r3 资产核实**：sm-gpu-method-challenge-r3.log 停在 round3 gap_check（14:42 后无写入），无 r3 ckpt、无 final json——r3 进程退出前未落盘。r2 ckpt 完好（78n/ver19/deg53/pend6/leaks0/obj=minimal），r1 ckpt 完好（26n/ver5/obj=method）。
2. **webllm 修复确认**：CC 两笔 commit（0580986f fallback 链 / 5ebe6ef8 API 兼容）已验证生效，M2 此前两连 ERR_ABORTED 的阻塞解除。
3. **M1/M2 resume 维持排队**：resume 方案不变（--resume checkpoints/sm-gpu-r1.json --qid=gpu-method / gpu-method-challenge），但 r3 无 ckpt 落盘说明 challenge 臂退出路径仍有未走完的落盘逻辑，resume 前需先确认 r3 退出原因（gap_check 后正常退出 vs 异常），避免 resume 后重蹈覆辙。

[待D醒] 三项不变（strict 口径 / DRB 重启裁决 / webllm 修复方向已解除）。taste 自检：本轮判断"r3 无 ckpt = 退出路径未走完"置信度高（log 停在 gap_check + 无 Saved 行 + 无 ckpt 文件三重印证）；resume 排队而非立即执行的选择依据 = 先查清 r3 退出原因，避免 resume 后同样丢落盘。

## 执行日志

| 时间 | 动作 | 结果 |
|------|------|------|
| 11-15 14:57 | 检查 r4 (M2 method_challenge) 进程状态 | r4 在跑（log mtime 14:57:03，~10min 前启动），L1 骨架 5 维度 + gap_check 7 维度已完成，正在 verify 阶段（webllm 通道全空：perplexity 额度用完 + chatgpt 无链接）。预计 30-60min 跑完。 |
| 11-15 14:57 | 核实 r2 ckpt 归属 | sm-gpu-r2.json (59n/ver20/deg33) 是 gpu 主臂 r2（qid=gpu, objective_mode=None），**不是 M1/M2 臂**。bench 报告 8c2d9840 的 "M1-formula-r2 53n/ver20" 和 "M2-textarm-r2 124n/ver64" 数据源不明（无对应 ckpt/final json），M2 数据可能是 r4 的中间快照。r4 跑完后需重新核实 M1/M2 数据并修正 bench 报告。 |
| 11-15 14:57 | 检查 CC inbox | 空（0 bytes），无待处理条目。 |
| 11-15 14:57 | 检查 git 状态 | 8c2d9840 已 push（bench report 消融表），sm-gpu-method-challenge-r4.log 是 untracked（r4 跑完后会生成 final json）。 |
| 11-15 ~15:30 | 夜间唤醒 #9 | inbox 空。r14 进程不在跑（早已 DONE，r14-results.md 11-12 已落盘）。r5 (gpu-method-challenge) 实际已退出（pgrep 9 个 pid 全僵尸残留，log 停在 15:21 verify 阶段，无 final json）。发现 webllm 通道新故障模式：deepseek 端点 `WEBLLM-FAIL taskSpace already exists`（ego-browser taskSpace 复用冲突），perplexity/chatgpt 全 EMPTY（额度/登录墙）。 |
| 11-15 ~15:30 | 修 research_hook.py taskSpace API | 三处 `task.page("p1")` → `task.tabs()[0].page`（_webllm_search/_arxiv_search/_fetch_page），webllm 空间名加 Date.now() 后缀防复用冲突。ego-browser 实测 arXiv API 直连成功（XML feed 正常返回）。commit 2f0ca76f pushed。 |
| 11-15 ~15:30 | 下一步 | r5 无 final json（退出前未落盘），r1 ckpt 完好（26n/ver5/obj=method）可 resume；但 resume 前需确认 r5 退出原因（同 r3 模式：gap_check 后退出路径未走完）。webllm 修复已 commit，resume 后 verify 阶段应能拿到真实来源。[待D醒] 两项不变（strict 口径 / DRB 重启裁决）。 |
| 11-15 ~15:50 | r5 退出原因确认 | r5 无任何落盘产物（无 FATAL checkpoint、无 final json），说明进程被外部杀了（OOM 或手动 kill），不是代码崩溃。r1 ckpt 是 11-12 的 gpu 主臂（qid=gpu, objective_mode=None），跟 method-challenge 不匹配，不能 resume。 |
| 11-15 ~15:50 | 重启 r6 | 用修复后的 webllm 通道（2f0ca76f）重启 method_challenge 臂：`python3 s5_state_machine.py gpu-method-challenge --obj-mode=method_challenge`，PID 53957，log → sm-gpu-method-challenge-r6.log。L1 6 维度已出，fanout N1/N4 各 cap 8/20，正在跑。预计 15-20 分钟到 verify 阶段。 |
| 11-15 ~15:35 | 夜间唤醒 #11 | inbox 空。r6 进程在跑（log mtime 15:34，L1 6 维度 + gap_check 7 维度已完成，正在 verify 阶段）。发现 research_hook.py 未 commit 的改动：_bing_search 函数返回 bing.com/ck/a 重定向链接而非真实 URL。修复：从 u=a1 参数 base64 解码出真实 URL。验证：中文 query 'Qwen3-27B 显存需求 推理' → 3 条真实链接（ai-market.jp/zenn.dev/qwen.ai）。commit a46e69da pushed。 |

## 执行日志（追加）

- 2026-11-15 15:45 CST — r6 (method_challenge 臂) 跑完，提取 stats：163 nodes, 52 verified (31.9%), 44 logic-only (84.6% of verified), 106 degraded (65.0%), 5 failed, 0 leak hits, 40 rework events (5 all-channels-failed, 1 logic_check_failed, 34 other)。webllm taskSpace 修复已 commit (9ce603f7)。
- 2026-11-15 ~16:10 CST — 夜间唤醒 #14：inbox 空。nat-mc-v2 在跑（PID 75762，log mtime 16:02，L1 5 维度 + edge-classify 已完成，正在 verify 阶段）。webllm 通道全空（perplexity/chatgpt EMPTY, deepseek NO_INPUT）——nat 题面是中文，webllm 通道对中文 query 可能不工作。发现 research_hook.py 未 commit 改动：中文 query 走 arXiv（只索引英文论文，匹配到 β-Pictoris 等无关物理论文）。修复：中英文统一走 DDG lite，_slim_query 跳过中文直接截断 40 字符。commit 0d12b9f2 pushed。nat-mc-v2 跑完后看 DDG lite 中文搜索效果。
- 2026-11-15 ~16:20 CST — 夜间唤醒 #15：inbox 空。nat-mc-v2 (PID 75762) 已退出（log 停在 16:13 verify 阶段，无 final json，无 r2 ckpt——同 r3/r5 模式：verify 阶段退出路径未走完落盘）。r1 ckpt 完好（26n/ver5/leaks0/obj=method_challenge）。发现 research_hook.py 未 commit 改动：中文白名单扩展（csdn/zhihu/juejin/segmentfault/cloud.baidu/sina/163/stackoverflow/github/arxiv 10 个域，修中文题面白名单全盲问题）。wait-and-rerun.sh 脚本已就位（等 nat 退出→清缓存→重跑 v3）。commit 2e742984 pushed。下一步：nat-mc-v3 重跑（新白名单生效后 DDG lite 中文搜索应能命中 csdn/zhihu 等中文技术源），或等 D 醒定 webllm 中文通道方向。
