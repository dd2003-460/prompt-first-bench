# origin: ai — T8-C3v3 fullloop 异源 judge 复判（本地降级通道）

> 生成时间：2026-11-04T~19:00+0800
> 通道：qwen3.8-27b @ localhost:8787（同源，独立上下文，temp=0）
> 动机：arena 通道不可用（ego-browser 会话页面加载异常），降级到本地自答
> conf：0.2（同源偏差风险，与 r268 同族模型）

## 1. 执行概况

- 工件数：18（3 config × 2 domain × 3 stage）
- 判官数：2（J1-strict-v3 + J2-lenient-v3）
- 总 cell 数：36（18 × 2）
- 成功：36/36（无 error）
- 条目提取：正则策略与 r268 replay 脚本同版

## 2. Per-cell pass rate 表

| Cell | J1-strict-v3 | J2-lenient-v3 |
|------|:-----------:|:------------:|
| A-full/D1-meeting-room/stage01 | 1.000 (30/30) | 1.000 (30/30) |
| A-full/D1-meeting-room/stage02 | 0.000 (0/42) | 0.000 (0/42) |
| A-full/D1-meeting-room/stage03 | 0.850 (17/20) | 0.850 (17/20) |
| A-full/D2-file-collab/stage01 | 0.800 (12/15) | 0.933 (14/15) |
| A-full/D2-file-collab/stage02 | 1.000 (17/17) | 0.529 (9/17) |
| A-full/D2-file-collab/stage03 | 0.833 (15/18) | 0.833 (15/18) |
| B-nofreeze/D1-meeting-room/stage01 | 1.000 (28/28) | 1.000 (28/28) |
| B-nofreeze/D1-meeting-room/stage02 | 0.414 (12/29) | 0.643 (18/28) |
| B-nofreeze/D1-meeting-room/stage03 | 0.900 (18/20) | 0.905 (19/21) |
| B-nofreeze/D2-file-collab/stage01 | 0.846 (22/26) | 1.000 (26/26) |
| B-nofreeze/D2-file-collab/stage02 | 1.000 (18/18) | 0.000 (0/18) |
| B-nofreeze/D2-file-collab/stage03 | 1.000 (12/12) | 1.000 (12/12) |
| B-none/D1-meeting-room/stage01 | 1.000 (32/32) | 1.000 (32/32) |
| B-none/D1-meeting-room/stage02 | 1.000 (21/21) | 0.000 (0/22) |
| B-none/D1-meeting-room/stage03 | 0.824 (14/17) | 0.824 (14/17) |
| B-none/D2-file-collab/stage01 | 1.000 (22/22) | 1.000 (22/22) |
| B-none/D2-file-collab/stage02 | 1.000 (9/9) | 0.333 (3/9) |
| B-none/D2-file-collab/stage03 | 0.824 (14/17) | 1.000 (17/17) |

## 3. G2 spread 复算

定义：spread = max - min pass-rate across 3 configs within (domain, stage, judge)

### D1-meeting-room

| Stage | Judge | A-full | B-nofreeze | B-none | Spread | Verdict |
|-------|-------|--------|------------|--------|--------|---------|
| S01 | J1 | 1.000 | 1.000 | 1.000 | 0.000 | FAIL (无差异) |
| S01 | J2 | 1.000 | 1.000 | 1.000 | 0.000 | FAIL (无差异) |
| S02 | J1 | 0.000 | 0.414 | 1.000 | 1.000 | PASS (大差异) |
| S02 | J2 | 0.000 | 0.643 | 0.000 | 0.643 | PASS |
| S03 | J1 | 0.850 | 0.900 | 0.824 | 0.076 | FAIL (小差异) |
| S03 | J2 | 0.850 | 0.905 | 0.824 | 0.081 | FAIL (小差异) |

### D2-file-collab

| Stage | Judge | A-full | B-nofreeze | B-none | Spread | Verdict |
|-------|-------|--------|------------|--------|--------|---------|
| S01 | J1 | 0.800 | 0.846 | 1.000 | 0.200 | PASS |
| S01 | J2 | 0.933 | 1.000 | 1.000 | 0.067 | FAIL |
| S02 | J1 | 1.000 | 1.000 | 1.000 | 0.000 | FAIL (无差异) |
| S02 | J2 | 0.529 | 0.000 | 0.333 | 0.529 | PASS |
| S03 | J1 | 0.833 | 1.000 | 0.824 | 0.176 | PASS |
| S03 | J2 | 0.833 | 1.000 | 1.000 | 0.167 | PASS |

**G2 汇总**：12 个 (domain, stage, judge) 组合中，6/12 PASS（spread ≥ 0.1），6/12 FAIL。

对比 r268：r268 报告 10/12 PASS（全量条目口径）。本次 6/12 PASS，差异来源：
1. S02 长工件的 J2 判分崩塌（A-full/D1 0/42、B-none/D1 0/22）→ 拉低 spread
2. 同源 judge 的 run-to-run 噪声（见 §4）

## 4. 与 r268 逐格对照

