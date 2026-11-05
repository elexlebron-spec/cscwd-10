"""Verify and merge the fixed v12 base and new v13 replay evidence."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
HERE=Path(__file__).resolve().parent
def payload(parts,count,size,digest):
    assert len(parts)==count, "Download the fixed repository ZIP including v12 and v13 folders."
    b=b"".join(p.read_bytes() for p in parts)
    assert len(b)==size and hashlib.sha256(b).hexdigest()==digest
    return b
base=payload(sorted((HERE.parent/"v12").glob("cost-transfer-v12.zip.part[0-9][0-9]")),19,9871479,"d23175cacd69d16ed1ded042eaef1c5a28724bc8ba71ea21105f79223565f414")
delta=payload(sorted(HERE.glob("replay-v13.zip.part[0-9][0-9]")),3,1240410,"1b13ddc93899dd16c12081fcc819a9cc144839d5b9771fdfb1de5730cf874000")
for name,b in [("v12-base.zip",base),("v13-delta.zip",delta)]:
    f=HERE/name
    f.write_bytes(b)
    with ZipFile(f) as z:z.extractall(HERE/"extracted")
print("Both archives verified and merged:",HERE/"extracted")
print("Next: cd",HERE/"extracted")
print("python3 tools/verify_replay_package_v13.py")
