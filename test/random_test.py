from template import *
def main():
    insert_time = []
    delete_time = []
    for right_interval in range(1000, 500000, 50000):
        array = np.random.randint(1, 100, right_interval)
        since = time.time()
        # for i in array:
        #     tree.insert(i)
        end = time.time() - since
        insert_time.append(end)
        print('AVL insert : ' + str(right_interval) + ' Data: ' + str(end) + 's')
    for right_interval in range(1000, 500000, 50000):
        array = np.random.randint(1, 100, right_interval)
        since = time.time()
        # for i in array:
        #     tree.delete(i)
        end = time.time() - since
        delete_time.append(end)
        print('AVL delete : ' + str(right_interval) + ' Data: ' + str(end) + 's')
        # for i in array:
        #     tree.insert(i)
if __name__=='__main__':
    main()