# N15: Autonomous Execution Loop: The system must handle state persistence across crash

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

Autonomous Execution Loop: The system must handle state persistence across crashes; estimated mean time between failures (MTBF) for the vLLM service on V100s is ~48 hours, requiring checkpointing every 15 minutes to prevent loss of multi-day research progress.

## Corrected Claim

Autonomous Execution Loop: The system must handle state persistence across crashes; estimated mean time between failures (MTBF) for the vLLM service on V100s is ~48 hours, requiring checkpointing every 15 minutes to prevent loss of multi-day research progress.

## Evidence

检索失败: no sources from any channel (all 5 failed)

## Search Query

vLLM stability MTBF V100 long-running inference checkpointing
