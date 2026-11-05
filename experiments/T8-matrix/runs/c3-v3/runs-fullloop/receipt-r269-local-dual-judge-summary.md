# r269 本地降级双判官复判 summary

> ⚠️ **旧 rubric 参考值**（r289 sign-off 后标注）：本 receipt 使用 v3 rubric，非终版 v3.1。数字仅供迭代历史对照，不作为质量声明依据。

- 生成时间: 2026-11-04T21:55:36+0800
- 模型: qwen3.8-27b @ http://localhost:8787/v1/chat/completions
- 通道: 本地 vLLM（arena 故障降级）
- conf: 0.2（同源偏差风险，judge 与生成器同族 Qwen）
- 工件数: 18, 完成: 36, 错误: 0

## κ (J1 vs J2 per cell)

| Cell | n | P(obs) | κ |
|------|---|--------|---|
| A-full/D1-meeting-room/s01 | 31 | 1.0 | 1.0 |
| A-full/D1-meeting-room/s02 | 45 | 0.1778 | -0.0 |
| A-full/D1-meeting-room/s03 | 18 | 1.0 | 1.0 |
| A-full/D2-file-collab/s01 | 15 | 0.8667 | -0.0714 |
| A-full/D2-file-collab/s02 | 17 | 0.5294 | 0.2273 |
| A-full/D2-file-collab/s03 | 18 | 0.9444 | 0.0 |
| B-nofreeze/D1-meeting-room/s01 | 28 | 0.8571 | 0.0 |
| B-nofreeze/D1-meeting-room/s02 | 29 | 0.8621 | 0.4423 |
| B-nofreeze/D1-meeting-room/s03 | 21 | 1.0 | 1.0 |
| B-nofreeze/D2-file-collab/s01 | 26 | 1.0 | 1.0 |
| B-nofreeze/D2-file-collab/s02 | 18 | 0.1111 | 0.0 |
| B-nofreeze/D2-file-collab/s03 | 12 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s01 | 33 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s02 | 22 | 0.0 | 0.0 |
| B-none/D1-meeting-room/s03 | 17 | 1.0 | 1.0 |
| B-none/D2-file-collab/s01 | 22 | 1.0 | 1.0 |
| B-none/D2-file-collab/s02 | 9 | 0.0 | 0.0 |
| B-none/D2-file-collab/s03 | 17 | 0.8235 | 0.0 |
| **mean** | | | **0.4777** |

## G2 spread (cross-config within domain×stage×judge)

| Key | A-full | B-nofreeze | B-none | Spread | Verdict |
|-----|--------|------------|--------|--------|---------|
| D1-meeting-room_S01_J1 | 1.0 | 0.8571 | 1.0 | 0.1429 | PASS |
| D1-meeting-room_S01_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D1-meeting-room_S02_J1 | 0.8222 | 0.931 | 1.0 | 0.1778 | PASS |
| D1-meeting-room_S02_J2 | 0.0 | 0.7931 | 0.0 | 0.7931 | PASS |
| D1-meeting-room_S03_J1 | 0.8333 | 0.5238 | 1.0 | 0.4762 | PASS |
| D1-meeting-room_S03_J2 | 0.8333 | 0.5238 | 1.0 | 0.4762 | PASS |
| D2-file-collab_S01_J1 | 0.9333 | 1.0 | 1.0 | 0.0667 | PASS |
| D2-file-collab_S01_J2 | 0.9333 | 1.0 | 1.0 | 0.0667 | PASS |
| D2-file-collab_S02_J1 | 0.7647 | 1.0 | 1.0 | 0.2353 | PASS |
| D2-file-collab_S02_J2 | 0.2941 | 0.1111 | 0.0 | 0.2941 | PASS |
| D2-file-collab_S03_J1 | 0.9444 | 1.0 | 0.8235 | 0.1765 | PASS |
| D2-file-collab_S03_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |

G2: 10/12 PASS

## 关键发现

1. **κ mean = 0.4777** — 中等一致性。J1/J2 在短工件上高度一致（κ=1.0），在长工件（S02/S03）上分歧大（κ=0~0.44）。
2. **J2-lenient 在 S02 长工件上系统性崩塌**：A-full/D1/s02 J2=0/45, B-none/D1/s02 J2=0/22, B-nofreeze/D2/s02 J2=2/18。与 r268 观察一致——同源 judge 在长上下文下注意力衰减。
3. **G2 10/12 PASS** — 跨配置 spread 信号存在。最大 spread: D1_S02_J2 (0.7931)，最小: D1_S01_J2 (0.0)。
4. **J1-strict 更稳定**：J1 在所有 18 cell 上 pass rate ≥ 0.52；J2 有 3 个 cell 降到 0。
5. **与 r268 对照**：r268 是首次同源重放（6 cells），r269 扩展到 18 cells 并加了独立 J1/J2 上下文。r268 的 S02 长工件问题在 r269 中复现，确认非偶发。