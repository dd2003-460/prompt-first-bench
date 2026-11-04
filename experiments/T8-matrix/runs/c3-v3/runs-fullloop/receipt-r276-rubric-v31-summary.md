# r276 rubric-v3.1 J2宽容条款重放验证 summary

- 生成时间: 2026-11-05T00:33:47+0800
- 模型: qwen3.8-27b @ http://localhost:8787/v1/chat/completions
- 通道: 本地 vLLM（rubric-v3.1 S01 效度修复验证）
- prompt: judge-prompts-rubric-v3.1.json (J1 sha256_16=8811ae284ab280bb, J2 sha256_16=2513668a49bc603f) J2来源宽容条款
- conf: 0.2（同源偏差风险，judge 与生成器同族 Qwen；本 run 目的是验证 rubric 改动效果，非最终测量）
- 工件数: 18, 完成: 36, 错误: 0

## 关键验证：分阶段通过率

| Stage×Judge | total | passed | rate | 预期 |
|-------------|-------|--------|------|------|
| S01_J1 | 155 | 154 | 0.9935 | 60-90%（v3 时 ~0%） |
| S01_J2 | 155 | 154 | 0.9935 | 与 r269 相近 |
| S02_J1 | 140 | 118 | 0.8429 | 与 r269 相近（±10pp） |
| S02_J2 | 132 | 103 | 0.7803 | 与 r269 相近（±10pp） |
| S03_J1 | 103 | 87 | 0.8447 | 与 r269 相近（±10pp） |
| S03_J2 | 103 | 96 | 0.932 | 与 r269 相近（±10pp） |

## κ (J1 vs J2 per cell)

| Cell | n | P(obs) | κ |
|------|---|--------|---|
| A-full/D1-meeting-room/s01 | 31 | 1.0 | 1.0 |
| A-full/D1-meeting-room/s02 | 37 | 0.8378 | 0.6237 |
| A-full/D1-meeting-room/s03 | 18 | 0.8333 | 0.0 |
| A-full/D2-file-collab/s01 | 15 | 0.8667 | -0.0714 |
| A-full/D2-file-collab/s02 | 17 | 0.7647 | 0.0 |
| A-full/D2-file-collab/s03 | 18 | 1.0 | 1.0 |
| B-nofreeze/D1-meeting-room/s01 | 28 | 1.0 | 1.0 |
| B-nofreeze/D1-meeting-room/s02 | 29 | 0.9655 | 0.782 |
| B-nofreeze/D1-meeting-room/s03 | 21 | 0.8571 | 0.7097 |
| B-nofreeze/D2-file-collab/s01 | 26 | 1.0 | 1.0 |
| B-nofreeze/D2-file-collab/s02 | 18 | 0.8333 | 0.0 |
| B-nofreeze/D2-file-collab/s03 | 12 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s01 | 33 | 1.0 | 1.0 |
| B-none/D1-meeting-room/s02 | 22 | 0.5909 | -0.0206 |
| B-none/D1-meeting-room/s03 | 17 | 1.0 | 1.0 |
| B-none/D2-file-collab/s01 | 22 | 1.0 | 1.0 |
| B-none/D2-file-collab/s02 | 9 | 0.3333 | 0.0 |
| B-none/D2-file-collab/s03 | 17 | 0.8235 | 0.0 |
| **mean** | | | **0.5569** |

## G2 spread (cross-config within domain×stage×judge)

| Key | A-full | B-nofreeze | B-none | Spread | Verdict |
|-----|--------|------------|--------|--------|---------|
| D1-meeting-room_S01_J1 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D1-meeting-room_S01_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |
| D1-meeting-room_S02_J1 | 0.8222 | 0.931 | 0.6364 | 0.2946 | PASS |
| D1-meeting-room_S02_J2 | 0.6216 | 0.8966 | 0.8636 | 0.275 | PASS |
| D1-meeting-room_S03_J1 | 0.8333 | 0.5238 | 1.0 | 0.4762 | PASS |
| D1-meeting-room_S03_J2 | 1.0 | 0.6667 | 1.0 | 0.3333 | PASS |
| D2-file-collab_S01_J1 | 0.9333 | 1.0 | 1.0 | 0.0667 | PASS |
| D2-file-collab_S01_J2 | 0.9333 | 1.0 | 1.0 | 0.0667 | PASS |
| D2-file-collab_S02_J1 | 0.7647 | 1.0 | 1.0 | 0.2353 | PASS |
| D2-file-collab_S02_J2 | 1.0 | 0.8333 | 0.3333 | 0.6667 | PASS |
| D2-file-collab_S03_J1 | 1.0 | 1.0 | 0.8235 | 0.1765 | PASS |
| D2-file-collab_S03_J2 | 1.0 | 1.0 | 1.0 | 0.0 | FAIL |

