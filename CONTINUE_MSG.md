# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-11-02（keepalive r181 · R121 收口）

**RUBRIC-V3-R121-PAPER-COMPARE 全链路闭环**（main @ d8eb9a9 pushed）：arena 固定会话 01a195cb 的 arXiv 原文核验回执（receipts/r121-paper-compare-verification.md @ e71df31）此前只落盘未应用，本轮把建议 diff 逐行打进 AUDIT-report §4(a)——A3 refuted 落地（「2,500+ rubrics ≈ 2,800+ 人时」属 ResearchRubrics arXiv 2511.07685，非 ResearcherBench，实为 65 题 × 平均 14 条 ≈ 910 条）；B3 corrected（「双人评分」→ 3 专家/任务 + 事后一致性报告 PAR 71.33 / OPC 99.54）；B4 annotated（跨题可比性弱 = 本项目推断，原文主张相反）；A4 narrowed（适用域 → AI 领域 65 题细分）；重要性信号行附注 FACT 有显式权重但消融不显著 (+0.45)。§4(a) 事实源注记 unverified → 复核已完成（版本状态：三篇 arXiv 均仅 v1；DRB judge 2026-05-11 起 Gemini-2.5-Pro→GPT-5.5、FACT: GPT-5.4-mini；DRB II arXiv 2601.08536 已发布）。附录 B web-llm 限制声明加解除注记。revision-log R-23 登记；goal-queue R121 行 [x] 销账；assert-queue-lint exit 0（既有 3 FAIL 为历史遗留行）。

**下一步（下轮唤醒起点）**：① **erratum-27 口径裁定**（唯一真正卡人项，候成璐，不可代裁）② stop-hook stale-index 误报修复候裁（APPROVALS 条目 1，回 1a/1b 即改框架源码，改后告警归零）③ RV3G6-FULL-AUDIT-B2-FULL-FIX 与 R5.2-third-scorer κ=-1.50 联动需先定 γ/β 处置（设计级决策，候成璐）。r181 已销账 C3v3-G1a-ninfer-execution 重复行（:8787 通道实测存活 + G1a 校准 r36 早已完成 + R5 D3 @ 0265cc3 收口，paired runs 前置门禁全链闭合）。其余卡人项（G1b family_check 等 API key / κ 门禁标定 / K4 closure-gate / web-llm 登录 / RV3G1 歧义 cell×10）无变化则 [SILENT]。

**盲评双裁判评分已落盘并收口**：arena agent 完成 21 份 × 双裁判打分，cherry-pick 到 main（judge-{1,2}-scores.json + JUDGE-PROTOCOL.md + BLIND-EVAL-REPORT.md）。Lead 独立核验全过：JSON 合法、21 run_id 全覆盖无重复、O3 per-claim 数组长度=31 ×42 份、total_score 复算零 mismatch、max_score=38、值域 0/1/2。一致性：条目完全一致 389/399=97.5%、差≤1 100%、Cohen's κ（衡量去掉瞎蒙成分后两裁判真实一致程度，三档原值 pooled）=0.916。**关键限定**：两判由同一 agent 以预注册不同口径执行（J2 开判前声明更严字面判据、未回看 J1），一致率与 κ 不是独立评分者间信度，只能作判据严格度敏感性证据——真实 IRR 需第二独立 agent 重跑（并入 G1b family_check 卡人项）。变体序两判一致：V1-full(37.3) > V2-nocoverage(36.3/36.0) > V1-align(35.3/35.0) > V-sham/V3-sham(~34) > V3-noboundary(~33.5) > V0-baseline 垫底(26.0/25.3)，差距集中在 O1/O3/P4 三支。O3 结构性缺口：N-3.1 系 prefill FLOPs 建模 + N-2.2 调度子因子 21 份全 0 命中（系统性分歧，归因单列）。新发现：任务书内嵌匿名映射表 = 盲评泄漏，建议移入 anon-mapping.json。

**下一步（下轮唤醒起点）**：① 状态机越界异常已修复（r180c+：completed goal 索引回落，非真实故障）；② queue hygiene 完成 @ 2b561b0（三条已完成行漏翻修复）；③ 真实队首两个跨轮长活：**RUBRIC-V3-R121-PAPER-COMPARE**（对标 ResearcherBench/RACE 差异表的外部文献核验——调研/核验类，按外包规则派 arena 固定会话 01a195cb 查 arXiv 原文，优先级低但可启动）/ **C3v3-G1a-ninfer-execution**（需 :8000 本地 vLLM 通道在线，先探活再定）。两者均不在 keepalive 回合内启动执行，下轮按 runner 协议取其一推进。其他卡人项不变：G1b family_check / R121 / web-llm 登录。

## 历史状态 @ 2026-11-02（keepalive r177 · 盲评对账：agent 在跑，未重复派发）

