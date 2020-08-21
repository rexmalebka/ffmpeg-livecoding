import math

def spread(*args, kind='mod'):

    if kind=='chop':
        return spreadchop(*args)
    elif kind=='fill':
        return spreadfill(*args)
    elif kind=='mod':
        return spreadmod(*args)
    elif kind=='rep':
        return spreadrepeat(*args)
    else:
        return spreadmod(*args)

def spreadchop(*args):
    len_arr = [len(k) for k in args]
    min_len = min(len_arr)
    new_arr = [k[:min_len] for k in args]
    return new_arr

def spreadfill(*args):
    len_arr = [len(k) for k in args]
    max_len = max(len_arr)
    new_arr = []
    for arg in args:
        if len(arg)<max_len:
            new_arr.append(arg + [arg[-1]]*(max_len - len(args)) )
        else:
            new_arr.append(arg)
    return new_arr

def spreadmod(*args):
    len_arr = [len(k) for k in args]
    max_len = max(len_arr)
    mod_arr = [max_len%k for k in len_arr]
    div_arr = [math.floor(max_len/k) for k in len_arr]
    new_arr = []
    for arg,div_arg,mod_arg in zip(args, div_arr, mod_arr):
        new_arr.append([])
        for k in arg:
            new_arr[-1].extend([k] * div_arg)
        new_arr[-1].extend([arg[-1]] * mod_arg)
    return new_arr

def spreadrepeat(*args):
    len_arr = [len(k) for k in args]
    max_len = max(len_arr)
    mod_arr = [max_len%k for k in len_arr]
    div_arr = [math.floor(max_len/k) for k in len_arr]
    new_arr = []
    for arg,div_arg,mod_arg in zip(args, div_arr, mod_arr):
        new_arr.append([])
        new_arr[-1].extend(arg * div_arg)
        new_arr[-1].extend(arg[:mod_arg])

    return new_arr

def execute(kind, looper):
    looper['spread'] = kind
    return looper

def parse():
    parser = argparse_ArgumentParser()

    parser.add_argument("kind",
                       help="kind of spread",
                       choices=['chop', 'fill', 'mod', 'rep']
                       )

    parser.add_argument("--looper",
                        help="looper to suscribe to.", 
                        nargs='?',
                        type=json.loads,
                        required= False,
                        default={"script":[]}
                       )

if __name__ == '__main__':
    args = parse()
    looper = execute()
    print()