G2: 9/12 PASS

## 与 r269 (v3 同源) 逐格对照

| Cell | Judge | r276 (v3.1 J2fix) | r269 (v3) | Δ |
|------|-------|-------------|-----------|---|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | 31/31 | +0.0000 |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | 31/31 | +0.0000 |
| A-full/D1-meeting-room/s02 | J1 | 37/45 | 37/45 | +0.0000 |
| A-full/D1-meeting-room/s02 | J2 | 23/37 | 0/45 | +0.6216 |
| A-full/D1-meeting-room/s03 | J1 | 15/18 | 15/18 | +0.0000 |
| A-full/D1-meeting-room/s03 | J2 | 18/18 | 15/18 | +0.1667 |
| A-full/D2-file-collab/s01 | J1 | 14/15 | 14/15 | +0.0000 |
| A-full/D2-file-collab/s01 | J2 | 14/15 | 14/15 | +0.0000 |
| A-full/D2-file-collab/s02 | J1 | 13/17 | 13/17 | +0.0000 |
| A-full/D2-file-collab/s02 | J2 | 17/17 | 5/17 | +0.7059 |
| A-full/D2-file-collab/s03 | J1 | 18/18 | 17/18 | +0.0556 |
| A-full/D2-file-collab/s03 | J2 | 18/18 | 18/18 | +0.0000 |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | 24/28 | +0.1429 |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | 28/28 | +0.0000 |
| B-nofreeze/D1-meeting-room/s02 | J1 | 27/29 | 27/29 | +0.0000 |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | 23/29 | +0.1034 |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | 11/21 | +0.0000 |
| B-nofreeze/D1-meeting-room/s03 | J2 | 14/21 | 11/21 | +0.1429 |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | 26/26 | +0.0000 |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | 26/26 | +0.0000 |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | 18/18 | +0.0000 |
| B-nofreeze/D2-file-collab/s02 | J2 | 15/18 | 2/18 | +0.7222 |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | 12/12 | +0.0000 |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | 12/12 | +0.0000 |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | 33/33 | +0.0000 |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | 33/33 | +0.0000 |
| B-none/D1-meeting-room/s02 | J1 | 14/22 | 22/22 | -0.3636 |
| B-none/D1-meeting-room/s02 | J2 | 19/22 | 0/22 | +0.8636 |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | 17/17 | +0.0000 |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | 17/17 | +0.0000 |
| B-none/D2-file-collab/s01 | J1 | 22/22 | 22/22 | +0.0000 |
| B-none/D2-file-collab/s01 | J2 | 22/22 | 22/22 | +0.0000 |
| B-none/D2-file-collab/s02 | J1 | 9/9 | 9/9 | +0.0000 |
| B-none/D2-file-collab/s02 | J2 | 3/9 | 0/9 | +0.3333 |
| B-none/D2-file-collab/s03 | J1 | 14/17 | 14/17 | +0.0000 |
| B-none/D2-file-collab/s03 | J2 | 17/17 | 17/17 | +0.0000 |

## 与 r270 (arena 异源) 逐格对照（外部参考）

