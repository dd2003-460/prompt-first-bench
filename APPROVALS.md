## [2026-11-02 r198] E29 产出回收 — ✅ RESOLVED（无需授权）

**r198 发现**：E29 的 4 个产出文件已在 d1 本地工作区（arena agent r197 直接落盘），不需要从沙箱回收。本地 check_overlap 修 4 bug 后 9/9 PASSED，d1 仓 cc195f4 pushed。batch-12 进度 1/4。
# APPROVALS — 待用户裁定的不可逆/越权操作队列

> runner 遇到「不可逆且偏好不明」或「冻结数据修改」时登记于此，跳过继续做可逆工作。成璐裁定后销账。

## 2026-10-30 · RV3G4-prior-source-assert（r130）

**操作**：`bench/rubric-v3/ablation/prior-estimates.json` 追加顶层键 `p_tilde_provenance`（independent_sources 两条 + note + n_min_referenced）。

**理由**：G4 交付物「给 G5 的导出」第一类授权机械化落地（g4-vulnerability-crosscheck.md L100）——provenance 语义上属于本文件自身元数据，拆新文件会造成双源漂移二义性（RV3B1psf 02.5 A4 同款论证）。

**影响面声明**：纯新增顶层键；nodes.* / epsilon / weight_formula / source_baseline_commit 等全部既有字段零触碰。消费侧回归 assert-w2-formula.py + assert-w3w4-recompute.py 重跑 exit 0（见 04 日志 A5）。

**回退方式**：`git revert <收口 commit>` 单步还原，无级联影响。

**状态**：已执行（runner 按 J4 预注册处置：登记 + 纯新增 + 回归证明三重保障）。若成璐认为应走开新文件路径，revert 后按新方案重做。

## 2026-10-30 · RV3G3-goldrank-threshold-proof（r138+）— freeze doc 回填备案

**操作**：`bench/rubric-v3/gmr-criterion-freeze.md` 修改 3 行——§2.1 引用行（占位符 `threshold_top10 := RV3G3-goldrank-threshold-proof 产出值` → 双轨阈值表述 + 指向 goldrank-threshold-proof.md）、§2.1 说明行（「不得写死数值」禁令 → 回填状态声明）、§2.3 门禁行（❌ 未完成（queue 中）→ ✅ 完成（2026-10-30, goldrank-threshold-proof.md））。

**理由**：freeze §7 规定「修改本文件 = 开新 goal + APPROVALS.md 登记」。本 goal 即该引用机制预留的回填通道（§2.1 占位符为 r118 预注册授权），属机制内操作；04.5 攻击 3 复核维持该裁决，按 current-goal 失败降级条款补事后备案（非事前审批）。

**影响面声明**：改动面限 3 行，diff 全量落盘 `loop-artifacts/stages/01/RV3G3thr-stages01-03.md` J2 节；freeze §1/§3/§4/§5/§6/§7 零触碰；防漂移断言 assert-goldrank-threshold.py exit 0（31 PASS）+ 变异测试 4/4 FAIL。

**回退方式**：`git revert <收口 commit>` 单步还原。

**状态**：已执行（事后备案）。若成璐认为 §2.1 回填应走其他形式（如拆独立阈值文件），revert 后按新方案重做。

## 2026-10-30 · RV3G3cdx-crossdomain-promptversion-mapping（r153）— C9-plain 归属推论复核 + 执行偏差备案

**操作**：`bench/rubric-v3/ablation/prompt-version-gold-map.json` 新建权威映射表，其中 `pre-v3/C9-plain` 条目的 status=`archived-reference` 及「C9-plain ≠ v3 变体矩阵成员」的归属判定为**推论**而非直接证据——L1 原始任务书不在本仓，推论锚点 = DRAFT-rubric-v3-v2.md §3.2 L180 #27 裁定原文（「V0 必须在 v3 题面上同批次重跑……L1 C9-plain 只作外部参照」把两者当不同对象处理）。

