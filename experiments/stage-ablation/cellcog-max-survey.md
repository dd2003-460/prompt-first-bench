# CellCog Max — DRB #1 Harness 结构调研（idea #46）

> 来源：cellcog.ai/blog/cellular-multi-agents + cellcog.ai/blog/manager-agent-architecture + cellcog.ai/benchmarks
> 调研时间：2026-11-12
> 状态：✅完成（公开信息层面；prompt 结构/路由细节 CellCog 明确不公开）

## 一、它是什么

CellCog Max = CellCog 公司的通用 AI 员工平台（不是专用 deep research agent），跑在 Claude Opus 5.5 上。
DRB 排名：#1 / 18 entries，overall 56.72（GPT-5.5 judge，2026-10-21 读取）。
四维全第一：comprehensiveness 57.06 / insight 57.67 / instruction following 56.58 / readability 53.81。

关键事实：**它是通用引擎，不是研究专用**。同一个 harness 做代码、dashboard、PDF、视频、音频、研究。
创始人原话："We are not a research-only company. We just happened to rank first at research."

## 二、架构核心：Cellular Multi-Agents

**设计哲学**：为终局（endgame）设计，不为当前模型能力设计。
- 单元 = "cell"（细胞）：拥有角色/任务/工作片段的 agent，能创建其他 cell、记忆、可替换
- 组织形态 = 自组织网络：agents hire/onboard/manage each other
- 核心信念：harness 是下一个战场（模型在收敛，harness 没有）
- 时间线：架构决策 2025-10，DRB #1 2026-07

**与我们的对比维度**：

| 维度 | CellCog | 我们 (pfb S5) |
|------|---------|---------------|
| 分解方式 | Manager 按 **outputs/artifacts** 分解（verified source ledger, market comparison matrix, risk register...） | 按 **dimensions** 分解（架构/显存/接口...） |
| 分解粒度 | 每个子任务 = 一个有类型 artifact + 验收标准 | 每个节点 = 一个 claim + verified/degraded/failed 状态 |
| 边类型 | 未公开（"keep the how"） | 三边分类（笛卡尔积/商/随机耦合）✅已实现 |
| 停止条件 | Budget caps: child count / depth / concurrency / elapsed time / spend | max_nodes + verify_threshold + contribution_threshold ✅已实现 |
| 核验 | Review against child contract before synthesis; repair/retry/reroute/escalate | J_verify (verified/total ≥ 0.6) + rework loop |
| 防泄漏 | Context is task-scoped and source-versioned; worker credentials never cross child edge | 题目不进 prompt（硬约束） |
| 目标函数 | 未公开（acceptance criteria per parent） | U(T) = C·A·S − λ·cost(T) [待标定] |
| 贡献估计 | 未公开（routing score = capability fit + eval fit + latency + cost + context + capacity） | classify_edge 返回 contribution 0~1 ✅已实现 |
| MECE | D 提到用了 MECE（微信兄弟说的），CellCog 博客未直接提 MECE 这个词 | 三边分类比 MECE 多一层：MECE 只管"拆得对不对"，不管"怎么展开" |

## 三、Manager-Agent 架构细节（公开部分）

### 10 阶段控制循环
1. Intake → 解释目标
2. Risk classification → 数据/动作/审查需求
3. Decomposition → 创建子贡献 + 依赖（graph validity / depth / child-count cap 门禁）
4. Eligibility → 请求候选 workers
5. Routing → 排序 eligible candidates
6. Assignment → 创建 bounded child contract
7. Supervision → 观察状态 + 异常处理
8. Review → 评估 artifacts + evidence
9. Repair → retry / revise / reroute / escalate
10. Closure → 综合 accepted contributions

### 关键设计原则
- **Decompose by outputs, not job titles**：弱分解 = "researcher/writer/reviewer"；强分解 = 命名具体 artifact
- **Graph constraints outside the manager**：task-graph service 拒绝 cycles / depth > cap / child count > cap / deadline > parent
- **Separate control plane from work plane**：manager 提议，deterministic services 执行
- **Parent closure ≠ all workers returned**：必须 parent acceptance criteria pass
- **Version every material graph change**

