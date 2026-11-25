# novelty-check — 查新（任务书模板）

> 来源（只读）：`aris/skills/novelty-check/SKILL.md`
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。原文引擎是 Codex MCP
> （`mcp__codex__codex`，model `gpt-6-astra`，reasoning `xhigh`）；本模板把所有
> "怎么调模型"处替换为 `{{EXECUTOR}}`。**核心逻辑（三阶段 / verdict limits
> 逐字块 / 反幻觉规则）原样保留。**
>
> 用法：`{{EXECUTOR}}` = 一次全新上下文的模型调用（本地 qwen3.8-27b subagent，
> 或 arena 跨模型族通道）。跨模型不变量：`{{EXECUTOR}}` 的模型族必须 ≠
> 执行器模型族。
>
> ⚠️ 本 skill 的 Phase B（文献搜索）原文用 WebSearch/WebFetch。本地移植时该阶段
> 走我们自己的检索通道（arena 多搜索 / arXiv API），产出 `NOVELTY_DOSSIER.md`
> 后再进 Phase C 的 `{{EXECUTOR}}` 调用。

## 材料黑白名单

原文没有显式 ✅/❌ 列表，黑白名单隐含在流程里（Phase B/C 边界）：

✅ 给什么（Phase C 原文）：
> "Write a dossier file such as `NOVELTY_DOSSIER.md` (or a project-local
> equivalent) containing the method description, core claims, candidate
> papers, and the exact questions below, then send only the file path"

dossier 内容（原文 "Dossier contents should include"，逐字）：
- The proposed method description
- All papers found in Phase B
- Ask: "Is this method novel? What is the closest prior work? What is the delta?"
- The NOVELTY VERDICT LIMITS block below, verbatim — the reviewer judges under it

> "When the method description plus the Phase-B paper list is more than a short
> note, avoid pasting it inline into the MCP prompt."（长材料走文件，只传路径）

❌ 不给什么：
- 任何先前 novelty 结论 / 先前对话上下文（fresh 调用，零上下文）。
- 凭记忆编造的文献——原文反幻觉规则（Important Rules 末条，逐字）：
  > "**Anti-hallucination for Closest Prior Work.** Every paper in the
  > prior-work table must pass pre-search verification ... Never fabricate
  > arXiv IDs, DOIs, or titles from memory."
  （原文用 `verify_papers.py` 三层 arXiv/CrossRef/Semantic Scholar 核验；
  移植时用我们自己的文献核验通道，核验不了的候选标 `[UNVERIFIED]` 并显式
  呈现不确定性，不丢弃。）

## 执行 prompt

### Phase A：提取核心 claim（执行器自己做，不调模型）

1. 读方法描述
2. 识别 3-5 个承载 claimed delta 的核心技术 claim：方法是什么 / 解决什么问题 /
   机制是什么 / 与显然 baseline 的差异

### Phase B：多源文献检索（每个核心 claim 都搜）

原文：对每个 claim 用全部可用源搜（arXiv / Google Scholar / Semantic Scholar；
每个 claim ≥3 种 query 变体；2024-2026 年份过滤；查 ICLR/NeurIPS/ICML 2025-2026
+ 近期 arXiv preprints；对潜在重叠论文读 abstract + related work）。
**移植注**：此阶段走 arena 多搜索 / arXiv API，不用原文 WebSearch。

### Phase C：跨模型核验

`{{EXECUTOR}}`（全新上下文，xhigh 档）：

```
Read the novelty dossier at <absolute path to NOVELTY_DOSSIER.md> and
follow all instructions in it.
```

dossier 内必须含上面 ✅ 列的四项，其中 verdict limits 块**逐字**复制：