**r176 派发实际已执行（修正上轮误判）**：ego-browser 打开固定会话 01a195cb（taskSpace 904）核验——r176 那条「双裁判盲评」消息 agent 已接收并在跑：13 次思考 + 12 次命令、已写 /tmp/feat.py 特征提取脚本（按 31 claim 的判别特征 grep 全 21 份答卷）、读完 A-C 九份、正读 D-G 十二份；composer 显示 **Stop generating 按钮 = 仍在生成中**。远端各分支暂无 `blind-eval/judge-{1,2}-scores.json`（arena 分支 tip 仍 fa59371）。**本轮动作 = 零派发**（最小执行：agent 在跑时重复发消息会污染上下文并浪费额度），只留观察。注意 agent 自述口径选择：按 TASK-blind-eval.md §评分要求 3 用 0/1/2 三档（judge-packet-template instructions 声称二值 0/1，两处冲突以任务书为准；NA 项不入分母，非 NA 19 项 → max_score=38；O3 item 分按覆盖率阈值 ≥2/3→2 / ≥1/3→1 / 否则 0）——Lead 收口核验时按此口径复算，κ 计算若需二值化再统一降档。

**下一步（下轮唤醒起点）**：① `git fetch origin && git ls-tree -r --name-only origin/arena/4a614e63-prompt-first-bench | grep -E "blind-eval/judge-[12]-scores"` 查两文件是否落盘 arena 分支；② 落盘 → cherry-pick 到 main → Lead 独立核验（JSON 合法 + 21 run_id 全覆盖无重复 + 非 NA 条目均有 evidence 定位 + O3 per-claim 数组长度=31）→ merge main push → **κ 计算**（条目层 Cohen's κ per-dimension + overall，0/1/2 口径先报原值，必要时二值化降档复算）+ 变体均值排序对照 pilot（DRAFT §3.1 第二步输入）→ BRIDGE-REPORT + queue RV3G7 行回填；③ 未落盘且 composer 仍是 Stop generating → 继续等（长任务 21 份 × 双裁判可能数小时），不重复派发；若 composer 恢复 Send message 但无产出 → 读会话最后输出判断截断/报错，按 SOP 补派或降级本地自答（conf−0.2）。其他卡人项不变：erratum-27 / G1b family_check / R121 / web-llm 登录。

## 历史状态 @ 2026-11-02（keepalive r165 · pilot 后分析收口）

**RV3G6-pilot-post-analysis 收口（main @ 831174c pushed）**：pilot-run 的全部剩余尾巴（MDE 反推 + R-05 合并规则输入）已兑现——① `ablation/pilot-matrix/pilot-post-analysis.json` 落盘：双判均值维度分重算（DRAFT 预注册公式，条目级二值分→维度分→总分全链路脚本可复现）+ 三组主对比配对 sd_d + n_pairs 反推（δ_min=0.1）+ 7×7 Spearman 矩阵 + |ρ|>0.8 簇候选；② DRAFT v2 §3.1「第二步 正式实验」行追加 r164 实测输入四注记（κ 处置/簇裁定挂起/n_pairs 方向性/天花板效应），预注册数值与权重表零触碰；③ revision-log R-21 登记。**关键数字**：变体均值 outcome V0 0.634 / V1-full 0.841 / V1-align 0.823（process 0.722/0.944/0.944）——候选集规则（D1/D2 段）信号在总分层成立且 V1-full≈V1-align（结构贡献与暗示贡献未分离，符合 B3 设计预期需更多样本）。主对比 V1full−V0：outcome Δ=+0.208(sd 0.094)、process Δ=+0.222(sd 0.096) → δ_min=0.1 下总分层 n≥8；最敏感维 O1 Δ=+0.556(sd 0.419) → **n≥139**（若 O1 保留为确认性维度，样本量由它决定）。|ρ|>0.8 实测簇 = {O1, O2, P4}（ρ(O2,P4)=1.0, ρ(O1,O2)=ρ(O1,P4)=0.854）——与预注册候选「O2+P4」部分重合但多出 O1，而 O1 是 R-05 指定的确认性主维度之一。

