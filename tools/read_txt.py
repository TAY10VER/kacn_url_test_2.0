def read_txt(filename):
    filepath = "./urls/"+filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()


if __name__ == '__main__':
    print(read_txt("m_urls.txt"))
    print(" - -" * 50)
    arrs = []
    for data in read_txt("m_urls.txt"):
        arrs.append(data.strip())

    print(arrs[2])