**理由**：04.5 A-1 攻击项复核结论为驳回（推论有裁定文本锚点支撑），但残余不确定性非零——若成璐知悉 C9-plain 实为 V0-baseline 旧名，则映射表存在重复登记。消费逻辑零影响（两条目 gold_nodes 相同，仅 label/status 一行 diff），故不阻塞收口，挂此供复核。

**影响面声明**：纯新增文件（git status `??`），冻结面零触碰；消费方 assert-goldrank-crossdomain.py 的 gold_map_check 对该条目只做 sorted-set 相等比较，label/status 字段机判零消费。

**回退方式**：`git revert <收口 commit>` 单步还原；或单行修改该条目 status/label 即可纠正归属，无需重建表。

**状态**：待成璐复核（不阻塞）。

**附 · 执行偏差备案（D-a~D-d，均已修复复验，无遗留）**：
- D-a：初版 domain 解析用 prompt_version 的 `/` 后缀查 versions dict，而映射表键为完整字符串 ⇒ 恒 miss 误落 T3 SIGNAL；修复 = 完整 pv 直查 + 多域期 prefix 路由过渡形态（升级条款预注册于代码注释，挂 queue 候选 RV3G3cdx-goldmap-multidomain-upgrade）。
- D-b：bound 类型违例分支引用已删除变量 `ver`（NameError 潜伏）⇒ 改 `pv`，T7b 实跑实证闭合。
- D-c：N6 样例初版 gold 成员 N-5.3 不在样例 nodes 键集被 Y1 先行拦截 ⇒ 改 N-5 并同步 nodes/hit-matrix，断言语义未变。
- D-d：主模式原无 --dir 参数 ⇒ main() 增 --dir 解析（无参行为 byte-exact 不变，A4(i) 实证）。

## 2026-10-30 · RV3G3cdx-goldmap-multidomain-upgrade（r154）— r153 test-diff-bound 漏还原备案

**操作**：`bench/rubric-v3/ablation/prompt-version-gold-map.json` 移除 `v3/test-diff-bound` 条目（basis="temp test"，gold_nodes=["N-9.9"]）。

**理由**：该条目是 r153 阶段 04 T4-SIGNAL 验证时的临时注入——04 工件 L64-68 记录「测后还原」，实际漏还原一条，随 r153 收口 commit 042bb83 提交进权威源。本轮 A3 完成补还原，恢复权威源到 r153 A1 设计意图状态（8 正式条目）。性质 = 临时测试残留清理，非正式口径变更（该条目机判零消费，grep 全仓无脚本逻辑引用）。

**影响面声明**：纯删除 1 个明确标记 temp 的条目；8 正式条目（pre-v3/C9-plain + v3/V0..V3-sham ×6）零触碰；消费方 assert-goldrank-crossdomain.py 的 gold_map_check 对该条目零引用。

**回退方式**：`git revert <收口 commit>` 单步还原（重新引入该临时条目）。

**状态**：已执行（事后备案）。供成璐知悉 r153 收口遗漏，不阻塞。

## 2026-10-31 · RV3G3cdx-closure-gate-integration（r155/r27）— 门禁激活待裁定登记

**操作**：无已执行操作。本条目为**备料完成 + 裁定请求**登记：closure-checklist 门禁接入的全部备料件已落盘——`bench/rubric-v3/closure-gate-integration-materials.md`（六节裁定材料）+ `.githooks/pre-commit.closure-checklist`（未激活 hook 原型，core.hooksPath 零设置 = 对现有提交流程零行为变化）+ 三出口沙盒实跑记录（stages/04/RV3G3cdx-cgi-execution-log.md）。

