# DESIGN — 逐阶段子模块消融实验（S0–S5 × D1）

> origin: ai · 2026-11-03 · T23-B 核心交付物
> 任务书：`projects/decomp/tasks/T23-merge-pfb-ablation.md`（decomp-bench commit 0a8dfc4）
> 前置结论：r1（`projects/decomp/experiments/autoresearch-r1/run/scoring-r1.md`）——结构 > 语言，但纯 prompt 不产生事实；「会调研」必须靠环境里真实可执行的工具。本实验把 r1 的三臂扩展为六阶段全链路 + 外部 baseline。

## 0. 一句话目标

回答两个问题：① pfb 六个阶段里，每一级增量是否显著为正（负收益的阶段 = 砍掉或重做）；② 完整流程 S5 能否跑赢 deepsearch 类开源 baseline D1（autoresearch 系统的发布判据）。

## 1. 显式依赖（开跑前必须 resolve）

| # | 依赖 | 状态 | 影响 |
|---|------|------|------|
| D-a | **T22 三道闸单点验证结果** | **已出（12/12 runs，2026-11-03 补跑）**：B_conflicts_zero=True（窄检测下），B_unanchored<half_A=False——闸是隔离器不是验证器，post 无锚点率≈raw 属预期。结论：**S5 保留三道闸**（价值 = 逐行 quarantine 审计链，独立于准确率维度）。完整证据：`experiments/stage-ablation/T22-r2-result.md` + decomp-bench `experiments/autoresearch-r2/scoring-r2-final.md`（main 21160ed）。限定：n=2/臂、矛盾检测为窄模式、accuracy 待人工原子标签 | S5 配置定案：04+04.5+三道闸（gates-postcheck.md），不再走降级路径 |
| D-b | `loop/modules/gates-postcheck.md` 的机器实现（gates.py） | **已回填且已验证**：decomp-bench main 21160ed → `experiments/stage-ablation/gates.py`（4 单测通过 + r2 全量 12 runs 实战跑通，含 rag-B max_tokens 截断修复）。唯一遗留：judge/正则 precision-recall 未在标注集校准 | S5 闸校验自动化就绪；r2 证明闸行为符合设计（隔离不删除），无需降级路径 |
| D-c | ego-browser 通道可用性（联网走 ego-lite 持久会话，deepseek/chatgpt 已登录） | 假设可用 | 02 阶段的真调研动作依赖它；不可用则 02 臂全部退化为「prompt 说查但不真查」，与 r1 同构，实验失去意义 → 触发降级方案 §7 |
| D-d | 本地 27b endpoint `http://127.0.0.1:8787/v1/chat/completions` | 假设可用 | 所有 S 臂的执行引擎；不可用 → 整体降级为只交付设计（conf-0.2） |

## 2. 实验矩阵

| 臂 | 配置 | 测什么 |
|----|------|--------|
| S0 | 裸 prompt（无流程，r1 A-minimal 原样：中文最简背景 + 「不确定就查」） | 基线 |
| S1 | 仅 01（含 decomp 分解模块 decomp-01.md 五步法） | 分解+留空的边际 |
| S2 | 01+02（信息调研，ego-browser 真联网） | 调研闭环的边际 |
| S3 | S3 = 01+02+02.5（交叉核验，≥2 独立来源 + 对抗核验） | 交叉核验的边际 |
| S4 | S3+03（行动分解：DAG 步骤 + 验收方式） | 行动规划的边际 |
| S5 | S4+04+04.5（执行验证+终审+三道闸 gates-postcheck） | 完整流程 |
| D1 | deepsearch 开源系统端到端（见 §5） | 外部 baseline |

臂间关系是**累积式**（S_k ⊇ S_{k-1}），每级增量 Δ_k = score(S_k) − score(S_{k−1}) 即该阶段的边际收益。S1 的 01 阶段固定启用 decomp-01 模块（这是 decomp 并入 pfb 后的标准形态；若要单独测「01 主文件 vs 01+decomp」，属于正交第二轴，不在本轮预算内，记入后续 backlog）。

### 各臂 prompt 构造规则

- 每个阶段 = `loop/prompt-first/<stage>.md` 全文注入为该阶段的 system/指令段；多臂时按阶段顺序拼接，阶段间用分隔标记。
- S0 不注入任何阶段文件，只有题面 + r1 A-minimal 的背景句。
- S1 追加 `loop/modules/decomp-01.md` 的「五步方法」节。
- S2–S5 的 02 阶段统一附加工具说明：可用 ego-browser 检索（搜索词 + URL 抓取），要求把来源标题/URL/观察时间写进输出（对齐 02 主文件第 3 条）。
- 所有臂同一模型、同 temperature=0、同 max_tokens=8000（沿用 t17 run-agent.py 参数）、n=2/题。

## 3. 题目集（5 题跨域，防过拟合）

