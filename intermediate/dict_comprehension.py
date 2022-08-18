def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     my_dict[i] = i
    # print(my_dict)
    
    my_dict = {i:i for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

if __name__ == '__main__':
    run()