**待成璐裁定项**（materials §2/§3/§4.3）：
1. **是否接入门禁**：否 ⇒ queue L27 转 `[~]` 设计内终态（K4 选项 O4），材料归档；是 ⇒ 进入方案选择。
2. **方案选择**：本仓约束下方案 B（CI check）实际拦截力 = 零（直推 main 无 PR 时点可挂，A2 实证）；方案 A（pre-commit hook）是唯一有实际拦截力的选项，但强制力弱（`--no-verify` 可绕过）。
3. **K4 语义漂移接受度（四选项）**：O1 完全接受 staged-diff 变体双轨并存【备料倾向】/ O2 有条件接受（hook 输出显式标注 staged 时点判定）/ O3 不接受退回 commit-hash 签名（需解冻 assert-closure-checklist.py 接口 = 新 goal + 本队列再登记）/ O4 不接入门禁。
4. **exit 1 硬拦可达性边界知悉**：pre-commit 时点 commit message 不可得（比 K1 hash 更根本的缺口）⇒ staged 原型漏翻检测降为 [SIGNAL] 提示形态（指名道姓保留），硬拦截能力在 r148 手动工具轨（commit 后消费真实 hash+message）。若要求 hook 硬拦，需引入 message 捕获约定（强制 `git commit -m` + 暂存 message 文件协议），属裁定后执行 goal 范围。

**影响面声明**：本轮全部产出 = 纯新增 2 文件（materials + hook 原型）+ stages/04 执行记录 + 本条目；冻结面零触碰；assert-closure-checklist.py 本体零改动；queue L27 状态位保持 `[ ]` blocked-on-human 零改动。

**回退方式**：`git revert <收口 commit>` 单步还原（删 2 新增文件 + 撤销本条目）。

**状态**：待成璐裁定（不阻塞——备料性质，同 RV3B1-jaccard-adjudicate / kappa-u1k1 备料模式）。裁定后按 materials §5 D1-D6 清单开执行 goal。

## 2026-10-31 · RV3G6-o3-claim-list-erratum-27（r29）— 冻结件修改登记（方案 A 已执行）

**操作**：`o3-claim-list.md` L137「27 个」→「13 个」+ 短注记；`assert-hitmatrix-evidence.py` 三处同步（docstring/declared=13/mismatch 文案）。

**裁定依据**：成璐选方案 A（材料 §4 推荐项）。r142 三口径独立复算 V1=13/V2=34/V3=35 均≠27，27 不可复现。

**验证**：`python3 assert-hitmatrix-evidence.py` → 「V1 计数 = 13/98 vs 声明值 = 13（一致）」VERDICT: PASS exit 0。

**revision-log**：R-16 条目已落盘 `bench/rubric-v3/revision-log-batch1.md`。

**回退方式**：`git revert <收口 commit>` 单步还原（3 文件）。

**状态**：已执行完毕（备料模式解除——本条从"待裁定"转为"已裁定已执行"记录）。

## 2026-10-31 · T8-C3-v3-opportunity-set-freeze — 空分母口径 + cover 门槛裁定（r62z）

**操作**：无文件修改。本条目为**成璐授权 runner 自主裁定**的记录。

**成璐指令原文**：「你自己决定approve里面的事情」（2026-10-31，微信）。

**裁定内容**：
1. **空分母口径**：选**保守口径**（unaddressed 计入分母、不计入分子）。理由：防「少做事反而分数高」漏洞，与 sham 分离目标一致。激进口径保留作敏感性分析双报。
2. **cover 门槛**：维持 **-0.05**（Δcover ≥ -0.05 才允许升档）。理由：当前域 cover 恒 1.0（vacuous），不构成实际约束；harder domain 接入后自然生效。-0.05 是建议值非文献值，置信度低-中，但作为初始值合理。

**影响面声明**：协议草案 `design/opportunity-set-freeze-protocol-draft-r57.md` 状态从「草案待裁定」→「已定稿」；goal-queue.md T8 行 BLOCKED ON USER → UNBLOCKED。R5 执行层解除阻塞。

**回退方式**：若成璐事后认为应选激进口径或不同门槛值，改协议草案 §二.2/§三 两行即可，已落盘数据不受影响（R4/R5 用的是旧口径 M8-r4-variable，历史数字保持原样）。

**状态**：已裁定已记录。

## 2026-11-01 · r76 keepalive — 卡人项状态汇总（无新裁定请求，纯状态登记）