| QID | 域 | 题面来源 | gold 锚点 |
|-----|----|---------|----------|
| Q1 | GPU 硬件规格 | r1 原题：H100 PCIe vs SXM LLM 推理吞吐差异（带隐藏矛盾：900/64≈14x 是互联带宽比陷阱） | `projects/decomp/experiments/autoresearch-r1/run/gold-facts.md`（直接复用，含误读清单 + 应识别缺口） |
| Q2 | 模型选型 | t17-generalization `task-model-selection.txt` 任务段（内部代码助手选开源模型，候选 6 个，根标量 ¢/1k_acc） | `projects/decomp/bench/gold-model-selection/tree.md`（gold 树 24 节点作锚点） |
| Q3 | 推理基础设施 | t17 `task-inference-infra.txt`（vLLM vs TGI vs 原生 vs SGLang，根标量 ¢/1k_out_tok） | `projects/decomp/bench/gold-inference-infra/tree.md`（25 节点） |
| Q4 | 数据处理架构 | t17 `task-rag-vs-longctx.txt`（50 万页企业知识库，纯 RAG / 纯长 ctx / 混合，根标量 ¢/1k_correct） | `projects/decomp/bench/gold-rag-vs-longctx/tree.md`（26 节点） |
| Q5 | 科研方法论 | t17 `task-methodology.txt`（贝叶斯 vs 频率学派，期望决策损失最低） | `projects/decomp/bench/gold-methodology/tree.md` |

- 跨域论证：Q1 叶子=物理规格（查表型），Q2=模型属性（基准分/单价/许可），Q3=工程属性（调度/KV/批量），Q4=信息流属性（召回/定位衰减），Q5=统计范式（场景依赖）——五题结构指纹互不相同，覆盖「查表 / 工程权衡 / 观点型」三类答案性质。
- gold 使用纪律：gold 只用于**判分对照**，不进入任何臂的 prompt（防泄漏）。Q2–Q5 的 gold 树是过程性锚点（看维度覆盖/黑盒收口），不是唯一正确数字。
- Q5 的特殊性（如实标注）：t17 当时判定该域「难以建成可排序 gold 标量」，其 gold 更偏观点综述 → Q5 的事实准确率维度置信度低，评分时权重降半（见 §4 权重列）。

## 4. 评分维度（机器可检，与 T22 对齐）

每 run 输出过一遍评分器，产出 6 维分数。评分器接口见 §6。

| 维度 | 定义 | 机器可检方式 | 主要咬合的臂 | Q5 权重 |
|------|------|-------------|-------------|---------|
| M1 事实准确率 | 与 gold 一致的断言数 / 全部可判定断言数 | 断言抽取（正则+LLM 辅助判定）→ 逐条对 gold 锚点条目打 match/mismatch/undecidable | S2+（有调研才可能高） | 0.5 |
| M2 无来源数字率 | 无来源锚点的数字断言 / 全部数字断言（越低越好） | 闸 1 正则（gates.py） | S0–S5 全臂可比 | 1.0 |
| M3 矛盾对数 | 同一事实不同版本共存数（越低越好） | 闸 2 断言库比对 | S3+ 应有下降 | 1.0 |
| M4 缺口标注覆盖率 | gold 锚点里的「应识别缺口」被该 run 显式标出的比例（越高越好；decomp KPI：该留空的有没有留空） | 缺口条目关键词匹配 + LLM 判定「该 run 是否把它列为未知/待核验/黑盒」 | S1+（decomp 黑盒表的直接检验） | 1.0 |
| M5 坏消息位置 | 限制陈述出现在输出前 1/3 的比例 | 闸 3 checklist（限制句分类器） | S5（闸 3 行为指标） | 1.0 |
| M6 调研真实性 | 输出中引用的 URL/来源是否真实存在且内容支持断言（抽样 ≥3 条/run 人工+ego 复核） | 半自动：URL 存活检查 + 人工核对引用-断言一致性 | S2+ 独有信号（S0/S1 预期 ≈0，这正是 r1 命门） | 1.0 |

总分 = Σ(维度归一化分 × 权重)，M2/M3/M5 反向计分。每臂每题 n=2，报 mean ± range；**n=2 只能出方向性结论**（t17 已证 n=2 噪声 ≥ 域差），任何「显著为正」的措辞必须附此限定，最终确认需 n≥4（记入后续 backlog，不在本轮预算）。

## 5. D1 baseline 选择

- 候选池（open DeepResearch 类端到端系统）：先调研 GitHub star/活跃度/可本地部署性，选 **1 个最成熟的**。倾向性候选（开跑前用 ego-browser 核一遍现状再定死）：GPT Researcher（python，可配本地模型）、Open Deep Research（LangChain 系）、STORM（Stanford，生成视角型报告）。
- 选择理由记录在 `runs/d1-choice.md`（为什么选它 + 放弃谁 + conf）。
- 运行方式：按其自身默认 pipeline 跑 5 题（它的 prompt/工具链不动，保持「开箱水平」），每题 1 次（D1 不计入 60 runs 预算，单列）。
- 公平性声明（如实）：D1 自带联网工具，S 臂的联网走 ego-browser 由 harness 代查后注入——两者「联网深度」不完全等价，比较时注明这是 harness 层差异，不是流程层差异。
- 降级：开源实现质量参差导致选不定 → 取 GPT Researcher 单点，conf 相应下调（任务书失败降级条款）。

