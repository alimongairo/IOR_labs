# NAIVE SEARCH
def naive_search(txt, pat):
    res = []
    count = 0
    len_t = len(txt)
    len_p = len(pat)
    for i in range(len_t - len_p + 1):
        if txt[i:i + len_p] == pat:
            res.append(i)
        count += len_p
    return res, count


# RK SEARCH
def RK_search(txt, pat):
    res = []
    count = 0
    len_t = len(txt)
    len_p = len(pat)
    hash_dict = HashDict(txt,pat)
    pat_hash = CalcHash(pat, hash_dict)
    for i in range(len_t - len_p + 1):
        current_val = CalcHash(txt[i:i + len_p], hash_dict)
        if pat_hash == current_val:
            if txt[i:len_p + i] == pat:
                res.append(i)
            count += len_p
        count += 1
    return res, count


def HashDict(txt, pat):
    symb_dict = {}
    symb_set = set(list(txt + pat))
    set_len = len(symb_set)
    for i in range(set_len):
        symb_dict[symb_set.pop()] = i
    return symb_dict


def CalcHash(p,hd):
    q = 11
    hash_val = 0
    j = 0
    for i in p:
        hash_val += hd[i] * pow(q,j)
        j += 1
    hash_val = hash_val // q
    return hash_val


# KMP SEARCH
def KMP_search(txt, pat):
    res = []
    count = 0
    len_t = len(txt)
    len_p = len(pat)
    i = 0
    j = 0
    pref = prefix(pat)
    while i < len_t:
        count += 1
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == len_p:
                res.append(i - len_p)
                j = 0
        else:
            if j > 0:
                j = pref[j-1]
            else:
                i += 1
    return res, count


def prefix(p):
    res = [0]*len(p)
    i = 1
    j = 0
    while i < len(p):
        if p[i] == p[j]:
            res[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                res[i] = 0
                i += 1
            else:
                j = res[j-1]
    return res
