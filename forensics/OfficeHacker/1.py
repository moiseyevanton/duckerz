import subprocess, re
out = subprocess.run(
    ["tshark","-r","office_hacker.pcapng",
     "-Y","frame.number>=181 && frame.number<=191",
     "-T","fields","-e","sll.trailer"],      # ТОЛЬКО трейлер, без frame.number
    capture_output=True, text=True).stdout
hexstr = re.sub(r'[^0-9a-fA-F]', '', out)     # оставить только hex

print(bytes.fromhex(hexstr).decode(errors="replace"))