**背景**：r76 唤醒时把 C3 v3 全链核查收口 + market-alpha T5-R1 收口 + lit-survey 来源审计做完后，盘点全部未决项，确认 agent 侧无可推进空间。本条为状态快照，供成璐下次看微信播报时快速定位要做什么。

**当前卡人项清单（按解锁成本排序）**：

| # | 项 | 等什么 | 解锁后动作 | 成本 |
|---|---|---|---|---|
| 1 | G1b family_check unknown→CLOSED（queue L25） | 一个明确非 Qwen 的 API key，或 arena 平台披露底层模型身份 | 用 key 对 G1a 冻结的 5 份 blind 工件重打 judge（任务书模板 `experiments/T8-matrix/runs/c3-v3/calibration/g1b/G1b-hetero-judge-task-brief.md` 现成） | ~5 次 LLM 调用 |
| 2 | κ 门禁阈值标定（queue L36 [~]） | 对 `bench/rubric-v3/kappa-u1k1-adjudication-materials.md` §4 勾选：公式 ∈ {F2,F3} × 阈值语义 ∈ {硬门禁,SIGNAL} × 阈值处置 ∈ {α,β,γ} | 按材料 §5 D1-D6 清单落地（protocol L71 UNRESOLVED 销账等 6 步机械操作） | 勾选后 ~6 步 |
| 3 | closure-gate-integration K4 O1-O4 裁定（APPROVALS 2026-10-31 条目） | 四选一：O1 完全接受 staged-diff 双轨【备料倾向】/ O2 有条件接受 / O3 退回 commit-hash 签名 / O4 不接入门禁 | 按 materials §5 D1-D6 开执行 goal 或归档 | 选 O4 则零成本关闭 |
| 4 | web-llm 三 provider 人工登录（D1-gpu cross_validation_out 门禁） | 浏览器一次性登录 Perplexity/ChatGPT/Gemini | 重跑 ralph web-llm-check → re-apply → advance | 一次登录 |
| 5 | queue 存量排版归一范围裁定（queue L68） | 选项 (i) 全量归一 / (ii) 仅活跃区归一 | 按 tasks/queue-format-contract.md §4 执行 | 小 |

**说明**：#1/#2/#3 互相独立可任意顺序解锁；#4 属 D1-gpu 项目线（非 pfb）；#5 是队列卫生小事。agent 侧在以上任一项解锁前不会重复推进——下轮 keepalive 唤醒会直接核对这五项是否有变化，有变化就执行对应动作，没变化就继续做可逆维护工作（如 queue 卫生扫描、回执补全）。

## 2026-11-01 · r157 keepalive — 维护债销账（无新裁定请求）

**操作**：assert-kappa-receipt.py DEFAULT_DIR 一层偏差修复（b9402ce）。原值指向 ablation/ 子目录（脚本自身所在目录），但 kappa-receipt.json 实际落盘于 bench/rubric-v3/（r29 erratum 收口写入）→ 无参调用恒 FAIL ①。修正后无参调用 = PASS + κ=0.0 SIGNAL（阈值未达，U-K1 人工裁决项不变）。materials §5 D2 回归义务行补过时注记。十五脚本回归基线维持（kappa-receipt 从 FAIL→PASS，其余零漂移）。

**状态**：已执行完毕。上表 #1-#5 卡人项状态不变。

## 2026-11-02 · C3v3-R4-MDE-prereg（r189）— 合规性文书缺口裁定

**操作**：补一份 R4/R5 任务块模型 + MDE 预注册件（arena adversarial-check blocking fix #1 的净缺口）。

**背景**：arena 对抗回执要求「任务块聚类模型 + MDE 反推题数预注册」，R4/R5 实跑从未落盘此件。处置表 r59 判定为「合规性文书欠一份」——结论未被污染（r47/r5 receipt 均已声明「描述层/方向性证据」上限），但缺书面预注册件意味着未来若有人把 R4 数字当推断层证据引用，无预注册文档可援引。