## 6. 评分脚本接口

```
score_run(run_json, gold_md, arm) -> dict
  run_json: {arm, qid, rep, model, params, output_text, sources[], wall_s, tokens{in,out}}
  gold_md:  对应 QID 的 gold 锚点（Q1=r1 gold-facts.md；Q2–Q5=t17 gold-*/tree.md）
  返回:     {M1..M6 原始计数 + 归一化分, total, boundary_violation(bool), notes[]}

run_all(arms=[S0..S5], qs=[Q1..Q5], n=2) -> runs/*.json   # 60 runs
run_d1(qs=[Q1..Q5]) -> runs/D1-*.json                      # 另计
aggregate() -> scoring.md                                  # 6 维 × 臂汇总表 + Δ_k + 判据核查
```

- 实现位置：`experiments/stage-ablation/score.py`（执行时写，框架参考 t17 `bench/runs/t17-generalization/score.py` + r1 `run_local.py`）。
- 闸 1/2/3 的正则与比对逻辑从 T22 的 gates.py 拷贝（依赖 D-b）；T22 未交付前先用最小实现（数字正则 + 字符串级矛盾检测）跑通管道，标 `gate_impl=minimal`。
- LLM 辅助判定（断言↔gold 匹配、缺口识别判定）用本地 27b 做 judge，judge 本身的不确定性在 scoring.md 里注明（judge 非独立模型，conf 上限 0.7）。

## 7. Run 预算与降级

**全量**：S0–S5 共 6 臂 × 5 题 × n=2 = **60 runs**；D1 另 5 runs（不计入 60）。

**缩略版降级**（预算过大或时间不够时，任务书条款）：先跑 **S0 / S2 / S5 / D1** 四臂 = 3×5×2 + 5 = **35 runs**（任务书写 20 runs 是按 3 臂算的口径，实际含 D1 为 35；若连 D1 也砍则 30 runs）。出方向性结论（Δ 符号 + S5 vs D1 总分序）后再决定是否补 S1/S3/S4 全量。

**其他降级**（任务书条款 + 本设计补充）：
- 27b endpoint 不可用 → 只交付设计文档 + 评分脚本骨架，conf-0.2。
- ego-browser 通道不可用 → S2+ 臂的 02 阶段无法真联网，实验退化为 r1 同构（prompt 说了不算），**停跑并报告 Lead**，不硬出结论。
- 单 run 超时/格式异常 → 重跑 1 次，仍失败记 `failed` 不参与均值，n 相应减少并在 scoring.md 注明。
- 某臂总耗时超预算 2× → 该臂 n 降到 1，标 `n=1 low-conf`。

## 8. 判据

1. **每级增量**：Δ_k = mean(score S_k) − mean(score S_{k−1})（按总分和按维度分别看）。Δ_k ≤ 0 的阶段 = 该子模块砍掉或重做（写入结论，附 n=2 限定）。重点关注：S2 的 Δ（调研闭环，r1 命门的正面检验）、S1 的 M4（decomp 缺口 KPI 是否在无调研条件下仍成立）。
2. **发布判据**：mean(total S5) vs mean(total D1)。S5 ≥ D1 → 完整流程跑赢开源 baseline，autoresearch 系统具备发布条件（仍需 n≥4 复确认）；S5 < D1 → 差距归因到具体维度（哪个 M 拖后腿），作为下一轮迭代输入。
3. **诚实条款**：所有结论带 conf + 数据来源；n=2 的结果一律标「方向性」；judge 自判的维度 conf 上限 0.7；D1 的 harness 差异如实标注。

## 9. 执行通道

- 模型：本地 qwen3.8-27b @ `http://127.0.0.1:8787/v1/chat/completions`，temp=0，max_tokens=8000。
- 联网：ego-browser（ego-lite 持久会话，deepseek/chatgpt 已登录；不要预设不可用）。02 阶段的检索动作由 harness 通过 ego-browser 执行，结果以「来源包」形式注入下一轮 prompt（来源标题/URL/观察时间/摘录），对齐 02 主文件的来源记录要求。
- 调研外包：需要深度调研的环节（如 D1 选型调研、gold 锚点时效性复核）走 arena-outsource SOP，外包回执落盘 `runs/receipts/`。
- 落盘：每 run 一个 JSON 进 `runs/`；汇总进 `scoring.md`；完成后更新本目录 README 状态列 + commit/push。

## 10. 不做的事（边界）

- 不测「01 主文件 vs 01+decomp」正交轴（第二轮）。
- 不提 n 到 ≥4（预算外，backlog）。
- 不改 loop/prompt-first/ 任何阶段文件（本实验只消费它们）。
- 不把 gold 泄漏进 prompt；不把 D1 的 pipeline 改动包装成公平对比。