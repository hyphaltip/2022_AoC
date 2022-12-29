#!/usr/bin/env python3
"""Day 7 of advent of code.

Calculate file sizes in directories.
"""
import argparse
import pprint
import re
import sys


def calc_filesizes(inputfh, debug=False):
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
            # print(f'pathstr is {pathstr} and num is {m.group(1)}')
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
            if pfolder != "/":
                pfolderpath = pfolder.split('/')
                pfolderpath.pop()
                while len(pfolderpath):
                    parentpath = "/".join([""] + pfolderpath)
                    parentpath = re.sub(r'\/\/', '/', parentpath)
                    if debug:
                        print(f'adding size from {f} to {parentpath} (size={info["size"]})')
                    if parentpath in dirs:
                        dirs[parentpath]['size'] += info['size']
                    pfolderpath.pop()
    if debug:
        print(pp.pprint(dirs))
    return (dirs)


def main():
    """Tuning Trouble2."""
    parser = argparse.ArgumentParser(description='Run AoC Day 7')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (or by stdin)')
    parser.add_argument('-s', '--maxsize', type=int, default=100000,
                        help='Directory size max')

    parser.add_argument('-t', '--totaldisk', type=int, default=70000000,
                        help='Total Disk size')
    parser.add_argument('-n', '--neededspace', type=int, default=30000000,
                        help='Needed free space')
    parser.add_argument('-v', '--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='debugging statements')
    args = parser.parse_args()
    if args.debug:
        print(f'totaldisk is {args.totaldisk} and neededspace is {args.neededspace}')
    filehash = calc_filesizes(args.input, args.debug)

    totalsize_smallfolder = 0
    dirsizes = {}
    rootalso = 0
    for d in filehash:
        info = filehash[d]

        if info['type'] == 'dir':
            dirsizes[d] = info['size']
        else:
            rootalso += info['size']
        if info['type'] == 'dir' and info['size'] <= args.maxsize:
            totalsize_smallfolder += info['size']
            if args.debug:
                print(f'folder {d} is size {info["size"]} type={info["type"]}')

    print(f'Total root file size is {dirsizes["/"]}')
    #  print(f'Calculated root file size is {rootalso}')
    print(f'Total size of small folders {totalsize_smallfolder}')
    unusedspace = args.totaldisk - dirsizes["/"]
    if args.debug:
        print(f"unused space is {unusedspace}")
    if unusedspace < args.neededspace:
        todelete = args.neededspace - unusedspace
        if args.debug:
            print(f"todelete left is {todelete}")
        possible_dirs = {}
        for fdir in sorted(dirsizes, key=lambda x: dirsizes[x], reverse=True):
            if dirsizes[fdir] >= todelete:
                if args.debug:
                    print(f'dir size:{dirsizes[fdir]} is dir {fdir}')
                possible_dirs[fdir] = dirsizes[fdir]
            else:
                if args.debug:
                    print(f'TOO SMALL dir size:{dirsizes[fdir]} is dir {fdir}')
        smallest = ''
        for f in sorted(possible_dirs, key=lambda x: possible_dirs[x]):
            if args.debug:
                print(f, possible_dirs[f])
            smallest = f
            break
        print(f"smallest dir that is bigger than {todelete} is {smallest} with size {possible_dirs[smallest]}")
    return 0


if __name__ == "__main__":
    main()

# END
