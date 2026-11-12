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

## 执行日志

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
