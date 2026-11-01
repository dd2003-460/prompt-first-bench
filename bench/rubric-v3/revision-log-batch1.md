# revision-log-batch1 — rubric-v3 DRAFT v2 修订记录（第一批）

> goal: RV3G6-draft-revision-batch1 · 分支 ralph/rv3g6-batch1 · 2026-10-30
> 上游：`AUDIT-report.md` §9.1 修订清单（batch1 = R-01~R-03 + R-06 + R-10，开跑前置条件）
> 对象：`DRAFT-rubric-v3.md`（v1，r59，保留为审计历史快照）→ `DRAFT-rubric-v3-v2.md`（本版）

## 包含 / 不包含清单（防误用声明）

**本版包含**（7 项工作全部落地）：
- [x] R-01 O1 拆账 + 二值条目计分 + 防刷分机械判据
- [x] R-02 全维尺度统一（yes/no 条目化 + 条目通过率 + κ 条目层 + 权重预注册写死）
- [x] R-03 §4 题面去方向暗示 + V1-align 对照组 + Pr2/Pr3 判据替换
- [x] R-06 §1-O3「宣称前置条件」硬条款（AUDIT-report §6 原文逐字）
- [x] R-10 变体矩阵冻结（同题面 + D1/D2 精确 diff + V-sham 等长中性替换）
- [x] C4 w2 公式断言脚本（`ablation/scripts/assert-w2-formula.py`，运行 exit 0，62/62 节点）
- [x] C3 W3W4 复算断言脚本（`ablation/scripts/assert-w3w4-recompute.py`，运行 exit 0，40/40 分数）

**本版不包含**（留 batch2，v2 文件内以 `[batch2: R-xx]` 醒目标记占位）：
R-04（pilot 两步走）/ R-05（维度合并规则）/ R-07（gold 新发现计分项 + 冻结纪律）/ R-08（P1/P3 代理量）/ R-09（边界声明段落写入 prompt 流程 + V3 sham 联动——注意：D2 段落文本本版已给出作为冻结对象，但「写入 loop/prompt-first 并 commit 冻结」的流程动作属 R-09）/ R-11（统计设计包）/ R-12（O2 层级机械化）/ ~~R-13（O3 claim 清单化）~~ **→ 已提前落地（RV3G6-o3-claim-list，见下方追加条目）** / R-14（O4 拆项）/ R-15（单域限定语）。

**使用门禁**：本版不可用于正式实验计分（batch2 未完成）；可用于 pilot 设计与题面冻结。

---

## 逐条修订对照

### R-01 · O1 拆账 + 计分统一（AUDIT-report §2-O1 + §7.1 B1/B7/#20/#21）

| | v1（L21-33） | v2（§1-O1） |
|--|--------------|-------------|
| 测什么 | 「是否覆盖非直觉老卡区间」（判语义正确性，与 O3 同一证据两计） | 「是否覆盖非默认可行区间」**只计覆盖行为**（B1 拆账：O1 管覆盖行为，O3 管 gold 命中，互斥） |
| 计分 | 0/1/2 三档表（四种写法冲突：档位描述含数量+质量混合判据） | 每候选 3 条 yes/no 条目（E1 纳入 / E2 三项检查证据 / E3 深度计入资格），维度分 = 通过数/(3×候选数)（B7 统一二值，删 tier/w 概念） |
| 封顶 | 无 | 计入深度分的低先验候选 ≤3（预注册写死） |
| 防刷分 | 无 | 四条 run 级门禁：Jaccard 双口径 / 维度定义时间戳先于搜索 / ≥3 档含中间档 / 证据密度下限（#20/#21） |
| 域锚点 | 「V100/P100/T4/2080Ti/1080Ti 档」「2020 年前卡型」具体卡型枚举 | 「低先验候选 = 不在被测者未受引导时的默认候选先验内」（judge 对照 V0 同题产出判定，域无关） |

**M5 登记（需人工裁决）**：防刷分判据 1「候选集 Jaccard<0.9」在 AUDIT-report §2-O1 中未展开定义。v2 落笔为**双口径兜底**：「同题重复 run 的候选集 Jaccard < 0.9，且相邻档候选集不得几乎相同」。两种读法（run 间稳定性 vs 档位区分度）都服务于 #20 防刷分目的，无法从仓库内证据裁定作者本意 → 双口径同时生效，待人工裁决后收敛为单一口径。

