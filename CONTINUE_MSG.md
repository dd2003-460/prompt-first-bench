# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-31（r73）

**r73 M8 联合判读 Lead 盲法核验收口（上轮 P1「M8 Lead 盲法判读」项，已核销）**：R4 receipt next_actions 里最后一个非 blocked 可执行项。做法：判读前冻结判定规则 v1（精确匹配 + 注册语义等价表三组：备选/淘汰理由/预算表述变体），然后对 9 config × 4 run = 36 个工件独立重算冻结机会集覆盖（只看 run_key 编号不见配置名，聚合到配置层才揭名）。结果：36/36 run cover=1.000，与 r60 事后诊断回执交叉一致；语义等价救援 45 处命中全量留痕审计，跨配置均匀分布无独占；纯精确匹配敏感性检查下各配置差异 ≤0.05 排序不变。联合判读（M8-frozen-v1 口径首次正式产出）：B-nofreeze FAIL Δtruth=-0.350 全场最低（freeze 负效应最稳健）/ B-noevidence PASS +0.156 / B-noowner PASS +0.017 边际 / 其余单删双删 FAIL。盲法强度降级如实登记（本会话见过 r60 结论，价值在规则先行+全量重算+逐条留痕，严格盲法需第二人）。落盘 runs-r4/receipt-r4-lead-blind-joint-readout.json + goal-queue L78 补记。main @ r73 两 commit pushed。

**opportunity-set-freeze goal 至此机械层+判读层全闭环**，剩余未决仅 G1b 异源 judge（blocked-on-human，另立 goal T8-C3-v3-G1b-hetero-judge）。

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

0. ~~P0 · opportunity-set-freeze 定稿~~ → **已关闭（r62z 裁定 + r64 成璐二次确认 + r73 判读层收口）**：协议定稿、机械层+Lead 盲法联合判读全部落盘，无剩余动作
1. **P1 · G1b 异源 judge**（blocked-on-human/external，C3 v3 conf 升档唯一路径）：需非 Qwen 家族 LLM——arena 会话通道或用户提供第二 API key。协议与切分已冻结（loop-artifacts/stages/01/C3v3-G1-blind-label-design.md §2），凭证到位后 ~2 回合可跑完。每次唤醒先查一次 arena 通道是否恢复，无变化则跳过
2. **P1 · closure-gate-integration K4 O1-O4 裁定**（APPROVALS 卡人项）：等成璐裁定，无变化则跳过
3. **P2 · web-llm 三 provider 人工登录**（D1-gpu cross_validation_out 门禁依赖）：需用户在浏览器一次性登录，无变化则跳过
4. **P2 · R5.2-third-scorer 前置盘点**：packet v2 输入面已对称（assert-packet-symmetry 67 PASS），缺第三打分器（不同家族）——与 G1b 同族依赖，合并等待即可

**r62g2 v9 重跑确认**：v9 重新 sweep（36/36，0 failed），数值不变，sham gap +0.007 FAILED。至此 v7/v8/v9 三个 judge 都做了独立重跑验证，全部与 r62p 面板值一致。main @ 11a14c9。

**r62d2/r62e v7+v8 重跑确认**：v7 和 v8 各重新 sweep 一遍（36/36，0 failed）。v7 数值与 r62y 修正后完全一致（sham gap -0.250）；v8 数值不变（sham gap +0.099 FAILED）。两个 judge 的 receipt 都加了 rerun_confirmation 字段。main @ 249d14b。

**r62b 截断审计**：360 个判分输出中 4 个被模型截断（JSON 不完整），全部通过 regex fallback 纳入。v7/v8 的 B-2del-eo/D2/seedb + v10 的 A-full/D1/seedb + B-nofreeze/D2/seedb。无遗漏，十 judge 面板数据完整。main @ d4f1993。

**r62y 解析修正**：v7/B-2del-eo/D2/seedb 输出被截断（9032 chars，JSON 不完整），之前 parse fail 被排除。regex fallback 纳入后 B-2del-eo v7 mean 0.625→0.476。v10/A-full 从 1.000 修正为 0.758——sham gap 从 -0.177 变 +0.065，v10 实际 FAILS sham separation。干净分离 5→4 个（v3/v7/v11/v6）。freeze 负效应不变 7/10。main @ 77b3884。

**r62w rubric 设计迭代史**：design/rubric-design-history.md 落盘——v2→v11 十轮迭代的完整分析（核心机制/sham gap/freeze rank/判定 + 四阶段设计轨迹 + 为什么 v11 赢）。以后新 judge 版本可以直接对照这个文档定位自己在迭代链上的位置。main @ 65cc07e。

**r62u v7-v10 单独回执落盘**：从 r62p 十 judge 面板提取四个独立 receipt（v7/v8/v9/v10），每个版本一个文件方便按版本引用。现在 v2-v11 全部十个 judge 都有独立回执 + 合并面板。main @ ab93326。