| Cell | Judge | r276 (v3.1 J2fix) | r270 (v3 arena) |
|------|-------|------------------|-----------------|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | 0/31 |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | 11/31 |
| A-full/D1-meeting-room/s02 | J1 | 37/45 | 16/45 |
| A-full/D1-meeting-room/s02 | J2 | 23/37 | 2/45 |
| A-full/D1-meeting-room/s03 | J1 | 15/18 | 18/21 |
| A-full/D1-meeting-room/s03 | J2 | 18/18 | 8/21 |
| A-full/D2-file-collab/s01 | J1 | 14/15 | 1/17 |
| A-full/D2-file-collab/s01 | J2 | 14/15 | 3/17 |
| A-full/D2-file-collab/s02 | J1 | 13/17 | 1/17 |
| A-full/D2-file-collab/s02 | J2 | 17/17 | 4/17 |
| A-full/D2-file-collab/s03 | J1 | 18/18 | 15/18 |
| A-full/D2-file-collab/s03 | J2 | 18/18 | 16/18 |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | 0/28 |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | 5/28 |
| B-nofreeze/D1-meeting-room/s02 | J1 | 27/29 | 0/29 |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | 1/29 |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | 20/22 |
| B-nofreeze/D1-meeting-room/s03 | J2 | 14/21 | 4/22 |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | 0/27 |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | 5/27 |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | 3/19 |
| B-nofreeze/D2-file-collab/s02 | J2 | 15/18 | 5/19 |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | 9/12 |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | 9/12 |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | 0/34 |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | 5/34 |
| B-none/D1-meeting-room/s02 | J1 | 14/22 | 10/22 |
| B-none/D1-meeting-room/s02 | J2 | 19/22 | 3/22 |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | 17/18 |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | 9/18 |
| B-none/D2-file-collab/s01 | J1 | 22/22 | 0/22 |
| B-none/D2-file-collab/s01 | J2 | 22/22 | 5/22 |
| B-none/D2-file-collab/s02 | J1 | 9/9 | 0/9 |
| B-none/D2-file-collab/s02 | J2 | 3/9 | 1/9 |
| B-none/D2-file-collab/s03 | J1 | 14/17 | 16/19 |
| B-none/D2-file-collab/s03 | J2 | 17/17 | 10/19 |

## 与 r268 逐格对照

| Cell | Judge | r276 | r268 |
|------|-------|------|------|
| A-full/D1-meeting-room/s01 | J1 | 31/31 | ? |
| A-full/D1-meeting-room/s01 | J2 | 31/31 | ? |
| A-full/D1-meeting-room/s02 | J1 | 37/45 | ? |
| A-full/D1-meeting-room/s02 | J2 | 23/37 | ? |
| A-full/D1-meeting-room/s03 | J1 | 15/18 | ? |
| A-full/D1-meeting-room/s03 | J2 | 18/18 | ? |
| A-full/D2-file-collab/s01 | J1 | 14/15 | ? |
| A-full/D2-file-collab/s01 | J2 | 14/15 | ? |
| A-full/D2-file-collab/s02 | J1 | 13/17 | ? |
| A-full/D2-file-collab/s02 | J2 | 17/17 | ? |
| A-full/D2-file-collab/s03 | J1 | 18/18 | ? |
| A-full/D2-file-collab/s03 | J2 | 18/18 | ? |
| B-nofreeze/D1-meeting-room/s01 | J1 | 28/28 | ? |
| B-nofreeze/D1-meeting-room/s01 | J2 | 28/28 | ? |
| B-nofreeze/D1-meeting-room/s02 | J1 | 27/29 | ? |
| B-nofreeze/D1-meeting-room/s02 | J2 | 26/29 | ? |
| B-nofreeze/D1-meeting-room/s03 | J1 | 11/21 | ? |
| B-nofreeze/D1-meeting-room/s03 | J2 | 14/21 | ? |
| B-nofreeze/D2-file-collab/s01 | J1 | 26/26 | ? |
| B-nofreeze/D2-file-collab/s01 | J2 | 26/26 | ? |
| B-nofreeze/D2-file-collab/s02 | J1 | 18/18 | ? |
| B-nofreeze/D2-file-collab/s02 | J2 | 15/18 | ? |
| B-nofreeze/D2-file-collab/s03 | J1 | 12/12 | ? |
| B-nofreeze/D2-file-collab/s03 | J2 | 12/12 | ? |
| B-none/D1-meeting-room/s01 | J1 | 33/33 | ? |
| B-none/D1-meeting-room/s01 | J2 | 33/33 | ? |
| B-none/D1-meeting-room/s02 | J1 | 14/22 | ? |
| B-none/D1-meeting-room/s02 | J2 | 19/22 | ? |
| B-none/D1-meeting-room/s03 | J1 | 17/17 | ? |
| B-none/D1-meeting-room/s03 | J2 | 17/17 | ? |
| B-none/D2-file-collab/s01 | J1 | 22/22 | ? |
| B-none/D2-file-collab/s01 | J2 | 22/22 | ? |
| B-none/D2-file-collab/s02 | J1 | 9/9 | ? |
| B-none/D2-file-collab/s02 | J2 | 3/9 | ? |
| B-none/D2-file-collab/s03 | J1 | 14/17 | ? |
| B-none/D2-file-collab/s03 | J2 | 17/17 | ? |