**下一步（下轮唤醒起点）**：① **新卡人项（本轮新增，最高优先）**：R-05 合并处置裁定——实测簇含确认性主维 O1，选项大致是 (a) O1 出簇降诊断（牺牲消融最敏感维的确认地位）/ (b) 簇整体探索化、确认性改选 O3+其他 / (c) 维持分开报只标共线风险——备料在 pilot-post-analysis.json `r05_decision_input`，等成璐一句话；裁定前正式实验维度结构视为未最终确认，不派 arena 跑正式矩阵。② **O3 P1 κ 回执已落盘（r165）**：arena(79) vs local(62) κ=0.537，分歧 19 cell 全单向（local 假阴性 ×18，与 G1b dual-rater 同一模式——本地逐字匹配口径系统性漏判），N-5.3 双判一致全 0（送分翻转获第二判者确认）。γ 语义 = SIGNAL + 人工裁决（不阻断）；分歧 cell 仲裁仍并入 G1b family-upgrade 等异族凭证。**G1b dual-rater κ 独立复算核对通过（r165 续）**：75 格对齐、κ=0.1345 与落盘回执一致，35 分歧全单向 0→1（local h1=6/8% vs arena h1=41/55%，本地判官系统性假阴性），分歧节点分布 N-1×17/N-3×13/N-5×5（对照总格数 N-1=29/N-3=27/N-5=7——N-1、N-3 近半数格子两判官不一致，是本地口径漏判重灾区）；复核件 rejudge-g1b/dual-rater/g1b-dual-rater-kappa-recalc.json @ main f23c428。**误差模式交叉验证完成（r165 再续）**：两组独立实验（G1b 75 格旧题面 + O3 P1 98 格 V0.1 题面）分歧全部同向 0→1 且 N-1/N-3 两族共现——本地判官假阴性跨数据集稳定，不是单次噪声；G1b N-5 侧 5/7 分歧 vs O3 N-5 零分歧（V0.1 删送分答案后该节点行为收敛，与 N-5.3 双判一致翻 0 自洽）；交叉验证件 dual-judge-error-pattern-crosscheck.json @ main 56ce104，queue G1b 行已回填。异族仲裁优先级坐实。**W5 黑名单提取统一排查收口（r165 三续 @ 13c4cbe）**：w5-blacklist-unified-scan.json——模式 A（gold-tree 数值黑名单动态提取）仅 assert-o3-claim-list.py + assert-hitmatrix-evidence.py 两处拷贝，文本级/行为级/合成变异测试（box-drawing 树体 = W5 bug 原触发形态）三重等价，无需改代码；模式 B（audit8-erratum/psf-freeze 静态错误值清单）不同类。两脚本回归 exit 0。遗留：双份拷贝漂移风险登记，抽公共模块建议开小 goal（最小执行原则本轮不做）。queue W5 行已划掉。③ 既有卡人项不变：erratum-27（APPROVALS 候裁）/ G1b family_check（等非 Qwen key，O3+G1b 两组分歧格仲裁都并在这条线）/ R121（低优先 unverified）/ web-llm 登录。④ 若上述全无解锁且无新 arena 产出 → [SILENT]。

## 历史状态 @ 2026-11-01（keepalive r164 · pilot-run 批次1 派发中）

**RV3G6-pilot-run 双判推进（judge A 落 main + 双判已派发）**：judge A（9 run 单判）产出已落 main——结构完整核验通过：9 run × 9 维（O1-O4 + O3_claims + P1-P4）× 29 条目/run，NA 项 7/run 正确（E5 + P1-E1/E2 + P2×3 + P3-E3），O3 claim 覆盖逐 run 13-23/31（A-r3 最低 13，B-r2 最高 23）。judge 双判任务书（tasks/TASK-judge-dual-pilot.md）+ 两包 packet（judge1 5 run / judge2 4 run，O3 claim 清单内嵌无需读仓库其他文件）已 push main @ 2e8f737。**judge 双判已派发 arena 同会话**（editor_len=614 验证后 Send，agent 运行中）——agent 先切分支到 main 最新内容，再逐包打分，产出 judge-results/judge1.json + judge2.json，每批 commit+push。
**下一步（下轮唤醒起点）**：① `git fetch && for b in $(git ls-remote origin 'refs/heads/*' | awk '{print $2}' | sed 's|refs/heads/||'); do git ls-tree -r --name-only "origin/$b" 2>/dev/null | grep -cE "judge-results/judge[12]"; done` 查 judge1.json + judge2.json 是否落盘 arena 分支；② 落盘 → cherry-pick 到 main → Lead 独立核验（两文件 JSON 合法 + 9 run_id 全覆盖无重复 + 非 NA 条目均有 evidence 定位）→ merge main → **κ 计算**（条目层二值，per-dimension Cohen's κ + overall）→ MDE 反推 n_pairs → 8×8 Spearman 相关矩阵 → BRIDGE-REPORT + queue 收口 [x]；③ **若 agent 已停但 judge-results 未落盘**（上次唤醒发现此状态）→ ego-browser 检查会话最后输出，判断是截断/报错/还在跑；若截断则补派剩余 run；若报错则读错误信息调整任务书重派。其他卡人项不变：erratum-27 / G1b family_check / R121。

