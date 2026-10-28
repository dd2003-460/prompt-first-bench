# T8: loop/prompt-first 消融研究——哪些 prompt 真有用，哪些是表演

**状态**: ready（T7.1 跑完后开跑；依赖 T7.1 基线工件）
**执行通道**: arena agent mode @ prompt-first-bench（任务书走仓库，prompt 只指路）
**动机**（成璐 r31/r33/r34 指令）：①中间轮次区分真矛盾 vs 表演 ②七阶段 prompt 逐条研究清楚 ③每类 prompt 用途/论文结论/复现完整调研 ④实验结构完整清晰 ⑤用可解释性方法加速消融。

## 现状盘点（r33 诚实核查，防重复造轮子）

已有资产（decomp 仓 `bench/`，与 pfb 互补不重叠）：
- **ablation-L1**（`bench/runs/ablation-L1/`）：11 变体 × 3run = 33 份评分收官。对象是**单 prompt 分解规则集**（C0 21 零件/C1-small/C2-expos…），不是六阶段 pipeline。结论：contract 类规则最致命（C6-nocontract 4.00 vs C0 14.63）、scratchpad 有真实作用（C7-noscratch 13.33）、exposneg 负向示例有害（C3/C5 ≈5.67）。
- **文献调研**（`bench/prompts/evidence/lit-survey.md` + landscape-survey + p4-open-source-survey）：TaskBench/PlanBench/APB/ResearchBench/RE-Bench 已查（组件级）。**缺**：multi-stage pipeline / critic-reviewer / staged-revision 类设计的文献调研。
- **组件级 WHY 注释**（`bench/prompts/components/F*.md`）：每个零件有 ID/WHY/SRC 头注——pfb 阶段文件该借鉴此格式。
- **self-opt-tester bench r4**（pfb 仓 `bench/self-opt-tester/bench.md`）：M1-M7 指标体系 + 独立打分裁决（自估偏差 +11.39 实证）。

**缺口（T8 要填的）**：pipeline 级消融空白 / pipeline 级文献缺失 / 中间轮次真实性无审计协议 / pfb 实验资产散落无统一目录。

## Part A: 中间轮次真实性审计（零额外 run，先做）

对象：pfb 仓全部历史核验/复核工件（loop-artifacts/stages/ + bench/self-opt-tester/run2-arena/ + decomp 仓 ablation-L1 review 记录）。

审计协议（每条"矛盾/漏洞/质疑"过三测）：
1. **具体性**：必须指向具体来源+具体字段（"S35 $19/spot vs S36 $2.50/spot 冲突"算数，"存在一定差异"不算）
2. **可证伪**：该矛盾后来被跟进消解或显式保留？只写不跟 = 表演
3. **反事实**：删掉这条质疑结论会变吗？不变 = 装饰
输出：每工件一张表（条目 | 真矛盾/真漏洞/表演 | 证据），落 `experiments/T8-audit/intermediate-rounds-audit.md`。

## Part B: 文献调研补齐（arena 代干，交叉核验 ≥2 源）

调研问题清单（每问给来源 URL + conf，按 AGENTS.md 网络规则走 ego-browser）：
1. multi-stage agent pipeline（plan→research→verify→review 分阶段 prompt）有没有系统性研究各阶段 prompt 的贡献度？（staged prompting / pipeline LLM agents / plan-and-execute ablation）
2. critic/reviewer prompt 设计：对抗性复核（adversarial review / self-critique / LLM-as-judge critique）什么条件下真提升、什么是表演？锚点：Self-Refine (arXiv 2303.17651)、CRITIC、LLM-as-judge 偏差文献
3. staged revision（04.5 反方复核后回退修复）vs one-shot 的效果对比证据
4. 把 L1 组件级结论（contract 致命/scratchpad 有效/负向示例有害）映射到 pipeline 阶段级的合理性论证
产出：`experiments/T8-lit/lit-survey-pipeline-prompts.md`（表格化：设计类型 | 代表工作 | 结论 | 与我们阶段文件的对应关系 | conf）

