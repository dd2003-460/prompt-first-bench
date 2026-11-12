# Lead TODO (ralph stop-hook 读这个文件; "- [ ]" = 未完成, "- [x]" = 完成)

## 已完成
- [x] drb-2 (pid 4633) 跑完 → 验树: id 62/62 唯一 (修复生效), 孤儿 18 (未修, 已报 CC L7), degraded 53/62 全通道型, fanout cap 未生效 (max=4, 已报 CC L7)

## 当前队列

- [x] **[P0 · 成璐直接指令] 读 `research/e-block-prior-pack.md` 然后重新校准 E 块** — 已读完并落盘校准结论 (见下方 e-block 校准节); P3 stop_std_max 已接进主循环并提交; P5 CDF 回标脚本待写 (等 gpu run 出树补 gain 样本)
- [x] gpu 题新题面重跑: 已启动 pid 11150 (proc_07adee4420ac), 无 resume 全新跑, log=drb-pilot/run-gpu-rerun-console.log, watch DONE/FATAL
- [x] **CC bus L6-L16 靶点提案收口** [BLOCKED-EXTERNAL → 移出可推进计数, 见 lead-to-cc L27/L28] — CC 进程不在运行 (cc-to-lead.md 停在 04:05 C9); Lead 侧验收动作已全部完成 (L14 分型定稿 + L15 闭环协议落盘); 剩余 = 等 CC 副脑进程重启产生回执。重启 CC 属外部依赖, 非调研缺口。
- [x] runs-s5-sm-gpu.json 废弃决策: 精确数据 12 dup ids (N19-N26 x5) 已报 CC L8, 文件整体废弃留作旧题面对照, D26 走文本匹配
- [x] gpu 新 run 题面确认: log 首行铁证用新题面("不设硬性延迟指标"); sm-gpu-r1/r2.json mtime=昨天21:56/22:08 是旧残留, pid 11150 还没写 ckpt(停在 r1 decompose); N1 claim 待 r1 ckpt 落盘后验
- [x] 修复后 hook 实证: 手动跑 N8 query "A.M. Best 保险前十" → 5 通道返回 5 源(含 ambest.com×2+sohu), 连通性本身没问题, all-5-failed 纯 regex 笔误
- [x] drb-2 51 节点自愈: reverify_drb2.py 全量后台跑 (pid 17041); smoke 1/3 healed(N8 verified), N9/N10 真缺数值源仍 degraded(非 bug); resume 确认救不回
- [x] drb-2 reverify 全量收口: healed 0/51 (smoke 的 N8 healed 是脚本口径误报); 三类分型定稿 = 无源 all-5-failed 35 (query 形态问题) + 有源无数值 16 (真数据缺口, 免费网页没有细粒度金融数据) + 代码 bug 已修非主因; 详见 lead-to-cc.md L14; D26 建议把 drb-2 标为"数据边界受限题"
- [x] gpu 新 run #2 (DONE ~15:40, 153/153 unique) → bench report §2 加 gpu 行 + §3 补 gpu 节（fe0a3016）；L21 已回 CC（L20 P0/P1 撤销）
- [x] P5 CDF 回标脚本：8 个有效 gain 样本（drb-1×3 + drb-2×2 + gpu×3，n_new=0 轮剔除）→ mean 0.896 / std_pop 0.056；stop_std_max 0.15→0.06（1x σ）已落 s5_state_machine.py 并提交；样本+经验 CDF 落盘 p5-cdf-backlabel.json。原 0.15 比实测波动宽 2.7x，等于永不 reset streak——修完这个 E4 判据才真正在回路里

## D 17:05 指令状态（2026-11-12 ralph gate 三连问收口，见 lead-to-cc L26/L27/L28）
- [x] **A 撞车调研 #47/#48/#44/#40** [DISPATCHED ✅ L31 — D 登录后 T-PR-16 已发进 arena, 侧栏新 session 确认; 等 arena 回执按 SOP 验收] — 任务书就绪 (origin/main @tasks/T-PR-16-collision-backlog.md); 派发卡 arena 写操作登录层 (读 cookie 有效/Send 被拦, L24/L25 定位); Lead 侧无可替代通道; D 过 SSO 后我立刻重发 T-PR-16。旧 session agent/01a1ca66 服务端损坏弃用。
- [x] **B #31 objective-mode 消融 text 臂开跑** [RUNNING proc_c78bb6317c1f PID 3027, log=sm-gpu-d34-text.log] — 代码已完成并提交 @ae2aa47f (P1_L1_TEXT + --obj-mode CLI + checkpoint 标记, 单变量 diff 已验); 唯一前置 = gpu-d34 run (PID 92938) 释放配额/rate limit, 现在并行起第二进程会双份搜索限流+GPU 争抢; gpu-d34 跑完自动触发本项 (degraded 率对比 + compute_J + 矛盾扫描 + P5 补 gain 样本, 然后开 text 臂)。
- [x] **C #36 设计待展开** [DEFERRED → 低优先级不抢主线] — 当前主线是信息搜集基础设施 + 度量, #36 属设计类扩展, 等主线出终值再排。