```
=== NOVELTY VERDICT LIMITS (these bound how you judge, never how widely you search) ===
Search exhaustively; judge calibrated. Two failures waste months equally:
passing an idea a published paper already contains, and killing a viable idea
because the territory has neighbors.
1. Proximity is information, not a verdict. Someone working nearby goes in the
   report; it is not by itself a reason to reject.
2. ABANDON has exactly one qualification: a specific published paper already
   contains this result — name that paper. No named paper, no ABANDON.
3. Crowded-but-deltaed is PROCEED: state the delta in one sentence a reviewer
   could verify. Thin or contested delta is PROCEED WITH CAUTION — say what
   would make it carry, not why it should die. CAUTION is not a safe middle:
   if you cannot name the specific thing that makes the delta thin, the
   verdict is PROCEED.
4. Concurrent or competing work is not a veto. That is a race — report it and
   let the user decide whether to run it.
5. A direct attack on a central problem is legitimate novelty when nobody has
   executed it well. "This area is hot" does not mean "this area is taken."
6. This check is an early gate, never the last one — more triage, pilots, or
   external review still stand between any idea and a paper, whatever order
   this run uses. A wrongly passed idea dies cheaply at one of them; a wrongly
   killed idea is never seen again. When torn between two verdicts, choose the
   more permissive one.
Say plainly when an idea clears the check. Do not manufacture overlap.
```

## verdict 映射表

原文 verdict 三值 + 判定规则（来自 verdict limits 块，逐字）：

| Verdict | 触发条件（原文语义） |
|---|---|
| `PROCEED` | crowded-but-deltaed：拥挤但有 delta，delta 能用一句 reviewer 可验证的话说出；或无法指出 delta 薄在哪（CAUTION 不是安全中间档：说不出 delta 薄的 specifics → PROCEED） |
| `PROCEED WITH CAUTION` | delta 薄或有争议——说清什么能让它立住，而不是说它该死 |
| `ABANDON` | **有且仅有**一种资格：某篇具体已发表论文已包含该结果——必须点名那篇论文。"No named paper, no ABANDON." |

评分锚点（原文 Phase D）：Score X/10，锚点 = 5/10 表示 "has clear neighbors
but a defensible delta worth a pilot"；1-3 保留给 "a named published paper
already contains" 的结果。

## 输出 schema

原文 Phase D 报告结构（逐字）：

```markdown
## Novelty Check Report

### Proposed Method
[1-2 sentence description]

### Core Claims
1. [Claim 1] — Closest: [paper] — What stays unknown or different: [delta]
2. [Claim 2] — Closest: [paper] — What stays unknown or different: [delta]
...

### Closest Prior Work
| Paper | Year | Venue | Overlap | Key Difference |
|-------|------|-------|---------|----------------|

### Overall Novelty Assessment
- Score: X/10 (anchor: 5/10 = has clear neighbors but a defensible delta worth
  a pilot; reserve 1-3 for results a named published paper already contains)
- Recommendation: PROCEED / PROCEED WITH CAUTION / ABANDON (per the verdict
  limits: crowded-but-deltaed ground is PROCEED; ABANDON must name the paper)
- Key differentiator: [what makes this unique, if anything]
- Risk: [what a reviewer would cite as prior work]

### Suggested Positioning
[State the delta honestly in one sentence a reviewer could verify]
```

## 关键规则（原文 Important Rules，保留）

- 两种失败同等浪费数月：虚假 novelty claim，和有邻居就被放弃的可行 idea。
  两个方向都要 brutal honest——idea 过了检查就明说。
- novelty 可以活在组合或发现里，即使每个单独 claim 都 LOW——判 idea 不判单 claim。
- "Applying X to Y" 的 novelty 来自应用揭示的东西（非显然交互/失败模式/洞见）。
  判揭示，不判模板。
- 方法和实验设定都要查 novelty。
- 方法不新但 FINDING 新时，明确说出来。
- 永远查最近 6 个月的 arXiv——领域动得快。
- 反幻觉：prior-work 表里每篇论文必须过检索前核验；核验不了标 `[UNVERIFIED]`
  并呈现不确定性；绝不凭记忆编 arXiv ID / DOI / 标题。
