# Workshop Draft 红队审视（research-verify-redteam）

> 日期 2026-11-24 01:25 · 对象 `workshop-draft-metacog-20261122.md`（180 行，12.2K 词）
> 方法：不辩护，主动攻击自己的产出。列最狠质询 → 判防御 → 排缺口 → 下结论。
> 与数字审计（`workshop-number-audit`）互补：数字审计守"承重数字对不对"，本审视守"claim 可防御性"。

## 核心判据
可发表性 = f(我们做了什么, 审稿人会打哪, 我们守得住吗)。只看第一项 = 自我评估（不够）。

## 质询（按杀伤力排序）+ 防御判定

### ① 构念错配污染覆盖轴（最狠，真实缺口）
**审稿人**：你的 headline（finding 3：预算买覆盖）是拿模型输出对 gold 树算的覆盖度，但 §6 自己承认——题面（32K floor、模型自选候选集）和 gold 树（固定 64K、固定候选集 3090/M2Ultra/L40S/A100/V100）是**两道不同的题**。那低覆盖分到底是"预算不够"还是"模型在解另一道题"？你的核心曲线被构念错配污染了。
**防御**：§6 已声明（construct mismatch，2026-11-23 发现），depth 轴 question-agnostic 不受影响，给了 fix 方向（pin context length + candidate set）。
**判定**：**部分守住（已标注，fix 在排队）**。draft 已在 finding 3（§4.1）和 §4.4 内联标注"coverage axis partially confounded by the construct mismatch in §6"，depth 轴 question-agnostic 不受影响——"至少标注"层已守住。剩余是真正的 fix（pin 题面 context length + candidate set 后重跑覆盖轴），属排队实验（不烧 GPU 但要重跑 15 run），不是标注缺口。投稿前 finding 3 的覆盖曲线结论已 scope 到"pre-pin"，可投但覆盖轴的强 claim 要等 pin 后重跑。

### ② 零结果的功效问题（headline 元认知发现，真实缺口）
**审稿人**：你的核心发现是"元认知随预算不变"（ANOVA F(2,12)=0.036，null）。但 n=3/tier 的功效太低——"不变"可能是**没检出效应**，不是"证明了不变"。null ≠ evidence of invariance。
**防御**：§6 给了 detector-robust 核心（monitoring 轴在 8-pattern 和 22-pattern 两个 detector 下都 flat，F=0.033），部分缓解。
**判定**：**已补（2026-11-24）**。功效分析已算并写入 draft §6：n=15 下 detect large effect (f=0.40) 功效仅 21.5%，medium 11.0%——null 严重 underpowered。headline 已从"verified dissociation"降级为"suggestion with stated power limits"。复算 F=0.036 对齐 draft（monitoring/gap 轴，每档 0.099/0.100/0.108）。剩余：50/719 端点功效仍低，等 replication 落地。

### ③ gold 同族先验未受控（stated，缓解非控制）
**审稿人**：gold 树是 origin:ai 重建、和模型同 27B 族。覆盖分测的是"和这个分解的相似度"，不是"和 ground-truth 的相似度"。偏差没消失，从打分函数搬进了参考树。
**防御**：§6 诚实声明（bias moved into reference），两个缓解（gold 比自然输出难 mean cov~0.35；跨域近零覆盖证明 question-specific 非 generic prior），leakage check 通过。
**判定**：**守得住（诚实降级）**，但同族先验本身**没有对照臂**（§6 明说 "not controlled"）。workshop 可接受（stated not hidden），但这是"已知缺口"不是"已解决"。

### ④ n=3 端点 CI ±0.29（守得住）
**审稿人**：50/719 档 n=3，CI 宽到 ±0.29，你的"peak"是噪声。
**防御**：§6 已降级——150 "peak" 明确标为 verbosity-driven rubric noise（control arm：LLM depth 与机械 depth r=0.049 不相关、与 answer length r=0.648）；robust 部分是 breadth-vs-depth split on realized node counts（n-independent）。
**判定**：**守得住（诚实降级 + 控制臂）**。peak claim 已主动放弃，只留 n-independent 部分。