### Worker Capability Registry
- Declared / Verified / Current eligibility 三层分离
- Hard filters before ranking（schema / tenant / policy / risk / health / capacity / budget）
- Routing score = w1(capability) + w2(eval) + w3(latency) + w4(cost) + w5(context) + w6(capacity)

## 四、CellCog 明确不公开的

> "The rule for this series is that we publish the why and the what, and we keep the how. Message formats, routing, scheduling and prompt structure stay in-house."

所以：
- 具体 prompt 模板 ❌
- MECE 分解的具体实现方式 ❌（D 的微信兄弟说用了 MECE，但 CellCog 博客没直接提）
- 路由/调度的具体算法 ❌
- 研究模式 vs 通用模式的差异 ❌

## 五、我们的剩余优化空间

### 已有优势（CellCog 没公开做的）
1. **三边分类**（笛卡尔积/商/随机耦合）→ 三种不同展开策略。CellCog 的 manager 只说了"decompose by outputs"，没区分边的语义类型。如果他们的分解也是纯 MECE（穷举式拆分），那在商结构上也会遇到 v17 式的爆炸——除非他们用 budget cap 硬压。
2. **贡献阈值停止**（contribution < 0.10 → 不展开）→ CellCog 有 budget cap 但没公开"按边际贡献过滤"的逻辑。
3. **U(T) 目标函数**（C·A·S − λ·cost）→ CellCog 的 acceptance criteria 是 per-parent 的，没有全局目标函数。
4. **防泄漏硬约束**（题目不进 prompt）→ CellCog 用 task-scoped context，但没明确说"题目本身不可见"。

### 可能的差距（CellCog 可能做了但我们没做的）
1. **Artifact-typed decomposition**：CellCog 每个子任务有明确的输出类型（source ledger / comparison matrix / risk register），我们的节点只有 claim + status。如果 DRB 评分看重"报告结构完整性"，artifact typing 可能直接提升 comprehensiveness 分数。
2. **Worker specialization + routing**：CellCog 有不同 specialist（research / code / review），按 capability 路由。我们是单一 LLM 做所有事。这解释了为什么 CellCog 是"通用引擎"但研究分高——它的 research specialist 可能比通用 prompt 更聚焦。
3. **Repair loop 更细**：CellCog 有 retry / revise / reroute / escalate 四种修复路径，我们只有 rework（重跑同一节点）。
4. **Institutional memory**：CellCog 的 cell 跨 session 记忆（"what a role learned, carried from one working session to the next"）。我们每次 run 从零开始（虽然有 checkpoint resume）。
5. **Risk classification before delegation**：CellCog 先分类风险再决定谁来做。我们没有这一步——所有节点走同一条路。

### 行动建议（按性价比排序）
1. **Artifact typing**（低成本高收益）：给每个节点加 `artifact_type` 字段（spec_fact / tradeoff_analysis / risk_item / recommendation / citation_check...），prompt 里要求模型输出时标注。这可能直接提升 DRB 的 comprehensiveness + readability 分数。
2. **Repair 分级**：当前 rework = 重跑。改成 retry（同参数重跑）/ revise（换角度重跑）/ drop（放弃标记 degraded）三级。
3. **Specialist prompt 分化**：不同 edge_type 用不同的 decompose prompt（已经做了 hint 注入，但可以更进一步——quotient 节点用"trade-off analyst"人设，stochastic 用"risk analyst"人设）。

## 六、DRB 评分机制（从 GitHub repo 确认）

- 100 PhD-level tasks × 22 fields
- 4 维度：comprehensiveness / insight / instruction following / readability
- Judge：GPT-5.5（RACE）+ GPT-5.4-mini（FACT citations）
- 评估代码开源：github.com/Ayanami0730/deep_research_bench
- 数据集：huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset