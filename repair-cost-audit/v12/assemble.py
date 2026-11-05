"""Reassemble the fixed supplement after downloading this repository/19 parts."""
from pathlib import Path
import hashlib
from zipfile import ZipFile
HERE=Path(__file__).resolve().parent
parts=sorted(HERE.glob("cost-transfer-v12.zip.part[0-9][0-9]"))
assert len(parts)==19, "Download all 19 parts beside this script, or download the repository ZIP."
payload=b"".join(p.read_bytes() for p in parts)
assert len(payload)==9871479
assert hashlib.sha256(payload).hexdigest()=="d23175cacd69d16ed1ded042eaef1c5a28724bc8ba71ea21105f79223565f414"
out=HERE/"cost-transfer-v12-supplement.zip"
out.write_bytes(payload)
with ZipFile(out) as z: z.extractall(HERE/"extracted")
print("Verified and extracted:", HERE/"extracted")
print("Next: cd", HERE/"extracted")
print("python3 tools/verify_cost_transfer_v12.py")
