# 27b 评估陷阱：vllm 把思考链单独放 `reasoning` 字段，只抓 `content` 会系统性低估

> origin: ai · 2026-11-25 · subagent B（think-trigger T2 实验）
> 触发：T2"接着考虑"实验 v1 只抓 content 打分，后发现 27b 是 thinking 模型、机制推理藏在隐藏 reasoning 里 → v2 补抓重评，臂B 总分从 3.00 修正到 5.67

## 陷阱（可复用，适用于所有调 27b 做评估的实验）

本地 27b（`qwen3.8-27b-mtp`，127.0.0.1:8787，vllm NVFP4）是 **thinking 模型**。
OpenAI 兼容 `/v1/chat/completions` 返回的 `message` 里：
- `content` = 可见文本（常只是"答案"或很短的总结）
- `reasoning` = **隐藏的完整思考链**（vllm 单独返回，`usage.completion_tokens_details.reasoning_tokens` 计数）

**只抓 `content` 评估 = 系统性低估模型的机制推理/爬层/预言能力**，因为：
1. 机制工作（爬层、推预言、建框架）发生在 reasoning 里，content 只见结论。
2. reasoning_tokens 通常远大于 content（实测 6 样本 reasoning_tokens 484–934，content 仅 153–1090 字）。
3. 偶发 reasoning_tokens=0（思考漏进 content）会让该样本"显得强"，造成跨样本不公平——v1 臂B run1 恰好 rt=0 拿了 6 分，其余 2 个 rt>0 被低估，导致 v1 误判"臂B 只有 1/3 达标"（实际 3/3）。

## 正确做法（硬规则）

调 27b 做**评估/打分**时：
```python
msg = resp["choices"][0]["message"]
content   = msg.get("content")   or ""
reasoning = msg.get("reasoning") or ""   # ← 必须抓这个
# 评估对象 = reasoning + content（完整思考链），不是只看 content
```
- 打分/判据（爬层/预言力/边界等）应在 `reasoning + content` 全文上判定。
- 记录 `reasoning_tokens`，若 =0 标注"思考漏进 content，该样本可见度高、跨样本比较需注意"。
- `finish_reason=length`（max_tokens 截断）时 reasoning 字段仍完整返回（实测未被截断），故截断不影响 reasoning 可见性。

## 数据支撑（T2 实验）

- v1（只抓 content）：臂B 爬层 1.33 / 预言力 0.67 / 边界 1.33（总 3.00/6）
- v2（抓 content+reasoning 重评）：臂B 爬层 2.00 / 预言力 2.00 / 边界 1.67（总 5.67/6）
- 修正方向：臂B 3/3 采样全部爬到机制层+推出可检验预言（v1 误判为 1/3）
- 详见 `tasks/think-trigger/exp-results/scores_v2.md`（含修正说明）

## 适用范围

任何用本地 27b 做"给输入→评输出质量"的实验（judge/评估/能力测试）。
不适用于：只要最终答案的生成任务（那时 content 够，reasoning 可忽略）。
