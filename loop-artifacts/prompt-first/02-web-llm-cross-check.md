# 网页 AI 交叉询问回执

- 时间：2026-10-30T00:29:56.055194+00:00
- 性质：网页 AI 回答仅是审阅线索，不是权威事实来源。

## 询问主张

rubric 评分中把 gold 推理树节点转换为原子 claim（atomic claim）清单、用多判者多数决判定产出是否包含该 claim 实质内容的做法，在 LLM-as-judge / rubric evaluation 文献中的对应实践名称与已知风险（如 claim 措辞泄漏答案、judge 间一致性 κ 的典型水平）

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
