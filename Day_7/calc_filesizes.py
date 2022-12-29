#!/usr/bin/env python3
"""Day 7 of advent of code.

Calculate file sizes in directories.
"""
import argparse
import pprint
import re
import sys


def calc_filesizes(inputfh):
    """Calculate dir and file sizes based on list of commands."""
    dirs = {}
    path = []

    for line in inputfh:
        m = re.search(r'\$ cd (\S+)', line)
        if m:
            dirname = m.group(1)
            if dirname == "/":
                path = ['/']
                dirs = {'/': {'type': 'dir',
                              'parent': '/',
                              'size': 0}}
            elif dirname == "..":
                path.pop()
            else:
                path.append(dirname)
                pathstr = "/".join(path)
                pathstr = re.sub(r'\/\/', '/', pathstr)
                if pathstr not in dirs:
                    parent = "/".join(path[:-1])
                    parent = re.sub(r'\/\/', '/', parent)
                    dirs[pathstr] = {'type': 'dir',
                                     'parent': parent,
                                     'size': 0}
            continue
        elif re.search(r'\$ ls', line):
            continue
        m = re.search(r'dir (\S+)', line)
        if m:
            pathstr = "/".join(path + [m.group(1)])
            pathstr = re.sub(r'\/\/', '/', pathstr)
            #  print(f'pathstr is {pathstr}')
            if pathstr not in dirs:
                parent = "/".join(path)
                parent = re.sub(r'\/\/', '/', parent)
                dirs[pathstr] = {'type': 'dir',
                                 'parent': parent,
                                 'size': 0}
            continue
        m = re.search(r'^(\d+)\s+(\S+)', line)
        if m:
            pathstr = "/".join(path + [m.group(2)])
            pathstr = re.sub(r'\/\/', '/', pathstr)
            #  print(f'pathstr is {pathstr}')
            if pathstr not in dirs:
                parent = "/".join(path)
                parent = re.sub(r'\/\/', '/', parent)
                dirs[pathstr] = {'type': 'file',
                                 'size': int(m.group(1)),
                                 'parent': parent}
            continue
        if len(line) > 1:
            print(f"got to line {line} which is unprocessed and ignored")

    pp = pprint.PrettyPrinter(width=41)
    for f in dirs:
        info = dirs[f]
        if info['type'] == "file":
            pfolder = info['parent']
            # first store count for the immediate parent
            if pfolder in dirs:
                dirs[pfolder]['size'] += info['size']
            # then walk up all the parents and add this count to them
            pfolderpath = pfolder.split('/')
            pfolderpath.pop()
            while len(pfolderpath):
                parentpath = "/".join([""] + pfolderpath)
                parentpath = re.sub(r'\/\/', '/', parentpath)
                print(f'adding size from {f} to {parentpath} (size={info["size"]})')
                if parentpath in dirs:
                    dirs[parentpath]['size'] += info['size']
                pfolderpath.pop()

    pp.pprint(dirs)
    return (dirs)


def main():
    """Tuning Trouble."""
    parser = argparse.ArgumentParser(description='Run AoC Day 7')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-s', '--maxsize', type=int, default=100000,
                        help='Directory size max')
    args = parser.parse_args()
    filehash = calc_filesizes(args.input)

    totalsize_smallfolder = 0
    for d in filehash:
        info = filehash[d]
        if info['type'] == 'dir' and info['size'] <= args.maxsize:
            totalsize_smallfolder += info['size']
            print(f'folder {d} is size {info["size"]} type={info["type"]}')
    print(f'Total size of small folders {totalsize_smallfolder}')
    return 0


if __name__ == "__main__":
    main()

# END
