# s = open('24_10724.txt').readline()
# s = s\
#     .replace('Z', ' ')\
#     .replace('X', ' ')\
#     .replace('V', ' ')\
#     .replace('N', ' ')\
#     .replace('M', ' ')\
#     .replace('S', ' ')\
#     .replace('G', ' ')\
#     .replace('H', ' ')\
#     .replace('J', ' ')\
#     .replace('K', ' ')\
#     .replace('L', ' ')\
#     .replace('Q', ' ')\
#     .replace('W', ' ')\
#     .replace('R', ' ')\
#     .replace('T', ' ')\
#     .replace('Y', ' ')\
#     .replace('U', ' ')\
#     .replace('I', ' ')\
#     .replace('O', ' ')\
#     .replace('P', ' ')
#
# arr = s.split()
#
# for el in arr:
#     str_arr = list(el)
#     while str_arr[0] == "0":
#         str_arr[0] = ''
#         el = ''.join(str_arr)
# print(max(arr, key=len))

# d_max = 0
# el_first = True
# d = 0
# for el in s:
#     if el in '0123456789ABCDEF':
#         if el != '0':
#             d += 1
#         else:
#             if d != 0:
#                 d += 1
#     else:
#         d = 0
#     d_max = max(d_max, d)
# print(d_max)

# --------------------------------------------

# s = open("k7a-3.txt").readline()
# s = s.replace('B', ' ').replace('E', ' ')
# print(max(len(c) for c in s.split()))

# -----------------------------------------------------

# s = open('24_10105.txt').readline()
# s = s.replace('T', ' ').split()
# d_max = 0
# for i in range(len(s) - 101):
#     d = 0
#     for j in range(i, i + 102):
#         d += len(s[j])
#     d_max = max(d_max, d)
# print(d_max)


# -----------------------------------------------

# s = open('24_9850.txt').readline()
# s = s.replace('L', ' ')\
#     .replace('I', ' ')\
#     .replace('S', ' ')\
#     .replace('E', ' ')\
#     .replace('N', ' ')\
#     .replace('O', ' ')\
#     .replace('K', ' ')
# print(len(max(s.split(), key=len)))

# -----------------------------------------------

# s = open('24_9845.txt').readline()
# d = d_max = 1
# for i in range(len(s) - 1):
#     if (s[i] in 'ABC' and s[i+1] in '89') or (s[i] in '89' and s[i+1] in 'ABC'):
#         d += 1
#         d_max = max(d_max, d)
#     else:
#         d = 1
# print(d_max)

# -----------------------------------------------

# s = open('24_9791.txt').readline()
# for cep in 'QWRTYUIOPSGHJKLZXVNM':
#     s = s.replace(cep, ' ')
#
# print(len(max(s.split(), key=len)))

# -----------------------------------------------

# s = open('24_9753.txt').readline()
# s = s.replace('Y', ' ')
# d_max = 0
#
# for i in range(len(s) - 151):
#     d = 0
#     for j in range(i, i + 152):
#         d += len(s[j])
#     d_max = max(d_max, d)
# print(d_max)

# -----------------------------------------------

# s = open('24_9709.txt').readline()
#
# s = s.replace('XYZ', ' ')
# max = max(s.split(), key=len)
# print(len('LPCZWRFXLCTKFJOVECZJUBIVMEECNNOXGJCAAYWWZZDGJGALXRZLNRCMTLTRZRQMILBGHVZIMYUMCMQMYPZMVPMLVCNFRDTPCIERYTYSVGAIQWFINATMJEWVGOBQBFQCRORUHZFWQBGJUMDXATVTSHLICCYRTEPCBBFLGILZDLNHRIXOIOYBIWDXOKETGGDEBJGHBCYPZCWWDQCBVLYBVRMJAUGXVVSQSICZZTVDXOFAHDKQQMBGZIJACYAQBUQSJEUOWGIYGSPJUEZLVBUQQPHSSCJQBDKCXVDXFRKXJBKJDEVBVDLZMAKOSSCPEIONIKUQKPGFUEIOAOLGKOSWMKUYXQKEJXKXWKFTUZCUAFNUPXXSOMXLNROGTLUTPZRFELOEGBTNXBQPHZLSCONWBZPOSBMBUGSONRPWIHKPVSAYMLOKILDDRBUVXPPFEGIGMWSBJFGCQNXVMIKPDAGZEIFZPLZAJHVXJZLLBMIBCKZJZRHOQJVWZOBIVOAENGYSOKRBUNXFQGFVOJSTWTFMHHKJUFVDDYMCYVFSYURKOUGXZPOGGNLJJFXVHQEGYXBWQGASEISOHRCLAVUABSKKJLYCCDIMWLDZNBOOLEVAUKJXMUDKNSUGNPOXOVVIAJWNABYTWBOIXUXBIURRGTQBPLWXEAYGBCBNAOMCGVMGIFBYGIRGPFCBMRFMYYVVAAVTYHJFKIDJXIOBCUUNSDNUVEPKBJPUPQWMZBFTYCEAIIROMEDUKLHCBEMRSZKICSNBEGEMVQXUNLWNEJJZJBKOMFTBRTLJAQEFLSKICZTANSEKZTILZYQKTNXPDHXBGOEHYDRKXAMCYIMKUFCBJZKPCSQTAWUIWXQBUPXLTEYKIFDEZCPJZPWQNUWAUTKTEFPIYBDTWZVZLSOPUWDXCCQGMZOSXZMWKTJNPCGCYIXFSZDQJHQUIYDJJKRVMHSZDXLCEPWOEBXIPAIVDBRIIKQCHDGFITTJABLOEPYMKQMXBKHCXOTYTAVKBDXHYMPMUVQWEJQONPORVIDIQHIZYTIVHTJFSVZMCRIBRHIIGVGDSOCSXWHAGQSPCJYYCDPXENOOQUEFBXMOGSGHDBMNRBKYGEANASPEOLMPTBOUWVOOLGXCEUFGCZMXHETNTYYWKIKGWBHJJCBLDFFQUTOBKWHYEFSAMLMJFGDQYKFKYURKPPWNNCZSKBGJGQZRMSHRVXMHNJCEATQHFLNAFSXFMFIQBIJVBGQUMYXLIDDJNNCKUEVIQDWCADZVNTVFDVGOZBAGJWJDIKVXGFOERLSMTEKIPICJVVDGAPULZZLDFKSERXMBODEMGONBORHEAGC'))