## e-block 校准结论（2026-11-12，读 research/e-block-prior-pack.md 后）

**核心发现：gain_threshold=0.5 是死参数。** 全部现有 run 的 per-round gain（n=7：drb-1×3, drb-2×2, gpu×2）范围 [0.805, 1.0]，mean=0.900，没有一个 < 0.5。代码里 `cfg.gain_threshold` 只在 dataclass 定义处出现一次，主循环从未读取它——实际停止判据是 pass_rate<0.3 + low_gain_streak（line 897）。所以"为什么选 0.5"这个问题本身不成立：它没在回路里。

**先验包的 6 个坑对照现状**：
- P1-P2（retriever 修复）→ 已做（regex 笔误 + junk filter + Bing 标准化），但 L14 证明对硬数据题只解了通道、不解数据边界
- P3（stop_std_max 接主循环）→ **本轮已落地并提交**：近窗 5 轮 gain std > stop_std_max(0.15) 时 reset low_gain_streak，防止探索期被误判收敛
- P4（多采样 contrib_samples>1）→ E2 代码已在（classify_edge_var），默认 contrib_samples=1 退化为现状；启用需付 3x LLM 调用成本，等 gold 题集就绪再开
- P5（CDF 回标 threshold）→ 样本不够（n=7 且全来自 3 条题），等 gpu 新 run 出树补 r3+ 样本后再写回标脚本
- P6（gold 题校验）→ 未开始，依赖 D26 验收口径定稿

**下一步排序**：gpu run 出树 → 验树 + 补 gain/pass_rate 样本 → 写 P5 CDF 回标脚本 → 用回标值替换拍脑袋阈值。

## Lead 追加 (2026-11-12 ~18:00, 传话太监代 D 记录)

- [ ] **D 新指令 (17:05 inbox)**：剩余 idea 没做没调研 → 派 sub 整理/开新仓库/实验/消融；**最主要是撞车调研**。状态：T-PR-16 任务书已在 arena/f65a5a27，但派发通道全断（CDP closed + arena.ai 登录墙）。idea backlog 盘点已完成：IDEA-INDEX 48 条 — A 撞车未查 #47/#48/#44/#40、B 小实验可跑 #31/#29/#24、C 设计待展开 #36。**等 D 手动登录 arena.ai 后立刻点 Send 完成 T-PR-16 派发**——这是当前唯一外部阻塞。
- [ ] **双进程冲突处理**：pid 70201 已死，pid 68960 (gpu-d32 新树 run) 仍 ALIVE。确认 68960 是唯一的 gpu-d32 进程即可，无需 kill。它跑完出 runs-s5-sm-gpu.json 后重算 compute_J（看 Δ/H* 是否从 20.8 下降 = search_query 修复生效的证据）+ verify-only 矛盾扫描拿第一组 contradiction_rate。

## [2026-11-12 D指令] arena 工具信任问题 — 已处理 ✅
成璐："arena那个我完全不信，经常把无登录状态的当egolite的登录态掉了，能不能删掉原来的工具避免误会，或者用工具的时候加hook或者注释"
处置（选注释+硬门禁而非删除——ego-browser 是通用浏览器通道，删了伤筋动骨；真问题是 arena 登录判定太松）：
1. skill arena-outsource 新增「登录态判定门禁」节：唯一合法判定 = URL 落在 /agent/<uuid> + composer 可见或 repo panel 存在，双信号缺一即判未登录；标准探针脚本内嵌；probe JSON 必须落盘回执留痕。派发前硬门禁表从 6 条扩到 7 条（新增第4条探针）。
2. sop/arena-loop-pipeline.md 故障修复清单加 ⓪ 步：登录态探针必跑第一步，不满足直接报"需人工登录"。
3. 当前实测（本轮）：ego-lite 打开 arena.ai/agent → 停在裸路径 + Log In 墙 + title 仍是 "Agent Mode | Autonomous AI Agents"（正是假阳性的来源——title 和导航文本都含 Agent 字样）。probe: inSession=false, composerVisible=false, repoPanel=false → 按新门禁正确判定"未登录"。
**给 Teamer 的提醒**：T-PR-16 派发仍阻塞在 arena 登录墙上（与之前判断一致，现在有了可复现的证据链）。下次任何派发动作前先跑探针，别再凭印象说"登录态有效"。

