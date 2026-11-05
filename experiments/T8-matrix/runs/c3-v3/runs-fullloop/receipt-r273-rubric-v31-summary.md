# r273 rubric-v3.1 终版重放验证 summary

- 生成时间: 2026-11-05T00:16:22+0800
- 模型: qwen3.8-27b @ http://localhost:8787/v1/chat/completions
- 通道: 本地 vLLM（rubric-v3.1 S01 效度修复验证）
- prompt: judge-prompts-rubric-v3.1.json (J1 sha256_16=987a2481877e49d3, J2 同 v3) 双条件触发
- conf: 0.2（同源偏差风险，judge 与生成器同族 Qwen；本 run 目的是验证 rubric 改动效果，非最终测量）
- 工件数: 18, 完成: 36, 错误: 0

## 关键验证：分阶段通过率

| Stage×Judge | total | passed | rate | 预期 |
|-------------|-------|--------|------|------|
| S01_J1 | 155 | 155 | 1.0 | 60-90%（v3 时 ~0%） |
| S01_J2 | 155 | 154 | 0.9935 | 与 r269 相近 |
| S02_J1 | 140 | 88 | 0.6286 | 与 r269 相近（±10pp） |
| S02_J2 | 140 | 33 | 0.2357 | 与 r269 相近（±10pp） |
| S03_J1 | 106 | 93 | 0.8774 | 与 r269 相近（±10pp） |
| S03_J2 | 103 | 90 | 0.8738 | 与 r269 相近（±10pp） |

## κ (J1 vs J2 per cell)

| Cell | n | P(obs) | κ |
|------|---|--------|---|
| A-full/D1-meeting-room/s01 | 31 | 1.0 | 1.0 |
| A-full/D1-meeting-room/s02 | 45 | 1.0 | 1.0 |
| A-full/D1-meeting-room/s03 | 18 | 0.8333 | 0.0 |
| A-full/D2-file-collab/s01 | 15 | 0.9333 | 0.0 |
| A-full/D2-file-collab/s02 | 17 | 0.5294 | 0.2273 |
| A-full/D2-file-collab/s03 | 18 | 1.0 | 1.0 |
| B-nofreeze/D1-meeting-room/s01 | 28 | 1.0 | 1.0 |
| B-nofreeze/D1-meeting-room/s02 | 29 | 1.0 | 1.0 |
| B-nofreeze/D1-meeting-room/s03 | 21 | 1.0 | 1.0 |
| B-nofreeze/D2-file-collab/s01 | 26 | 1.0 | 1.0 |
| B-nofreeze/D2-file-collab/s02 | 18 | 0.1111 | 0.0 |
| B-nofreeze/D2-file-collab/s03 | 12 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s01 | 33 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s02 | 22 | 0.0 | 0.0 |
| B-none/D1-meeting-room/s03 | 17 | 1.0 | 1.0 |
| B-none/D2-file-collab/s01 | 22 | 1.0 | 1.0 |
| B-none/D2-file-collab/s02 | 9 | 0.0 | 0.0 |
| B-none/D2-file-collab/s03 | 17 | 1.0 | 1.0 |
| **mean** | | | **0.6793** |

## G2 spread (cross-config within domain×stage×judge)

| Key | A-full | B-nofreeze | B-none | Spread | Verdict |
|-----|--------|------------|--------|--------|---------|
| D1-meeting-room_S01_J1 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D1-meeting-room_S01_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D1-meeting-room_S02_J1 | 0.0 | 0.8966 | 1.0 | 1.0 | PASS |
| D1-meeting-room_S02_J2 | 0.0 | 0.8966 | 0.0 | 0.8966 | PASS |
| D1-meeting-room_S03_J1 | 0.8571 | 0.5238 | 1.0 | 0.4762 | PASS |
| D1-meeting-room_S03_J2 | 0.8333 | 0.5238 | 1.0 | 0.4762 | PASS |
| D2-file-collab_S01_J1 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D2-file-collab_S01_J2 | 0.9333 | 1.0 | 1.0 | 0.0667 | PASS |
| D2-file-collab_S02_J1 | 0.7647 | 1.0 | 1.0 | 0.2353 | PASS |
| D2-file-collab_S02_J2 | 0.2941 | 0.1111 | 0.0 | 0.2941 | PASS |
| D2-file-collab_S03_J1 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D2-file-collab_S03_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |

