# T8: loop/prompt-first 消融研究——哪些 prompt 真有用，哪些是表演

**状态**: ready（T7.1 跑完后开跑；依赖 T7.1 基线工件）
**执行通道**: arena agent mode @ prompt-first-bench（任务书走仓库，prompt 只指路）
**动机**（成璐 r31/r33 指令）：①leader/subagent 中间轮次要能区分"真发现矛盾/漏洞" vs "装模作样演示" ②七阶段 prompt 逐条研究清楚——提升在哪、什么提示有用、什么是无意义负载 ③每类 prompt 的用途/论文结论/复现要完整调研 ④实验设计/中间过程/结果结构要完整清晰。

## 现状盘点（r33 诚实核查，防重复造轮子）

已有资产（decomp 仓 `bench/`，与 pfb 互补不重叠）：
- **ablation-L1**（`bench/runs/ablation-L1/`）：11 变体 × 3run = 33 份评分收官。但对象是**单 prompt 分解规则集**（C0 21 零件/C1-small/C2-expos…），不是六阶段 pipeline。结论：contract 类规则最致命（C6-nocontract 4.00 vs C0 14.63）、scratchpad 有真实作用（C7-noscratch 13.33）、exposneg 负向示例有害（C3/C5 ≈5.67）。
- **文献调研**（`bench/prompts/evidence/lit-survey.md` + landscape-survey + p4-open-source-survey）：TaskBench/PlanBench/APB/ResearchBench/RE-Bench 已查，结论"无人测分解结构正交性"。**缺**：multi-stage pipeline prompt / reviewer-critic prompt / staged workflow 这类设计的文献调研（现有调研覆盖的是单 prompt 组件级）。
- **组件级 WHY 注释**（`bench/prompts/components/F*.md`）：每个零件有 ID/WHY/SRC 头注——这个格式该被 pfb 阶段文件借鉴。
- **self-opt-tester bench r4**（pfb 仓 `bench/self-opt-tester/bench.md`）：M1-M7 指标体系 + 独立打分裁决流程（自估偏差 +11.39 实证）。

**缺口（T8 要填的）**：
1. 六阶段 pipeline 作为整体的消融从未做过（L1 是单 prompt 内部零件）
2. 每阶段 prompt 的"这类设计有什么用"文献依据缺失（stage-gate/critic-reviewer/staged-revision 类）
3. 中间轮次真实性没有审计协议
4. pfb 仓内实验资产散落（loop-artifacts/stages/ 混着多任务工件、bench/ 只有 self-opt-tester），无统一实验目录

## Part A: 中间轮次真实性审计（零额外 run，先做）

对象：pfb 仓全部历史核验/复核工件（loop-artifacts/stages/ + bench/self-opt-tester/run2-arena/ + decomp 仓 ablation-L1 的 review 记录）。

审计协议（每条"矛盾/漏洞/质疑"过三测）：
1. **具体性**：必须指向具体来源+具体字段（"S35 $19/spot vs S36 $2.50/spot 冲突"算数，"存在一定差异"不算）
2. **可证伪**：该矛盾后来被跟进消解或显式保留？只写不跟 = 表演
3. **反事实**：删掉这条质疑结论会变吗？不变 = 装饰
输出：每工件一张表（条目 | 真矛盾/真漏洞/表演 | 证据），落 `experiments/T8-audit/intermediate-rounds-audit.md`。

## Part B: 文献调研补齐（arena 代干，交叉核验 ≥2 源）

调研问题清单（每问给来源 URL + conf，按 AGENTS.md 网络规则走 ego-browser）：
1. multi-stage agent pipeline（plan→research→verify→review 分阶段 prompt）有没有系统性研究各阶段 prompt 的贡献度？（关键词：staged prompting / pipeline LLM agents / plan-and-execute ablation）
2. critic/reviewer prompt 的设计研究：对抗性复核（adversarial review / self-critique / LLM-as-judge critique）什么条件下真提升、什么条件是表演？已知锚点：Self-Refine (arXiv 2303.17651)、CRITIC、LLM-as-judge 偏差文献
3. staged revision（04.5 这种"反方复核后回退修复"）vs one-shot 的效果对比证据
4. 把 L1 的组件级结论（contract 致命/scratchpad 有效/负向示例有害）映射到 pipeline 阶段级的合理性论证
产出：`experiments/T8-lit/lit-survey-pipeline-prompts.md`（表格化：设计类型 | 代表工作 | 结论 | 与我们阶段文件的对应关系 | conf）

## Part C: 七阶段 pipeline 消融（paired runs，方案经对抗核验后开跑）

方法：同域同题 paired runs，A 组全量 prompt，B 组删减版。删减候选（按可疑度排序）：
- 02 §2 ralph web-llm 强制命令段（arena 环境无 ralph，疑似无效负载）
- 04.5「通用原则」三节 12 条（与操作流程高度重叠，疑似冗余）
- 各阶段 Reviewer 质检标准（删后看 reviewer 行为是否退化）
- 01 候选集冻结声明（T6 已验证生效 → 阳性对照，必留）

度量（复用 self-opt-tester M1-M7 + 新增）：
- M8 核验真实性率 = 真矛盾数/(真矛盾+表演)（Part A 协议打分）
- M9 token 效率差（A vs B input 总量，bili.log 口径）
判定：删减后 M8 不降且 M9 显著升 → 该段无意义负载，移除；M8 降 → 有用，保留并记录作用机制。
样本：≥2 域 × 2 配置 = 4 runs 起步（n=1 不出结论，bench r4 教训）。

## 结构整改（实验资产归位，pfb 仓内）

新建 `experiments/` 顶层目录，结构固定：
```
experiments/
  T8-audit/          # Part A 审计表
  T8-lit/            # Part B 文献调研
  T8-ablation/       # Part C 消融：design.md(方案) + runs/<domain>-<config>/ + report.md
  README.md          # 实验索引：每个实验一行（目的/状态/结论指针）
```
旧资产迁移：`loop-artifacts/stages/` 按任务归档到 `experiments/<task-id>/stages/`；`bench/self-opt-tester/` 保留原地但在 experiments/README.md 登记。迁移走 git mv，历史可溯。

## 验收标准

1. Part A 审计表覆盖全部历史核验工件，每条有三测结果
2. Part B 文献调研 ≥4 问全答，每答 ≥2 独立来源 + conf，经一轮对抗核验（r29 标准）
3. Part C 消融方案先过对抗核验再开跑；产出 per-段落 verdict（有用/无用/未决 + 证据）
4. 无用段落实际从 workspace loop/prompt-first/ 移除并 sync pfb 仓
5. pfb 仓 experiments/ 结构落地，README 索引齐全

## 失败降级

- arena 跑 paired runs 成本过高 → 先做 Part A+B（零/低成本），Part C 标 pending
- 单 run 超时 → 重跑 1 次，仍死标 VOID 换下一域
- 文献某问穷尽渠道无答案 → 如实标"信息搜集瓶颈"（r29 停止条件），不编
