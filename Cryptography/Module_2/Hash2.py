def hashing_f(key):
    mod = key * 0.618033
    result = int(len(hash_table) * (mod - int(mod)))
    return result


def insert(hash_table, key, value):
    hash_key = hashing_f(key)
    hash_table[hash_key].append(value)