**r62s v7 误杀率分析**：v7 echo-rate floor 在非 sham run 触发 2/32 (6.25%)，sham 零触发。floor 抓的是真实质量问题不是 sham——v7 的 sham 分离靠 item 级打分不靠 floor。v7 可作副判但需理解其机制。main @ edfc68f。

**r62p 十 judge 面板完整分析**：从磁盘解析全部 10 个 judge 版本（v2-v11）× 36 run = 360 判分。Sham 分离 5/10 成功（v3/v7/v11/v10/v6），freeze 负效应 7/10 确认。v11 仍是推荐主判，v7 是候选副判（sham gap -0.250 更强但需查误杀率）。matrix-10judge.md + receipt-10judge-panel-consolidated.json 落盘。main @ 197cb89。

**r62n J1v6 sweep + 六 judge 面板**：J1v6 (prepared-plan exception) 36/36 判完。A-full 0.810（修复 v5 过度修正），B-nofreeze rank 1/9（freeze 负效应 5/5 judges 确认），sham 分离 PARTIAL（mean gap -0.141 但 cell 级不一致）。六 judge 面板合并回执 receipt-6judge-panel-consolidated.json + matrix-6judge.md 落盘。v11 仍是唯一干净 sham 分离方案。main @ 57fd652。

**r62k 协议执行计划状态标注**：opportunity-set-freeze-protocol-draft-r57.md §四 四项逐条标状态——item2（opportunity-sets-v1.json）DONE r60；item4（matrix 口径列 + assert-m8-no-suffix.py）DONE r62g；item1（成璐裁定空分母口径 + cover 门槛）BLOCKED ON USER；item3（下一 run 新口径）BLOCKED ON USER（依赖 item1）。main @ 4211ab6。

**r62i v4 回执标注被取代**：receipt-j1v4-sweep-analysis.json 加 superseded_note，指向 r62d 五 judge 合并回执。避免后续读者误用 4-judge 子集当完整面板。main @ 76210c8。

**r62g 协议§四.4 机械层落地**：matrix-v11.md 加口径列（待下一 run 填充）+ assert-m8-no-suffix.py 创建并 PASS（M8 引用无版本后缀检查）。协议执行计划 4 项中第 4 项完成，剩余 1-3 项卡 P0 裁定。main @ 5dfb08e。

**r62d-e 五 judge 面板合并 + queue 收口**：receipt-5judge-panel-consolidated.json 落盘（9 config × 5 judge 完整矩阵）。后续报告口径确定：v11 主判 + v2 密度参照。queue L78 更新为五 judge 状态。当前自主工作全部收口，剩余 P0 卡人项不变（空分母口径 + cover 门槛数值）。bh-mass-spectrum subagent 仍在跑。main @ c5536ca。


**r62 J1v4 全量 sweep 收口（36/36, 0 failed）**：J1-strict-v4（anti-spin rule）跑完 R4 全部 9 config。结论与 r41 校准集验证一致：① anti-spin rule 对 sham 失守——sham 0.699 rank 5/9，反而高于 A-full 0.613（rank 3），配对差 D1 持平 0.0、D2 sham 反超 +0.17；根因是 sham 工件里编造的具体数字（Zapier $30/mo 之类）让「零数值断言」条件失效。② B-nofreeze 在第四个 judge 下仍 rank 1/9（0.393）——freeze 负效应现在被四个独立 rubric（v11/v2/v3/v4）全部确认，是整个 C3 v3 矩阵最稳健的发现。③ 四 judge 联合读数表落盘回执：sham 分离只有 v3（anti-template）成功但误杀 75%，v11 特异性指纹是唯一无副作用的解法（迭代终点）。main pushed。

**r61 cover 独立复算通过**：纯 Python 关键词匹配（无 LLM）重算 36 run cover，与原回执一致——全 config avg=1.0，唯一 miss=B-sham/D1/seedb O07（该 run 输出确实零次出现「淘汰」「理由」）。分母收缩否定结论经独立方法确认。main pushed。

**r60k-l 分母收缩结论撤回 + 限定语收回**：r57 的「B-noevidence 分母收缩 -25.5%」结论被 r60 cover 分析否定——根因是范畴错误（judge 条目数 ≠ 模型覆盖机会数；冻结集口径下分母固定，不存在收缩）。已同步修正四处：① m8-denominator-analysis-r57.json 补 r60_correction 节 ② 冻结协议草案 L38 标注否定 ③ queue L78 标注 ④ matrix-v11.md r57 节限定语部分收回（evidence/owner 方向恢复为「方向性证据」，不再带「未分离」限定语；freeze 负效应三 judge 下均 rank 1/9 最稳健）。main pushed。

