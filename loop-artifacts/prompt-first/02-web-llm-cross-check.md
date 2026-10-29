# 网页 AI 交叉询问回执

- 时间：2026-10-29T21:16:16.460128+00:00
- 性质：网页 AI 回答仅是审阅线索，不是权威事实来源。

## 询问主张

LLM-as-judge 评测中，给独立打分器（另一 LLM）的 evidence packet（输入证据包）应固化哪些字段，才能避免打分器因信息缺失产生系统性偏低/偏高？特别是：任务书行数、迭代轮数这类可机械测量的过程指标，应该以什么形式提供（原始值+来源路径 vs 摘要）？

## 上下文

阶段 02；只要求可复核来源线索

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
