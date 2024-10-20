#1
a = str(input())
g_count = a.count('G')
c_count = a.count('C')
m_count = a.count('A') + a.count('G') + a.count('C') + a.count('T')
pr_g = g_count / m_count * 100
pr_c = c_count / m_count * 100
print(pr_g,pr_c)
#2
