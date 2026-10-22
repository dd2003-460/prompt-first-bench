# RALPH 因素/任务动态分解重构计划

> 目标：把 RALPH 从「卡片中心、刚性强制」的编排，重构为「字段中心、动态、可跨节点流动」的编排，
> 让弱模型（本地 35B）在外部信息充足时也能稳定跑通分解闭环，并提升普通 agent 的执行稳定性与最终质量。
> 背景：当前 `D1-ralph-smoke-matrix` 卡在 stage 01 r1，Commander `Recombobulating 2h35m`，
> 8+ 个 invalid-agent-output，根因是 enforce hook + mutation ban 与弱模型冲突导致死循环。

---

## 0. 当前卡点诊断（已验证）

- 现象：stage 01 r1 主 agent 空转 2h35m；报错 `RALPH_TASK_CARD ... (mode=enforce)`；
  `stages/01/r1/` 下 8+ 个 `.invalid-agent-output.md`；`completed_cards: []`。
- 根因：协议清晰但**刚性过强**。`enforce` 把"任何偏离"变成致命阻断；Commander 禁写。
  35B 一旦偏离即用硬错误打断，且无法自愈 → 死循环。
- 结论：**流程对强模型可操作，对弱模型因刚性强制而脆弱**。重构方向 = 放宽约束 + 字段中心化。

---

## 1. 核心转向：卡片中心 → 字段中心（field-centric）

- **节点（node）= 一组必须满足的条件（字段）**，不再是硬编码的卡片分类。
- **字段是一等公民**，可跨节点流动、可被回填、可动态新增。
- 节点完成判据：`所有 required 字段的 disposition ≠ pending`。
- 主 agent 不再被迫走"builder/gate/assemble/validate/apply"刚性五步协议，
  而是**填一张结构化字段表**；偏离不再致命，只是字段未填满。

### 放宽主 agent 限制（Phase 1，先止血）
- 去掉 `RALPH_TASK_CARD` 的 `mode=enforce` 致命阻断 → 改为 soft 提示/校验。
- 去掉 Commander 的 Write/Edit 禁令（mutation ban）→ 允许主 agent 直接写字段切片。
- 只把**模板文件位置**告诉主 agent（stage-contract、submission-template、输入包），
  由它按模板自行决定如何分解与派发，而非由 hook 强塞卡片。
- **验证点**：放开后当前 `D1-ralph-smoke-matrix` 是否不再 2h 空转、能否推进到 stage 02。

---

## 2. 字段模型（核心机制）

每个字段带 `disposition`（处置状态）：

| disposition | 含义 | 是否需要人类 | 谁来填 |
|---|---|---|---|
| `confirmed` | 已知背景 / 给定条件 | 否 | 直接作为节点已有条件 |
| `assumed_default` | 不确定偏好（字段的具体**范围**未知） | **否** | 默认「全范围」，soul 默认画像兜底 |
| `research_required` | 未知信息（如最新显卡、价格行情） | 否（subagent 调研） | 派发调研 subagent 填入带证据的字段 |

- **已知背景字段 = 已满足条件**（节点起点）。
- **中间字段 = 不确定偏好 或 未知信息**：
  - 不确定偏好（范围未知）→ `assumed_default`，**无需人类输入**，默认全范围。
  - 未知信息（需事实）→ `research_required`，真正需要填入的需求字段。
- **动态性**：允许新增字段 = 节点条件数动态增加；停止规则：字段一旦可确认/可推断/可研究即停止继续拆分（禁止无穷拆词）。

---

## 3. 动态分解执行路径

1. 主 agent 读模板 + 输入包，按语义角色（`background / decision_object / objective / comparison_set / constraints / deliverable / uncertainty`）拆出字段。
2. 主 agent **直接填已知字段**（廉价，可增量"一次填一个词"），不确定偏好默认全范围。
3. 剩余 `research_required` 字段 → **按字段派发 subagent**：每个 subagent 模板只接收一个字段参数，只填那一个字段（窄任务、高成功率）。
4. 字段回填 → 状态机推进到下一节点；父节点填满的字段成为子节点的 `confirmed` 给定条件。
5. 递归 coarse-to-fine，直到所有 required 字段都带证据填满 → **标准分解完成**。
6. 剩余：动作 / 架构级执行分解（同一套机制：字段最终变成 `action` 字段，派发执行 subagent）。

---

## 4. 状态机改动

