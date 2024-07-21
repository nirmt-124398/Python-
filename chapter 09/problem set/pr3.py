def genrat(n):
    tables=""
    for i in range(1,11):
        tables+=f"{n} X {i} = {n*i}\n"
    with open(f"tables/tableOf_{n}.txt","w") as f:
            f.write(tables)

for i in range(2,21):
    genrat(i)