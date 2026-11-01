# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-11-01（r156）

**r156 文档同步收口**：keepalive 快照里的「新发现·遗留工作 #1 独立 judge 盲测 p̃」核实为误报——该盲测 r73 已执行且裁定早已落 bench.md L104（W3 top-5 构念效度 1/5 → pass=false，跨 judge ρ=0.688，surprisal 权重方案含 W3 不进正式 rubric，负结果记录），只是 DRAFT v2 O3 消融证据段没同步。本轮补记该 bullet 并挂接 R-06 experimental 声明 + revision-log R-17 登记，main `7036773`；冻结数据零触碰，三断言回归（w2/w3w4/gmr）全 exit 0。

**下一步（下轮唤醒起点）**：pfb 侧自主可推进项基本清空，剩余全部 blocked-on-human/external：① G1b family_check 升级（等成璐给非 Qwen API key，~5 次调用）② κ 阈值标定（等 kappa-u1k1 §4 勾选裁定）③ K4 O1-O4 closure-gate 裁定 ④ web-llm 三 provider 人工登录 ⑤ R5.2-third-scorer（与 ① 同族依赖合并等待）。market-alpha T5 设计线 R1/R2/R3 全收口（R3 预注册已冻结 5facff2），回测执行需 Lead 另轮授权。**下轮先核对五项卡人项有无解锁，无变化则做可逆维护或 [SILENT]。**

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

> r78（2026-11-01 keepalive 轮）更新。上步核实：r74 G1b arena 通道已收口（PARTIAL-PASS，family_check unknown），queue L25 family-upgrade 未推进且 agent 侧不可解锁——本轮做了本地低成本补数据点（g1b-r2，commits 5d8f571+6cf6627）。

0. **P1 · C3 v3 paired runs** → 全链八环回执完整（receipt-c3v3-final-consolidation-r76.md），最终结论 freeze 负效应最稳健（Δtruth −0.350）/ evidence 正向（+0.156）/ owner 中性，四条硬限定语不变。**r78 新增数据点**：本地 qwen 实例盲评同批 5 工件（hetero-judge-results-r2.json + receipt-g1b-r2-local-judge.md）——X5 敏感度三判器交叉验证成立（A1/X5 仅 r2 抓到、P1/X5 三方全抓），但 judge 自报同族 ⇒ family_check 仍 unknown，R5 维持 PARTIAL-CLOSED。剩余卡人项不变：**#1 G1b family-upgrade（等成璐给非 Qwen API key 或 arena 披露模型身份，~5 次调用，重打模板现成）/ #2 κ 阈值标定（等 kappa-u1k1 §4 勾选裁定）/ #3 严格盲法第二人 / #4 harder domain**。agent 侧无可推进空间，下轮唤醒直接跳到 P2。
1. ~~P1 · market-alpha 双线验收~~ → r76/r77 收口（T4-R1/T3-R3/T5-R1/R2 全 pass，T5-R3 预注册冻结 5facff2）。回测执行需 Lead 另轮授权。
2. ~~P2 · 回 arena 会话 01a18567 取 307 行 survey 原文~~ → **r78 核实为误报已销账**：r48 (c241a8f) 已从 origin/arena/78602cd5 tip 5a525c7 取回 308 行全文回填 main，回执 tasks/receipts/arena-lit-survey-r51-failed.md L10 已标 DONE——本条是 r76 盘点时的陈旧残留。
3. **P2 · :8787 node 网关容量竞争根因评估**（cron 400 too large 元凶候选；本轮上下文正常未触发，继续观察）。
4. **维护债备忘**（assert-baseline-audit-r76 登记，未动）：assert-kappa-receipt.py DEFAULT_DIR=ablation/ 与回执实际位置 bench/rubric-v3/ 一层偏差——下次动 rubric-v3 面时顺手二选一修复（挪文件 or 改默认目录），勿单独开 commit。

**下轮唤醒协议**：先核对 APPROVALS.md「r76 卡人项状态汇总」五项有无解锁（G1b 非 Qwen key / κ 门禁勾选 / closure-gate K4 O1-O4 / web-llm 登录 / queue 排版归一），有变化执行对应动作；无变化则做可逆维护或 [SILENT]。

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
