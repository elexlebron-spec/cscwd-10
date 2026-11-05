# Cost transfer audit — fixed v12 supplement

Contains the complete **v11 original upstream observations** (274-test scikit-learn module, nested 56-test family, all 48 sessions) and **v12 post hoc cross-profile/forecast analysis**. No new timing runs or revised upstream bodies. All zero and adverse outcomes remain.

Download the repository ZIP (Code → Download ZIP), then open a terminal in this folder:

```sh
python3 assemble.py
cd extracted
python3 tools/verify_cost_transfer_v12.py
python3 tools/analyze_upstream_v11.py
python3 tools/analyze_cost_transfer_v12.py
```

The archive is split into 19 binary parts for reliable transport. The assembler verifies the full length and SHA256 before extraction. These commands require only standard-library Python. The verifier checks 202 manifest hashes and reproduces 8 JSON/CSV outputs byte for byte in a separate temporary copy. No pytest installation or expensive fresh experiments are required.

**Archive:** 9,871,479 bytes  
**SHA256:** `d23175cacd69d16ed1ded042eaef1c5a28724bc8ba71ea21105f79223565f414`

Read `extracted/READ_FIRST.txt` for file mapping, scientific limits, licenses and fresh-execution instructions. The original v11 entry's “unpublished” statement is historical and superseded by this public release.

Main limits: one module and its nested subset; setup-aware accounting retains teardown in private residual; only profile-zero plans replayed; instrumented isolated sessions, not parallel completion or end-to-end acceleration. Cross-profile evidence does not causally identify noise or calibration. No industrial withdrawal adoption claim.

The unchanged [v8 scientific base](https://github.com/elexlebron-spec/cscwd-10/tree/278d73cb6a4ab812d538207ea6b165e80dbf62fb/repair-cost-audit/v8) supplies older engineering/control experiments and historical certification failures. Institutional full text, third-party scientific PDFs and private documents are excluded from this release.
