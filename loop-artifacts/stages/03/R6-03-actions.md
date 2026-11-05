# R6 · 阶段 03 行动分解：漏载检测机制

> 规则包：`00-common-review.md` + `03-action-decomposition.md` + `04-execution-verification.md`（2,317 o200k，阶段门控）
> 输入：阶段 01 的 R/A/G/X 四类 + 阶段 02.5 的 C1–C3

## 设计目标

把 01 阶段的 4 类漏载变成 **1 个可执行脚本的 4 组断言**，exit code 可挂 CI。

## 步骤（依赖 + 并行）

| # | 步骤 | 输入 | 依赖 | Owner | 产出 | 验收 |
|---|---|---|---|---|---|---|
| A1 | 解析 INDEX.md 路由表 → `{stage: [files]}` | INDEX.md | — | agent | 内存结构 | 6 个 stage 全解析，缺一 exit 2 |
| A2 | 扫每个规则文件的跨文件引用（`见 0X-`、`参考 0X-`、`loop/prompt-first/0X-`） | 7 个 .md | A1 | agent | 引用图 | 每条引用带行号 |
| A3 | **X-miss 断言**：∀ 引用 A→B，要求 B ∈ route(stage(A)) 或 B ∈ route(该阶段下一跳) | A1+A2 | A2 | agent | 未覆盖引用清单 | 清单为空 → exit 0；非空 → exit 1 并打印 |
| A4 | **A-miss 断言**：扫规则文件里声明的上游产出路径（`loop-artifacts/stages/<N>/`），检查本次 run 是否已生成 | A1+仓库 | A2 | agent | 缺失产出清单 | 允许「尚未到该阶段」豁免，但须显式列出 |
| A5 | **R-miss 断言**：每个阶段的 route 包成员数 = 该阶段声明需要的文件数 | A1 | A1 | agent | 一致性 | 6/6 通过 |
| A6 | **G-miss 断言**：每个已存在的 `loop-artifacts/stages/<N>/` 内有 `verdict:` 行 | 仓库 | A4 | agent | 判定覆盖率 | 本 run 覆盖率 100% |
| A7 | 把 A3–A6 结果写 JSON + 退出码 | A3–A6 | 全部 | agent | `route-coverage.json` | schema 稳定 |

**并行**：A1 是所有步骤的前置（串行瓶颈）；A3/A4/A5/A6 在 A1+A2 之后可并行。
**失败路径**：若某规则文件引用了一个根本不存在（拼写错）的文件名 → 归 X-miss 的 **dangling** 子类，单独列，不混入覆盖缺口（否则数字会虚高）。

## 判定口径（防凑数）

- 只有 **A3 的未覆盖引用 = 0** 才允许说「INDEX 路由无漏载」。
- A4 的缺失产出若属「run 尚未到该阶段」，必须写明豁免理由，否则计为 fail。
- 检测脚本自身必须能被第三方在干净 checkout 上复跑（不依赖网络、不依赖本 run 的临时文件）。

## 阶段判定

- 7 个步骤全部原子化（单步可在一次工具调用内完成），依赖无环，验收均为 exit code 或文件存在性。
- **verdict: pass** → 进入阶段 04 执行。