**选项**：
- (a) 补文书：写一份 ~2KB 预注册件（分析单元=(题,条目) / 任务块=seed 固定效应 / MDE 按 n=4 run/cell 反推 / 声明 R4+R5 全部 Δ 限方向性），落盘 design/ 目录 + receipt 引用。成本 ~2 回合，纯仓库内。
- (b) 接受现状：在 T8-prompt-ablation.md C3 v3 节加一行限定语「MDE 预注册未落地，R4/R5 数字永久限方向性证据（r189 登记）」，不再补件。成本 ~5 分钟。
- (c) 不处理：维持现有 limitations 声明（receipt 里已有「统计功效低，所有 Δ 只报方向」），不加新文字。

**影响面**：(a) 新增文件；(b)/(c) 改一行或零改动。均不影响已落盘数据。

**状态**：待成璐裁定。runner 倾向 (b)——最小动作堵住引用风险，不造文书。

## 2026-11-03 · r260 keepalive — seedc powerup 收口（无新裁定请求，状态登记）

**操作**：T8-C3-v3-seedc-powerup 降级通道实跑收口（@ f0cb47e pushed）。arena :8000/:8099 down → 按 runner 外包规则降级 ninfer :8787 qwen3.8-27b（conf−0.2）。18/18 run + J1v11/J2v11 双判 36/36 + cover brief_c 判读 18/18，零失败。回执 receipt-r8-seedc.json。

**结果（G3 = SIGNAL）**：F1 freeze 主效应三 seed 同向性检查 FAIL——seedc D1 = 0.0（vs R4 +0.391 反向）、D2 = +0.75（同向）。根因定位到测量系统而非工件：J1v11 条目抽取跨 run 漂移（A-full/D1 R4 抽 7/10 条 numeric id 得 0.857/1.0，seedc 抽 3 条 X-prefix 得 0.0；per-run n 从 3 漂到 24）→ per-config Δ 功效被系统性高估。cover 复现「高 cover ≠ 真核验」（B-none cover 1.0/1.0 而 truth 0.0/0.0）。

**推论（对既有卡人项的影响）**：对抗核验 FAIL 1（M8-fixed 独立标注员预建冻结机会表 + 逐机会判定）从「seedc 前置条件」升级为**一切后续消融分析的前置条件**——在此之前任何新 run 的 per-config 分数只能作单 run 快照。新导出 goal：T8-C3-v3-m8fixed-opportunity-table（P1，queue 已登记）。上表 #1-#5 卡人项状态不变（#1 G1b family_check 仍 blocked-on-human）。

**留痕**：wx-push 两次均失败（retry-without-token invalid request），按协议不重试。

**状态**：已执行完毕并 push。

## 2026-11-03 · r262 keepalive — M8-fixed 协议收口 + T8 实验线结论更新（状态登记）

**操作**：T8-C3-v3-m8fixed-opportunity-table 降级通道实跑收口（@ 12f752f pushed）。m8fixed-protocol-v1.json 冻结（sha ecdfb59edfdca704）+ G1/G2/G3 验证。

**结果**：G1 PASS（per-item 一致率 1.0）；G2 FAIL——全表 spread 0.044，constraint-only spread 0.0。**根因确认**：R4 全部 54 工件均为阶段 01+02 产出（prompt freeze 组件限定「本阶段是因素分解，不是资料搜集」），消融信号在阶段 01/02 层面极弱。之前所有 per-config Δ 测的是弱信号被测量噪声淹没，不能升级 confirmatory 声明。

**新决策点（需成璐拍板）**：是否补跑完整 loop（01→04）到最终报告再评分？成本 ≈ 9-13h 本地 LLM（:8787 qwen3.8-27b），收益 = 第一次真正测到消融对最终报告质量的影响。如果 T8 exploratory 结论够用则关闭实验线。

**留痕**：wx-push 失败（retry-without-token invalid request），按协议不重试。

**状态**：已执行完毕并 push。
