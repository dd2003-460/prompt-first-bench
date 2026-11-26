# 实验台账（全局视角的唯一落盘 · 2026-11-26 D 需求建立）

> **为什么有这个文件**：D 2026-11-26："需要一个能有全局视角的实验员条理清晰安排实验去消融（前人做不到的进展）"。
> 全局视角不能放在任何 agent 的上下文里（27b sub 7死6 实证：上下文一死视角就没了）。本文件 = 实验员的全局视角本体，任何 agent 读它即知全盘，它不随任何上下文死亡。

## 规则（闸门，跑实验前逐条过）

1. **预注册闸门**：每个实验开跑前，本表对应行的"预注册判据"列必须已填且 commit（跑完只读，事后修订另开行标 post-hoc）。无预注册的实验不许跑——防事后凑故事，也是 novelty claim 的防御点。
2. **一行一实验**：一个消融问题 = 一行。假设必须是可证伪的一句话（"X 导致 Y"），不是"看看 X"。
3. **novelty 定位必填**：每行"前人 diff"列写：前人做到哪（引用 competitor-survey.md 或文献）+ 我们多走的这一步是什么。写不出 = 不是进展，是重复，不进队列。
4. **状态机**：planned → preregistered → running → done / invalid。invalid 不删除，保留 + 作废原因（负结果也是资产：它排除了什么错误解释）。
5. **机械判据优先**：判据尽量落到可复算的数字（judge 脚本/oracle），模型判断只作 secondary。
6. **排序权在 arena**：下一步跑哪个臂（信息增益最大优先）由 arena 读本文件后排，Lead 验收排序理由，sub 只执行排好的单个臂。

## 每组实验的落盘规范（D 2026-11-26 要求："每一组实验对照/实验组数据和judge清晰"）

> 台账管"有哪些实验、下一步跑什么"（管理视角）；本节管"每组实验内部数据是否清晰"（实验视角）。D 的要求落在本节。

**最小单元 = 一个目录 `exp-results/<exp-id>/`，四件套齐备才算"清晰"：**

| 件 | 文件 | 内容 | 闸门 |
|---|---|---|---|
| 预注册 | `spec.md` | 假设（可证伪一句话）/ 对照臂与实验臂定义 / judge 判据+版本 / 样本量 | 跑前 commit，commit 时间戳必须早于 arms 数据 |
| 数据 | `arms/<arm-name>/` | 每臂：原始输出（raw，不裁剪）+ 提取数据 | 对照臂和实验臂各一目录，命名一致可比 |
| judge | `judge/eval.json` | judge 脚本版本 + 判据引用 + 每臂逐样本分数 + 汇总 | 必须由脚本生成可复算（手填=不合格） |
| 结论 | `report.md` | 一行：对照 vs 实验 Δ + 判据 + 数字 + 是否过预注册线 | 数字必须与 eval.json 一致（lint 比对） |

**"清晰"的可检验定义**：任何人读 `report.md` 一行 + 打开 `eval.json` 能复算出每个分数，不用再翻散文找数字。lint 三条：① 四件套文件存在 ② spec commit 时间 < arms 数据 mtime（预注册先行）③ report 数字 == eval.json 数字（机械比对）。

**存量处置**：现有实验（T8b/T8c smoke、stage-ablation）大多散文件不合规 → 盘点 completeness 字段查现状，不合规的排队重组（脚本搬目录 S1 + report 一行 S2）。**新实验（T8c 正式批起）直接按本规范跑**，不合规的 run 不收进台账。

## 表

