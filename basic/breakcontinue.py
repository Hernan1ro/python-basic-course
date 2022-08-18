def run():
    for contador in range(500):
        if contador % 2 != 0:
            continue
        print(contador)


    for i in range(1000):
      print(i)
      if i == 500:
        break


if __name__ == "__main__":
    run()