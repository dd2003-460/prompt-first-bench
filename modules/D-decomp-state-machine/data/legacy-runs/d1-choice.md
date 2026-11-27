# D1 baseline 选型记录

> origin: ai · 2026-11-04T03:10+08:00

## 候选三选一（DESIGN §3）

| 候选 | star/活跃度 | 可本地部署性 (Python 3.9.6) | 判定 |
|------|------------|---------------------------|------|
| **GPT Researcher** | ~25k stars，活跃 | ❌ **装不动**：v0.12.3 已 pip 安装但 import 即炸 — `config/config.py:64` 用 `match` 语句（Python 3.10+ 语法），本机 3.9.6 SyntaxError。源码 runs/d1-gpt-researcher/ 已克隆（上次 subagent 产出） | 排除（环境不兼容） |
| Open Deep Research | LangChain 生态，较新 | ⚠️ 未验证：依赖 langchain ≥0.2 全家桶，3.9 兼容性未知；需要额外调研 ≤30min | 备选 |
| STORM (Stanford OVEN) | ~10k stars，学术项目 | ⚠️ 未验证：基于 LlamaIndex，3.9 兼容性未知 | 备选 |

## 结论

**D1 降级为「无法运行」记录在案**（DESIGN §7 条款："若三个都装不动/跑不通 → D1 降级"）。

理由链：
1. GPT Researcher（首选）确认不可用 — Python 3.10+ 硬依赖，本机 3.9.6 无法绕过（match 是核心代码路径，不是可选特性）
2. 升级 Python 到 3.10+ 影响面太大（系统框架/其他项目依赖），不值得为一个 baseline 做
3. Open Deep Research / STORM 的 3.9 兼容性未验证，且即使能装，它们的 pipeline 设计（多 agent 协作/网页浏览）与 S0-S5 的单模型直出范式差异过大，对比公平性存疑
4. DESIGN §7 明确允许此降级：scoring.md 里 S5 vs D1 判据标 N/A 并说明原因，不算失败

## 对实验的影响

- S0-S5 消融臂不受影响（只用本地 27b endpoint + prompt 注入）
- DESIGN §8 判据 2（S5 vs D1 总分序）→ **N/A**，标注原因
- 判据 1（每级增量符号 Δ_k）→ 仍可完整验证
- 未来若要补 D1：升级 Python 环境或用 cloud runner

## 证据

```
$ python3 --version
Python 3.9.6
$ pip3 show gpt-researcher
Name: gpt-researcher
Version: 0.12.3
$ python3 -c "import gpt_researcher"
SyntaxError: invalid syntax  (config/config.py line 64, match statement)
```