**r60e 联合读数收口**：9 config × 4 口径（truth-v11 / cover / J1v2 / J1v3）全表落盘。关键发现：cover 在所有 9 个 config 下恒为 1.000（零方差）——冻结机会集对当前 D1/D2 域过宽松，每个 run 都覆盖了全部核验点，cover 维度没有区分力。含义：M8 双报 (truth, cover) 协议机械层就绪但经验上 vacuous，cover 门槛只在 cover<1.0 时激活，需要比当前 D1/D2 更难的任务才能触发。回执已更新。

**r60c J1v3 全量 sweep 收口（36/36, 0 failed）**：后台进程跑完 J1-strict-v3（anti-template rule）对 R4 全部 9 config × 2 domain × 2 seed 的判分。结论与 r41 单点验证一致并量化坐实：① anti-template rule 成功把 sham 从 A-full 附近拉开（v3 gap -0.477 vs v2 gap +0.045），核心验证目标达成；② 但对 local-reasoning 域过度触发——75% run 被标 template_suspect（含 1/4 A-full），3 个非 sham config 归零，区分度退化（v2 有 9 级 → v3 只有 5 级且 0.000 三方并列）；③ 根因确认：本实验模型无联网工具，「零外部证据」条件对所有工件恒真，judge 把结构差异当模板信号——这正是 r41 诊断、v4 起改 anti-spin 的原因；④ B-nofreeze 在三个 judge（v11/v2/v3）下都是 rank 1/9 或并列最低——freeze 负效应是整个 C3 v3 矩阵里最稳健的发现；⑤ B-noevidence 反转是 judge-dependent 的（v11 最高 0.906 → v3 跌到 0.219 rank 6），不是 config 的稳定属性。回执 receipt-j1v3-sweep-analysis.json。main pushed。

**r60 P0 推进：opportunity-set-freeze 机械层落地 + J1v2 第二口径交叉验证收口**。

**r60 P0 推进：opportunity-set-freeze 机械层落地 + J1v2 第二口径交叉验证收口**。① opportunity-sets-v1.json 落盘冻结（4 seed × 9-10 项/seed，机械规则 v0.3 + 人工补全层）+ receipt-r4-cover-analysis.json——cover 检查发现：**分母收缩假设被否定**（B-noevidence cover=1.000 与 A-full 持平，Δtruth=+0.156 不是分母 artifact），全部 36 run cover≥0.975 → 冻结集对当前两域任务过宽松、区分度不足；原处置表「evidence/owner 方向置信度下调」的限定语可部分收回。注意：本轮是事后诊断非正式冻结流程（Lead 盲法前置未执行，limitations 已登记）。② J1v2 density-audit rubric 全量 R4 sweep 完成（36 judged, 0 failed，后台进程）+ receipt-j1v2-sweep-analysis.json——四个结论：freeze 负效应跨 rubric 稳健（B-nofreeze 两版都是 rank 1/9，v2 下 gap 更大 0.475 vs 0.054）；B-noevidence 最高分跨 rubric 复现（非 v11 artifact）；J1v2 floor 机制零触发（空转工件条目本身不 pass，不满足联合条件）；**J1v2 对 sham 失守**（sham 编造数字喂饱 density 指标，sham 0.823 ≈ A-full 0.868，v11 特异性指纹查『数字是否对应真实核验对象』才是本质优势）。跨版本一致性 r≈0.02——同族 judge 换 rubric 文本判分近乎独立，再次坐实跨版本分数不可比。main pushed。

**P0 剩余（卡人项，等成璐一句话）**：裁定两项——① 空分母口径：模型完全没提到的核验点算不算进分母（我默认保守=算，激进=不算，建议保守）② cover 门槛数值：质量提升允许覆盖率下降多少还认账（我暂写 -5%，无文献依据纯建议值）。裁定后协议定稿，下一 run 起 M8 双报 (truth, cover) + 正式 Lead 盲法冻结流程生效。

**r57c-e 三项复核补强（已收口）**：① KeyError 'J1' 误报定位——旧 one-shot 脚本用错键名层级，与用户改动无关；G1a raw 10/10 机械复现对账通过。② F4 补测：judge 条目 8/8 ≤ run 输出显式断言（12-20 条），三层口径关系修正为题面(5-8) ⊂ run输出(12-20) ⊇ judge 条目。③ 判官区分度复核：R4 全部 52 run J1v11 stdev=0.229/range=0.9，有真实区分度——G1a 零分歧归因修正为校准集工件质量好（集合属性）；同族偏软残余边界仍需 G1b 异源定案。main @ a494277 pushed。

**r57 opportunity-set-freeze 草案落地（已收口）**：arena blocking fix #3 四要素协议草案 + R4 分母收缩量化（B-noevidence 8.38 vs A-full 11.25 条，-25.5%）+ matrix-v11 限定语回填。注：r60 cover 分析已否定分母收缩假设（见上）。main @ 15d94a6 pushed。

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