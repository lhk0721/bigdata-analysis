import matplotlib.font_manager as fm

def do():
    f = [f.name for f in fm.fontManager.ttflist] # ttf리스트에서 f.name만 꺼내기. []는 리스트화.
    _f = dict()
    
    for c in f:
        if c not in _f:
            _f[c] = 1
        else:
            _f[c] = _f[c] + 1
            
    for k in _f.keys():
        print(k)

def main():
    do()

if __name__ == '__main__':
    main()
    