**M5 已裁定（2026-10-31, 成璐）**：选项 A——仅档位区分度（跨维度去重，#20 fix (c) 原文语义）。run 间稳定性不纳入判据（无原文支撑 + legitimate convergence 误伤风险）。DRAFT v2 L38/L311 已同步改写，销账。材料 = bench/rubric-v3/jaccard-m5-adjudication-materials.md。

### R-02 · 全维尺度统一（AUDIT-report §2 横切节 + §7.1 B6/#26）

| | v1 | v2 |
|--|----|----|
| §0 原则 4 | 「每个维度给 0/1/2 三档，判据必须机械可判」 | 「每维拆 3-6 个 yes/no 条目，维度分 = 条目通过数/条目数（0-1 连续）；κ 在条目层（二值）计算」+ 新增原则 5「权重与总分公式预注册写死，不留满分另定」 |
| O2 | L1 0.5/L2 1/L3 2 个/项 + min(2,Σ) 封顶 | 4 条 yes/no 条目直译过渡（E1-E4），`[batch2: R-12]` 占位 |
| O4 | 0/1/2 三档表 | 3 条 yes/no 条目（E1 前提参数化 / E2 数值区间 / E3 另一侧推荐），`[batch2: R-14]` 占位 |
| P1/P3 | 0/1/2 三档表（证据源在 run 中不存在，B8） | 各 3 条 yes/no 条目 + **NA 档机制**（通道不可用 ≠ 0 分），`[batch2: R-08]` 占位 |
| P2/P4 | 0/1/2 三档表 | 各 3 条 yes/no 条目，`[batch2: R-09]` 占位（P4） |
| Outcome 总分 | 「O1+O2+O3+O4（满分另定，建议 O3 占大头）」 | **0.4×O3 + 0.25×O1 + 0.2×O2 + 0.15×O4**（预注册写死 + 理由 + 禁止开跑后改） |
| Process 总分 | 「各 0-2，满分 8」 | **0.25×P1+0.25×P2+0.25×P3+0.25×P4**（预注册写死 + NA 档归一化规则） |

**边界裁定（Q5）**：batch1 只做横切机制改写 + O1 完整重写（R-01 独立成项）；O2/O4/P1-P4 条目内容为现判据二值化直译，深度重设计（R-12/R-14/R-08/R-09）留 batch2 占位。防止越界实施 batch2 内容（03 预注册规则 2 的 grep 验证对象）。

### R-03 · §4 题面去方向暗示 + V1-align + Pr 判据替换（AUDIT-report §7.1 B3/B11 + §3.4）

| 注射点（v1 L165-183 补丁 + L191-194 预言） | v2 处置 |
|-------------------------------------------|---------|
| c 区「发布 ≥5 年」年代锚点 | 删除。分区边界改「由任务画像推导」，题面不给年代/价格阈值/卡型示例（M1：v1 的「低于当代旗舰 50%」具体阈值一并删除） |
| c 区准入条件「保值性好/性价比可能更高」价值断言 | 删除。V1 主补丁不保留任何价值倾向词；「默认先验之外候选不少于前者一半」是数量义务（最小化残余倾向，V1-align 连此也剥离） |
| 分区标签「当代旗舰区/上代主流区/老马区/非 GPU 区」（带先验的命名） | V1 改「分区 a/b/c/d 由任务画像推导」；V1-align 进一步去掉「默认先验」字样（M4 修正：三层对比 V1/V1-align/V0 才能拆出倾向 vs 结构两个效应） |
| 三问指向特定卡型生态（kernel 支持到哪一代/二手价 vs 发布价/实测数据） | 域无关占位：①生态成熟度 ②经济状况 ③实测瓶颈——题面只规定问题类别，指标实例化是被测者的工作（也是 O1-E2 判定对象） |
| V1-align 对照组 | **新增**（§4.2）：纯结构版补丁，与 4.1 逐处差异列明（删数量义务句 / 分区描述纯占位 / 三问适用全部候选） |
| Pr2「老马区候选数 ≥2 比例 > V0」当能力信号 | **降级为 manipulation check**（只检验题面被执行，不作能力证据；finding #19 自证问题消除） |
| Pr3「老卡进入最终排名前 3 = baseline 决策错误」 | **换外部真值判据**：低先验候选须在实测口径（reference/calc.py 或等价外部真值管道重算，非模型自评）下确实优于 V0 首选；「进入模型自己写的前 3」明确不算（自我指涉废弃） |

