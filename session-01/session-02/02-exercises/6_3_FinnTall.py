i = 1
cnt = 0

while i <= 100:
    rest = i % 3
    if rest == 0 and 20 < i < 80:
        print(i)
        cnt += 1
    i += 1

print(f"Det er {cnt} tall som har denne kombinasjonen ")