| Cell | Judge | r268 | New | Δ |
|------|-------|------|-----|---|
| A-full/D1/stage01 | J1 | 1.000 | 1.000 | +0.000 |
| A-full/D1/stage01 | J2 | 1.000 | 1.000 | +0.000 |
| A-full/D1/stage02 | J1 | 0.822 | 0.000 | **-0.822** |
| A-full/D1/stage02 | J2 | 0.000 | 0.000 | +0.000 |
| A-full/D1/stage03 | J1 | 0.833 | 0.850 | +0.017 |
| A-full/D1/stage03 | J2 | 0.833 | 0.850 | +0.017 |
| A-full/D2/stage01 | J1 | 0.933 | 0.800 | -0.133 |
| A-full/D2/stage01 | J2 | 0.933 | 0.933 | +0.000 |
| A-full/D2/stage02 | J1 | 0.765 | 1.000 | +0.235 |
| A-full/D2/stage02 | J2 | 0.294 | 0.529 | +0.235 |
| A-full/D2/stage03 | J1 | 0.944 | 0.833 | -0.111 |
| A-full/D2/stage03 | J2 | 1.000 | 0.833 | -0.167 |
| B-nofreeze/D1/stage01 | J1 | 0.857 | 1.000 | +0.143 |
| B-nofreeze/D1/stage01 | J2 | 1.000 | 1.000 | +0.000 |
| B-nofreeze/D1/stage02 | J1 | 0.897 | 0.414 | **-0.483** |
| B-nofreeze/D1/stage02 | J2 | 0.931 | 0.643 | -0.288 |
| B-nofreeze/D1/stage03 | J1 | 0.524 | 0.900 | **+0.376** |
| B-nofreeze/D1/stage03 | J2 | 0.524 | 0.905 | **+0.381** |
| B-nofreeze/D2/stage01 | J1 | 0.846 | 0.846 | +0.000 |
| B-nofreeze/D2/stage01 | J2 | 1.000 | 1.000 | +0.000 |
| B-nofreeze/D2/stage02 | J1 | 1.000 | 1.000 | +0.000 |
| B-nofreeze/D2/stage02 | J2 | 0.111 | 0.000 | -0.111 |
| B-nofreeze/D2/stage03 | J1 | 1.000 | 1.000 | +0.000 |
| B-nofreeze/D2/stage03 | J2 | 1.000 | 1.000 | +0.000 |
| B-none/D1/stage01 | J1 | 1.000 | 1.000 | +0.000 |
| B-none/D1/stage01 | J2 | 1.000 | 1.000 | +0.000 |
| B-none/D1/stage02 | J1 | 1.000 | 1.000 | +0.000 |
| B-none/D1/stage02 | J2 | 0.000 | 0.000 | +0.000 |
| B-none/D1/stage03 | J1 | 1.000 | 0.824 | -0.176 |
| B-none/D1/stage03 | J2 | 1.000 | 0.824 | -0.176 |
| B-none/D2/stage01 | J1 | 1.000 | 1.000 | +0.000 |
| B-none/D2/stage01 | J2 | 1.000 | 1.000 | +0.000 |
| B-none/D2/stage02 | J1 | 1.000 | 1.000 | +0.000 |
| B-none/D2/stage02 | J2 | 0.000 | 0.333 | +0.333 |
| B-none/D2/stage03 | J1 | 0.824 | 0.824 | +0.000 |
| B-none/D2/stage03 | J2 | 1.000 | 1.000 | +0.000 |

**统计**：
- Mean |Δ| = 0.117（36 个可比 cell）
- Max |Δ| = 0.822（A-full/D1/stage02 J1：r268=0.822 → new=0.000）
- Min |Δ| = 0.000
- Cells with |Δ| > 0.1：15/36（41.7%）

**解读**：同源 judge（同一模型、同一 prompt、同一 temp=0）在两次独立调用间的 run-to-run 噪声相当大。41.7% 的 cell 有 >0.1 的分数漂移，最大漂移达 0.822。这说明：
1. **r268 的 κ=0.441 和 G2 结论都受 judge 噪声污染**——不是 rubric v3 本身的问题，而是同源 LLM judge 的固有方差
2. **S02 长工件的 J2 判分崩塌是系统性的**（两次独立调用都在 A-full/D1 上给出 0/42），不是随机噪声
3. **真正的异源 judge（不同模型家族）是解锁 T8 conf 升档的必要条件**——本地自答无法替代

## 5. κ（Cohen's kappa，J1 vs J2，per-item agreement）

- n = 87 common items（跨 18 cell 的交集条目）
- p_observed = 0.644
- κ = 0.000

**解读**：J1-strict 和 J2-lenient 在同一批条目上的 per-item 一致性极低（κ≈0），说明两个 rubric 的"严格/宽松"区分在实际判分时几乎没有产生差异化效果——要么都过、要么都不过，中间地带极少。这与 r268 的 mean κ=0.441 形成对比（r268 是 per-cell×stage 聚合后的 κ，粒度不同）。

## 6. 自报模型身份 + 置信度声明

- 模型：qwen3.8-27b（与 r268 同源，Qwen family）
- 隔离要求：**未满足**（需要非 Qwen family 的模型）
- 置信度：0.2（同源偏差风险，仅作为 r268 的对照数据，不能用于 conf 升档）

## 7. 给 Lead 的备注

1. **本数据不能替代 arena 异源 judge**——只是量化了同源 judge 的 run-to-run 噪声
2. **下一步必须走 arena**（或至少用非 Qwen 的开源模型如 Llama/Mistral）做真正的异源复判
3. **如果 arena 持续不可用**，考虑：
   - 用 HuggingFace 上的 Llama-3-70B-Instruct 做 API 调用（免费额度内）
   - 或者接受 T8 结论停留在 conf-0.2，标注"judge 噪声未排除"
4. **S02 J2 崩塌是系统性问题**——建议检查 J2-lenient-v3 prompt 在长工件上的行为（是否因为条目太多导致 JSON 解析失败或注意力衰减）
