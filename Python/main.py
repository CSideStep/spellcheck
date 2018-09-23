import dict_reader
from functools import reduce


def main():
    d = dict_reader.dict_reader()
    print(get_best_fit("test", d, 1))


def get_best_fit(word:str, dr:dict_reader.dict_reader, sensitivity):
    return sorted(set([(get_score(word, dw), dw) for dw in dr.get_data() if get_score(word, dw) + sensitivity >= len(word)])
                  ,key=lambda x: x[0]
                  ,reverse=True)


def get_score(input1, input2):
    global score

    if len(input1) > len(input2):
        score = -(len(input1) - len(input2)) +\
                reduce(lambda a,b : a+b,[(input1[i] == input2[i]) for i in range(len(input2))]) +\
                len(input2) * (input2 in input1)

    else:
        score = -(len(input2) - len(input1)) +\
                reduce(lambda a,b : a+b,[(input1[i] == input2[i]) for i in range(len(input1))]) +\
                len(input1) * (input1 in input2)
    return score


if __name__ == "__main__":
    main()