G2: 7/12 PASS

## 与 r269 (v3 同源) 逐格对照

| Cell | Judge | r273 (v3.1 终版) | r269 (v3) | Δ |
|------|-------|-------------|-----------|---|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | 31/31 | +0.0000 |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | 31/31 | +0.0000 |
| A-full/D1-meeting-room/s02 | J1 | 0/45 | 37/45 | -0.8222 |
| A-full/D1-meeting-room/s02 | J2 | 0/45 | 0/45 | +0.0000 |
| A-full/D1-meeting-room/s03 | J1 | 18/21 | 15/18 | +0.0238 |
| A-full/D1-meeting-room/s03 | J2 | 15/18 | 15/18 | +0.0000 |
| A-full/D2-file-collab/s01 | J1 | 15/15 | 14/15 | +0.0667 |
| A-full/D2-file-collab/s01 | J2 | 14/15 | 14/15 | +0.0000 |
| A-full/D2-file-collab/s02 | J1 | 13/17 | 13/17 | +0.0000 |
| A-full/D2-file-collab/s02 | J2 | 5/17 | 5/17 | +0.0000 |
| A-full/D2-file-collab/s03 | J1 | 18/18 | 17/18 | +0.0556 |
| A-full/D2-file-collab/s03 | J2 | 18/18 | 18/18 | +0.0000 |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | 24/28 | +0.1429 |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | 28/28 | +0.0000 |
| B-nofreeze/D1-meeting-room/s02 | J1 | 26/29 | 27/29 | -0.0345 |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | 23/29 | +0.1034 |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | 11/21 | +0.0000 |
| B-nofreeze/D1-meeting-room/s03 | J2 | 11/21 | 11/21 | +0.0000 |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | 26/26 | +0.0000 |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | 26/26 | +0.0000 |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | 18/18 | +0.0000 |
| B-nofreeze/D2-file-collab/s02 | J2 | 2/18 | 2/18 | +0.0000 |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | 12/12 | +0.0000 |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | 12/12 | +0.0000 |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | 33/33 | +0.0000 |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | 33/33 | +0.0000 |
| B-none/D1-meeting-room/s02 | J1 | 22/22 | 22/22 | +0.0000 |
| B-none/D1-meeting-room/s02 | J2 | 0/22 | 0/22 | +0.0000 |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | 17/17 | +0.0000 |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | 17/17 | +0.0000 |
| B-none/D2-file-collab/s01 | J1 | 22/22 | 22/22 | +0.0000 |
| B-none/D2-file-collab/s01 | J2 | 22/22 | 22/22 | +0.0000 |
| B-none/D2-file-collab/s02 | J1 | 9/9 | 9/9 | +0.0000 |
| B-none/D2-file-collab/s02 | J2 | 0/9 | 0/9 | +0.0000 |
| B-none/D2-file-collab/s03 | J1 | 17/17 | 14/17 | +0.1765 |
| B-none/D2-file-collab/s03 | J2 | 17/17 | 17/17 | +0.0000 |

## 与 r270 (arena 异源) 逐格对照（外部参考）

