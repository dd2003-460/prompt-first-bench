# 网页 AI 交叉询问回执

- 时间：2026-10-29T21:27:59.523971+00:00
- 性质：网页 AI 回答仅是审阅线索，不是权威事实来源。

## 询问主张

LLM-as-judge 评测中，审计一份给独立打分器的 evidence packet 单行摘要（含锚点数/降级数/token 数值等断言）时，逐条核验的最佳实践是什么？只要求可复核来源线索

## 上下文

阶段 02；R5.2-packet-audit goal；只要求可复核来源线索

## 回执

### perplexity-review

- 传输：browser_playwright
- 状态：error
- 错误：Perplexity prompt box is unavailable; login or UI changed

### chatgpt-review

- 传输：browser_playwright
- 状态：error
- 错误：ChatGPT prompt box is unavailable; sign in manually in the visible browser first

### gemini-review

- 传输：browser_playwright
- 状态：error
- 错误：Gemini prompt box is unavailable; sign in manually in the visible browser first

## 使用限制

将上述回答与独立来源分开记录；不得把网页 AI 的未引证说法写成已验证事实。
