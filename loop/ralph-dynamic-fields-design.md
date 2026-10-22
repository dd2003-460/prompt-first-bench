# RALPH 动态字段驱动状态机设计

> origin: ai
> human intent: 放宽主 agent 强制派发约束，改为"字段三分法 + 动态增减 + 跨节点空缺传递"，用字段分流降低对本地小模型的往返依赖，提升稳定性；保留独立 gate 审计兜底质量。
> status: design

## 1. 目标与动机

当前实现强制主 agent（Commander）通过 `RALPH_TASK_CARD` 派发 builder 子代理，每个子代理只填 ≤3 个语义字段，运行时合并回 `task_spec`。这在本地小模型下已能跑通，但存在两类摩擦：

- **往返过多**：确定字段（已知背景）也要拆卡 → 派发 → 等 SubagentStop → 合并，增加 OMLX 并发请求，易被 prefill 守卫节流甚至死锁（实测 smoke 出现过）。
- **陌生 agent 难操作**：`_semantic_contract()` 偏抽象，无 few-shot，非领域专家看到 prompt 不一定能正确分解。

本设计用"字段即节点条件"统一 4.1 因素分解 / 4.2 信息搜集任务分解 / 4.3 执行动作分解：每一层节点只声明要填的字段，主 agent 直填确定字段，未知字段才派 subagent；空缺字段跨节点传递，下一节点把仍空缺者变成待填需求。

## 2. 字段三分法

每个字段标记来源，决定由谁填、怎么填：

| 类别 | 含义 | 无人类输入时的处置 | 谁填 |
|---|---|---|---|
| 已知背景字段 | 已有条件、确定值 | 直接填 | 主 agent 直填 |
| 中间字段·偏好 | 不确定范围的偏好 | 默认全范围（`disposition=assume`） | 主 agent 按 soul 默认画像填 |
| 中间字段·信息 | 不确定但可推断 | `disposition=inferred` + 证据 | 主 agent 填 |
| 未知字段 | 真正需外部信息填补的需求（最新显卡、价格行情） | 标记 `research`，不填 | 派 subagent 调研后填 |

`disposition` 沿用现有 `SEMANTIC_ROLES` 体系（`confirmed/inferred/assume/research`），不新增枚举。

## 3. 动态增删字段

节点 = 一组需满足条件（字段）。条件数量由主 agent 动态声明：

- `contracts.py` 已有 `factor_groups(state, stage, key)`，读 `task_spec.factor_roles` 自定义因素 → 动态生成 builder 卡。
- 扩展：开放主 agent 直接声明/追加 `factor_roles`（当前仅状态机间接用）。新增字段即新增"需满足条件"。
- 每卡仍可细化到 1 字段 / 1 词，降低单卡输出长度，防本地模型溢出。
- 注意：过度碎片化会增加调用次数，需平衡（建议每卡 ≤3 字段）。

## 4. 跨节点空缺字段清单

新增持久化字段 `task_spec.open_fields`：列出当前节点仍空缺、需下一节点填或派发的字段。

- 节点完成（advance）时，`reconcile_partial_merges` 逻辑扩展：把"已填字段"写回 `task_spec`，把"仍空缺字段"物化为 `open_fields`。
- 下一节点启动时读取 `open_fields` 作为"待填需求"，按 disposition 分流：确定/偏好主 agent 直填，未知派 subagent。
- 这把 1-loop 各阶段的"输入/输出契约"（`02-任务分解.md` 要求的 `input_refs`/`output_schema`）显式化为可机读的空缺清单。

## 5. Hook 放宽边界（保留 gate 兜底）

关键不变量：**未知字段与最终 advance 必须过独立 gate 审计**。

- 放宽：Commander 被允许 Write/Edit `task_spec` 中 `disposition ∈ {confirmed, inferred, assume}` 的字段（确定/偏好/可推断）。
- 保留：任何含 `research` 字段的任务、以及 `stage_result` 的 advance，仍由独立 `requirements-auditor` / `dag-auditor` / `evidence-verifier` 等 gate 卡审计，Hook 拒绝未过 gate 的 advance。
- `prompt_renderer.py` 第一动作闸门从"强制派发 builder"改为："确定字段可直填；仅未知字段须派发对应 subagent"。

## 6. 与现有代码映射

| 设计点 | 现有实现 | 改动 |
|---|---|---|
| 因素分解流程 | `contracts.py:_semantic_contract()` + `loop/1-loop/01-目标澄清.md` | 补 few-shot 示例 |
| 动态分桶 | `contracts.py:factor_groups()` / `SEMANTIC_ROLE_GROUPS` | 开放主 agent 声明 `factor_roles` 入口 |
| 字段合并 | `contracts.py:reconcile_partial_merges()` | 扩展写回 + 物化 `open_fields` |
| 强制派发闸门 | `prompt_renderer.py` 第一动作闸门 | 改为"确定字段直填 / 未知派发" |
| 独立审计 | `requirements-auditor` 等 gate 卡 | 保留，作为 advance 唯一闸门 |

## 7. 落地步骤（小步、可逆）

1. `01-目标澄清.md` 与 `_semantic_contract()` 补 1-2 个 few-shot 分解示例（先解决"陌生 agent 能否操作"）。
2. Hook 放宽：Commander 可写 `task_spec` 的 `confirmed/inferred/assume` 字段；验证 95 项测试仍过。
3. 物化 `open_fields`：在 `reconcile_partial_merges` 写回时生成空缺清单。
4. 保留 gate 审计为 advance 唯一闸门；补回归测试锁死。

## 8. 对任务分解的迁移

"字段即节点条件"统一 4.1/4.2/4.3：

- **粗到细执行字段分解**：把执行动作建模为字段（`action`/`owner`/`branch_condition`），每层节点只声明本层字段，下一层继承父层已填 + 新增本层空缺。复用 `02` 的 DAG / `parallel_group_id` / `join_policy` 作为字段依赖图。
- **分支条件**：字段 `disposition` 即分支依据——`assume` 走默认全范围、`research` 派 subagent、`confirmed` 进下一节点。比"先推断后提问"闸门更机械、更可自动化。

## 9. 稳定性与质量评估

**稳定性（提升）**：
- 确定字段主 agent 直填，省去"派发→等 SubagentStop→合并"往返，减少 OMLX 并发请求 → 降低被 prefill 守卫节流/死锁概率。
- 主 agent 上下文连贯填已知字段，避免拆卡丢失前后文、partial 文件缺失导致 merge 失败。

**质量（不降反升）**：
- 确定/偏好字段主 agent 直填：上下文连贯。
- 未知字段仍派 subagent + 独立 gate 审计：保住深度调研与防跳步底线。
- 红线：若彻底去 Hook，普通 agent 会省略 gate → 质量塌方。正确做法是"放宽 Commander 写确定字段，但未知字段与最终 advance 仍过独立 gate"。

**运维层卡死（非状态机问题，需单独处理）**：实测主 agent 卡死主要来自 OMLX 端口配错（`ANTHROPIC_BASE_URL=http://127.0.0.1:8000` 但服务起在 8653 → `ConnectionRefused`）、Claude Code 首次目录信任提示 + 无 TTY、OMLX 0.5.1 prefill 守卫节流。这些需保证"服务端口与 `ANTHROPIC_BASE_URL` 一致 + tmux 提供 TTY + 信任目录"，与字段机制正交。