### ⑤ gap marker 是 prompt-elicited 非自发（headline 构念，stated）
**审稿人**：你的元认知轴测的是"模型是否按指令打 [待核验] 标签"，不是"模型是否真有元认知"。82%（GPU）的 gap 命中是 prompt 指令的标签——你测的是指令遵循，不是 self-monitoring。
**防御**：§6 声明（prompt-elicited vs spontaneous），判断"在哪打"仍是模型的，budget-invariance 结论不依赖这个区分（prompt 跨 run/budget/domain 一致）。
**判定**：**守得住（构念 scoping）**，但 headline 的"agent knows it doesn't know"必须读成"when prompted, marks uncertain claims"——这个 scoping 已经写进 §6，防御充分。

### ⑥ 单模型无能力曲线（scoped，守得住）
**审稿人**：只有 27B，没有 7b/70b，"open-weight ~27B range" 之外不能外推。
**防御**：§6 声明，claim 已 scope 到 27B range。
**判定**：**守得住（scoped）**。真实缺口但已声明边界。

### ⑦ 检索通道静默故障 + 60.6% 无 URL（stated，守得住）
**审稿人**：source-anchored verification 只在有 URL 的子集上可算，60.6% search 节点没存 URL，跨 run 比较不可比。
**防御**：§6 声明两个独立问题（retention gap vs channel outage），r3 已排除，fix 方向给了（unconditional URL persistence）。
**判定**：**守得住（stated + 排除受污染 rep）**。

## 缺口排序（硬伤 > 缓解中 > 在补）

| 序 | 质询 | 严重性 | 状态 |
|---|---|---|---|
| 1 | ① 构念错配污染覆盖轴 | **硬伤** | 声明未修，**不依赖在飞数据**，现在可补（pin 题面） |
| 2 | ② 零结果功效 | **硬伤** | 声明 detector 稳健，**缺功效分析**，现在可补（算 power） |
| 3 | ③ 同族先验未受控 | 缓解中 | stated，无对照臂，workshop 可接受 |
| 4 | ④ n=3 端点 | 在补 | 已降级，719/Q7 落地后 n↑ |
| 5 | ⑤ prompt-elicited | 缓解中 | stated + scoped，防御充分 |
| 6 | ⑥ 单模型 | 缓解中 | scoped，future work |
| 7 | ⑦ 通道故障/retention | 缓解中 | stated + 排除 r3 |

## 结论

**审稿人打不到致命处的地方**（claim 已主动放弃 / 诚实降级）：④ peak 已放弃只留 n-independent 部分；⑤ 构念已 scope 到 prompt-elicited；⑥⑦ 边界已声明。这些守得住。

**真实缺口（stated not hidden，但需补才能投）**：
1. **① 构念错配**——最该补，且**现在就能做**（不烧 GPU、不依赖在飞数据）：pin 题面的 context length + candidate set，重跑覆盖轴。或至少把 finding 3 的覆盖曲线明确标注"pre-pin，构念错配未控"。
2. ~~**② 零结果功效**~~——**已补（2026-11-24）**：功效分析写入 draft §6（large effect 功效 21.5%），headline 降级为"suggestion with stated power limits"。

**投稿就绪度判定**：结构上能投（References 闭环 15/15、8 节完整、0 TODO）。两个硬伤的防御状态：
- **① 构念错配**：已内联标注（finding 3 + §4.4 + §6 三处），覆盖轴 claim 已 scope 到 pre-pin——**可投**；强 claim 等 pin 题面后重跑（排队实验）。
- **② 零结果功效**：已补功效分析（large effect 21.5%），headline 降级为"suggestion with stated power limits"——**已守**。

**红队结论**：当前 draft 在两个最狠质询上都有防御（①标注+scope，②功效声明+claim 降级），其余 5 个质询（③同族先验/④n=3 端点/⑤prompt-elicited/⑥单模型/⑦通道故障）均 stated not hidden。**没有"打穿就致命"的未防御缺口**。剩余提升项（非阻塞投稿）：pin 题面重跑（覆盖轴强 claim）、replication 落地（50/719 端点功效）、719 nodepth + Q7 跨题（在飞）。