## Part C: 可解释性加速消融（r34 新增，核心加速器）

**原理**：全 paired runs 贵且慢（每配置 ≥2 域 × 多 run）。先用归因方法把 7 段 prompt 缩到 top-k 嫌疑段，再只对 top-k 跑 paired runs 确认。两层：

### C1 注意力/归因分析（离线，零 arena 成本）
- 方法：对已有 run 的 transcript（decomp 仓 `tasks/p1/stage*/transcript-*.jsonl` + arena 会话导出）做 token 级归因——若本地 vLLM 环境可用（qwen3.8-27b-w8a16 @ 100.112.53.47:8000，L1 batch2 用过），用 attention rollout 或 integrated gradients 算"每段 prompt 文本 → 关键输出 token"的归因分数；模型不可用则降级为**行为代理指标**（见 C2）
- 产出：每段 prompt 的归因排名 + 置信说明（attention 归因在 decoder-only 模型上是近似，conf 上限 0.5，只用于排序不用于判定）

### C2 行为代理指标（零成本，对已有工件直接算）
对每段 prompt 找它的**签名行为**（该段要求的具体动作痕迹），在历史工件里统计出现率：
- 候选集冻结声明 → 工件中"冻结/frozen"显式声明的出现率 + 后续阶段漂移次数
- 证据来源完备 → 主张带 URL/时间戳的比例
- owner 标注 → 步骤带 owner 字段的比例
- Reviewer 质检标准 → reviewer 工件是否逐条对照质检项打勾
- ralph web-llm 命令段 → 工件中该命令的真实调用记录（预期≈0，坐实无效负载）
出现率低 + 无对应质量差 = 强嫌疑段；出现率高且质量相关 = 保护段。

### C3 定向 paired runs（只对 top-k 嫌疑段，k≤3）
- 配置：A 全量 / B 删 top-k 嫌疑段（一次删一个，k 个配置）/ 阳性对照（删候选集冻结，预期 M8 降）
- 样本：≥2 域 × 2 run/配置；度量 M8（核验真实性率，Part A 协议）+ M9（token 差，bili.log 口径）
- 判定：M8 不降且 M9 显著升 → 移除该段；M8 降 → 保留并记录机制
- **顺序门禁**：C1+C2 完成且 top-k 选定后才开 C3；C3 方案本身先过一轮对抗核验（r29 标准）

## Part D: 结构整改（实验资产归位，pfb 仓内）

新建 `experiments/` 顶层目录：
```
experiments/
  README.md          # 实验索引：每个实验一行（目的/状态/结论指针）
  T8-audit/          # Part A 审计表
  T8-lit/            # Part B 文献调研
  T8-ablation/       # Part C: design.md(方案) + attribution/(C1-C2) + runs/<domain>-<config>/ + report.md
```
旧资产迁移：`loop-artifacts/stages/` 按任务归档到 `experiments/<task-id>/stages/`；`bench/self-opt-tester/` 原地保留但登记进 README。迁移走 git mv，历史可溯。

## 验收标准

1. Part A 审计表覆盖全部历史核验工件，每条有三测结果
2. Part B ≥4 问全答，每答 ≥2 独立来源 + conf，经对抗核验（r29）
3. Part C1/C2 归因排名 + 行为代理指标表落地，top-k 嫌疑段有明确选择理由
4. Part C3 定向消融 per-段落 verdict（有用/无用/未决 + 证据）；无用段落实际从 workspace loop/prompt-first/ 移除并 sync pfb
5. pfb experiments/ 结构落地，README 索引齐全

## 失败降级

- vLLM 环境不可用 → C1 降级为纯 C2 行为代理（如实标注 conf 降档），不阻塞 C3
- arena paired runs 成本过高 → 先交 Part A+B+C1/C2（零/低成本成果），C3 标 pending
- 单 run 超时 → 重跑 1 次，仍死标 VOID 换下一域
- 文献某问穷尽渠道无答案 → 标"信息搜集瓶颈"（r29 停止条件），不编