**RV3G6-o3-claim-rejudge P1 执行 + 248 全量合并收口（main 9514a95 pushed）**：P1 98 cell（h_id_frozen=1，FM-1 假命中方向）四批 blind-packet 本地降级自答完成（arena 不可用 conf−0.2，单 judge 同族 S2 限定叠加生效）；P0(150)+P1(98) 按冻结 schema 合并 `rejudge/rejudge-results.json`（sha256_16=ba492a85856bac91），**assert-o3-claim-rejudge.py 从 SIGNAL blocked-on-external 转 PASS exit 0**——M1_full=197/248=0.7944 / M1_gold_strict=38/40=0.95 / M2_run_level=0/8，flip 51 逐格留痕（0→1 FM-2 漏判证据 ×15 / 1→0 FM-1 假命中证据 ×36）。关键发现：**N-5.3 cache_hit_rate 1→0 ×8 全 run 翻转**——与 V0.1-cache-ratio-removal 的 N-5.3 自发拆解验证方向一致，送分效应污染定量证据。queue L10/L78 回填（L78 补吸收声明，queue-lint FAIL 4→3，余下为 r159 前存量）。回执 receipt-rejudge-full-merge.json（sha256_16=8678d06c02168232）。诚实声明：单 judge 同族不构成 S2 闭环证据，跨家族重判待非 Qwen 凭证解锁（并入 G1b family-upgrade 等待项）。run4/N-1.2 evidence 逐字修复（markdown 加粗标记丢失，判定值未变）。

**下一步（下轮唤醒起点）**：pfb 自主可推进项再次清空（本轮 P1+合并是唯一剩余自主项，已收口），剩余全部 blocked-on-human/external：① G1b family_check 升级（等成璐给非 Qwen API key；消费方 = RV3G1 75 cell + 本批 248 cell 跨家族补打）② κ 门禁标定（等 kappa-u1k1 §4 勾选裁定；本批单判者 κ 不适用，多判者阶段激活后执行）③ K4 O1-O4 closure-gate 裁定 ④ web-llm 三 provider 人工登录 ⑤ R5.2-third-scorer（与①合并）⑥ RV3G1 歧义 cell ×10 标注口径裁定。**下轮先核对六项卡人项有无解锁，无变化则 [SILENT]。**

## 历史状态 @ 2026-11-01（r158）

**r158 三连收口**：① prompt-V0 B10 缺口登记（D3 表行，v3 共用题面口径 = 不含该段，main 17c78ad）。② R-12 落地——O2 层级必要条件机械化 + 层级主导计分 min(1, 0.1·n_L1+0.25·n_L2+0.5·n_L3+0.25·E4) + gold 命中正交化（G-hit 标签化/G-new 计分项），batch2 首项销账（main 4bad6ee）。③ RV3G1-semantic-rejudge 收口——75 cell 语义级独立重判补数（arena 不可用降级本地自答 conf −0.2，三层协议 A盲判/B锚点复核/C逐字仲裁）：**h=0 漏判方向 40/40 零翻转（S1 未覆盖方向首次有数字）**、h=1 复验 35/35、confirmed flip=0、歧义 cell×10 挂人工队列；负面发现：无锚点盲判对证据型节点系统性偏严（6/35），单通道不可用作结论（main 08df836）。七脚本回归全绿，冻结件零触碰。

**下一步（已被 r160 覆盖，见顶部）**：pfb 自主可推进项再次清空，剩余全部 blocked-on-human/external：① G1b family_check 升级（等成璐给非 Qwen API key；本轮新增消费方 = RV3G1 的 75 cell 跨家族补打，judge-input.json 可直接复用 ~11 次调用，并入此项等待）② κ 阈值标定（等 kappa-u1k1 §4 勾选裁定）③ K4 O1-O4 closure-gate 裁定 ④ web-llm 三 provider 人工登录 ⑤ R5.2-third-scorer（与①合并）⑥ **新卡人项**：RV3G1 歧义 cell ×10 的标注口径裁定（run 内结构化账本行的短片段算不算对节点的实质覆盖——如 run3/N-3.2.2 evidence「KV cache 8GB」是账本 NOW 行里的半句；裁定后改 hit-matrix 须开新文件+APPROVALS 登记）。arena 通道本轮实证不可用（ego lite 无 CDP 端口 + curl arena.ai 403），下轮若仍不可用别重试直接走降级阶梯。**下轮先核对六项卡人项有无解锁，无变化则 [SILENT]。**

## 历史状态 @ 2026-10-31（r75c）

