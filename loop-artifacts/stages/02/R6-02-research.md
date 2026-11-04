# R6 · 阶段 02 信息调研：阶段门控的既有实践

> 规则包：`00-common-review.md` + `02-information-research.md` + `02.5-cross-check.md`（2,807 o200k，阶段门控）

## 问题

INDEX 路由 = 三层（INDEX → 阶段包 → 产出）还是两层？学界/工业界同类做法踩过什么坑？

## 证据

### E1 · Anthropic Agent Skills：progressive disclosure 三层模型

- 来源：`https://www.beri.net/learning/anthropic-equipping-agents-agent-skills`（转述 Anthropic 工程博客《Equipping agents for the real world with Agent Skills》，2025-10-16 发布，作者 Barry Zhang / Keith Lazuka / Mahesh Murag）
- 原文要点：「only a skill's YAML metadata, its name and description, sits in context at startup; the body of SKILL.md loads when Claude judges the skill relevant to a request; and any additional bundled files load only when the instructions point at them」
- 推论：三层 = **元数据（常驻）→ 正文（按相关加载）→ 引用文件（按需）**。
- conf：**0.6**（二手转述；未直读 Anthropic 一手页面）

### E2 · 三层实现细节 + 一条硬约束：「引用只许一层」

- 来源：`https://dotzlaw.com/insights/claude-skills/`
- 原文要点：「**Keep references one level deep.** A reference file should not point to another reference file that points to another. One level of progressive disclosure (SKILL.md to reference file) is the practical limit before agents get lost in a documentation tree」
- 量化例子：「8 skills × 300 lines + 1000 lines references ≈ 70,000 tokens at startup；progressive disclosure 启动约 500 tokens，任一时刻约 2,000 tokens」
- 推论：**分层削减的量级可达 1–2 个数量级**，但层级超过 2 层就开始丢信息。
- conf：**0.5**（博客，非官方文档；但给出了可复算的算术例子）

### E3 · 为什么「少而准」不只是省 token

- 来源 1：`https://playerzero.ai/resources/what-context-rot-is-and-how-to-measure-it`（汇总 Chroma 2025 / NoLiMa ICML 2025 / RULER / Lost-in-the-Middle）
  - 「Chroma, Context Rot (2025)｜18 models…｜Performance became increasingly unreliable as input length grew, across every model tested」
  - 「NoLiMa…At 32K tokens, 11 of the 13 fell below half their short-context baseline」
- 来源 2：`https://atlan.com/know/llm-context-window-limitations/`
  - 「context rot…accuracy drops over 30% when relevant information sits in middle positions」
- 推论：**12,086 tok 的规则每轮重发，除了花 token，还让后段规则落到「中段位置」→ 被忽略的风险随 turn 数上升**。阶段门控的收益因此不止 token，还有规则可召回性。
- conf：**0.6**（两篇均为二手汇总，但引用的原始研究可追；数值彼此一致）

## 与本文档的直接关联

| 观察 | 对 INDEX 的含义 |
|---|---|
| 三层模型（E1） | 我们现在是**两层**：INDEX（常驻）+ 阶段包（按需）。缺 E1 的「元数据层」——即每个阶段包的 1 行摘要常量驻 |
| 引用只许一层（E2） | INDEX → 阶段包 已是 1 层，合规；**但阶段包里的文件若再互相指引，就超层** |
| 中段丢失（E3） | 规则不只是「读没读」，还有「读的位置」。每轮重发 12k 规则会持续把规则推向中段 |

## 阶段判定

- 每个 claim 带 URL + 原文摘句 + conf；E1/E2/E3 三条独立（官方设计说明 / 实现博客 / 实证研究汇总）。
- **verdict: pass** → 进入阶段 02.5。
