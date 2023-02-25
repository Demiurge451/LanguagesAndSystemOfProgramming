import re


def find_interrogatory_sentence(s: str) -> str:
    pattern = re.compile("[^!?.\s][^!?.]+?[?]")
    match = re.findall(pattern, s)
    for i in range(0, len(match)):
        match[i] = re.sub("\n", " ", match[i])

    return match


def read_from_file() -> str:
    with open("input.txt", "r", encoding='utf-8') as f:
        input_str = f.read()

    return input_str


def write_to_file(output_str: str):
    with open("output.txt", "w", encoding='utf-8') as f:
        for x in output_str:
            f.write(str(x))
            f.write("\n")


def main():
    s = read_from_file()
    interrogatory_sentences = find_interrogatory_sentence(s)
    write_to_file(interrogatory_sentences)


main()
