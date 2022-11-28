aa_d = {}

DNA_d = []

actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"


def get_amino_acids(name):
    with open(name, "r") as aminoFile:
        contents = aminoFile.read()
        lines = contents.splitlines()
    for i in lines:
        a = i.split()
        x = a[0]
        y = a[1]
        aa_d[x, y] = a[2:]
    return (aa_d)


def get_DNA(name):

    with open(name, "r") as dnaFile:
        contents = dnaFile.read()
        lines = contents.splitlines()
        a = ""
        for i in lines:
            if i == ">HSGLTH1 Human theta 1-globin gene":
                DNA_d.append(i)
            else:
                a += i
        DNA_d.append(a)
        return (DNA_d)
    pass


def translate(DNA_d):
    lst = DNA_d
    group = []
    nlst = []
    nlst2 = []
    b = ""

    for i in range(1, len(lst)):
        for j in range(0, len(lst[i]), 3):
            group.append(lst[i][j:j+3])
    for cod in group:
        for k, v in aa_d.items():
            for values in k:
                if cod in ["AA", "CC", "GG", "TT", "CA", "CG", "CT", "GA", "GC", "GT", "TA", "TC", "TG", "AC", "AG", "AT", "A", "G", "C", "T"]:
                    nlst2.append(cod)
                else:
                    if cod in values:
                        nlst.append(v[1])

    for letter in nlst:
        b += letter
    return b


fn1, fn2 = "amino_acids.txt", "DNA.txt"
aa_d = get_amino_acids(fn1)
DNA_d = get_DNA(fn2)
protein = translate(DNA_d)
# print(protein)
# print("Dictionary")
print(aa_d)
# print("FASTA file")
# print(DNA_d)
# print("Translations match:", str(protein == actual))
# # # should return "PLHS"
# print(translate(["noting", "CCACTGCA"]))
# # #should returns "D-"
# print(translate(["nothing", "GACTAA"]))
# print(protein)

# print(5)