### R-06 · O3 宣称前置条件硬条款（AUDIT-report §6 + §7.1 B2 声明路径）

- 位置：v2 §1-O3 内新增「#### 宣称前置条件（硬条款）」小节。
- 文本：**AUDIT-report §6 引用块逐字复制**（从「本文引用的 O3 构念效度数字…」到「…p̃ 重估 + 构念效度复测。」整段，含双重限定 + 双闭环解锁条件 (i)(ii)）。
- 验证方式：04 阶段 `diff` 比对 AUDIT-report §6 引用块与 v2 该小节正文，要求零差异（03 预注册规则 1）。
- 附带状态声明（R-06 关联，AUDIT-report §3.3）：surprisal 加权（w2）标 **experimental**，主公式 = W1，构念效度主判据 = gmr（过线阈值待 RV3G3-goldrank-threshold-proof 论证前不得写死）。

### R-10 · 变体矩阵冻结（AUDIT-report §7.1 B10/#27）

| 要素 | v1（§3.2 L139-148） | v2（§3.2） |
|------|---------------------|------------|
| 共用题面 | 未声明（V0 = C9-plain 旧题面，#27 配对破坏） | **所有变体共用同一 v3 基础题面**；V0 必须同批次重跑，L1 C9-plain 只作外部参照 |
| 变体集 | V0/V1/V2/V3 | V0/V1/**V1-align**/V2/V3/**V-sham**（V1-align 来自 R-03；V-sham 来自 B9/B10 长度/格式控制） |
| diff 记录 | 无（「V2 = V1 去掉候选集扩展指令」一句话，无行号无 commit） | 冻结 diff 登记表：D1（§4.1 代码块 L219-L236）/ D2（P4 边界类型声明段 L154-L161），每行 = 段落原文定位 + 行号 + 操作 + 冻结 commit hash |
| V-sham 替换文本 | 无 | §4.3 全文给出（纯格式规范模板，等长中性，M2 修正：无时间/停止语义） |
| 开跑门禁 | 无 | 「无 diff 记录的变体不得开跑」 |

**回填状态（C-01 裁定后终态）**：D1/D2/sham 行号已回填并逐行 sed 核验（v2 当前版本：D1=L219-L236 含围栏，D2=L154-L161 含围栏，sham=L258-L269）。**冻结 commit hash 不写入 v2 表格**——自指问题（hash 指向包含本表的 commit 本身）无法在表内解决。裁定：**冻结语义 = 收口 commit 的 `DRAFT-rubric-v3-v2.md` 文件快照**；具体 hash 在本节登记 → **冻结版本 = ralph/rv3g6-batch1 分支收口 commit `61416b43f80e28d9785137f320003bf8e121d306`（r116，2026-10-30，main 与 origin 双端 ls-remote 已验证同 hash）**。取回方式：`git show 61416b4:bench/rubric-v3/DRAFT-rubric-v3-v2.md`。本登记由后续 fixup commit 写入（只改本 revision-log 本节，零触碰 v2 冻结段落区域，无行号漂移风险）。

### R-13 · O3 claim 清单化 + 映射一致性指标（AUDIT-report §2-O3 L79 / §9.1 L293）【提前落地 · RV3G6-o3-claim-list】

| 要素 | 原计划（batch2） | 实际落地（本 goal，2026-10-30） |
|------|------------------|--------------------------------|
| 交付物 | O3 命中判据替换为原子 claim 清单 | `bench/rubric-v3/o3-claim-list.md`（六节：§1 三失败模式 FM-1/2/3 带 run 原文 evidence / §2 31 节点 claim 全覆盖零 NA / §3 映射一致性指标 M1/M2 + identity-baseline / §4 多判者协议 N=3 ≥2/3 / §5 S2 限定语 byte-exact + 未决项 / §6 冻结声明） |
| DRAFT v2 改动 | — | O3 节「命中判据」行替换为 claim 级判据引用（保留 h_v 符号）+ 新增 `[batch2: R-13]` 已提前落地状态行；其余行零改动（J4 最小 diff） |
| 机判防护 | — | `ablation/scripts/assert-o3-claim-list.py` exit 0（4 检查组：31 节点覆盖 / 零 gold 专有数值泄漏 / M1-M2 基线复算一致 / DRAFT 旧措辞消失） |

**范围切割说明**：R-13 原属 batch2（~2 回合估算），本 goal 提前交付其**核心件**（判据件 + 指标定义 + 多判者协议文字化）。**不含**：claim 级独立重判执行（需 fresh-context judge，工具纪律禁 subagent → unverified，导出 queue `RV3G6-o3-claim-rejudge`，arena 通道，样本 31×8 全 cell 优先 h=0 的 150 cell）+ 31 条 claim 措辞人工审定（APPROVALS.md 条目 4 登记，不阻塞）。batch2 开跑时 R-13 按「已完成核心件」处理，剩余部分以 queue 项跟踪。

---

## C3/C4 机判断言（G5 导出，AUDIT-report §1-G5 行）

| 脚本 | 断言内容 | 运行结果（04 实际执行） |
|------|----------|--------------------------|
| `ablation/scripts/assert-w2-formula.py` | 双 judge 逐节点 w2 = 1+min(−log₂p̃, log₂(1/ε)) 复算（orig tol 5e-5 / new tol 5e-4，M3 分侧容差） | **exit 0**：orig 31/31 + new 31/31 = 62/62 节点一致，0 mismatch |
| `ablation/scripts/assert-w3w4-recompute.py` | hit-matrix + prior-estimates 独立复算 W0-W4 × 8 run vs stats-w3w4.json | **exit 0**：5 方案 × 8 run = 40/40 分数一致，0 mismatch |
| `ablation/scripts/assert-psf-freeze.py`（RV3B1-prompt-side-freeze 新增） | ① 02.5 附录 D2 副本 byte-exact ② §3.2 V3-sham 行存在且六变体行不变 ③ §4.4 行数=6+字符偏差≤10%+黑名单零命中 | **exit 0**：10/10 PASS（r129 实际运行） |

防护意义（G4 S3 降档教训）：纸面协议（「w2 按公式计算」「分数可复算」）在执行前零防护力——现在任何对冻结 JSON 的单点篡改都会让对应脚本 FAIL。

---

## R-09 部分落地追加条目（RV3B1-prompt-side-freeze · r129 · 2026-10-30）

**范围**：R-09 的「D2 写入 prompt + V3 sham 联动」流程动作已落地；「可观测三问细化」仍待 batch2。

| 项 | 落点 | 验证 |
|----|------|------|
| A1 · D2 正文 6 行执行侧副本 | `loop/prompt-first/02.5-cross-check.md` 文末附录区（标题显式声明「非本 loop 规则」防误读） | assert-psf-freeze.py 检查① byte-exact PASS |
| A2 · §4.4 V3-sham 替换段 | v2 §4.3 之后新建：引用/脚注格式规范主题，代码块内 6 行，与 D2 正文等长（偏差 ≤10%），不含边界类型三类语义 token | 检查③ PASS |
| A3 · §3.2 变体矩阵 V3-sham 行 | V-sham 行后插入；既有六行零改动（对照冻结 commit 61416b4 快照） | 检查② PASS |
| A4 · L164 `[batch2: R-09]` 占位符 | 更新为「部分落地」状态注记 | grep 定点 |
| A5 · 机判脚本 | `ablation/scripts/assert-psf-freeze.py` exit 0 + 变异测试（逐项破坏必须 FAIL） | 04 日志 |
| A6 · 本登记 | 本节 | — |

**§4.4 回填行号**：见上表 A2（v2 当前版本行号以文件实际为准，assert 脚本按内容定位不依赖行号）。

**诚实保留**：web-llm 三 provider 登录态失效 → 本 goal 证据链仓库内闭合（DRAFT v2 冻结快照 + 02.5 目标文件 + revision-log），外部第二意见边际贡献 ≈ 0，unverified 降级沿用（per-goal 回执 `loop-artifacts/prompt-first/02-web-llm-cross-check-RV3B1psf.md`）。

---

## R-16 · o3-claim-list §3.2 声明 4「27」数字勘误（方案 A，r142 导出 / r29 执行）

| 项 | 内容 |
|---|---|
| 触发 | r142 (RV3G6-o3-claim-rejudge-evidence-audit) A4：三口径独立复算 V1=13/V2=34/V3=35 均≠27，27 为起草期不可复现人工计数 |
| 裁定 | 成璐选方案 A（直接改 13 + 短注记），材料 = `bench/rubric-v3/o3-claim-list-erratum-27-materials.md` §3/§4 |
| 改动 1 | `o3-claim-list.md` L137：「27 个」→「13 个」+ 尾注「（V1 口径，assert-hitmatrix-evidence.py 机判；原值 27 见 r142 勘误）」 |
| 改动 2 | `ablation/scripts/assert-hitmatrix-evidence.py` 三处同步：docstring L26-28 / `declared = 13`（L151）/ mismatch 文案（L154） |
| 验证 | `python3 assert-hitmatrix-evidence.py` → 「V1 计数 = 13/98 vs 声明值 = 13（一致）」VERDICT: PASS exit 0 |
| APPROVALS | 本条目即冻结件修改登记（§6 红线通道）；回退 = `git revert <收口 commit>` |
| 日期 | 2026-10-31 |

---

## R-17 · O3 消融证据段补记独立 judge 盲测 r1 结果（r73 产出回填）

| 项 | 内容 |
|---|---|
| 触发 | keepalive 快照 P2「新发现：rubric-v3 遗留工作 #1 独立 judge 盲测 p̃」——核实后发现该盲测 r73 已执行且裁定已落 bench.md L104，但 DRAFT v2 O3 消融证据段未同步（v1 时代旧句「若独立 judge 盲测支持再升级」已被 R-06 experimental 声明取代但未注明依据实测） |
| 改动 | `DRAFT-rubric-v3-v2.md` O3 消融证据段新增一条 bullet：r73 盲测 W3 top-5 构念效度 1/5 → pass=false + ρ=0.688 + 最终裁定（surprisal 权重方案不进正式 rubric，负结果记录），显式挂接 R-06 experimental 状态声明 |
| 性质 | 文档同步（非冻结数据修改）：judge-blindtest-r1.json / stats-w3w4.json 等冻结件零触碰；与 AUDIT-report G2 F2 双源根因结论一致，无新事实引入 |
| 验证 | grep 确认新 bullet 存在 + 既有 bullet 零改动（diff 面仅 +1 行） |
| 日期 | 2026-11-01 |

---

## R-18 · prompt-V0 矛盾预算段 B10 缺口登记（r158 · ralph/v0-conflict-budget-close）

| 项 | 内容 |
|---|---|
| 触发 | keepalive bridge 对账发现 b92a70c/a6145b6 两个 commit 在 v3 批次开跑前修改了 `ablation/prompt-V0.txt`（新增「找矛盾预算」指令段），但该段未登记进 DRAFT v2 §3.2 冻结 diff 表——B10 规则「无 diff 记录的变体不得开跑」的机械前提被破坏：若 v3 批次直接以现版 prompt-V0.txt 为共用题面，所有变体都携带未注册的 V1 侧组件，消融归因链断裂 |
| 核实事实 | ① 泄漏扫描不受影响：assert-leak-triage.py 旧/新版 token 集完全相同（均 {0.25,0.30,0.45,1,2,9,10,20,90,100,200}），rare-token 白名单口径不变；② L1 计分链锚定 aad07bd (r69) 落盘版（TASK-ablation 输入材料节 + #27 裁定 C9-plain 只作外部参照），hit-matrix/prior-estimates 等冻结件零触碰；③ gold-tree.md 无「矛盾」标记节点，O2 E1-E4 判据与 D3 段正交（E2/E3 判的是产出内矛盾层级，不依赖题面是否要求找矛盾）；④ 该段语义上属 V1 侧组件预研（矛盾挖掘深度是 O2 维度测的对象，放进 baseline 会污染 V0/V2 对照） |
| 改动 | `DRAFT-rubric-v3-v2.md` §3.2 冻结 diff 表追加 D3 行（状态 = 未注册/B10 缺口，任何变体要测其效应须先补 diff+冻结 commit 再开跑；在此之前共用题面按「不含 D3 段」口径执行）+ `TASK-ablation.md` 输入材料节加版本注记（L1 数据锚定 aad07bd 版） |
| 性质 | 文档同步 + 缺口显式化（非冻结数据修改、非行为变更）：prompt-V0.txt 本体零改动（保持 r157 会话工作成果原样），冻结 JSON/矩阵零触碰 |
| 待办导出 | 若 v3 批次决定测「矛盾挖掘」组件效应：新开 goal 把 D3 段从 prompt-V0.txt 移出（或单列 prompt-V1-conflict 文件）+ 补 §3.2 D3 行冻结 commit + 同批次重跑受影响变体（B10/#27）。当前不代裁，挂候选 |
| 日期 | 2026-11-01 |

---

## R-19 · O2 层级必要条件机械化 + 层级主导计分 + gold 命中正交化（R-12 落地 · ralph/rv3g6-o2-mechanize-r12）

| 项 | 内容 |
|---|---|
| 触发 | queue 候选 RV3G6-o2-mechanize-r12：AUDIT-report #5/#11/#12 + B2 fix(2) 的 O2 侧落地——batch1 直译态「O2 = 通过条目数/4」把 L1×4 与 L3×1 等权，且 E1-E4 判据仍用层级语义词（judge 无法机械执行） |
| 改动 | `DRAFT-rubric-v3-v2.md` §2-O2 整节替换为 R-12 终态：① L1/L2/L3 各给「产出内可定位的必要条件」（L1=两具名对象+同维度反向取值+片段可定位；L2=L1 基础上双变量数值锚点+显式不相容断言+来源/推算依据；L3=L2 基础上外部可查数字或可复算公式+具体机制链路解释）；② 计分改层级主导 `O2 = min(1, 0.1·n_L1 + 0.25·n_L2 + 0.5·n_L3 + 0.25·E4)`——取消旧 min(2,Σ) 封顶下「深度>广度」被广度淹没的问题，单 L3 贡献 0.5、L1×10 才到 1.0；③ gold 命中正交化：G-hit 降级为附加诊断标签不计分，G-new（gold 未覆盖的新深层发现，须附可验证路径）改正式计分项 `O2_final = min(1, O2 + 0.25·G_new)`，盲评确认前按 0.5 条保守计 |
| 权重依据 | 0.1/0.25/0.5 沿用 v1 相对比例（0.5/1/2 归一化后近似 0.2/0.4/0.8，此处取更保守的 0.1/0.25/0.5 使单 L3=0.5 即半满、E4 质量门 0.25 封顶闭环价值）；min(1,·) 保持维度分 0-1 连续口径与 W 组合层兼容。pilot 双判数据出来后如 κ 不达标或区分度异常，按 batch2 规则回修并记 revision-log |
| 性质 | 冻结文档修订（DRAFT 状态，非已冻结件）；O2 之外零触碰（diff 面仅 §2-O2 一节）；C0 历史 run 的 O2 分数不受影响（v2 从未对 C0 出过正式分，L1 链锚定 aad07bd 不变） |
| 遗留边界 | ① G-new 独立盲评确认通道复用 C3 v3 G1b 异源 judge 资产，family_check 解锁前按 0.5 条计；② 层级必要条件 judge 间一致性待 pilot 双判首验（κ 回执走 assert-kappa-receipt.py 既有 schema） |
| 验证 | grep 确认「[batch2: R-12]」占位改为已落地注记 + 旧「通过条目数 / 4」计分句零残留（全文唯一匹配 = 新计分公式行）；七脚本回归全绿（O2 无既有断言脚本，回归面 = 防误伤） |
| 日期 | 2026-11-01 |

---

| 触发 | queue KAPPA-U1K1-DISPOSITION（成璐裁定：F2 Fleiss'κ + β 维持 0.6 + γ 降 SIGNAL+人工裁决；P1 双判者对照 κ=0.537 实证分歧 19 cell 后激活） |
| 改动 | U-K1 销账落地 D1-D6：judge-protocol-batch1.md L71 U-K1 段替换为裁定结果（F2+β+γ）；assert-kappa-receipt.py docstring 口径更新 + method 收紧为取值域约束（fleiss/pairwise/cohen）+ judges 从「恰两个」放宽「≥2」；DRAFT v2 L16/L208 追加口径绑定注记（L208「不过不开评」措辞按 γ 软化）；o3-claim-list §4.3 写入具体公式与数字（κ_fleiss < 0.6, β 沿用声明, γ 语义）；queue RV3G4-kappa-gate-execution 联动注记 |
| 性质 | 冻结件修改（o3-claim-list §4.3）→ APPROVALS.md 登记；其余为非冻结文档修订。U-K1 是发散型缺口（§4.3 原文从未写公式），本条落地的是裁定结果而非还原本意 |
| 验证 | assert-kappa-receipt.py 实跑基线回归（既有 kappa-receipt.json 应仍 PASS——method 含 'cohen' 历史兼容）+ 新增 3-judge 合成回执正变异（judges=3 → PASS）+ method 域外反变异（method="unknown" → FAIL） |
| 日期 | 2026-11-01 |

---


---

## R-20 · batch2 修订全落地（R-04/R-05/R-07/R-08/R-09/R-11/R-14/R-15 · ralph/rv3g6-draft-revision-batch2）

| 项 | 内容 |
|---|---|
| 触发 | queue RV3G6-draft-revision-batch2 [~] 可启动（U-K1 前置已闭合）：AUDIT-report §9.1 第二批 ~24 回合修订，DRAFT v2 状态行声明「不可用于正式实验计分」的解除条件 |
| 改动 | `DRAFT-rubric-v3-v2.md` 八处：① §3.1 R-04 pilot→定维度两步走（删 L1 预检，pilot 矩阵定义域写死）；② Process 总分节 R-05 维度合并规则预注册（\|ρ\|>0.8 簇报 + 确认性 2 维/探索性 6 维分层 + 8×8 相关矩阵强制附报）；③ §1-O3 R-07 G-new 正式计分项 O3_final=min(1, O3+0.25·n_Gnew) + gold 冻结纪律（sha256 登记 run 元数据，rubric 后于 gold 冻结才可改）；④ §2-P1/P3 R-08 判据替换为工件机械提取代理量（P1-E3 关键事实外部来源比例≥50% + P1-E4 独立域名≥2 + P3-E1 独立来源数≥2 比例≥50%）+ 开跑前通道探测写入 run 元数据 + NA 档机制；⑤ §2-P4 R-09 可观测三问细化（E1-E3 即三问可执行形态，抽样核验一致率项挂 pilot 后——pilot 前无定义域）；⑥ §3.3 R-11 统计设计修订包（δ_min=0.1 预注册 + MDE≈2.802·sd_d/√n_pairs 反推 + 配对置换检验主/Wilcoxon 敏 + Holm 全族 28 项作用域明确 + judge 盲化匿名变体标签 + κ 条目层 U-K1 γ 语义）；⑦ §1-O4 R-14 结构/正确性拆 E4/E5 独立二值条目（±10% 容差预注册初值，β 沿用声明同 U-K1 阈值口径；E5 独立核对复用 G1b 异源 judge 资产，family_check 解锁前 NA 归一化）；⑧ §6 R-15 结论适用范围写死「单域，不外推」（跨域/跨题面版本/跨模型规模引用违规条款）。状态行同步更新为「batch1+batch2 全部落地，可用于 pilot 开跑」 |
| 权重依据 | R-14 ±10% 容差 = 预注册初值非标定值（显式 β 沿用声明，pilot 双判后回修须记 log）；R-11 δ_min=0.1 = v1 20 分制 2 档等比换算到 0-1 连续口径；R-07 单条封顶 0.25 防刷分（与 O2 G-new 0.25 同量级不同维）；R-05 候选簇（P1+P3/O2+P4）标「基于 B5 分析非断言」，成簇与否以 pilot 实测为准 |
| 性质 | 冻结文档修订（DRAFT 状态，非已冻结件）；§4 冻结块（D1/D2/sham）零触碰——B10 消融 diff 链不受影响；hit-matrix/prior-estimates/gold-tree 等冻结数据零触碰 |
| 遗留边界 | ① R-08「关键事实」句子级判定需 judge 执行，pilot 双判首验 κ（走 assert-kappa-receipt.py 既有 schema）；② R-14 E5 / R-07 G-new 的独立核对通道均复用 C3 v3 G1b 异源 judge 资产，family_check 解锁前按保守口径（NA / 0.5 条）；③ R-11 sd_d 先验用 L1 配对差值样本标准差（外部参照不进检验），pilot 首跑后实测重算 n_pairs；④ R-09 抽样核验一致率项 pilot 前无定义域，不假装可执行 |
| 验证 | grep 确认「待 batch2 / 留 batch2 / 占位防误用」全文零残留（residual 无匹配）+ 16 断言脚本回归 15 PASS（assert-closure-checklist 需 commit-hash+goal 参数，非回归失败）+ 状态行与 §6 销账注记一致 |
| 日期 | 2026-11-01 |

## 诚实保留（负面结果与弱点，不掩盖）

1. **R-06 逐字一致性已 diff 验证**（04 执行后更新）：AUDIT-report.md L186 与 v2 L77 字节级相等（python `a == b → True`，413 字符），非手工重打。
2. **V1-align 切分的外部第二意见缺失**——web-llm 三 provider 全失败（登录过期，与 AUDIT-report 附录 B 一致），「结构 vs 暗示」切分是否干净只有仓库内自证，unverified。
3. **Jaccard 双口径已裁定收敛（M5, 2026-10-31）**——选项 A 仅档位区分度，见 M5 段销账注记。
4. **batch2 占位的条目框架可能整体重构**——O2/O4/P1/P3 的 v2 条目是二值化直译过渡态，R-08/R-12/R-14 落地时大概率改写；本版保证的是 batch1 期间（pilot 设计期）可用，不是终态。
5. **D2 段落是本 goal 新写的 prompt 侧文本**——AUDIT-report B9 要求「先把边界类型声明段落写进 loop/prompt-first/02.5（或 03）并 commit 冻结」，本 goal 只在 DRAFT v2 内给出 D2 文本作为冻结对象（R-10 范围），写入 prompt 文件的流程动作属 R-09（batch2）。这是范围切割，不是遗漏。
6. **权重数值（0.4/0.25/0.2/0.15 与四等分）是本 goal 的预注册选择**——AUDIT-report 只要求「权重预注册写死」未给具体值；取值依据（O3 主分占大头 / process 四维无主次）写在 v2 对应位置，供人工审。
7. **「≥5 年」元文本保留（C-02 裁定）**：v2 §4 设计变更声明中引用 v1 锚点原文（「发布 ≥5 年」）属审计可追溯性需要（说明删了什么），不是题面指令，不计为 A5 验收残留；冻结块（D1/D2/sham）内方向暗示词 grep = 0 命中才是硬标准。
---

## R-21 · pilot 后分析落盘 + DRAFT 正式实验段更新（RV3G6-pilot-post-analysis · ralph/rv3g6-pilot-post-analysis）

| 项 | 内容 |
|---|---|
| 触发 | RV3G6-pilot-run 收口（main @ 43e38ec，κ 修正回执 kappa-results-corrected.json）后的 §3.1 第二步前置：pilot 数据须回代 R-05/R-11——DRAFT L206「pilot 用途限定为两件事」的兑现动作 |
| 改动 | ① 新增 `ablation/pilot-matrix/pilot-post-analysis.json`：双判均值维度分重算（DRAFT 预注册公式）+ 三组主对比配对 sd_d + n_pairs 反推（δ_min=0.1）+ 7×7 Spearman 矩阵 + |ρ|>0.8 簇候选 + 变体总分（outcome/process 预注册权重）；② DRAFT v2 §3.1 第二步行追加 r164 实测输入四注记（κ 处置/簇裁定挂起/n_pairs 方向性/天花板效应），不改任何预注册数值与权重表 |
| 关键数字 | κ overall 0.857(n=162) / O3 claim 1.0(n=279) / O1 0.506(SIGNAL)；簇 {O1,O2,P4} ρ(O2,P4)=1.0；V1full−V0 outcome Δ=+0.208(sd 0.094, n≥8)、process Δ=+0.222(sd 0.096, n≥8)；O1 Δ=+0.556(sd 0.419, n≥139)；变体均值 outcome V0 0.634 / V1-full 0.841 / V1-align 0.823 |
| 性质 | 冻结文档修订（DRAFT 状态，非已冻结件）；只加注记不动预注册值（权重表/δ_min/阈值零触碰）；kappa-results-corrected.json 等既有回执零触碰 |
| 遗留边界 | ① O1 入簇但属确认性主维度 → R-05 合并处置需成璐裁定（JSON r05_decision_input 已备料），裁定前正式实验维度结构未最终确认；② P2 全 NA（无 run-log）→ 矩阵 7×7 非预注册 8×8，正式实验须补 run-log 采集否则 P2 永久缺列；③ 同序号配对为约定非随机化，n=3 每对 → n_pairs 只作方向性输入；④ V1 侧 O2/P4 天花板效应未解决，区分度问题进正式实验设计清单 |
| 验证 | python 独立重算（条目级二值分 → 维度分 → 总分/sd/ρ 全链路脚本可复现，源 = judge-A.json + judge1/2.json）；grep 确认 DRAFT 预注册权重表（L124/L194）与 δ_min 行零 diff |
| 日期 | 2026-11-02 |
