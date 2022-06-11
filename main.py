#!C:\Users\Mario Ehab\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html\n")
import cgi 
import numpy as np
form = cgi.FieldStorage()

print("<head>")
print("<link rel=" , '"stylesheet"',"href=" , '"./style.css"',">")
print("</head>")

print  ("<BODY id=",'"divpy"', "style=" , '"font-size: 30px;"',">")

print("<div>" )


print("<div class=" , '"title"',">" )
print("<h1>")
print("Local alignment")
print("</h1>")
print("</div>" )


print("<div>" )

if(form.getvalue("seq1")[0]==">"):
    textArea1 = form.getvalue("seq1").split("\n",1)[1]
    textArea1 = "".join([l.strip() for l in textArea1[0:]])
else:
    textArea1 = "".join([l.strip() for l in form.getvalue("seq1")[0:]])
# textArea1 = textArea1.strip('<>')

if(form.getvalue("seq2")[0]==">"):
    textArea2 = form.getvalue("seq2").split("\n",1)[1]
    textArea2 = "".join([l.strip() for l in textArea2[0:]])
else:
    textArea2 = "".join([l.strip() for l in form.getvalue("seq2")[0:]])

    

gap_result= int(form.getvalue("gap"))

def pam_matrix():
    data = open("pam250.txt", 'r')
    letters = data.readline()
    letters = letters.replace('\n', '')
    letters_arr = letters.split(' ')
    n = len(letters_arr)
    score_matrix = np.zeros((n, n))
    for i in range(0, n):
        arr = data.readline().split(" ")
        for j in range(0, n):
            score_matrix[i][j] = float(arr[j])
    return letters_arr, score_matrix

def match_score(c1, c2, letters, score_matrix):
    mapped_values = {}
    for i, v in enumerate(letters):
        mapped_values[v] = i
    a = mapped_values[c1]
    b = mapped_values[c2]
    return score_matrix[a][b]

x=[1]
def sequence_input_check(allowed):
    sequence = textArea1
    sequence = sequence.upper()
    for i in range(len(sequence)):
        if sequence[i] not in allowed:
            x[0]= 0
            print("Invalid sequence.Try again.")
            print("<br>")
            print("<form action=" , '"index.html"',">")    
            print("<input type=" , '"submit"',"id=" + '"sub"',"value=" , '"Add new sequence"',">")    
            print("</form>")
            
            return 0
    return sequence

def sequence_input_check1(allowed):
    sequence = textArea2
    sequence = sequence.upper()
    for i in range(len(sequence)):
        if sequence[i] not in allowed :
            print("Invalid sequence.Try again.")
            print("<br>")
            if(x[0]==1):
                print("<form action=" , '"index.html"',">")    
                print("<input type=" , '"submit"',"id=" + '"sub"',"value=" , '"Add new sequence"',">")    
                print("</form>")
            return 0
    return sequence

def local_alignment(first, second, letters, matrix):
    if gap_result < 1:
        gap = gap_result
    else:
        gap = -gap_result

    opt_loc = (0, 0)
    local_alignment = [[0 for j in range(len(second) + 1)] for i in range(len(first) + 1)]
    for i in range(len(first) + 1):
        local_alignment[i][0] = 0
    for i in range(len(second) + 1):
        local_alignment[0][i] = 0
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            matcher = match_score(first[i - 1], second[j - 1], letters, matrix)
            local_alignment[i][j] = max(0, local_alignment[i - 1][j] + gap, local_alignment[i][j - 1] + gap,
                                            local_alignment[i - 1][j - 1] + matcher)
    maximum = 0
    for i in range(len(local_alignment)):
        for j in range(len(local_alignment[i])):
            if local_alignment[i][j] > maximum:
                maximum = local_alignment[i][j]
                opt_loc = (i, j)
    

    print("<br>")        
    print("Result:\n"+"<br>")
    print("<br>")
    b="S "+second
    a=" "+first
    print("<table>")
    print("<tr>")
    for i in range(len(b)):
        print("<td style=" , '"color:black;background: rgb(206, 200, 166);font-weight:bold;"',">")
        print (b[i])
        print("</td>")
    print("</tr>")
    
    for i in range(len(textArea1)+1):
        print("<tr>")
        print("<td style=" , '"color:black;background: rgb(206, 200, 166);font-weight:bold;"',">")
        print (a[i])
        print("</td>")
        for j in range(len(textArea2)+1):
            if(maximum == local_alignment[i][j]):
                 print("<td style=" , '"color: red; font-weight:bold;"',">")
                 print(local_alignment[i][j] , end=" " )
                 print("</td>")
            else:
                print("<td>")
                print(local_alignment[i][j] , end=" " )
                print("</td>")
        print("</tr>")
    print("</table>")


    seq = ''
    seq2 = ''
    i = opt_loc[0]
    j = opt_loc[1]

    while i != 0 and j != 0:
        diag = local_alignment[i - 1][j - 1]
        up = local_alignment[i - 1][j]
        left = local_alignment[i][j - 1]
       
        if max(diag, left, up) == diag:
            i = i - 1
            j = j - 1
            seq += first[i]  
            seq2 += second[j]   
        else:
            if first[i-1] == second[j-1]:
                i = i - 1
                j = j - 1
                seq += first[i]
                seq2 += second[j]

            # left path
            elif max(diag, left, up) == left:
                j = j - 1
                seq += "-"
                seq2 += second[j]
            # up path
            elif max(diag, left, up) == up:
                i = i - 1
                seq += first[i]
                seq2 += '-'
#########################################################################################

#########################################################################################
    print("<br>")
    print("Local Alignment Score = ",maximum)
    print("<br>")
    print("<table>")
    print("<tr>","Alignment of sequence 1 and sequence 2  ")
    #################################################################################
    for i in range(len(seq)):
        
        print("<td>")
        print (seq[-i-1])
        print("</td>")
    print("</tr>")
    print("</table>")

    print("<table>")
    print("<tr>")
    for i in range(len(seq2)):
        print("<td>")
        print (seq2[-i-1])
        print("</td>")
    print("</tr>")
    print("</table>")
    print("<br>")
##############################################################################
    seq3=''
    for i in range(len(seq)):
      if(seq[i] == seq2[i]):
        seq3 += seq2[i]
      else:
            break
    print("Locally Aligned Sequence:")
    print("<table>")
    print("<tr>")
    for i in range(len(seq3)):
        print("<td>")
        print (seq3[-i-1])
        print("</td>")
    print("</tr>")
    print("</table>")
#########################################################################
    

    
0

def main():
    letters, matrix = pam_matrix()
    first = sequence_input_check(letters)
    second = sequence_input_check1(letters) 
    local_alignment(first, second, letters, matrix)




if __name__ == "__main__":
    main()


print("<form action=" , '"index.html"',">")    
print("<input type=" , '"submit"',"id=" + '"sub"',"value=" , '"Add new sequence"',">")    
print("</form>")


print("</div>")
print("</div>" )

print  ("</BODY>")