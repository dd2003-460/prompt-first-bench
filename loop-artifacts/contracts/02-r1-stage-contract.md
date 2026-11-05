# RALPH 字段中心 · 阶段契约

阶段：02-r1

## 你只维护一张字段表（不强制固定任务文件）

- 权威输入：`loop-state.json`、`loop-artifacts/contracts/02-r1-stage-contract.md`、`loop-artifacts/contracts/02-r1-submission-template.json`。
- 用 `ralph field-apply` 把字段原子写入字段表（**禁止直接 Write/Edit `loop-state.json`**，运行时只读它）。
- 每条字段形如：concept / role / attribute / disposition / rationale / evidence_refs / confidence / impact / reversible。
- disposition 取英文枚举值之一：confirmed / assumed_default / research_required / pending；直接照抄。
- 例：{"concept": "字段名", "role": "背景", "attribute": "具体属性", "disposition": "confirmed", "rationale": "...", "evidence_refs": [], "confidence": 1.0, "impact": "material", "reversible": true}。
- `confirmed`=已知背景或已有可复核证据的事实；`assumed_default`=不确定偏好（默认全范围，无人类输入）；
`research_required`=未知事实（派单字段调研 subagent 带回 evidence_refs）；`pending`=尚未处理。当前价格/在售性/最新兼容性/基准等外部事实在查到具体来源前不得标 confirmed。
- 对每个 `research_required` 字段，用 Agent 派**只填这一个字段**的窄调研 subagent；它把该字段 JSON 交回，你合并进表。
- 每回填一个字段，若引出新的未知项，作为新的 `pending` 字段加进同一张表（差集=新字段，自动增殖）。
- **只回传空缺**：系统只告诉你还差哪些 `pending` 字段；你照着补，不会因为没一次交齐而失败。
- `loop-artifacts/` 下的长文档（契约/输入包/提交模板）由子代理读取；Commander 自身直接维护字段表，不要再派发任务卡。

## 提交（用命令，不要输出 token）

字段 + 本阶段 required_outputs 齐全后，**用命令显式推进**——运行时不会解析聊天里的 `<RALPH_STAGE_RESULT>` token（只有 stage 01 字段齐全会**自动**推进）。
正确动作：
1. 若本阶段字段有更新，先落盘：`ralph field-apply . loop-artifacts/stages/02/r1/fields.json`（或写入同目录字段增量文件）。
2. 写 advance 动作文件 `loop-artifacts/stages/02/r1/advance.json`：
```json
{
  "action": "advance",
  "status": "passed",
  "stage_id": "02",
  "revision": "r1",
  "next_stage": "<节点图上本阶段的后继 id>",
  "payload": { "stage_review": "<简述已满足的字段条件与依据>", 
                "task_spec": "<即 loop-state.json 里的 task_spec（含完整 attribute_matrix）>" }
}
```
3. 运行 **`ralph apply . loop-artifacts/stages/02/r1/advance.json`**（等效 `ralph validate --result ... --apply`）即完成推进；运行时自动校验、原子落盘。

只有「用户/项目/环境都无答案、不能推断或研究、且会改变硬可行性/硬预算/验收」的字段，
才在 `payload.questions` 一次性提问；否则不要用 `blocked_human` 卡住。

## 02：调研分解结果（字段化）

对 01 的每个 `research_required` 字段派窄调研 subagent，把结果写回 `attribute_matrix`（带具体 evidence_refs）。站点首页无效；当前市场事实须额外填 observed_at（ISO 日期）。
若同一字段的 WebSearch/WebFetch 连续失败、且已配置两个网页 LLM，可运行 `ralph web-llm-check` 询问具体来源线索；LLM 回执不是一手证据，必须据此再验证实际页面，做不到就保留 research_required/uncertain。
调研完成字段置 `confirmed` / `assumed_default`；引出新未知项作为 `pending` 字段增殖，直到无 `pending`。
同时为每个分解项整理「后续执行需要什么」雏形，供 03 细化。本阶段不做交叉验证（在 02.5）。
