def file_write(fname, tasks):
    with open(fname, "w") as fp:
        for x in tasks:
            fp.write("%s,%s\n" % (x[0],x[1]))


def file_read(fname):
    tasks = []
    try:
        with open(fname, "r") as fp:
            t1 = fp.readlines()
            for x in t1:
                task = x.rstrip('\n')
                tasks.append(task.split(','))
        return tasks
    except FileNotFoundError:
        print("File {} is not found".format(fname))
        exit()