| Cell | Judge | r273 (v3.1 终版) | r270 (v3 arena) |
|------|-------|------------------|-----------------|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | 0/31 |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | 11/31 |
| A-full/D1-meeting-room/s02 | J1 | 0/45 | 16/45 |
| A-full/D1-meeting-room/s02 | J2 | 0/45 | 2/45 |
| A-full/D1-meeting-room/s03 | J1 | 18/21 | 18/21 |
| A-full/D1-meeting-room/s03 | J2 | 15/18 | 8/21 |
| A-full/D2-file-collab/s01 | J1 | 15/15 | 1/17 |
| A-full/D2-file-collab/s01 | J2 | 14/15 | 3/17 |
| A-full/D2-file-collab/s02 | J1 | 13/17 | 1/17 |
| A-full/D2-file-collab/s02 | J2 | 5/17 | 4/17 |
| A-full/D2-file-collab/s03 | J1 | 18/18 | 15/18 |
| A-full/D2-file-collab/s03 | J2 | 18/18 | 16/18 |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | 0/28 |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | 5/28 |
| B-nofreeze/D1-meeting-room/s02 | J1 | 26/29 | 0/29 |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | 1/29 |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | 20/22 |
| B-nofreeze/D1-meeting-room/s03 | J2 | 11/21 | 4/22 |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | 0/27 |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | 5/27 |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | 3/19 |
| B-nofreeze/D2-file-collab/s02 | J2 | 2/18 | 5/19 |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | 9/12 |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | 9/12 |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | 0/34 |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | 5/34 |
| B-none/D1-meeting-room/s02 | J1 | 22/22 | 10/22 |
| B-none/D1-meeting-room/s02 | J2 | 0/22 | 3/22 |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | 17/18 |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | 9/18 |
| B-none/D2-file-collab/s01 | J1 | 22/22 | 0/22 |
| B-none/D2-file-collab/s01 | J2 | 22/22 | 5/22 |
| B-none/D2-file-collab/s02 | J1 | 9/9 | 0/9 |
| B-none/D2-file-collab/s02 | J2 | 0/9 | 1/9 |
| B-none/D2-file-collab/s03 | J1 | 17/17 | 16/19 |
| B-none/D2-file-collab/s03 | J2 | 17/17 | 10/19 |

## 与 r268 逐格对照

| Cell | Judge | r273 | r268 |
|------|-------|------|------|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | ? |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | ? |
| A-full/D1-meeting-room/s02 | J1 | 0/45 | ? |
| A-full/D1-meeting-room/s02 | J2 | 0/45 | ? |
| A-full/D1-meeting-room/s03 | J1 | 18/21 | ? |
| A-full/D1-meeting-room/s03 | J2 | 15/18 | ? |
| A-full/D2-file-collab/s01 | J1 | 15/15 | ? |
| A-full/D2-file-collab/s01 | J2 | 14/15 | ? |
| A-full/D2-file-collab/s02 | J1 | 13/17 | ? |
| A-full/D2-file-collab/s02 | J2 | 5/17 | ? |
| A-full/D2-file-collab/s03 | J1 | 18/18 | ? |
| A-full/D2-file-collab/s03 | J2 | 18/18 | ? |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | ? |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | ? |
| B-nofreeze/D1-meeting-room/s02 | J1 | 26/29 | ? |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | ? |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | ? |
| B-nofreeze/D1-meeting-room/s03 | J2 | 11/21 | ? |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | ? |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | ? |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | ? |
| B-nofreeze/D2-file-collab/s02 | J2 | 2/18 | ? |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | ? |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | ? |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | ? |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | ? |
| B-none/D1-meeting-room/s02 | J1 | 22/22 | ? |
| B-none/D1-meeting-room/s02 | J2 | 0/22 | ? |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | ? |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | ? |
| B-none/D2-file-collab/s01 | J1 | 22/22 | ? |
| B-none/D2-file-collab/s01 | J2 | 22/22 | ? |
| B-none/D2-file-collab/s02 | J1 | 9/9 | ? |
| B-none/D2-file-collab/s02 | J2 | 0/9 | ? |
| B-none/D2-file-collab/s03 | J1 | 17/17 | ? |
| B-none/D2-file-collab/s03 | J2 | 17/17 | ? |