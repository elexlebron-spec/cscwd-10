# Repair cost contract audit v7

Reproduction materials for *When Additive Repair Costs Mislead Collaborative Design Workflows* (2026-10-28). Download [artifact.zip](artifact.zip), verify [SHA256SUMS](SHA256SUMS), then extract and read `READ_THIS_FIRST.txt`.

The archive contains code, frozen protocols, all reported experiment inputs/results, unsuccessful observer/parser stages, public upstream source archives with notices, and independent verification commands. It excludes the manuscript and all third-party research article PDFs, including the institutionally accessed nearest paper. No GPU, API key or proprietary data is required. Python3.12 with pinned dependencies and Apple command-line build tools were used; recorded outcomes can be audited without compiling the planner.

## Quick verification

From the extracted `CSCWD2027_Artifact_v7` folder:

```sh
cd cscwd2027_starter
python3 -m venv .venv-repro
.venv-repro/bin/python -m pip install -r requirements-planner.txt
.venv-repro/bin/python -m unittest discover -s tests -v
cd ..
cscwd2027_starter/.venv-repro/bin/python tools/verify_evidence_v7.py
```

Expected:30 passing tests,zero skips; source checks;111 upstream build records;324 fixed-scale interventions;62 planner engine invocations. Full planner and Make reproduction commands are in the entry file; use new output directories.

## New v7 evidence

- Formal additive/core-corrected/union baseline on54 beam inputs,1134 randomized timing records. All objective values independently enumerated; core reaches the union optimum in all54 cases,with53 identical selected representatives. Median paired core/union selection-time ratio0.670. Timing excludes FE replay,initialization and calibration.
- Integer-coefficient re-audit of1350 structural evaluations. Certificates:450/450,449/450,449/450 at alpha0.1,1,10. Exact objective scaling does not make the floating-point engine an exact-arithmetic solver. One timeout and one strict objective-recomputation rejection remain in the data.
- All256 finest-mesh physical layouts enumerated. Thirty-two weight permutations across3 budgets yield12 physically better,30 worse and54 equal union outcomes,despite improved accounting. Aligned-weight core/union choices attain each budget's mechanical optimum in this finite candidate space.
- Descriptive family,size and control strata;178 complete low/high pairs preserving costs,intent and conflicts;448 intent/work component points. The original primary certificate set is retained for headline comparisons.

## Earlier findings and boundaries

- Structural audit:450 primary attempted,448 certified,241 positive charitable gaps;mean2.88%. Complete faces and incomplete cases retained.
- Beam:54 settings,43 strict MILP face passes,11 numerical membership failures retained. Enumeration separately checks objectives. Tight primary case reduces compliance4.81% at equal volume. Uniform-value controls have zero charitable regret.
- zlib1.3.2:111 valid scored builds. Singletons7 recipes,pairs8,eight-path batch14;separate singletons56. Counts do not establish speedup.
- Common-cost intervention:54 existing inputs ×six levels;all union optimum faces invariant,18 additive faces switch. Conditional core correction requires disjoint residual footprints.
- Unmodified Fast Downward24.06.1:40 implementation-probe and22 engineering-adapter invocations. Six existing beam settings are reused,not six deployments. Additive aggregation occurs at the search-heuristic layer. The executed plan still charges each executed action once. Integer costs rounded to1e-6 units are independently enumerated; largest per-plan bound4.5e-6.
- Nearest full text reviewed:the2026 dependency-aware repair framework permits scoring extensions and selected-action lists. Our distinct evaluation is not proof that their framework cannot support shared materialization costs.
- Additive and FF planning heuristics,cost sharing,union costs,MILP,and engineering batching are prior art. The contribution is an empirical integration-contract audit,not a new general optimization algorithm. Human preferences and industrial prevalence remain unverified. Cabinet results do not support acceleration.

## Provenance and rights

Fast Downward commit `1eef26b2cbf599a1894606aa898d9d49e1034cb9` and zlib1.3.2 sources are bundled under their original licenses. Notices and hashes are included. Research materials are provided for inspection and reproduction; no blanket relicensing of third-party sources is granted. The private Springer article and extracted full text are excluded. This repository provides a public versioned artifact,not an independent archival DOI or an anonymous review service.