# -----------------------------------------------
# s = open('24_9552.txt').readline()
# s = s.replace('PCSGO', 'PC CSGO').replace('PC', "**").replace('CSGO', '****')
# d = d_max = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         d += 1
#         d_max = max(d_max, d)
#     else:
#         d = 0
# print(d_max)

# ----------------------------------------------

# s = open('24_9377.txt').readline()
# digits = set('0123456789')
# letters = set(s) - digits
#
# for let in letters:
#     s = s.replace(let, "A")
#
# for let in letters:
#     for dig in digits:
#         s = s.replace('A'+dig, "A " + dig).replace(dig + "A", dig + " A")
#
# words = [x if x[0] == "A" or x[0] != '0' and x[-1] not in '13579' else ' ' for x in s.split()]
# s = ''.join(words)
# while 'A ' in s or ' A' in s:
#     s = s.replace('A ', ' ').replace(' A', ' ')
# print(len(max(s.split(), key=len)))

# -----------------------------------------------

# s = open('24_9169.txt').readline()
# s = s.replace('FAT', ' ').replace('BAD', ' ')
# lens = [len(x) for x in s.split(' ')][1:-1]
# print(min(a+b for a,b in zip(lens, lens[1:])) + 9)

# ------------------------------------------------

# s = open('24_8959.txt').readline()
# s = s.replace('NPC', '***').replace('EA', '**')
# d_max = d = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         d += 1
#     else:
#         d = 0
#     d_max = max(d_max, d)
# print(d_max)

# -------------------------------------------------

# s = open('24_8654.txt').readline()
#
# d = d_max = 4
# for i in range(len(s) - 4):
#     if s[i+1] + s[i + 4] == 'BD':
#         d = 4
#     else:
#         d += 1
#         d_max = max(d_max, d)
# print(d_max)

# -------------------------------------------------

# s = open('24_8480.txt').readline()
# s = s.replace('AA', ' ')\
#     .replace('BB', ' ')\
#     .replace('CC', ' ')\
#     .replace('AC', ' ')\
#     .replace('AB', ' ')\
#     .replace('BA', ' ')\
#     .replace('BC', ' ')\
#     .replace('CA', ' ')\
#     .replace('CB', ' ')
# print(len(max(s.split(), key=len)) + 2)

# --------------------------------------------------

# s = open('24_8431.txt').readline()
# d = d_max = 0
# for i in range(len(s)-2):
#     if 'X' in s[i:i+3] and 'Y' in s[i:i+3] and 'Z' in s[i:i+3]:
#         d = -2
#     else:
#         d += 1
#         d_max = max(d_max, d)
# print(d_max)

# --------------------------------------------------------

# s = open('24_8378.txt').readline()
# s = s.replace('TAA', ' ')
# d = d_max = 6
# for el in s.split():
#     if 'ATG' in el and 'TGA' not in el and 'TAG' not in el:
#         arr = el.split('ATG')
#         d += len(arr[1])
#     d_max = max(d, d_max)
#     d = 6
# print(d_max)

# --------------------------------------------------------

# from string import ascii_uppercase
#
# s = open('24_7981.txt').readline()
# count = 0
# for letter in ascii_uppercase:
#     count_back = 0
#     for i in range(len(s) - 1):
#         if s[i] == letter:
#             count += count_back
#             count_back += 1
#         if s[i] in 'ABC' and s[i+1] in 'ABC':
#             count_back = 0
# print(count)

# ----------------------------------------------------
# from string import ascii_uppercase

# s = open('24_7981.txt').readline()
#
# d = d_max = 0
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         if s[i] == s[j] and s[i:j].count(s[i]) == 2:
#             d = j - i + 1
#             d_max = max(d, d_max)
#
# print(d_max)