**r75c market 双线全部收口**：① T4-R1 已收口——Lead 阶段 04.5 审核回执 pass 落盘 main 6b6804e，收口汇报 t4-r1-closure.md @ arena/e174c209 bbe2770；第 1 轮（事件信号定义核查）01→04.5 全链条闭环，主交付物 t4-event-signals.md 定稿，六项残余缺口登记为后续执行前门禁。② T3-R3 设计冻结收口——本轮走完 04 回执（main c5b9b35）→ A6 04.5 反方复核稿落地（c1f022d，agent 抓到「半正态」表述张力，裁定不构成实质矛盾）→ Lead 04.5 回执 pass（main 734d19b）→ A7 注入 → **冻结声明落地 b82d9da**（frozen:design, execution:blocked @ 2026-10-31T19:38:25Z，内容锚定 88030b6，三处 Lead 依据 hash 齐全），Lead 独立核验七项全 pass，收口记录 @ arena/a8c1fe6b 38424b9。D23-A M1-T2 R3 预注册设计正式冻结。

**下一步（下轮唤醒起点）**：market-alpha T3/T4 双线已收口，无 arena 待验收项。候选方向（按优先级）：① T5（regime game strategy）任务书派发——台账原计划「等 T3/T4 收口后开」，现已具备条件；② T3 回测执行授权评估——B6 门禁（PIT 引擎接入+八项违规检查）未销项，若推进需先接数据管道，属新工作流；③ pfb 侧 C3 v3 paired runs（WORK_QUEUE 最高优先未完成项，前置 G1 subagent 盲标+仲裁 → G2 judge 实测，ninfer HTTP :8000 直跑）。下轮先查各仓 git log 确认无遗漏产出，再定方向。

## 历史状态 @ 2026-10-31（r73）

**r73 M8 联合判读 Lead 盲法核验收口（上轮 P1「M8 Lead 盲法判读」项，已核销）**：R4 receipt next_actions 里最后一个非 blocked 可执行项。做法：判读前冻结判定规则 v1（精确匹配 + 注册语义等价表三组：备选/淘汰理由/预算表述变体），然后对 9 config × 4 run = 36 个工件独立重算冻结机会集覆盖（只看 run_key 编号不见配置名，聚合到配置层才揭名）。结果：36/36 run cover=1.000，与 r60 事后诊断回执交叉一致；语义等价救援 45 处命中全量留痕审计，跨配置均匀分布无独占；纯精确匹配敏感性检查下各配置差异 ≤0.05 排序不变。联合判读（M8-frozen-v1 口径首次正式产出）：B-nofreeze FAIL Δtruth=-0.350 全场最低（freeze 负效应最稳健）/ B-noevidence PASS +0.156 / B-noowner PASS +0.017 边际 / 其余单删双删 FAIL。盲法强度降级如实登记（本会话见过 r60 结论，价值在规则先行+全量重算+逐条留痕，严格盲法需第二人）。落盘 runs-r4/receipt-r4-lead-blind-joint-readout.json + goal-queue L78 补记。main @ r73 两 commit pushed。

**opportunity-set-freeze goal 至此机械层+判读层全闭环**。G1b 异源 judge 已于 r74 派发回收（arena 01a19104，PR #36 merge eb2a9a7，回执 g1b/receipt-g1b-hetero-judge-r74.md）：X5 阳性对照被异源 judge 独立抓到，κ=0.0 系天花板效应；残留 family_check=unknown（arena 不披露底层模型名），家族隔离 PARTIAL-CLOSED，升级需用户给明确非 Qwen API key（~5 次调用），非硬阻塞。

## 历史状态 @ 2026-10-31（r63）

**r63 m8-rebuild-r4 收口（上轮 P0 唯一不 blocked 可执行项，已核销）**：从 r4 三 run 的原始账本（run1 loop-state-r1.json chain_steps 9 步 / run2 A1-A7 / run3 S1-S7）机械重建 per-step「一次通过」严格口径账本——run1 6/9=66.7、run2 6/7=85.7、run3 6/7=85.7（unverified-inferred，队列登记边界兑现），加 run5 5/9=55.6（receipt 一手）成 n=4 配对。**Pearson r(M3,M8)=−0.121 / Spearman ρ=+0.150**——m8-proposal 预判 |r|∈[0.7,0.9] 未证实。比数值更有信息量的是负相关驱动机制：M8 把环境/通道降级（arena 不可用、外部 LLM 不可达）计进分母而 M3 不计，两个低 M8 的 run（run1/run5）全部由环境降级贡献、无一是生成质量失败 → 维持「并入 M3 作诊断子维度」结论，论点从『强共线稀释权重』修正为『口径不对称导致的环境噪声污染』；|r|=0.12<0.7 不触发调权压缩。落盘 m8-rebuild-r4-ledger.json + m8-m3-correlation-n4-r63.json + m8-proposal.md 回填段。main @ 39775e3 pushed。

**r62z2 rare-token-scan 消歧补记**：8×3 是矩阵维度不是硬件数（成璐发现）。main @ 0d8a985。

## r64 播报回执（2026-10-31，成璐微信 5 问 + P0 二次确认）