| ID | 假设 | 臂 | 状态 | 结果(key_metric) | 三件套 | 证据 |
|---|---|---|---|---|---|---|
| T1 | stop_hook 检测连续薄思考（基线 430 字符/调用）→ 注入反思指令，给执行补上"想"的触发点 | 薄思考触发反思注入; 冷却门控 _THINK_COOLDOWN=3; 厚思考不触发（对照） | done | 隔离环境 5 场景全过（audit 留痕 think-trigger HIT t1-thin-thinking stats=[(100,1)×5]） | ✓✓✓ | tasks/think-trigger/exp-results/prereg_t2b.md; stage-gate 仓 1b30bc6 + APPROVALS 08697954（复验 5 场景全过，decomposition.md L34-35） |
| T2 | 27b 能接住 D 的爬层链：给前半段可续出机制+可检验预言（后半段 gold 只作判据不泄露） | 臂A 无提示（前半段+接着考虑）; 臂B general 提示（往一般机制想，推出可检验预言） | done | 臂B 3/3 爬到机制层+推预言+边界；臂A 0/3 预言；域偏移 100%（flip=0，6/6 漂混沌域） | ✓✓✓ | tasks/think-trigger/exp-results/raw_outputs_v2.json; tasks/think-trigger/exp-results/scores_v2.md |
| T2b | 软域锚点（自查句"核对爬到的机制域是不是这个问题所在的域"）能把 27b 从混沌域拉回 D 的 loss landscape 域 | 实验臂 B+软锚点; 控制臂 = T2 臂B（复用 raw_outputs_v2.json） | done | 0/3 D 机制域命中（无效，生死线第 3 条命中；混沌域 13-17 次/样本） | ✓✓✓ | tasks/think-trigger/exp-results/prereg_t2b.md; tasks/think-trigger/exp-results/raw_outputs_t2b.json; tasks/think-trigger/exp-results/scores_t2b_t2c.md |
| T2c | 显式域声明（直接告知 loss landscape/非凸优化域，禁混沌框架）能修复域偏移 | 实验臂 显式域声明; 控制臂 = T2b 软锚点（复用 raw_outputs_t2b.json） | done | 3/3 有效（D 域 19-26 次/样本，混沌域降至 1-5；内容质检 3/3 域内真推理；3/3 推出 D 原文没有的新可检验预言） | ✓✓✓ | tasks/think-trigger/exp-results/prereg_t2c.md; tasks/think-trigger/exp-results/raw_outputs_t2c.json; tasks/think-trigger/exp-results/scores_t2b_t2c.md |
| T4 | 修脚本打转（同一报错签名 10 轮内 ≥2 次 或 同一文件 6 轮内改 ≥5 次且有报错）触发 general 思考升级注入 | T4-A 重复报错触发; T4-B 文件打转+报错触发; 同文件全成功不触发（对照）; 不同报错不触发（对照） | done | 隔离沙箱 9 场景全过 + 12 生产 session 0 误报 0 crash | ✗✗✗ | stage-gate 仓 7229159 + APPROVALS eeae4de1（decomposition.md L36） |
| T6 | 在显式域声明之上加 SOP 4 结构检查点（正交完备/证据分级/域核对/往返无损）提升输出质量（prompt 级代理） | 控制臂 = T2c 实验臂（复用 raw_outputs_t2c.json）; 实验臂 = 控制臂 + CHECKPO… | done | 3/3 结构自查 + 2/3 新预言，域不回退（完整 agent 级 A/B 待异族 judge） | ✓✓✓ | tasks/think-trigger/exp-results/prereg_t6.md; tasks/think-trigger/exp-results/raw_outputs_t6.json; tasks/think-trigger/exp-results/scores_t6.md |
| T8a | pfb 六阶段流程在 GPU 选卡题上产出质量优于直接求解（6 因子 rubric C·F·T·P·D·R） | Arm A 直接求解（单 call 4096tok）; Arm B pfb 六阶段（6 call 各 1536tok） | invalid | Δ(B-A)=+0.015（SE=0.049，t=0.30，噪声/信号 3.3x）；6/6 输出撞 token 上限 → rubric 无效+截断 confound，被 T8b 取代（数据保留为预算受限观察） | ✓✓✓ | tasks/think-trigger/exp-results/prereg_t8.md; tasks/think-trigger/exp-results/raw_outputs_t8.json; tasks/think-trigger/exp-results/t8_run.log |
| T8b | smoke 三问（不 claim 质量提升）：pfb 六阶段 B 臂 recall 是否成功/有无退化/unit 级覆盖如何 | Arm A 直接求解（max 16384，3 样本）; Arm B pfb 六阶段（6×4096，3 样本） | smoke | unit 级覆盖 A 0.900 / B 0.883（Δ-0.017，机械 judge 层面无覆盖退化）；correctness 时点快照 0/6（3090×4/W4/n=2）；B 13/18 stage 截断（72%）；N-5.2 带宽… | ✓✓✓ | tasks/think-trigger/exp-results/t8b-smoke-report.md; tasks/think-trigger/exp-results/raw_outputs_t8b.json; tasks/think-trigger/exp-results/t8b_positive_control… |
| T8c-smoke-r1 | token-matched 对照（两臂同 24576 completion tokens）：pfb 六阶段 B' 在 correctness 上优于直接求解 A' | Arm A' 直接求解; Arm B' pfb 六阶段 | invalid | 第 1 批（17:4x）6/6 误读 gpu_price 歧义 → 作废归档 invalid-runs/ | ✗✓✗ | tasks/think-trigger/exp-results/invalid-runs |
| T8c-smoke-r2 | token-matched 对照（两臂同 24576 completion tokens）：pfb 六阶段 B' 在 correctness 上优于直接求解 A'（n=3/臂 s… | Arm A' 直接求解（单次 24576）; Arm B' pfb 六阶段（6×4096） | smoke | Arm B FINAL 截断 3/3=100%（>50% 作废）→ 无法比较，按 pre-commit 规则停止；Arm A 3/3 推荐 3090（正确 winner，c_pass 锚点）；根因=harness per-stage ca… | ✓✓✓ | tasks/think-trigger/exp-results/t8c-smoke-eval.json; tasks/think-trigger/exp-results/t8c-smoke-state.json; tasks/think-trigger/exp-results/t8c-stop-rootcause-2… |
| T8c-formal | H1：token 预算匹配且题面无歧义（三歧义已消解：64K 定值/候选集定死 3090+V100/c_pass 口径）条件下，B' correctness 优于 A'（W1 方… | Arm A' 直接求解; Arm B' pfb 六阶段 | planned | - | ✓✓✓ | tasks/think-trigger/exp-results/t8c-preregistration.md; tasks/think-trigger/exp-results/t8c-formal-blocked.md; t8c-spec-final.md 冻结 2c16f644f + 预注册 8c168c2a4；b… |
| T8c-ReAnchor-A | 6 文件重锚定（V100 $704 / winner→V100×4 / MAX_A 73728）+ probe fixture 重写，使对照在正确锚点下可执行 | - | planned | - | ✓✗✓ | tasks/think-trigger/exp-results/reanchor-taskcard.md; tasks/think-trigger/exp-results/t8c-reanchor-table-704.json |
| T8c-ReAnchor-B | - | - | planned | - | ✓✗✓ | tasks/think-trigger/exp-results/posthoc-taskcard.md |
| T8c-smoke-rerun | 新锚点（V100 $704）+ MAX_A 73728（=6×12288，覆盖六阶段真实需求下限 69227）下重跑 smoke，Stage 0 截断率 ≤50% 通过后进正式 | Arm A'（同步 73728 上限）; Arm B'（六阶段） | planned | - | ✓✓✓ | tasks/think-trigger/exp-results/reanchor-taskcard.md |
| J1 | correctness 层机械判别器（无 LLM）能区分三型断点：A1 候选构建/A2 候选集粒度/A3 排序权重 | - | done | selftest 11/11；dry-run 判别 3/3（含第三型 A2 发现）；gold anchors 7/7 一致；敏感性 A1/A3 全网格 100% 稳定 | ✓✗✓ | modules/B-pipeline-ablation/research/correctness-layer-design.md; modules/B-pipeline-ablation/research/correctness_layer_v0.py; modules/B-pipeline-ablation/res… |
| J2 | correctness 层整合进 judge pipeline 后，coverage 与 correctness 互补非冗余（coverage 高 ≠ 结论对） | - | done | 17/17 行 MD↔JSON 一致；S5 cov=0.3889（基准 0.389±0.01）；T8b 6/6 verdict 吻合；Pearson(cov,CORR)=0.462；三型分布 17 条 A1×7/A2×9/A3×1 | ✓✗✓ | modules/B-pipeline-ablation/research/joint-scores-20261125.md; modules/B-pipeline-ablation/research/judge_pipeline_v0.py; commits 9fa00c2a0→2e40716f4→4c3304138… |
| J3a | gold 树结构层级正交（顶层 4 因素=3 性能+1 成本，各压缩下层）且 c_pass 是顶层估计器、有作用域 | - | done | 37 节点/守恒 7 组机械核验通过（extract_j3a_factors.py + verify_j3a_properties.py §4 完备无缺口）；判断层 Lead 直判（SHARED≠非正交 conf0.8 / 五层必要 co… | ✓✗✓ | tasks/think-trigger/exp-results/j3a-factors.json; tasks/think-trigger/exp-results/j3a-hierarchy.md; commit a966b5488（S1/S2 机械层脚本+Lead 直判） |
| J3a-l2hit-calib | l2_hit→MFU 与 l2_hit→η_bw 两个弹性函数可用 F-A 框架+双工况探针实测标定（黑箱 S-b，无闭式） | F-A 框架 + 双工况探针 | planned | - | ✓✓✓ | tasks/think-trigger/exp-results/j3a-l2hit-calib-design.md |
| J3b | c_pass 作用域边界有可检验判据，候选集外泛化排名可用本地 KB 规格（L40S/A100/H100/M2Ultra）跑 oracle 计算 | - | done | 泛化排名表 + tf_peak 敏感性 + 4 判据 + 排错样本归因作用域（4090 翻转引用 T8b 已有结果） | ✓✗✓ | tasks/think-trigger/exp-results/j3b_generalization.py; commit 8ad7dea37 |
| T5 | 咒语从固定指针改成动态检索（索引+检索+执行，与 RAG 同构）：不同类型问题检索到不同思考流程 | - | done | 路由表 4 问题类型（理论研究/调试卡住/选域/证据质量）已实施（ROUTING.md + CLAUDE.md 调度器路由）；遗留 CLAUDE.md L30 编号外观项待 D 同意 | ✗✗✗ | ROUTING.md + CLAUDE.md（decomposition.md T5 节；遗留 L30 编号项） |
| probe-condgate | - | - | done | 4 条探针（task/expect/last_line/finish/hit 字段） | ✓✗✓ | tasks/think-trigger/exp-results/probe_condgate_raw.json |
| T17-stage-ablation | pfb 六个阶段每级增量显著为正（H1），且完整流程 S5 跑赢 deepsearch 开源 baseline D1 | S0 裸 prompt; S1 +01 分解; S2 +02 调研; S3 +02.5 交叉核验; S4 +03 行动… | done | 5 题×6 臂×3 run=90 runs：同族 27B judge S1-S0 +0.129（H1 confirmed）；异族 GPT judge -0.187（同一数据结论方向反转=评分严重依赖评委身份） | ✗✓✓ | experiments/stage-ablation/T17-stage-ablation-final-report.md; experiments/stage-ablation/raw-data-full-perdim.json; experiments/stage-ablation/DESIGN.md |
| V3-judge-final | S5（S1+hooks）在 V3 judge 下显著超过 S0 基线（61 runs，bootstrap CI + paired sign test） | S0 baseline; S1 分解树; S5 memory hook（S1+hooks）; 16 secondary… | done | S5-S0 +0.190（p=0.0010，+14/-1/0）；S5 总分 0.805 [0.762,0.841]；S1-S0 +0.014 ns（同族 judge，绝对值仅相对有效） | ✗✓✓ | experiments/stage-ablation/RESULTS-FINAL.md; experiments/stage-ablation/bootstrap-cis.json |
| T22-r2 | 三道闸（数字锚点/矛盾/限制声明）能把 post 发布文本的无锚点数字率打到 raw 的 50% 以下 | A raw（不过闸）; B 全闸; C 只过数字闸 | done | 判据不成立：B 无锚点率 100%（gpu 133/133）——闸是隔离器不是验证器；矛盾对 0（成立但窄模式）；n=2/臂 | ✗✓✓ | experiments/stage-ablation/T22-r2-result.md |
| T25-research-hook | ego-browser 直访已知站点通道（搜索引擎全不可用时的降级方案）能让 02 阶段真调研成立 | - | done | Bing 返回垃圾/DDG 空/Startpage Cloudflare 墙；arxiv.org/nvidia.com 直访正常 → research_hook v2.1 落地 | ✗✗✓ | experiments/stage-ablation/T25-research-hook-v2-validation.md |
| G1-large-sample | prompt lever（A3 量纲纪律/A4 few-shot 推导链示范）提升 nat/soc 两域 gold point 覆盖率 | S0 baseline; A3 量纲纪律; A4 few-shot 推导链 | done | 2 域×30 reps=180 runs：S0 nat 0.600/soc 0.957；A3 零效应（-0.011，p=0.84 ns）；A4 弱正向（+0.022/+0.024，sign test p=1.000 ns，d≈0.11，需… | ✗✓✓ | experiments/stage-ablation/G1-large-sample-report.md; experiments/stage-ablation/production-final-report.md |
| G5-five-arm | S8G（S5+P1 通用质量规则+增强 hook）保持 S5 水平并跨题泛化 | S0; S1; S5; S7F research_hook; S7V +two-pass 验证; S8G | done | 全题 mean：S8G 0.776（S5 0.805 / S7F 0.586 / S7V 0.630 / S0 0.615 / S1 0.630） | ✗✓✓ | experiments/stage-ablation/G5-five-arm-comparison.md |
| S8B | 掩码重建能把自校验符号翻正（P1: A2 mask-rebuild > A0 baseline） | A0 baseline; A1 persona 质询; A2 掩码重建 | done | P1 不成立：A2 nat -0.056 / soc -0.238（负效应+成本 2-3 倍）；A1 零效应（噪声内）；n=3/臂，同族 judge 仅相对有效 | ✗✓✓ | experiments/stage-ablation/S8B-result.md |
| S8E-pilot-r2 | research_hook（arXiv API 多查询+关键词过滤）提升 M1 断言准确率 | S8E（Q1+Q4 ×2 rep） | done | Q1 M1=0.467、Q4 M1=0.638、overall M4=0.75（pilot n=4，低于 paper 基线 S7 0.771） | ✗✓✓ | experiments/stage-ablation/S8E-pilot-r2.md; experiments/stage-ablation/s8e-scores.json |
| S10-combo-arms | 机械式具体指认（B 臂）比人话模糊反馈（D/E 臂）更能驱动 R4 定向修正 | S10-A v0 基线; S10-B 机械检查; S10-C 机械+讲原因; S10-D 人话 reviewer; S… | done | 5 臂×3 题×6 rep=90 runs：Q1 NVLink 缺口 B 6/6 检出+6/6 修正；C/D/E 0/6 | ✗✓✓ | experiments/stage-ablation/s10-preliminary-analysis.md; experiments/stage-ablation/s10-run-summary.json |
| M7-dim | 分解稀释矛盾推理注意力（S1<S0），调研+核验补回（S5 最高）——M7 建模/矛盾裁决维度 | S0 裸跑; S1 仅分解; S5 完整 | planned | Q1 初步（3 rep×3 arm）：S0 0.750 / S1 0.500 / S5 0.833；待做：Q2-Q5 gold 锚点提取 + 全量 90-run 重算（DRAFT 未完成） | ✗✓✓ | experiments/stage-ablation/M7-design.md |
| r14-structural | decomp 状态机结构测试：产出健康树（quotient 占比 ≤20%、节点数 100-150、leaks=0） | - | done | unique 节点 40（低于区间：id 撞号伤+max_depth=4 截断）；quotient 10.0%（r13 为 90% hack）；verified 32.5%；leaks 0 → 判进 Phase 2 DRB | ✗✗✓ | experiments/stage-ablation/r14-results.md; experiments/stage-ablation/runs-s5-sm-gpu.json |
| gpu-rerun | - | - | invalid | 75 records/34 unique（撞号伤复发，reworks=[] 计数疑 bug）→ 被 gpu-rerun2-results.md 整体取代（153/153 unique） | ✗✗✓ | experiments/stage-ablation/gpu-rerun-results.md; experiments/stage-ablation/gpu-rerun2-results.md |
| FTM-three-arm | 文本臂（T）拆解质量优于公式臂（F）（verified 率对比） | F 公式注入; T 文本臂; M minimal（跑中） | running | F verified 37.7%（20/53）vs T 51.6%（64/124，+14pp）；M 臂数据待补 | ✗✓✓ | experiments/stage-ablation/ftm-bench-report.md |
| G9-independence | rubric 维度间相互独立（Decision 22 本体论反例检验） | - | done | gpu 15 维度两两判定（层级相关/相关/独立，如 g0×g1 层级相关 conf 0.95）；nat/soc 同法（g9-independence-nat.json/soc.json） | ✗✗✓ | experiments/stage-ablation/g9-independence.md; experiments/stage-ablation/g9-independence-gpu.json |
| S5-SM-bench-DRB | S5 状态机管线在 DRB 公开题四维加权总分 ≥ CellCog Max 56.72 对标线（无泄漏、verified 率正常） | DRB 公开题 drb-1/drb-2/drb-16 | running | - | ✗✓✓ | experiments/stage-ablation/s5-sm-bench-report.md; experiments/stage-ablation/J-drb-2-reverified.json |
| judge-v2-comparison | 连续 [0,1] judge（每点独立打分）下 A4（深度引导）两域领先 | S0; A3; A4; S3 | done | A4 nat 0.594 / soc 0.756 领先；S3 第三（0.570/0.717）；A3≈S0 确认零效应；臂间差异 n=25-30 不显著 | ✗✓✓ | experiments/stage-ablation/judge-v2-comparison.md |

## 队列（arena 排序区）

- 待排：（盘点回填后由 arena 出排序 + 理由）

## 指针

- 竞品/前人基线：`pfb/experiments/stage-ablation/competitor-survey.md`
- 阶段消融设计：`pfb-thinkmech/experiments/stage-ablation/DESIGN.md`
- 机制准入（新检测器/触发器才准进队列）：`tasks/think-trigger/decomposition.md` 机制准入门节
- 盘点原料：`exp-results/experiment-inventory-20261126.json`
