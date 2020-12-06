import csv
import click


@click.command()
@click.option('--path', default=False, help='file input.')
def run(path):
    print('converting')
    nodes = []
    result = []
    with open(path, 'rt')as f:
        f.readline()
        data = csv.reader(f)
        for row in data:
            if int(row[0])+1 not in nodes:
                column = [int(row[0])+1]
                nodes.append(int(row[0])+1)
                result.append(column)
                pass
            else:
                pass
            pass
        f.close()
        pass
    with open(path, 'rt')as f:
        f.readline()
        data = csv.reader(f)
        for row2 in data:
            index = nodes.index(int(row2[0])+1)
            result[index].append(int(row2[1])+1)
            pass
        f.close()
        pass

    with open('result.txt', 'w') as f:
        v = len(nodes)
        e = 0
        for r0 in result:
            for c0 in r0:
                if c0 not in nodes:
                    v = v + 1
                    nodes.append(c0)
                    pass
                pass
            e = e + len(r0) - 1
            pass
        f.write(str(v) + ' ' + str(e) + '\n')
        for r in result[:len(result)-2]:
            for c in r:
                f.write(' '+str(c))
                pass
            f.write(' \n')
            pass
        for last in result[len(result)-1]:
            f.write(' '+str(last))
            pass
        f.close()
        print('convert graph with: ')
        print('amount of node: ' + str(v))
        print('amount of edge: ' + str(e))
        print('result to result.txt')
        pass
    print('finish')
    pass


if __name__ == '__main__':
    run()