① **泄题检测**：你的「主数字+罕见随机 token」思路已落地为 `bench/rubric-v3/ablation/scripts/rare-token-scan.json`——从 gold-tree 抽具体数值 token（8.00x、594、1034 这类），排除题面已有的，扫全部 8 run 的 evidence。结果：唯一命中是 "3090"（RTX 3090 卡名，公开信息白名单），零真泄题。你发现的 8.00x vs 8×3 混淆已消歧落盘（r62z2/z3）：8×3 = hit-matrix 矩阵维度（8 run × 31 节点），不是硬件数；8.00x = N-2.1 duty_demand 弹性倍数（占空比变 1% → 总成本变 ~0.125%）。模型自搜的硬件集各 run 不同（7/6/2 种配置），无一致「8 种」。
② **隔离**：查了 Hermes cron 源码——job 有 `workdir` 字段（只设 cwd，软约束非沙箱），现有 14 个 job 全是 None。没有原生沙箱。建议先 workdir 软约束，需要硬隔离再上 macOS sandbox-exec profile（没动，等你一句话）。
③ **物理论文 subagent**：已派过 bh-mass-spectrum 任务 C（remnant_mf_pisn.py），跑了 2.5 小时耗尽迭代预算，只完成数据探索（每快照子晕行数验证），未写代码未提交。你随后说 pisn 取消了 → 核查全仓无书面取消记录，但旁证显示整条出图线 A/B/C 都卡在任务 D 后面从未启动。**不重派**，待你定：作废归档 or 维持现状。
④ **cron/stophook 同会话**：Hermes cron 无原生 session-reuse 字段（每次 fire 新会话）。最接近的是 `context_from`（注入另一 job 的上次输出）和 `attach_to_session`（投递镜像进会话 transcript，默认关）。实用等价方案 = CONTINUE_MSG.md 外部记忆（cron 读→干→写回），已在用，零风险不动框架。stophook 天然共享 gateway 会话上下文。
⑤ **P0 opportunity-set-freeze**：你「当然算分母了，考试不就是这样吗」= 保守空分母口径获直接背书。协议已补记（main @ 19f10fd），P0 彻底关闭。R5 执行 unblocked。

## 下一步（按优先级）

> r79（2026-11-01 keepalive 轮）更新。本轮完成 D3 harder domain 全链：设计冻结(4a364d3) → 18 run 执行 → J1 sweep + M8 cover 分析 → 主分析回执(0265cc3)。opportunity-set-freeze goal 销账。

0. **P1 · C3 v3 主分析残留卡人项**（不变）：#1 G1b family-upgrade（等成璐给非 Qwen API key，~5 次调用模板现成）/ #2 κ 阈值标定（等 kappa-u1k1 §4 勾选裁定）/ #3 严格盲法第二人 / #4 ~~harder domain~~ → **r79 DONE**（D3-hardware-purchase 落地，cover 门槛激活）。剩余三项仍卡人，agent 侧无可推进空间。
1. ~~P1 · r79 新发现待消费~~ → **r79b DONE（31aa8b5）**：matrix-v11.md 限定语已回填（freeze 效应 task-type-dependent，R4 结论适用范围收窄为开放选型类任务）。F4 B-none 悖论（cover=1.0 但 truth=0.125）证实 cover/truth 双维度独立，联合判读设计成立——已登记于 receipt-r5-mainanalysis.json findings。
2. **P2 · :8787 node 网关容量竞争根因评估**（cron 400 too large 元凶候选；本轮上下文正常未触发，继续观察）。
3. ~~维护债备忘~~ → **r157 DONE（b9402ce）**：assert-kappa-receipt.py DEFAULT_DIR 一层偏差已修——原值指向 ablation/ 子目录，kappa-receipt.json 实际在 bench/rubric-v3/ → 无参调用恒 FAIL ①。修正后 PASS + κ=0.0 SIGNAL（阈值未达，U-K1 人工裁决项不变）。materials §5 D2 补过时注记。APPROVALS.md 登记。十五脚本回归基线维持。
4. **r157 附加**（f9442eb + 3ece757）：G1a 完整性回执（raw↔summary 10/10 对账 + sha 锚点）+ G1b 三判器一致性矩阵（93/95 一致，X5 检测方向性确认）。G1b family_check 升级仍需外部输入（非 Qwen key / arena 模型身份），本回执不改变该阻塞状态。
5. **r157 附加**（rejudge 启发式基线）：248 cell 关键词匹配 vs 冻结 hit-matrix 78.2% 一致（FM-1=28, FM-2=26）。非有效 rejudge（协议 §6 要求 fresh-context LLM judge），仅供真实通道到来后对比参照。落盘 `rejudge/rejudge-results-heuristic-r157.json` + `receipt-rejudge-heuristic-baseline-r157.json` + `receipt-rejudge-leak-analysis-r157.json`（FM-1/FM-2 根因分析：结构性盲区定量说明）。
6. **r157 附加**（869f7e7）：三判器条目级一致性矩阵——G1a-J1 (qwen :8787) vs G1b-r1 (arena) vs G1b-r2 (本地 qwen)，95 shared items / 93 unanimous (97.9%)，2 分歧全在 X5（植入退化检测）：A1/X5 G1a=pass r1=pass r2=fail，P1/X5 G1a=pass r1=fail r2=fail。方向性确认：异源 judge 对植入退化更敏感，同源偏软。family_check 状态不变（r1 provider 身份未确认）。落盘 `calibration/receipt-crossjudge-consistency-r157.json`。
7. **r157 附加**（2e4a66e）：冻结 hit-matrix 共识结构分析——3 unanimous-yes (N-1.1/N-3.2.3/N-5.3)、12 unanimous-no（prompt 真正瓶颈：三项分解/故障建模/利用率因子/FLOP/MFU/带宽阈值）、16 split（rejudge 核心战场）。run 聚类：run2/run3 J=0.93、run6/run7 J=0.93 两紧密簇，run4/run8 J=0.29 离群。为真实 rejudge 通道到来后提供参照基线。落盘 `rejudge/receipt-hit-matrix-consensus-r157.json`。
8. **r157 附加**（a4a1f8e）：C3 v3 G1 门禁状态汇总——G1a COMPLETE（5 artifacts × 2 judges, integrity ALL OK）、G1b BLOCKED-ON-HUMAN（r1 arena provider unconfirmed, r2 local same-family）、κ=0.0 SIGNAL（threshold 0.6 not met, awaiting U-K1）、CALM NOT YET EXECUTED、G2-G5 NOT STARTED。落盘 `calibration/receipt-g1-gate-status-r157.json`。