- `node = { required_fields[], completion: 所有 required 字段 disposition ≠ pending }`。
- **字段跨节点传递**：父节点填满的字段 → 子节点 `confirmed` 条件。
- **分支条件**：字段值决定子字段需求。例：若 `gpu_vendor = NVIDIA` → 需要 `cuda_version` 字段；
  若 `= AMD` → 需要 `rocm_version` 字段。分支本身也是字段触发的子节点展开。
- **门禁（gate）判据变为机械可验证**：`所有 required 字段都有 evidence_refs 填满且 disposition ≠ pending`；
  不再依赖弱模型自由写一段 "verdict: pass" 散文。
- 调研 subagent 只返回一个字段的 `{value, evidence_refs, confidence, disposition}`，结构极窄，弱模型也能稳定产出。

---

## 5. 可行性评估

**可实现**，且主要是"把现有结构升级"而非重写：

- `task_spec` 本就是结构化字段（已有 `attribute_matrix / assumptions / constraints`）→ 字段模型是其自然扩展。
- `enforce` 改 soft、`mutation ban` 放开 → 改动集中在 `hooks.py` / `stage_policy.py`。
- 节点完成判据从"卡片集合"改为"字段集合" → 改 `protocol.py` 的 gate/validation。
- 字段流转 → 改 `state.py` 的 apply/persist。
- 按字段派发 → 改 `prompt_renderer.py` 的模板渲染（从"卡片清单"改为"字段清单 + 每字段 subagent 模板"）。

主要工作量在 prompt 模板重写与协议判据改造，**不涉及状态机语言/转移/门禁的语义重写**（保持原有 stage 推进语义）。

---

## 6. 泛化到任务分解（coarse-to-fine / 分支条件）

- **粗到细**：顶层节点字段少而抽象 → 每个字段展开成子节点（自带字段）→ 递归，直到字段可证据化填满。
- **分支条件**：字段值触发不同子字段集（见 §4 的 gpu_vendor 例子），天然支持决策树式分解。
- **执行分解**：字段最终收敛为 `action` 字段（具体可执行步骤），同一机制派发执行 subagent →
  从"研究分解"平滑过渡到"动作/架构分解"，无需换一套编排。
- 这套机制对**任意"目标→需填条件→派发调研/执行"类任务**通用，不限于 GPU 调研。

---

## 7. 对普通 agent 稳定性 / 质量的提升（外部信息充足时）

- **稳定性 ↑**：
  - 结构化字段契约替代自由协议 → 弱模型"能做错的地方"变少。
  - 默认全范围偏好 → 几乎消除 `ask_human` 阻断（弱模型最易卡在追问上）。
  - 每 subagent 任务极窄（只填一个字段）→ 上下文不溢出、成功率高。
  - 偏离从"致命阻断"降级为"字段未填满"→ 不会死循环。
- **质量 ↑（外部信息充足时）**：
  - 调研 subagent 带 `evidence_refs` 回填字段 → 每个结论可溯源。
  - 门禁机械保证"无 required 字段遗漏"→ 分解完整性可验证，不会漏字段就放行。
  - soul 默认画像保证偏好一致性，避免弱模型随机假设。
- **风险 / 需验证**：
  - 字段膨胀 / 无限拆 → 必须有停止规则（§2 已列）。
  - 主 agent 填字段可能循环 → 用"窄任务 + 默认全范围 + 字段去重"约束。
  - 门禁若纯机械可能放过低质量证据 → 保留 `research_required` 字段的置信度阈值。

---

## 8. 实施步骤（建议顺序）

- **Phase 1（止血）**：`enforce` 改 soft + 放开 mutation ban + 只给模板位置。
  验证：当前 `D1-ralph-smoke-matrix` 能否推进过 stage 01。
- **Phase 2（字段模型）**：字段 `disposition` 三态 + 节点完成判据改为字段集合；state 支持字段流转。
- **Phase 3（按字段派发）**：subagent 模板改为"单字段参数"；主 agent 填已知、默认偏好全范围、派发未知。
- **Phase 4（分支 + 递归）**：字段值触发子字段集（分支条件）；coarse-to-fine 递归分解。
- **Phase 5（评估）**：在 35B 上跑基准，对比"卡死率 / 分解完整性 / 最终质量" vs 旧刚性编排。

---

## 9. 开放问题（待确认）

- 主 agent「一次填一个词」的粒度如何约束，避免反复改写同一字段？→ 建议字段级 idempotency + 去重。
- `assumed_default` 全范围是否需要在最终交付里标注"此为默认假设，非用户指定"？→ 是，门禁摘要须显式列出 assumed 字段。
- 分支条件展开的子节点，其 required 字段是否也走同一 gate？→ 是，统一字段门禁。