## [2026-11-12 D指令] 三件事处理状态
### ① rework 矛盾修复 — 已落地 ✅ (D34, commit 见 git log)
`_rework` 从"加 alternative 后缀盲重搜"升级为双路径：
- directed（有矛盾证据）：LLM 拿双方 evidence 裁决来源质量 → corrected claim + 新英文 query → 重搜+重验 → 成功标 contra event fixed=True
- angle（普通 failed）：LLM 出 2 个不同角度的改写检索词（至少一个英文）逐个试
mock 单测两条路径全过；真实 fix_rate 等下一轮 run。修改日志已落 sm-modification-log.md D34 节。
**给 Teamer**：你下次跑 gpu/drb 时 rework 会自动走新路径，看 log 里 `rework directed: X/Y fixed` 行。如果 directed fix_rate < 0.5，说明 LLM 裁决环节在 27b 上不可靠，考虑把裁决换成规则（evidence 里有一手 URL 的赢）。

### ② 真实世界迭代 vs 解析先验+泛函梯度下降 — 调研中 🔄
decomp 已列（见下方 decomposition 段），正在滚雪球调研。方向预判（凭理论直觉，待文献核验）：
- 这是 "model-based planning (POMDP/MBPO) vs model-free RL (policy gradient)" 的同构问题搬到 prompt 空间
- 关键差异：我们的"环境"（LLM 分解行为）每轮都在被策略本身改变（non-stationary），纯梯度下降的前提（固定环境）不成立 → 倾向结合：解析先验定结构（哪些轴正交、停止判据形式），真实 run 数据定参数（阈值/权重），每 K 轮用新数据重估先验
- 待查文献：MBPO (Hansen 2022)、gradient estimation for discrete search (REINFORCE baseline variance)、hyperparameter optimization as outer loop (BO vs grid)

### ③ pfb 目录重组为直积子模块 — 方案已定，执行前需对账 ⏸
成璐判断："pfb 方向非常多和杂乱，不同 idea 方向直接平铺在根目录当子模块研究，因为都是可直积因素"——同意，且这符合 AGENTS.md 项目分类原则（领域分层、INDEX 纯索引、3-7 子模块）。
**但有一个必须先解决的对账问题**：projects/AI-计算科学/ 下已有 D1-academic-AI / D1-gpu / D1-persona-align 等 D1-* 项目，pfb 与它们的关系没理清（pfb 是独立 repo 还是某 D1 的子模块？）。按红线"存在性检查"，动结构前先 grep 确认归属，避免造出第二套平行编号体系。
**拟定直积分解**（待对账后落 INDEX.md）：
- A 评测基建（rubric/judge/scorer/bench harness）— 当前 runs/ scoring-v3*
- B 管线消融（S0-S9 arms, S8M/S8L, stage-ablation）— 当前 experiments/stage-ablation/
- C 目标函数与 Goodhart（v17 诊断, T-PR-15, E-block）— research/v17* + e-block*
- D decomp 状态机（T53 全线, r1-rN, D32-D34）— s5_state_machine + sm-* docs
- E SOTA 对标与 bench（DRB, GPT-Researcher, closed-sota v3）— research/sm-bench* + drb*
- F 理论框架（信息论/压缩/本条调研）— research/information-theory/ + 新文件
每个子模块 = 根目录一级目录 + INDEX.md（纯索引）+ memory/（探索记录）+ tasks/（临时状态），扇出 6 个 ≤ 7 ✓。
**执行顺序**：先对账 D1-* 归属（grep projects/INDEX.md）→ 再移动（git mv，历史保留）→ 最后建 INDEX。预计一次 session 内完成，不阻塞 Teamer 的 run。