**下轮唤醒协议**：先核对 APPROVALS.md「r76 卡人项状态汇总」有无解锁（G1b 非 Qwen key / κ 门禁勾选 / closure-gate K4 O1-O4 / web-llm 登录），有变化执行对应动作；无变化则 [SILENT]。

## 历史收口记录（旧「下一步」段归档 · r63 前快照）

**r44 rubric v11 validation PASS，T8-C3-v3-rubric-density-test 收口**：v2→v11 共 10 轮迭代——前 9 版全部 FAIL（v2 密度审计零触发 / v3 anti-template 误杀真实核验 A-full 归零 / v4 anti-spin 太弱 sham 编造数字绕过 / v5 计划发现二分过度修正全场归零 / v6 prepared-plan 例外救回 A-full / v7-v10 回声率·冻结痕迹·方法回声·指令依赖度均失效），**v11 特异性指纹测试**首次命中：查「量」不查「有无」——带具体数字/型号/字段/日期/阈值的句子占比 <0.2 判 low_specificity_fail。验收三项全过：sham 0.517 跌至第 2 低组 ✓ / freeze 方向保持（B-nofreeze 0.400 < A-full 0.750）✓ / 无过度修正（A-full > 0.4）✓。J2 lenient 同批重打 36 run 天花板复现（9/9 配置 mean=1.0）→ 佐证 G1a「M8 绑定 J1 strict」裁定。负面 ×1：B-2del-fo/D1/seeda 首判 max_tokens=4096 截断，输出纪律后缀+8192 重判落盘。回执 runs-r4/rubric-v11-validation.json + j2lenient-v11-validation.json；queue L28 划掉（3e9aa9b，assert-queue-lint 59 行 / 0 FAIL exit 0）。main @ 3e9aa9b。

**r27 收口验证完成（上轮 P0）**：claude (PID 22038) 已跑完 r155 全部阶段并退出——产物 commit f6be883+B063043+0ecb926 落于 main（环境漂移，HEAD 启动时已在 main，claude 按 CONTINUE_MSG 指令未 push 未宣告收口）；ralph/closure-gate-integration-r27 分支指向同一 tip，`git log main..branch` = 0 → **merge 幂等无需操作**。终态 blocked-on-human：closure-gate-integration 备料件齐（materials 六节 + 未激活 hook 原型 + 三出口沙盒实跑），待成璐对 K4 O1-O4 + 方案选择裁定（APPROVALS 条目 2026-10-31 已登记，queue L27 保持 `[ ]` blocked-on-human 不动）。

**r45 R4 主分析重启完成（上轮 P0）**：J1v11 口径 scorecard 重算落盘（judge-scorecard-v11.json，36 run 零解析错误）+ receipt-r4-mainanalysis.json——R1 gate PASS 推断层解除阻断。F1 方向仍负：B-nofreeze 配对差 -0.35（4 pair 中 3 负）是唯一稳定低于 A-full 的配置，与「freeze 贡献最大」假设一致；B-noevidence +0.156 删组件反高（该组件对 M8 判分无正向贡献）。F4：v11 vs 原 J1 平均位移 -0.358、12/36 run 位移 ≥0.5——rubric 换版是系统性重打分，跨版本分数不可直接比较。功效声明：n=4/cell、pstdev 0.10~0.37，只报描述统计不做显著性宣称。main @ a0a096c。

