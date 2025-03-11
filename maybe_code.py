# cp_1_x = (cp_0_x(x) + cp_0_x(-x)) // 2 + random_x0 * (cp_0_x(x) - cp_0_x(-x)) // (2 * x)

# cp_1_x = sum(coef * x^(exp // 2) for exp, coef in R(cp_1_x).dict().items())
# cp_1_x.degree()

# cp_1_x = (cp_0_x(x) + cp_0_x(-x)) // 2 + random_x0 * (cp_0_x(x) - cp_0_x(-x)) // (2 * x)

# cp_1_on_wg = [cp_0_on_wg[i] + cp_0_on_wg[i+1] // 2 + random_x0 * (cp_0_on_wg[i] - cp_0_on_wg[i+1]) // (2 * wg[i]) for i in range(len(cp_0_on_wg))[:-1:2]]

# print(len(cp_0_on_wg))
# cp_before = cp_0_on_wg_reverse
# degree = 1000

# while degree > 0:
#     rand_x = channel.receive_random_field_element()
#     cp_after =  [(cp_before[i] + cp_before[i+1]) // 2 + \
#                  rand_x * (cp_before[i] - cp_before[i+1]) // (2 * wg[i]) for i in range(len(cp_before))[::2]]
#     mer = MerkleTree(cp_after)
#     commit = mer.root
#     channel.send(commit)
#     cp_before = cp_after
    # degree //= 2

# print(cp_before)