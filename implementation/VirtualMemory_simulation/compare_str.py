def main():
    with open("output.txt", 'r', encoding='utf-8') as output,open("gt.txt", 'r', encoding='utf-8') as gt:
        idx=1
        while True:
            output_line=output.readline()
            gt_line=gt.readline()
            if output_line != gt_line:
                print(f"第{idx}行出错")
            elif output_line=="" or gt_line=="":
                break
            idx += 1


if __name__== "__main__":
    main()