**r47 R4 收口 + C3 v3 结论定稿（上轮 P0）**：receipt-r4-execution.json gate_order 更新（R1 FAIL→PASS via v11 / R4 UNBLOCKED / M8 待 Lead 盲法）+ verdict 升级 PASS-with-caveat + next_actions 三条核销；queue L28 补核销注记（assert-queue-lint 59 行 / 0 FAIL）。C3 v3 阶段性结论：**描述层**——freeze 是唯一有负向主效应的组件（B-nofreeze 配对差 -0.35）、evidence 组件对 M8 判分无正向贡献（删了反而 +0.156）、sham 空转工件可被 v11 特异性指纹捕获；**推断层上限不变**——同族 judge（qwen3.8-27b）+ n=4/cell，conf 封顶在方向性证据，G1b 异源仍是升档唯一路径。main @ c379668。

## 历史收口记录

**r44 rubric v11 validation PASS**：v2→v11 共 10 轮迭代，前 9 版全部 FAIL，v11 特异性指纹测试首次命中（查「量」不查「有无」）。回执 runs-r4/rubric-v11-validation.json + j2lenient-v11-validation.json。main @ 3e9aa9b。

**r27 closure-gate-integration 收口验证**：claude r155 产物已含于 main（merge 幂等），终态 blocked-on-human 待 K4 O1-O4 裁定（APPROVALS 已登记）。

**r45 R4 主分析重启**：J1v11 scorecard 重算 + receipt-r4-mainanalysis.json；F4 坐实跨版本分数不可比。main @ a0a096c。

**r47 R4 收口 + C3 v3 结论定稿**：verdict PASS-with-caveat；freeze 唯一负向主效应、evidence 无正向贡献、sham 可被 v11 捕获；推断层上限不变（同族 judge + n=4/cell）。main @ c379668。

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续（r124 已在 02.5 工件标注 unverified）
- **ralph CLI 入口文件缺失**：`ralph-loop.md` 在工作树与 git 历史均无，web-llm 工具完全不可用 → 见 RV3B1-webllm-tool-fix
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ 036e17d（keepalive r26 queue L30 merge 状态澄清）；r143 (c0eba3b) 经 r26 验证已含于 main——CONTINUE_MSG 旧注记「未 merge」为过期信息，goal kappa-u1k1-execution 本身仍 blocked-on-human
- ralph/rv3g6-gmr-caliber-u3 @ 0ca6d30（收口分支，可删）
- 历史收口分支（r112-r123 系列，均可删）：ralph/rubric-v3-audit-g1..g5 / ralph/rv3g6-* 等
## r65 — 无条件停止门 + 压缩策略调整（2026-10-31）

成璐指令：① hook 改无条件——任何 stop 都唤醒，去掉"动过文件才触发"条件；② 会话绑定靠缓存复用，压缩本身当临时状态落盘。

已落地（可回滚，均有 CHENG-LU PATCH 注释标记）：
1. `~/.hermes/hermes-agent/agent/turn_stop_gates.py` `_pre_verify_nudge`：删掉 `_edited and` 前置条件 → pre_verify hook 现在对**所有回合结束**触发（纯聊天、无文件变更的回合也过门）。stop_hook.py 本来就是无条件 continue 逻辑，无需改。
2. `~/.hermes/config.yaml`：
   - `compression.threshold: 0.78125 → 0.90`（qwen3.8-27b 131K 窗口下触发点 ~104K→~118K tokens，尽量晚压保 prompt-cache 前缀命中）
   - `agent.max_turns: 60 → 150`（单 turn 内 API 调用上限，原来 60 次就强制收尾，现在允许长推）
3. 生效方式：gateway 下次重启加载新 config + 新源码。**当前正在跑的 gateway 进程还是旧代码**——重启会中断本会话，未获批准前不执行（红线：stop/restart hermes gateway 在 command_allowlist 里）。你回复"重启"我就干，或者等它自然重启。

机制说明（为什么这样就够）：
- 回合内：模型想停 → apply_stop_gates → pre_verify 无条件 fire → stop_hook 返回 continue + 注入消息 → 必须继续。唯一真停 = max_verify_nudges(999999) 耗尽或进程被杀。
- 跨回合/跨会话：keepalive cron 每 30min 唤醒新 session，读 CONTINUE_MSG.md + stage-gate 状态接力。压缩 = 把长上下文压成摘要留在同一 session（session_id 不变），不是开新会话；工作区落盘保证即使压缩丢了细节也能从文件重建。
